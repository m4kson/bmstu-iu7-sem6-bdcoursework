CREATE EXTENSION IF NOT EXISTS pgcrypto;

--вставка тестовых данных

-- Вставка данных в таблицу tractors
INSERT INTO tractors (model, release_year, enginetype, enginepower, fronttiresize, backtiresize, wheelsamount, tankcapacity, ecologicalstandart, length, width, cabinheight)
VALUES 
('John Deere 5075E', 2020, 'Diesel', 75, 14, 18, 4, 90, 'Euro 6', 3.5, 1.8, 2.1),
('New Holland T7.190', 2019, 'Diesel', 190, 16, 20, 4, 220, 'Euro 5', 3.8, 1.9, 2.2),
('Case IH Puma 185', 2021, 'Diesel', 185, 18, 22, 4, 210, 'Tier 4B', 3.6, 1.8, 2.1);


-- Вставка данных в таблицу assemblylines
INSERT INTO assemblylines (name, length, height, width, status, production, downtime, inspectionsamountperyear, lastinspectiondate, nextinspectiondate, defectrate)
VALUES 
('Line 1', 100, 5, 3, 'работает', 100, 10, 12, '2023-01-01', '2024-01-01', 2),
('Line 2', 120, 6, 4, 'работает', 120, 15, 10, '2023-02-01', '2024-02-01', 3),
('Line 3', 80, 4, 3, 'работает', 80, 8, 8, '2023-03-01', '2024-03-01', 1);


-- Вставка данных в таблицу users
INSERT INTO users (id, name, surname, fatherame, department, email, password, dateofbirth, sex, role)
VALUES 
('65e3c7db-c6ce-4b2f-9124-d9bf1c9c68c9', 'Иван', 'Иванов', 'Иванович', 'Производство', 'ivan@example.com', 'password123', '1990-05-15', 'Мужской', 'Работник');

-- Вставка данных в таблицу details
INSERT INTO details (name, country, amount, price, length, width, height)
VALUES 
('Болт M12x30', 'Россия', 1000, 1.5, 30, 12, 12),
('Плоская шайба', 'Россия', 2000, 0.5, 15, 15, 2),
('Винт M8x30', 'Китай', 1500, 1.0, 30, 8, 8);

select * from servicerequests;
select * from servicereports;
select * from assemblylines;
select * from users;
select * from details;


--тест1 для триггера4 (вставка в таблицу заявок): статус линии должен измениться на "на обслуживании"    done
INSERT INTO servicerequests (lineid, userid, requestdate, status, type, description)
VALUES 
(1, 1, CURRENT_TIMESTAMP, 'открыта', 'ремонт', 'text sample');


--тест2 для триггера2 (вставка в таблицу отчетов): статус заявки на обслуживание должени измениться на "завершена"  done
-- Пример INSERT-запроса для т'блицы servicereports
INSERT INTO servicereports (lineid, userid, requestid, opendate, closedate, totalprice, description)
VALUES 
(1, 2, 1, '2024-05-09 11:30:00', '2024-05-09 15:30:00', 50.0, 'Замена подшипника выполнена успешно.');

--тест3 для триггера3 (вставка в таблицу отчетов): должно обновиться downtime и статус на "работает" (заявка будет на ремонт, поэтому поля техосмотров не меняются) done
INSERT INTO servicerequests (lineid, userid, requestdate, status, type, description)
VALUES 
(3, 3, '2024-05-09 11:30:00', 'открыта', 'ремонт', 'text sample');

INSERT INTO servicereports (lineid, userid, requestid, opendate, closedate, totalprice, description)
VALUES 
(3, 4, 2, '2024-05-09 12:30:00', '2024-05-09 13:30:00', 150.0, 'Замена болта выполнена успешно.');

--тест4 для триггера3 (вставка в таблицу отчетов): должно обновиться downtime и статус на "работает", измениться LastInspectionDate и NextInspectionDate done
INSERT INTO servicerequests (lineid, userid, requestdate, status, type, description)
VALUES 
(4, 5, '2024-05-09 11:30:00', 'открыта', 'техосмотр', 'text sample');

INSERT INTO servicereports (lineid, userid, requestid, opendate, closedate, totalprice, description)
VALUES 
(4, 6, 3, '2024-05-09 12:30:00', '2024-05-09 13:30:00', 10.0, 'Техосмотр пройден успешно.');



