Last login: Tue Apr 22 22:17:21 on ttys000
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

postgres=# \c students
Вы подключены к базе данных "students" как пользователь "andrewpshenichny".
students=# CREATE TABLE publications (
    author_first_name varchar(16),
    author_surname varchar(32),
    year_of_publication integer,
    frequency ENUM('year', 'month', 'week'),
    issue_number varchar(16),
    is_continued boolean
);
ERROR:  type "enum" does not exist
СТРОКА 5:     frequency ENUM('year', 'month', 'week'),
                        ^
students=# CREATE TABLE publications (
    author_first_name varchar(16),
    author_surname varchar(32),
    year_of_publication integer,
    frequency ('year', 'month', 'week'),
    issue_number varchar(16),
    is_continued boolean
);
ERROR:  syntax error at or near "("
СТРОКА 5:     frequency ('year', 'month', 'week'),
                        ^
students=# CREATE TABLE publications (
    author_first_name varchar(16),
    author_surname varchar(32),
    year_of_publication integer,
    frequency ('year', 'month', 'week') integer,
    issue_number varchar(16),
    is_continued boolean
);
ERROR:  syntax error at or near "("
СТРОКА 5:     frequency ('year', 'month', 'week') integer,
                        ^
students=# CREATE TABLE publications (
    author_first_name varchar(16),
    author_surname varchar(32),
    year_of_publication integer,
    frequency varchar(10),
    issue_number varchar(16),
    is_continued boolean
);
CREATE TABLE
students=# INSERT INTO publications (author_first_name, author_surname, year_of_publication, frequency, issue_number, is_continued)
VALUES
('Лев', 'Толстой', 1869, 'year', '1', false),
('Джордж', 'Оруэлл', 1949, 'year', '1', false),
('Альберт', 'Месси', 1958, 'year', '1', false),
('Иван', 'Смирнов', 2000, 'week', '5', true),
('Мария', 'Петрова', 2010, 'month', '3', true),
('Сергей', 'Иванов', 2015, 'year', '7', true);
INSERT 0 6
students=# \d publications;
                                    Таблица "public.publications"
       Столбец       |          Тип          | Правило сортировки | Допустимость NULL | По умолчанию 
---------------------+-----------------------+--------------------+-------------------+--------------
 author_first_name   | character varying(16) |                    |                   | 
 author_surname      | character varying(32) |                    |                   | 
 year_of_publication | integer               |                    |                   | 
 frequency           | character varying(10) |                    |                   | 
 issue_number        | character varying(16) |                    |                   | 
 is_continued        | boolean               |                    |                   | 

students=# SELECT author_first_name, author_surname, year_of_publication, frequency, issue_number, is_continued FROM publications;
 author_first_name | author_surname | year_of_publication | frequency | issue_number | is_continued 
-------------------+----------------+---------------------+-----------+--------------+--------------
 Лев               | Толстой        |                1869 | year      | 1            | f
 Джордж            | Оруэлл         |                1949 | year      | 1            | f
 Альберт           | Месси          |                1958 | year      | 1            | f
 Иван              | Смирнов        |                2000 | week      | 5            | t
 Мария             | Петрова        |                2010 | month     | 3            | t
 Сергей            | Иванов         |                2015 | year      | 7            | t
(6 строк)

(END)
 author_first_name | author_surname | year_of_publication | frequency | issue_number | is_continued 
-------------------+----------------+---------------------+-----------+--------------+--------------
 Лев               | Толстой        |                1869 | year      | 1            | f
 Джордж            | Оруэлл         |                1949 | year      | 1            | f
 Альберт           | Месси          |                1958 | year      | 1            | f
 Иван              | Смирнов        |                2000 | week      | 5            | t
 Мария             | Петрова        |                2010 | month     | 3            | t
 Сергей            | Иванов         |                2015 | year      | 7            | t
(6 строк)

~
~
~
~
~
(END)




























































 author_first_name | author_surname | year_of_publication | frequency | issue_number | is_continued 
-------------------+----------------+---------------------+-----------+--------------+--------------
 Лев               | Толстой        |                1869 | year      | 1            | f
 Джордж            | Оруэлл         |                1949 | year      | 1            | f
 Альберт           | Месси          |                1958 | year      | 1            | f
 Иван              | Смирнов        |                2000 | week      | 5            | t
 Мария             | Петрова        |                2010 | month     | 3            | t
 Сергей            | Иванов         |                2015 | year      | 7            | t
(6 строк)

~
~
~
~
~
students=# 



























































students=# 
