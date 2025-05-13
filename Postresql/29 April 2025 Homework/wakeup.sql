CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE activities (
    id SERIAL PRIMARY KEY,
    category_id INTEGER REFERENCES categories(id),
    start_time TIMESTAMP NOT NULL,
    end_time TIMESTAMP NOT NULL
);

CREATE TABLE sleep_periods (
    id SERIAL PRIMARY KEY,
    start_time TIMESTAMP NOT NULL,
    end_time TIMESTAMP NOT NULL
);

INSERT INTO categories (name) VALUES ('Работа'), ('Учёба'), ('Отдых');

INSERT INTO activities (category_id, start_time, end_time) VALUES
(1, '2024-04-25 09:00:00', '2024-04-25 11:00:00'),
(2, '2024-04-25 12:00:00', '2024-04-25 14:30:00'),
(3, '2024-04-25 15:00:00', '2024-04-25 16:00:00');

INSERT INTO sleep_periods (start_time, end_time) VALUES
('2024-04-25 23:00:00', '2024-04-26 07:00:00');