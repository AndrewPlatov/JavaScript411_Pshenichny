CREATE TABLE publications (
    author_first_name varchar(16),
    author_surname varchar(32),
    year_of_publication integer,
    frequency varchar(10),
    issue_number varchar(16),
    is_continued boolean
);

INSERT INTO publications (author_first_name, author_surname, year_of_publication, frequency, issue_number, is_continued)
VALUES
('Лев', 'Толстой', 1869, 'year', '1', false),
('Джордж', 'Оруэлл', 1949, 'year', '1', false),
('Альберт', 'Месси', 1958, 'year', '1', false),
('Иван', 'Смирнов', 2000, 'week', '5', true),
('Мария', 'Петрова', 2010, 'month', '3', true),
('Сергей', 'Иванов', 2015, 'year', '7', true);