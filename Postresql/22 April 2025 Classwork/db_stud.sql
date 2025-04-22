CREATE TABLE group411(
    first_name varchar(16),
    surname varchar(32),
    fathername varchar(32),
    is_student boolean,
    is_online boolean,
    row_number integer,
    comp integer
);

INSERT INTO group411(
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

SELECT first_name, fathername, is_online FROM group411;

-- Условия в запросах SQL

SELECT first_name, fathername, is_online FROM group411 WHERE first_name='Артур';
UPDATE group411 SET is_online=true WHERE first_name='Андрей';
UPDATE group411 SET is_online=null WHERE surname='Вафин' or surname='Джифов';

-- Упорядочивание в запросах

select surname, first_name, fathername, is_online from group411 order by surname;
select surname, first_name, fathername, is_online from group411 order by first_name;
