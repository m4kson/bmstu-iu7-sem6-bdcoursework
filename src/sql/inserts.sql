CREATE EXTENSION IF NOT EXISTS pgcrypto;

-- Вставка данных в таблицу tractors
INSERT INTO tractors (id, model, release_year, enginetype, enginemodel, enginepower, fronttiresize, backtiresize, wheelsamount, tankcapacity, ecologicalstandart, length, width, cabinheight)
VALUES 
(gen_random_uuid(), 'John Deere 5075E', 2020, 'Diesel', 'PowerTech 3029H', 75, 14, 18, 4, 90, 'Euro 6', 3.5, 1.8, 2.1),
(gen_random_uuid(), 'New Holland T7.190', 2019, 'Diesel', 'FPT Industrial NEF 6', 190, 16, 20, 4, 220, 'Euro 5', 3.8, 1.9, 2.2),
(gen_random_uuid(), 'Case IH Puma 185', 2021, 'Diesel', 'FPT Industrial NEF 6', 185, 18, 22, 4, 210, 'Tier 4B', 3.6, 1.8, 2.1);


-- Вставка данных в таблицу assemblylines
INSERT INTO assemblylines (id, name, length, height, width, status, production, downtime, inspectionsamountperyear, lastinspectiondate, nextinspectiondate, defectrate)
VALUES 
(gen_random_uuid(), 'Line 1', 100, 5, 3, 'Active', 100, 10, 12, '2023-01-01', '2024-01-01', 2),
(gen_random_uuid(), 'Line 2', 120, 6, 4, 'Active', 120, 15, 10, '2023-02-01', '2024-02-01', 3),
(gen_random_uuid(), 'Line 3', 80, 4, 3, 'Active', 80, 8, 8, '2023-03-01', '2024-03-01', 1);


-- Вставка данных в таблицу users
INSERT INTO users (id, name, surname, fatherame, department, email, password, dateofbirth, sex, role)
VALUES 
(gen_random_uuid(), 'Иван', 'Иванов', 'Иванович', 'Производство', 'ivan@example.com', 'password123', '1990-05-15', 'Мужской', 'Работник');

-- Вставка данных в таблицу details
INSERT INTO details (id, name, country, amount, price, length, width, height)
VALUES 
(gen_random_uuid(), 'Болт M12x30', 'Россия', 1000, 1.5, 30, 12, 12),
(gen_random_uuid(), 'Плоская шайба', 'Россия', 2000, 0.5, 15, 15, 2),
(gen_random_uuid(), 'Винт M8x30', 'Китай', 1500, 1.0, 30, 8, 8);

select * from servicerequests
select * from assemblylines
select * from users

INSERT INTO servicerequests (id, lineid, userid, requestdate, status, type, description)
VALUES 
(gen_random_uuid(), '9b609d2f-7e3c-4a6e-ada9-d03660bb5b80', 'b18d5594-82af-4bc9-8815-3668d89424c9', CURRENT_TIMESTAMP, 'открыта', 'ремонт', 'text sample');

-- Пример INSERT-запроса для таблицы servicereports 
INSERT INTO servicereports (id, lineid, userid, requestid, opendate, closedate, totalprice, description)
VALUES 
(gen_random_uuid(), 'a0de17d1-594e-4096-9f21-2b4d70bf764e', 'f4d00039-2025-4715-bb06-8ac8dd136162', 'f5fb51ed-72f9-4701-8c69-76812e093505', CURRENT_TIMESTAMP, '2024-05-09 11:30:00', 50.0, 'Замена подшипника выполнена успешно.');
