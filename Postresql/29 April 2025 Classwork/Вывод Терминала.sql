Last login: Tue Apr 29 19:53:07 on ttys008
andrewpshenichny@Andrews-MacBook-Pro ~ % psql postgres
psql (17.4 (Homebrew))
Введите "help", чтобы получить справку.

postgres=# /c students
postgres-# \c students
Вы подключены к базе данных "students" как пользователь "andrewpshenichny".
students-# create table warehouse(
    id serial primary key,
    city varchar(64),
    toponim varchar(128),
    building int,
    office int,
    unique(city, toponim, building, office));
ERROR:  syntax error at or near "/"
СТРОКА 1: /c students
          ^
students=# \c students
Вы подключены к базе данных "students" как пользователь "andrewpshenichny".
students=# create table warehouse(
    id serial primary key,
    city varchar(64),
    toponim varchar(128),
    building int,
    office int,
    unique(city, toponim, building, office));
CREATE TABLE
students=# insert into warehouse(city, toponim, building, office) values
students-# ("Кукуевск", "ул. Павловка", 13, 26);
ERROR:  column "Кукуевск" does not exist
СТРОКА 2: ("Кукуевск", "ул. Павловка", 13, 26);
           ^
students=# insert into warehouse(city, toponim, building, office) values
("Кукуевск", "ул. Павловка", 13, 26);
ERROR:  column "Кукуевск" does not exist
СТРОКА 2: ("Кукуевск", "ул. Павловка", 13, 26);
           ^
students=# insert into warehouse(city, toponim, building, office) values ("Кукуевск", "ул. Павловка", 13, 26);
ERROR:  column "Кукуевск" does not exist
СТРОКА 1: ...arehouse(city, toponim, building, office) values ("Кукуевск"...
                                                               ^
students=# insert into warehouse(city, toponim, building, office) values ('Кукуевск', 'ул. Павловка', 13, 26), ('Крыжовенка', 'пр. Ленина', 46, 2);
INSERT 0 2
students=# select * from warehouse;
 id |    city    |   toponim    | building | office 
----+------------+--------------+----------+--------
  1 | Кукуевск   | ул. Павловка |       13 |     26
  2 | Крыжовенка | пр. Ленина   |       46 |      2
(2 строки)

students=# create table good_unit(
students(# id serial primary key,
students(# name varchar(64),
students(# price int,
students(# );
ERROR:  syntax error at or near ")"
СТРОКА 5: );
          ^
students=# create table units(
students(# id serial primary key,
students(# name varchar(64) unique);
CREATE TABLE
students=# insert into units(name) values('kg'), ('штука'), ('литр');
INSERT 0 3
students=# select * from units;
 id | name  
----+-------
  1 | kg
  2 | штука
  3 | литр
(3 строки)

students=# create table good_unit(
id serial primary key,  -- not null
name varchar(64) not null,
price int default 0,
quantity float default 0,
unit int references units(id) default 3,
wh int references warehouse(id) not null);
CREATE TABLE
students=# insert into good_unit(name, price, quantity, unit, wh) values ('помидоры', 75, 10, 1, 1);
INSERT 0 1
students=# select id from units where name='kg', 1;
ERROR:  syntax error at or near ","
СТРОКА 1: select id from units where name='kg', 1;
                                              ^
students=# insert into good_unit(name, price, quantity, unit, wh) values('помидоры', 75, 10, (select id from units where name='килограмм'), 1);

select good_unit.name, price, quantity, units.name, city, toponim, building, office from good_unit, units, warehouse; -- свалка просто всего

select good_unit.name, price, quantity, units.name, city, toponim, building, office from good_unit, units, warehouse where units.id=unit and warehouse.id=wh;
INSERT 0 1
   name   | price | quantity | name  |    city    |   toponim    | building | office 
----------+-------+----------+-------+------------+--------------+----------+--------
 помидоры |    75 |       10 | kg    | Кукуевск   | ул. Павловка |       13 |     26
   name   | price | quantity | name  |    city    |   toponim    | building | of
fice 
----------+-------+----------+-------+------------+--------------+----------+---
-----
 помидоры |    75 |       10 | kg    | Кукуевск   | ул. Павловка |       13 |   
  26
 помидоры |    75 |       10 | штука | Кукуевск   | ул. Павловка |       13 |     26
 помидоры |    75 |       10 | литр  | Кукуевск   | ул. Павловка |       13 |     26
 помидоры |    75 |       10 | kg    | Крыжовенка | пр. Ленина   |       46 |      2
 помидоры |    75 |       10 | штука | Крыжовенка | пр. Ленина   |       46 |      2
 помидоры |    75 |       10 | литр  | Крыжовенка | пр. Ленина   |       46 |      2
 помидоры |    75 |       10 | kg    | Кукуевск   | ул. Павловка |       13 |     26
 помидоры |    75 |       10 | штука | Кукуевск   | ул. Павловка |       13 |     26
 помидоры |    75 |       10 | литр  | Кукуевск   | ул. Павловка |       13 |     26
 помидоры |    75 |       10 | kg    | Крыжовенка | пр. Ленина   |       46 |      2
 помидоры |    75 |       10 | штука | Крыжовенка | пр. Ленина   |       46 |      2
 помидоры |    75 |       10 | литр  | Крыжовенка | пр. Ленина   |       46 |      2
(12 строк)

set mark: ...skipping...
  26
 помидоры |    75 |       10 | литр  | Кукуевск   | ул. Павловка |       13 |     26
 помидоры |    75 |       10 | kg    | Крыжовенка | пр. Ленина   |       46 |      2
 помидоры |    75 |       10 | штука | Крыжовенка | пр. Ленина   |       46 |      2
 помидоры |    75 |       10 | литр  | Крыжовенка | пр. Ленина   |       46 |      2
 помидоры |    75 |       10 | kg    | Кукуевск   | ул. Павловка |       13 |     26
 помидоры |    75 |       10 | штука | Кукуевск   | ул. Павловка |       13 |     26
 помидоры |    75 |       10 | литр  | Кукуевск   | ул. Павловка |       13 |     26
 помидоры |    75 |       10 | kg    | Крыжовенка | пр. Ленина   |       46 |      2
 помидоры |    75 |       10 | штука | Крыжовенка | пр. Ленина   |       46 |      2
 помидоры |    75 |       10 | литр  | Крыжовенка | пр. Ленина   |       46 |      2
(12 строк)

   name   | price | quantity | name |   city   |   toponim    | building | office 
----------+-------+----------+------+----------+--------------+----------+--------
 помидоры |    75 |       10 | kg   | Кукуевск | ул. Павловка |       13 |     26
(1 строка)

...skipping...
   name   | price | quantity | name |   city   |   toponim    | building | office 
----------+-------+----------+------+----------+--------------+----------+--------
 помидоры |    75 |       10 | kg   | Кукуевск | ул. Павловка |       13 |     26
(1 строка)

~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
...skipping...
   name   | price | quantity | name |   city   |   toponim    | building | office 
----------+-------+----------+------+----------+--------------+----------+--------
 помидоры |    75 |       10 | kg   | Кукуевск | ул. Павловка |       13 |     26
(1 строка)

~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
students=# select good_unit.name, price, quantity, units.name, city, toponim, building, office from good_unit, units, warehouse where units.id=unit and warehouse.id=wh;
   name   | price | quantity | name |   city   |   toponim    | building | office 
----------+-------+----------+------+----------+--------------+----------+--------
 помидоры |    75 |       10 | kg   | Кукуевск | ул. Павловка |       13 |     26
(1 строка)

students=# insert into units(name) values('десяток');
INSERT 0 1
students=# select * from units;
 id |  name   
----+---------
  1 | kg
  2 | штука
  3 | литр
  4 | десяток
(4 строки)

students=# insert into good_unit(name, price, quantity, unit, wh) values ('яйца', 200, 10, 4, 1), ('шляпы', 2000, 10, 2, 1), ('молоко', 100, 20, 3, 1);
INSERT 0 3
students=# select good_unit.name, price, quantity, units.name, city, toponim, building, office from good_unit, units, warehouse where units.id=unit and warehouse.id=wh;
   name   | price | quantity |  name   |   city   |   toponim    | building | office 
----------+-------+----------+---------+----------+--------------+----------+--------
 помидоры |    75 |       10 | kg      | Кукуевск | ул. Павловка |       13 |     26
 яйца     |   200 |       10 | десяток | Кукуевск | ул. Павловка |       13 |     26
 шляпы    |  2000 |       10 | штука   | Кукуевск | ул. Павловка |       13 |     26
 молоко   |   100 |       20 | литр    | Кукуевск | ул. Павловка |       13 |     26
(4 строки)

(END)
   name   | price | quantity |  name   |   city   |   toponim    | building | office 
----------+-------+----------+---------+----------+--------------+----------+--------
 помидоры |    75 |       10 | kg      | Кукуевск | ул. Павловка |       13 |     26
 яйца     |   200 |       10 | десяток | Кукуевск | ул. Павловка |       13 |     26
 шляпы    |  2000 |       10 | штука   | Кукуевск | ул. Павловка |       13 |     26
 молоко   |   100 |       20 | литр    | Кукуевск | ул. Павловка |       13 |     26
(4 строки)

~
~
~
~
~
~
~
~
~
(END)


























































   name   | price | quantity |  name   |   city   |   toponim    | building | office 
----------+-------+----------+---------+----------+--------------+----------+--------
 помидоры |    75 |       10 | kg      | Кукуевск | ул. Павловка |       13 |     26
 яйца     |   200 |       10 | десяток | Кукуевск | ул. Павловка |       13 |     26
 шляпы    |  2000 |       10 | штука   | Кукуевск | ул. Павловка |       13 |     26
 молоко   |   100 |       20 | литр    | Кукуевск | ул. Павловка |       13 |     26
(4 строки)

~
~
~
~
~
~
~
~
~
(END)


























































   name   | price | quantity |  name   |   city   |   toponim    | building | office 
----------+-------+----------+---------+----------+--------------+----------+--------
 помидоры |    75 |       10 | kg      | Кукуевск | ул. Павловка |       13 |     26
 яйца     |   200 |       10 | десяток | Кукуевск | ул. Павловка |       13 |     26
 шляпы    |  2000 |       10 | штука   | Кукуевск | ул. Павловка |       13 |     26
 молоко   |   100 |       20 | литр    | Кукуевск | ул. Павловка |       13 |     26
(4 строки)

~
~
~
~
~
~
~
~
~
(END)
   name   | price | quantity |  name   |   city   |   toponim    | building | office 
----------+-------+----------+---------+----------+--------------+----------+--------
 помидоры |    75 |       10 | kg      | Кукуевск | ул. Павловка |       13 |     26
 яйца     |   200 |       10 | десяток | Кукуевск | ул. Павловка |       13 |     26
 шляпы    |  2000 |       10 | штука   | Кукуевск | ул. Павловка |       13 |     26
 молоко   |   100 |       20 | литр    | Кукуевск | ул. Павловка |       13 |     26
(4 строки)

~
~
~
~
~
~
~
~
~
(END)
   name   | price | quantity |  name   |   city   |   toponim    | building | office 
----------+-------+----------+---------+----------+--------------+----------+--------
 помидоры |    75 |       10 | kg      | Кукуевск | ул. Павловка |       13 |     26
 яйца     |   200 |       10 | десяток | Кукуевск | ул. Павловка |       13 |     26
 шляпы    |  2000 |       10 | штука   | Кукуевск | ул. Павловка |       13 |     26
 молоко   |   100 |       20 | литр    | Кукуевск | ул. Павловка |       13 |     26
(4 строки)

~
~
~
~
~
~
~
~
~
(END)


























































   name   | price | quantity |  name   |   city   |   toponim    | building | office 
----------+-------+----------+---------+----------+--------------+----------+--------
 помидоры |    75 |       10 | kg      | Кукуевск | ул. Павловка |       13 |     26
 яйца     |   200 |       10 | десяток | Кукуевск | ул. Павловка |       13 |     26
 шляпы    |  2000 |       10 | штука   | Кукуевск | ул. Павловка |       13 |     26
 молоко   |   100 |       20 | литр    | Кукуевск | ул. Павловка |       13 |     26
(4 строки)

~
~
~
~
~
~
~
~
~
(END)


























































   name   | price | quantity |  name   |   city   |   toponim    | building | office 
----------+-------+----------+---------+----------+--------------+----------+--------
 помидоры |    75 |       10 | kg      | Кукуевск | ул. Павловка |       13 |     26
 яйца     |   200 |       10 | десяток | Кукуевск | ул. Павловка |       13 |     26
 шляпы    |  2000 |       10 | штука   | Кукуевск | ул. Павловка |       13 |     26
 молоко   |   100 |       20 | литр    | Кукуевск | ул. Павловка |       13 |     26
(4 строки)

~
~
~
~
~
~
~
~
~
(END)
   name   | price | quantity |  name   |   city   |   toponim    | building | office 
----------+-------+----------+---------+----------+--------------+----------+--------
 помидоры |    75 |       10 | kg      | Кукуевск | ул. Павловка |       13 |     26
 яйца     |   200 |       10 | десяток | Кукуевск | ул. Павловка |       13 |     26
 шляпы    |  2000 |       10 | штука   | Кукуевск | ул. Павловка |       13 |     26
 молоко   |   100 |       20 | литр    | Кукуевск | ул. Павловка |       13 |     26
(4 строки)

~
~
~
~
~
~
~
~
~
students=# create view all_goods as select good_unit.name as good, price, quantity, units.name unit, city, toponim, building, office from good_unit, units, warehouse where units.id=unit and warehouse.id=wh;
CREATE VIEW
students=# \l
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

students=# \c students
Вы подключены к базе данных "students" как пользователь "andrewpshenichny".
students=# \dt
                  Список отношений
 Схема  |     Имя      |   Тип   |     Владелец     
--------+--------------+---------+------------------
 public | good_unit    | таблица | andrewpshenichny
 public | group411     | таблица | andrewpshenichny
 public | publications | таблица | andrewpshenichny
 public | units        | таблица | andrewpshenichny
 public | warehouse    | таблица | andrewpshenichny
(5 строк)

students=# SELECT column_name
FROM information_schema.columns
WHERE table_name = 'warehouse';
 column_name 
-------------
 id
 building
 office
 city
 toponim
(5 строк)

students=# SELECT column_name
FROM information_schema.columns
WHERE table_name = 'units';
 column_name 
-------------
 id
 name
(2 строки)

students=# 
