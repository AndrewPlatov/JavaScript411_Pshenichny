Last login: Thu Apr 17 22:55:54 on ttys000
andrewpshenichny@Andrews-MacBook-Pro ~ % psql postgres
psql (17.4 (Homebrew))
Введите "help", чтобы получить справку.

postgres=# \l
                                                                 Список баз данных
    Имя    |     Владелец     | Кодировка | Провайдер локали | LC_COLLATE | LC_CTYPE | Локаль | Правила ICU |             Права доступа             
-----------+------------------+-----------+------------------+------------+----------+--------+-------------+---------------------------------------
 postgres  | andrewpshenichny | UTF8      | libc             | C          | C        |        |             | 
 students  | andrew           | UTF8      | libc             | C          | C        |        |             | 
 template0 | andrewpshenichny | UTF8      | libc             | C          | C        |        |             | =c/andrewpshenichny                  +
           |                  |           |                  |            |          |        |             | andrewpshenichny=CTc/andrewpshenichny
 template1 | andrewpshenichny | UTF8      | libc             | C          | C        |        |             | =c/andrewpshenichny                  +
           |                  |           |                  |            |          |        |             | andrewpshenichny=CTc/andrewpshenichny
(4 строки)

postgres=# \du
                                        Список ролей
     Имя роли     |                                Атрибуты                                 
------------------+-------------------------------------------------------------------------
 andrew           | Создаёт БД
 andrewpshenichny | Суперпользователь, Создаёт роли, Создаёт БД, Репликация, Пропускать RLS
 student          | 

postgres=# set role andrew;
SET
postgres=> \l
                                                                 Список баз данных
    Имя    |     Владелец     | Кодировка | Провайдер локали | LC_COLLATE | LC_CTYPE | Локаль | Правила ICU |             Права доступа             
-----------+------------------+-----------+------------------+------------+----------+--------+-------------+---------------------------------------
 postgres  | andrewpshenichny | UTF8      | libc             | C          | C        |        |             | 
 students  | andrew           | UTF8      | libc             | C          | C        |        |             | 
 template0 | andrewpshenichny | UTF8      | libc             | C          | C        |        |             | =c/andrewpshenichny                  +
           |                  |           |                  |            |          |        |             | andrewpshenichny=CTc/andrewpshenichny
 template1 | andrewpshenichny | UTF8      | libc             | C          | C        |        |             | =c/andrewpshenichny                  +
           |                  |           |                  |            |          |        |             | andrewpshenichny=CTc/andrewpshenichny
(4 строки)

postgres=> \du
                                        Список ролей
     Имя роли     |                                Атрибуты                                 
------------------+-------------------------------------------------------------------------
 andrew           | Создаёт БД
 andrewpshenichny | Суперпользователь, Создаёт роли, Создаёт БД, Репликация, Пропускать RLS
 student          | 

postgres=> create user student1 with password 'queen';
ERROR:  permission denied to create role
ПОДРОБНОСТИ:  Only roles with the CREATEROLE attribute may create roles.
postgres=> set role andrewpshenichny;
SET
postgres=# alter role andrew with createrole;
ALTER ROLE
postgres=# set role andrew;
SET
postgres=> create user student1 with password 'queen';
CREATE ROLE
postgres=> create database urok1 owner student;
ERROR:  must be able to SET ROLE "student"
postgres=> create database urok1 owner student1;
ERROR:  must be able to SET ROLE "student1"
postgres=> \du
                                        Список ролей
     Имя роли     |                                Атрибуты                                 
------------------+-------------------------------------------------------------------------
 andrew           | Создаёт роли, Создаёт БД
 andrewpshenichny | Суперпользователь, Создаёт роли, Создаёт БД, Репликация, Пропускать RLS
 student          | 
 student1         | 

postgres=> create user student with password 'queen' createdb;
ERROR:  role "student" already exists
postgres=> create user student2 with password 'queen' createdb;
CREATE ROLE
postgres=> \du
                                        Список ролей
     Имя роли     |                                Атрибуты                                 
------------------+-------------------------------------------------------------------------
 andrew           | Создаёт роли, Создаёт БД
 andrewpshenichny | Суперпользователь, Создаёт роли, Создаёт БД, Репликация, Пропускать RLS
 student          | 
 student1         | 
 student2         | Создаёт БД

postgres=> create database urok1 owner student2;
ERROR:  must be able to SET ROLE "student2"
postgres=> set role student2;
SET
postgres=> create database urok1 owner student2;
CREATE DATABASE
postgres=> \l
                                                                 Список баз данных
    Имя    |     Владелец     | Кодировка | Провайдер локали | LC_COLLATE | LC_CTYPE | Локаль | Правила ICU |             Права доступа             
-----------+------------------+-----------+------------------+------------+----------+--------+-------------+---------------------------------------
 postgres  | andrewpshenichny | UTF8      | libc             | C          | C        |        |             | 
 students  | andrew           | UTF8      | libc             | C          | C        |        |             | 
 template0 | andrewpshenichny | UTF8      | libc             | C          | C        |        |             | =c/andrewpshenichny                  +
           |                  |           |                  |            |          |        |             | andrewpshenichny=CTc/andrewpshenichny
 template1 | andrewpshenichny | UTF8      | libc             | C          | C        |        |             | =c/andrewpshenichny                  +
           |                  |           |                  |            |          |        |             | andrewpshenichny=CTc/andrewpshenichny
 urok1     | student2         | UTF8      | libc             | C          | C        |        |             | 
(5 строк)

postgres=> drop database urok1;
DROP DATABASE
postgres=> \l
                                                                 Список баз данных
    Имя    |     Владелец     | Кодировка | Провайдер локали | LC_COLLATE | LC_CTYPE | Локаль | Правила ICU |             Права доступа             
-----------+------------------+-----------+------------------+------------+----------+--------+-------------+---------------------------------------
 postgres  | andrewpshenichny | UTF8      | libc             | C          | C        |        |             | 
 students  | andrew           | UTF8      | libc             | C          | C        |        |             | 
 template0 | andrewpshenichny | UTF8      | libc             | C          | C        |        |             | =c/andrewpshenichny                  +
           |                  |           |                  |            |          |        |             | andrewpshenichny=CTc/andrewpshenichny
 template1 | andrewpshenichny | UTF8      | libc             | C          | C        |        |             | =c/andrewpshenichny                  +
           |                  |           |                  |            |          |        |             | andrewpshenichny=CTc/andrewpshenichny
(4 строки)

postgres=> set role andrewpshenichny;
SET
postgres=# \du
                                        Список ролей
     Имя роли     |                                Атрибуты                                 
------------------+-------------------------------------------------------------------------
 andrew           | Создаёт роли, Создаёт БД
 andrewpshenichny | Суперпользователь, Создаёт роли, Создаёт БД, Репликация, Пропускать RLS
 student          | 
 student1         | 
 student2         | Создаёт БД

postgres=# drop role student2;
DROP ROLE
postgres=# \du
                                        Список ролей
     Имя роли     |                                Атрибуты                                 
------------------+-------------------------------------------------------------------------
 andrew           | Создаёт роли, Создаёт БД
 andrewpshenichny | Суперпользователь, Создаёт роли, Создаёт БД, Репликация, Пропускать RLS
 student          | 
 student1         | 

postgres=# drop role student1;
DROP ROLE
postgres=# drop role student;
DROP ROLE
postgres=# \du
                                        Список ролей
     Имя роли     |                                Атрибуты                                 
------------------+-------------------------------------------------------------------------
 andrew           | Создаёт роли, Создаёт БД
 andrewpshenichny | Суперпользователь, Создаёт роли, Создаёт БД, Репликация, Пропускать RLS

postgres=# \o
postgres=# \o
postgres=# \o results.txt;
postgres=# \o requests_Familia.sql;
postgres=# 
