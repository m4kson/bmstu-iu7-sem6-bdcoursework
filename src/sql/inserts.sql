CREATE EXTENSION IF NOT EXISTS pgcrypto;

--вставка тестовых данных

-- Вставка данных в таблицу tractors
INSERT INTO tractors (model, release_year, enginetype, enginemodel, enginepower, fronttiresize, backtiresize, wheelsamount, tankcapacity, ecologicalstandart, length, width, cabinheight)
VALUES 
('John Deere 5075E', 2020, 'Diesel', 'PowerTech 3029H', 75, 14, 18, 4, 90, 'Euro 6', 3.5, 1.8, 2.1),
('New Holland T7.190', 2019, 'Diesel', 'FPT Industrial NEF 6', 190, 16, 20, 4, 220, 'Euro 5', 3.8, 1.9, 2.2),
('Case IH Puma 185', 2021, 'Diesel', 'FPT Industrial NEF 6', 185, 18, 22, 4, 210, 'Tier 4B', 3.6, 1.8, 2.1);


-- Вставка данных в таблицу assemblylines
INSERT INTO assemblylines (id, name, length, height, width, status, production, downtime, inspectionsamountperyear, lastinspectiondate, nextinspectiondate, defectrate)
VALUES 
('Line 1', 100, 5, 3, 'Active', 100, 10, 12, '2023-01-01', '2024-01-01', 2),
('Line 2', 120, 6, 4, 'Active', 120, 15, 10, '2023-02-01', '2024-02-01', 3),
('Line 3', 80, 4, 3, 'Active', 80, 8, 8, '2023-03-01', '2024-03-01', 1);


-- Вставка данных в таблицу users
INSERT INTO users (id, name, surname, fatherame, department, email, password, dateofbirth, sex, role)
VALUES 
('65e3c7db-c6ce-4b2f-9124-d9bf1c9c68c9', 'Иван', 'Иванов', 'Иванович', 'Производство', 'ivan@example.com', 'password123', '1990-05-15', 'Мужской', 'Работник');

-- Вставка данных в таблицу details
INSERT INTO details (id, name, country, amount, price, length, width, height)
VALUES 
('29c94e51-8dab-4d67-95f2-4fbb1bf6f95e', 'Болт M12x30', 'Россия', 1000, 1.5, 30, 12, 12),
('19c475f6-35ed-498b-8dab-46bcb4fdfa7b', 'Плоская шайба', 'Россия', 2000, 0.5, 15, 15, 2),
('7d0513b2-0a09-43a5-b3aa-21f01e252c77', 'Винт M8x30', 'Китай', 1500, 1.0, 30, 8, 8);

select * from servicerequests;
select * from servicereports;
select * from assemblylines;
select * from users;


--тест1 для триггера4 (вставка в таблицу заявок): статус линии должен измениться на "на обслуживании"
INSERT INTO servicerequests (id, lineid, userid, requestdate, status, type, description)
VALUES 
('fbf609cc-a5d1-4406-b858-60e50481f4a4', '12a8b960-924b-41f7-80c3-ccc393e4b274', '65e3c7db-c6ce-4b2f-9124-d9bf1c9c68c9', CURRENT_TIMESTAMP, 'открыта', 'ремонт', 'text sample');


--тест2 для триггера2 (вставка в таблицу отчетов): статус заявки на обслуживание должени измениться на "завершена"
-- Пример INSERT-запроса для т'блицы servicereports
INSERT INTO servicereports (id, lineid, userid, requestid, opendate, closedate, totalprice, description)
VALUES 
('0a4ec264-b524-4b83-ad7c-7f02005add4a', '12a8b960-924b-41f7-80c3-ccc393e4b274', '65e3c7db-c6ce-4b2f-9124-d9bf1c9c68c9', 'fbf609cc-a5d1-4406-b858-60e50481f4a4', '2024-05-09 11:30:00', '2024-05-09 15:30:00', 50.0, 'Замена подшипника выполнена успешно.');

--тест3 для триггера3 (вставка в таблицу отчетов): должно обновиться downtime и статус на "работает" (заявка будет на ремонт, поэтому поля техосмотров не меняются)
INSERT INTO servicerequests (id, lineid, userid, requestdate, status, type, description)
VALUES 
('f9c03b25-243e-47e4-a376-847538b86f68', '60c51385-4f28-4113-a6c8-55541534f6a4', '65e3c7db-c6ce-4b2f-9124-d9bf1c9c68c9', '2024-05-09 11:30:00', 'открыта', 'ремонт', 'text sample');

INSERT INTO servicereports (id, lineid, userid, requestid, opendate, closedate, totalprice, description)
VALUES 
('56763f79-a01f-4bcf-98d1-0cb45cddc3d7', '60c51385-4f28-4113-a6c8-55541534f6a4', '65e3c7db-c6ce-4b2f-9124-d9bf1c9c68c9', 'f9c03b25-243e-47e4-a376-847538b86f68', '2024-05-09 12:30:00', '2024-05-09 13:30:00', 150.0, 'Замена болта выполнена успешно.');

--тест4 для триггера3 (вставка в таблицу отчетов): должно обновиться downtime и статус на "работает", измениться LastInspectionDate и NextInspectionDate
INSERT INTO servicerequests (id, lineid, userid, requestdate, status, type, description)
VALUES 
('d481da61-d260-4b63-92fa-5aa9fe8d5ddc', '629ca7b0-908f-4e68-8a6f-ad17eba75a71', '65e3c7db-c6ce-4b2f-9124-d9bf1c9c68c9', '2024-05-09 11:30:00', 'открыта', 'техосмотр', 'text sample');

INSERT INTO servicereports (id, lineid, userid, requestid, opendate, closedate, totalprice, description)
VALUES 
('3059180a-7000-44c9-9d49-55afe7a498b5', '629ca7b0-908f-4e68-8a6f-ad17eba75a71', '65e3c7db-c6ce-4b2f-9124-d9bf1c9c68c9', 'd481da61-d260-4b63-92fa-5aa9fe8d5ddc', '2024-05-09 12:30:00', '2024-05-09 13:30:00', 10.0, 'Техосмотр пройден успешно.');



