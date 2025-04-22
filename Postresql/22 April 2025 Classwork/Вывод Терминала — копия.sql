Last login: Thu Apr 17 23:03:18 on ttys000
andrewpshenichny@Andrews-MacBook-Pro ~ % psql postgres
psql (17.4 (Homebrew))
Введите "help", чтобы получить справку.

postgres=# CREATE TABLE group411(
    first_name varchar(16),
    surname varchar(32),
    fathername boolean,
    is_online boolean,
    row_number integer,
    comp integer
);
CREATE TABLE
postgres=# \dt
                Список отношений
 Схема  |   Имя    |   Тип   |     Владелец     
--------+----------+---------+------------------
 public | group411 | таблица | andrewpshenichny
(1 строка)

postgres=# \d group411;
                                 Таблица "public.group411"
  Столбец   |          Тип          | Правило сортировки | Допустимость NULL | По умолчанию 
------------+-----------------------+--------------------+-------------------+--------------
 first_name | character varying(16) |                    |                   | 
 surname    | character varying(32) |                    |                   | 
 fathername | boolean               |                    |                   | 
 is_online  | boolean               |                    |                   | 
 row_number | integer               |                    |                   | 
 comp       | integer               |                    |                   | 

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

postgres=# psql students;
ERROR:  syntax error at or near "psql"
СТРОКА 1: psql students;
          ^
postgres=# \c students
Вы подключены к базе данных "students" как пользователь "andrewpshenichny".
students=# CREATE TABLE group411(
    first_name varchar(16),
    surname varchar(32),
    fathername boolean,
    is_online boolean,
    row_number integer,
    comp integer
);
CREATE TABLE
students=# \dt
                Список отношений
 Схема  |   Имя    |   Тип   |     Владелец     
--------+----------+---------+------------------
 public | group411 | таблица | andrewpshenichny
(1 строка)

students=# \d group411;
                                 Таблица "public.group411"
  Столбец   |          Тип          | Правило сортировки | Допустимость NULL | По умолчанию 
------------+-----------------------+--------------------+-------------------+--------------
 first_name | character varying(16) |                    |                   | 
 surname    | character varying(32) |                    |                   | 
 fathername | boolean               |                    |                   | 
 is_online  | boolean               |                    |                   | 
 row_number | integer               |                    |                   | 
 comp       | integer               |                    |                   | 

students=# INSERT INTO group411(
    surname, first_name, fathername, is_student, is_online
) VALUES 
('Вафин', 'Артур', 'Фердинандович', true, false),
('Гетагазов', 'Артур', 'Магомедович', true, false),
('Джифов', 'Азиз', 'Хуршедшоевич', true, false),
('Карташов', 'Филипп', 'Дмитриевич', true, false),
('Костылёва', 'Ульяна', 'Константиновна', true, false),
('Молотягин', 'Олег','Владимирович', true, false),
('Османов', 'Рустам', 'Исмаил оглы', true, false),
('Поздняков', 'Константин', 'Александрович', true, false),
('Пшеничный', 'Андрей', 'Михайлович', true, false),
('Суровнева', 'Софья', 'Дмитриевна', true, false);
ERROR:  column "is_student" of relation "group411" does not exist
СТРОКА 2:     surname, first_name, fathername, is_student, is_online
                                               ^
students=# CREATE TABLE group411(
    first_name varchar(16),
    surname varchar(32),
    fathername varchar(32),
    is_student boolean,
    is_online boolean,
    row_number integer,
    comp integer
);
ERROR:  relation "group411" already exists
students=# INSERT INTO group411(
    surname, first_name, fathername, is_student, is_online
) VALUES 
('Вафин', 'Артур', 'Фердинандович', true, false),
('Гетагазов', 'Артур', 'Магомедович', true, false),
('Джифов', 'Азиз', 'Хуршедшоевич', true, false),
('Карташов', 'Филипп', 'Дмитриевич', true, false),
('Костылёва', 'Ульяна', 'Константиновна', true, false),
('Молотягин', 'Олег','Владимирович', true, false),
('Османов', 'Рустам', 'Исмаил оглы', true, false),
('Поздняков', 'Константин', 'Александрович', true, false),
('Пшеничный', 'Андрей', 'Михайлович', true, false),
('Суровнева', 'Софья', 'Дмитриевна', true, false);
ERROR:  column "is_student" of relation "group411" does not exist
СТРОКА 2:     surname, first_name, fathername, is_student, is_online
                                               ^
students=# DROP TABLE group411;
DROP TABLE
students=# CREATE TABLE group411(
    first_name varchar(16),
    surname varchar(32),
    fathername varchar(32),
    is_student boolean,
    is_online boolean,
    row_number integer,
    comp integer
);
CREATE TABLE
students=# INSERT INTO group411(
    surname, first_name, fathername, is_student, is_online
) VALUES 
('Вафин', 'Артур', 'Фердинандович', true, false),
('Гетагазов', 'Артур', 'Магомедович', true, false),
('Джифов', 'Азиз', 'Хуршедшоевич', true, false),
('Карташов', 'Филипп', 'Дмитриевич', true, false),
('Костылёва', 'Ульяна', 'Константиновна', true, false),
('Молотягин', 'Олег','Владимирович', true, false),
('Османов', 'Рустам', 'Исмаил оглы', true, false),
('Поздняков', 'Константин', 'Александрович', true, false),
('Пшеничный', 'Андрей', 'Михайлович', true, false),
('Суровнева', 'Софья', 'Дмитриевна', true, false);
INSERT 0 10
students=# select * from group411;
 first_name |  surname  |   fathername   | is_student | is_online | row_number | comp 
------------+-----------+----------------+------------+-----------+------------+------
 Артур      | Вафин     | Фердинандович  | t          | f         |            |     
 Артур      | Гетагазов | Магомедович    | t          | f         |            |     
 Азиз       | Джифов    | Хуршедшоевич   | t          | f         |            |     
 Филипп     | Карташов  | Дмитриевич     | t          | f         |            |     
 Ульяна     | Костылёва | Константиновна | t          | f         |            |     
 Олег       | Молотягин | Владимирович   | t          | f         |            |     
 Рустам     | Османов   | Исмаил оглы    | t          | f         |            |     
 Константин | Поздняков | Александрович  | t          | f         |            |     
 Андрей     | Пшеничный | Михайлович     | t          | f         |            |     
 Софья      | Суровнева | Дмитриевна     | t          | f         |            |:
 first_name |  surname  |   fathername   | is_student | is_online | row_number | comp 
------------+-----------+----------------+------------+-----------+------------+------
 Артур      | Вафин     | Фердинандович  | t          | f         |            |     
 Артур      | Гетагазов | Магомедович    | t          | f         |            |     
 Азиз       | Джифов    | Хуршедшоевич   | t          | f         |            |     
 Филипп     | Карташов  | Дмитриевич     | t          | f         |            |     
 Ульяна     | Костылёва | Константиновна | t          | f         |            |     
 Олег       | Молотягин | Владимирович   | t          | f         |            |     
 Рустам     | Османов   | Исмаил оглы    | t          | f         |            |     
 Константин | Поздняков | Александрович  | t          | f         |            |     
 Андрей     | Пшеничный | Михайлович     | t          | f         |            |     
 Софья      | Суровнева | Дмитриевна     | t          | f         |            |:
































































 first_name |  surname  |   fathername   | is_student | is_online | row_number | comp 
------------+-----------+----------------+------------+-----------+------------+------
 Артур      | Вафин     | Фердинандович  | t          | f         |            |     
 Артур      | Гетагазов | Магомедович    | t          | f         |            |     
 Азиз       | Джифов    | Хуршедшоевич   | t          | f         |            |     
 Филипп     | Карташов  | Дмитриевич     | t          | f         |            |     
 Ульяна     | Костылёва | Константиновна | t          | f         |            |     
 Олег       | Молотягин | Владимирович   | t          | f         |            |     
 Рустам     | Османов   | Исмаил оглы    | t          | f         |            |     
 Константин | Поздняков | Александрович  | t          | f         |            |     
 Андрей     | Пшеничный | Михайлович     | t          | f         |            |     
 Софья      | Суровнева | Дмитриевна     | t          | f         |            |:
































































 first_name |  surname  |   fathername   | is_student | is_online | row_number | comp 
------------+-----------+----------------+------------+-----------+------------+------
 Артур      | Вафин     | Фердинандович  | t          | f         |            |     
 Артур      | Гетагазов | Магомедович    | t          | f         |            |     
 Азиз       | Джифов    | Хуршедшоевич   | t          | f         |            |     
 Филипп     | Карташов  | Дмитриевич     | t          | f         |            |     
 Ульяна     | Костылёва | Константиновна | t          | f         |            |     
 Олег       | Молотягин | Владимирович   | t          | f         |            |     
 Рустам     | Османов   | Исмаил оглы    | t          | f         |            |     
 Константин | Поздняков | Александрович  | t          | f         |            |     
 Андрей     | Пшеничный | Михайлович     | t          | f         |            |     
 Софья      | Суровнева | Дмитриевна     | t          | f         |            |:
 first_name |  surname  |   fathername   | is_student | is_online | row_number | comp 
------------+-----------+----------------+------------+-----------+------------+------
 Артур      | Вафин     | Фердинандович  | t          | f         |            |     
 Артур      | Гетагазов | Магомедович    | t          | f         |            |     
 Азиз       | Джифов    | Хуршедшоевич   | t          | f         |            |     
 Филипп     | Карташов  | Дмитриевич     | t          | f         |            |     
 Ульяна     | Костылёва | Константиновна | t          | f         |            |     
 Олег       | Молотягин | Владимирович   | t          | f         |            |     
 Рустам     | Османов   | Исмаил оглы    | t          | f         |            |     
 Константин | Поздняков | Александрович  | t          | f         |            |     
 Андрей     | Пшеничный | Михайлович     | t          | f         |            |     
 Софья      | Суровнева | Дмитриевна     | t          | f         |            |     
(10 строк)

students=# SELECT first_name, fathername, is_online FROM group411;
 first_name |   fathername   | is_online 
------------+----------------+-----------
 Артур      | Фердинандович  | f
 Артур      | Магомедович    | f
 Азиз       | Хуршедшоевич   | f
 Филипп     | Дмитриевич     | f
 Ульяна     | Константиновна | f
 Олег       | Владимирович   | f
 Рустам     | Исмаил оглы    | f
 Константин | Александрович  | f
 Андрей     | Михайлович     | f
 Софья      | Дмитриевна     | f
(10 строк)

students=# SELECT first_name, fathername, is_online FROM group411;
 first_name |   fathername   | is_online 
------------+----------------+-----------
 Артур      | Фердинандович  | f
 Артур      | Магомедович    | f
 Азиз       | Хуршедшоевич   | f
 Филипп     | Дмитриевич     | f
 Ульяна     | Константиновна | f
 Олег       | Владимирович   | f
 Рустам     | Исмаил оглы    | f
 Константин | Александрович  | f
 Андрей     | Михайлович     | f
 Софья      | Дмитриевна     | f
(10 строк)

students=# SELECT first_name, fathername, is_online FROM group411 WHERE first_name='Артур';
UPDATE group411 SET is_online=true WHERE first_name='Андрей';
UPDATE group411 SET is_online=null WHERE surname='Вафин' or surname='Джифов';
 first_name |  fathername   | is_online 
------------+---------------+-----------
 Артур      | Фердинандович | f
 Артур      | Магомедович   | f
(2 строки)

UPDATE 1
UPDATE 2
students=# select surname, first_name, fathername, is_online from group411 order by surname;
select surname, first_name, fathername, is_online from group411 order by first_name;
  surname  | first_name |   fathername   | is_online 
-----------+------------+----------------+-----------
 Вафин     | Артур      | Фердинандович  | 
 Гетагазов | Артур      | Магомедович    | f
 Джифов    | Азиз       | Хуршедшоевич   | 
 Карташов  | Филипп     | Дмитриевич     | f
 Костылёва | Ульяна     | Константиновна | f
 Молотягин | Олег       | Владимирович   | f
 Османов   | Рустам     | Исмаил оглы    | f
 Поздняков | Константин | Александрович  | f
 Пшеничный | Андрей     | Михайлович     | t
 Суровнева | Софья      | Дмитриевна     | f
(10 строк)

  surname  | first_name |   fathername   | is_online 
-----------+------------+----------------+-----------
 Джифов    | Азиз       | Хуршедшоевич   | 
 Пшеничный | Андрей     | Михайлович     | t
 Гетагазов | Артур      | Магомедович    | f
 Вафин     | Артур      | Фердинандович  | 
 Поздняков | Константин | Александрович  | f
 Молотягин | Олег       | Владимирович   | f
 Османов   | Рустам     | Исмаил оглы    | f
 Суровнева | Софья      | Дмитриевна     | f
 Костылёва | Ульяна     | Константиновна | f
 Карташов  | Филипп     | Дмитриевич     | f
(10 строк)

students=# update group411 SET row_number=2, comp=4 where first_name = 'Софья';
UPDATE 1
students=# UPDATE group411 SET comp=4, row_number=1 WHERE surname='Гетагазов';
UPDATE 1
students=# select surname, first_name, fathername, is_online from group411 order by surname;
  surname  | first_name |   fathername   | is_online 
-----------+------------+----------------+-----------
 Вафин     | Артур      | Фердинандович  | 
 Гетагазов | Артур      | Магомедович    | f
 Джифов    | Азиз       | Хуршедшоевич   | 
 Карташов  | Филипп     | Дмитриевич     | f
 Костылёва | Ульяна     | Константиновна | f
 Молотягин | Олег       | Владимирович   | f
 Османов   | Рустам     | Исмаил оглы    | f
 Поздняков | Константин | Александрович  | f
 Пшеничный | Андрей     | Михайлович     | t
 Суровнева | Софья      | Дмитриевна     | f
(10 строк)

students=# select surname, first_name, fathername, is_online, row_number_comp from group411 order by surname;
ERROR:  column "row_number_comp" does not exist
СТРОКА 1: ...elect surname, first_name, fathername, is_online, row_number...
                                                               ^
students=# select surname, first_name, fathername, is_online, row_number, comp from group411 order by surname;
  surname  | first_name |   fathername   | is_online | row_number | comp 
-----------+------------+----------------+-----------+------------+------
 Вафин     | Артур      | Фердинандович  |           |            |     
 Гетагазов | Артур      | Магомедович    | f         |          1 |    4
 Джифов    | Азиз       | Хуршедшоевич   |           |            |     
 Карташов  | Филипп     | Дмитриевич     | f         |            |     
 Костылёва | Ульяна     | Константиновна | f         |            |     
 Молотягин | Олег       | Владимирович   | f         |            |     
 Османов   | Рустам     | Исмаил оглы    | f         |            |     
 Поздняков | Константин | Александрович  | f         |            |     
 Пшеничный | Андрей     | Михайлович     | t         |            |     
 Суровнева | Софья      | Дмитриевна     | f         |          2 |    4
(10 строк)

students=# UPDATE group411 SET row_number=3, comp=4 where first_name = 'Ульяна';UPDATE 1
students=# update group411 SET row_number=2.1,comp=4 where first_name = 'Рустам';
UPDATE 1
students=# select surname, first_name, fathername, is_online, row_number, comp from group411 order by surname;
  surname  | first_name |   fathername   | is_online | row_number | comp 
-----------+------------+----------------+-----------+------------+------
 Вафин     | Артур      | Фердинандович  |           |            |     
 Гетагазов | Артур      | Магомедович    | f         |          1 |    4
 Джифов    | Азиз       | Хуршедшоевич   |           |            |     
 Карташов  | Филипп     | Дмитриевич     | f         |            |     
 Костылёва | Ульяна     | Константиновна | f         |          3 |    4
 Молотягин | Олег       | Владимирович   | f         |            |     
 Османов   | Рустам     | Исмаил оглы    | f         |          2 |    4
 Поздняков | Константин | Александрович  | f         |            |     
 Пшеничный | Андрей     | Михайлович     | t         |            |     
 Суровнева | Софья      | Дмитриевна     | f         |          2 |    4
(10 строк)

students=# update group411 SET row_number=2.1,comp=1 where first_name = 'Рустам';
UPDATE 1
students=# UPDATE group411 SET row_number=4, comp=3.2 WHERE surname='Поздняков';UPDATE 1
students=# select surname, first_name, fathername, is_online, row_number, comp from group411 order by surname;
  surname  | first_name |   fathername   | is_online | row_number | comp 
-----------+------------+----------------+-----------+------------+------
 Вафин     | Артур      | Фердинандович  |           |            |     
 Гетагазов | Артур      | Магомедович    | f         |          1 |    4
 Джифов    | Азиз       | Хуршедшоевич   |           |            |     
 Карташов  | Филипп     | Дмитриевич     | f         |            |     
 Костылёва | Ульяна     | Константиновна | f         |          3 |    4
 Молотягин | Олег       | Владимирович   | f         |            |     
 Османов   | Рустам     | Исмаил оглы    | f         |          2 |    1
 Поздняков | Константин | Александрович  | f         |          4 |    3
 Пшеничный | Андрей     | Михайлович     | t         |            |     
 Суровнева | Софья      | Дмитриевна     | f         |          2 |    4
(10 строк)

students=# select surname, first_name, fathername, is_online o, row_number r, comp c from group411 order by surname;
  surname  | first_name |   fathername   | o | r | c 
-----------+------------+----------------+---+---+---
 Вафин     | Артур      | Фердинандович  |   |   |  
 Гетагазов | Артур      | Магомедович    | f | 1 | 4
 Джифов    | Азиз       | Хуршедшоевич   |   |   |  
 Карташов  | Филипп     | Дмитриевич     | f |   |  
 Костылёва | Ульяна     | Константиновна | f | 3 | 4
 Молотягин | Олег       | Владимирович   | f |   |  
 Османов   | Рустам     | Исмаил оглы    | f | 2 | 1
 Поздняков | Константин | Александрович  | f | 4 | 3
 Пшеничный | Андрей     | Михайлович     | t |   |  
 Суровнева | Софья      | Дмитриевна     | f | 2 | 4
(10 строк)

students=# select surname, first_name, fathername, is_online o, row_number r, comp c from group411 row_number=2 order by surname;
ERROR:  syntax error at or near "="
СТРОКА 1: ...e o, row_number r, comp c from group411 row_number=2 order b...
                                                               ^
students=# select surname, first_name, fathername, is_online o, row_number r, comp c from group411 where row_number=2 order by surname;
  surname  | first_name | fathername  | o | r | c 
-----------+------------+-------------+---+---+---
 Османов   | Рустам     | Исмаил оглы | f | 2 | 1
 Суровнева | Софья      | Дмитриевна  | f | 2 | 4
(2 строки)

students=# select surname, first_name, fathername, is_online o, row_number r, comp c from group411 where comp=4 order by surname;
  surname  | first_name |   fathername   | o | r | c 
-----------+------------+----------------+---+---+---
 Гетагазов | Артур      | Магомедович    | f | 1 | 4
 Костылёва | Ульяна     | Константиновна | f | 3 | 4
 Суровнева | Софья      | Дмитриевна     | f | 2 | 4
(3 строки)

students=# select surname, first_name, fathername, is_online o, row_number r, comp c from group411 where is_online=false by surname;
ERROR:  syntax error at or near "by"
СТРОКА 1: ...ber r, comp c from group411 where is_online=false by surname...
                                                               ^
students=# select surname, first_name, fathername, is_online o, row_number r, comp c from group411 where is_online=f order by surname;
ERROR:  column "f" does not exist
СТРОКА 1: ...ow_number r, comp c from group411 where is_online=f order by...
                                                               ^
students=# select surname, first_name, fathername, is_online o, row_number r, comp c from group411 where is_online=false;
  surname  | first_name |   fathername   | o | r | c 
-----------+------------+----------------+---+---+---
 Карташов  | Филипп     | Дмитриевич     | f |   |  
 Молотягин | Олег       | Владимирович   | f |   |  
 Суровнева | Софья      | Дмитриевна     | f | 2 | 4
 Гетагазов | Артур      | Магомедович    | f | 1 | 4
 Костылёва | Ульяна     | Константиновна | f | 3 | 4
 Османов   | Рустам     | Исмаил оглы    | f | 2 | 1
 Поздняков | Константин | Александрович  | f | 4 | 3
(7 строк)

students=# select surname, first_name, fathername, is_online o, row_number r, comp c from group411 where is_online=true;
  surname  | first_name | fathername | o | r | c 
-----------+------------+------------+---+---+---
 Пшеничный | Андрей     | Михайлович | t |   |  
(1 строка)
students=# select surname, first_name, fathername, is_online o, row_number r, comp c from group411 where comp<row_number;
  surname  | first_name |  fathername   | o | r | c 
-----------+------------+---------------+---+---+---
 Османов   | Рустам     | Исмаил оглы   | f | 2 | 1
 Поздняков | Константин | Александрович | f | 4 | 3
(2 строки)

students=# UPDATE group411 SET comp=2 WHERE is_online=true;
UPDATE 1
students=# select surname, first_name, fathername, is_online o, row_number r, comp c from group411 order by surname;
  surname  | first_name |   fathername   | o | r | c 
-----------+------------+----------------+---+---+---
 Вафин     | Артур      | Фердинандович  |   |   |  
 Гетагазов | Артур      | Магомедович    | f | 1 | 4
 Джифов    | Азиз       | Хуршедшоевич   |   |   |  
 Карташов  | Филипп     | Дмитриевич     | f |   |  
 Костылёва | Ульяна     | Константиновна | f | 3 | 4
 Молотягин | Олег       | Владимирович   | f |   |  
 Османов   | Рустам     | Исмаил оглы    | f | 2 | 1
 Поздняков | Константин | Александрович  | f | 4 | 3
 Пшеничный | Андрей     | Михайлович     | t |   | 2
 Суровнева | Софья      | Дмитриевна     | f | 2 | 4
(10 строк)

students=# 
