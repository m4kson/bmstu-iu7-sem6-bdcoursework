-- Создание ролей (пользователей) с паролями
CREATE ROLE operator_production WITH SUPERUSER CREATEDB CREATEROLE CONNECTION LIMIT -1 LOGIN PASSWORD 'operator';
CREATE ROLE service_specialist WITH NOSUPERUSER NOCREATEDB NOCREATEROLE CONNECTION LIMIT -1 LOGIN PASSWORD 'specialist';
CREATE ROLE administrator WITH NOSUPERUSER NOCREATEDB NOCREATEROLE CONNECTION LIMIT -1 LOGIN PASSWORD 'admin';
CREATE ROLE unauthorized_user WITH NOSUPERUSER NOCREATEDB NOCREATEROLE CONNECTION LIMIT -1;

-- Назначение прав ролям
GRANT SELECT ON Tractors, AssemblyLines, ServiceReports, ServiceRequests TO operator_production;
GRANT UPDATE ON AssemblyLines, ServiceRequests, Users TO operator_production;
GRANT INSERT ON ServiceRequests TO operator_production;

GRANT SELECT ON Tractors, AssemblyLines, ServiceRequests, ServiceReports, Details, DetailOrders TO service_specialist;
GRANT UPDATE ON DetailOrders, ServiceReports, Users TO service_specialist;
GRANT INSERT ON ServiceReports, DetailOrders TO service_specialist;

-- (*) Здесь следует уточнить, какие права должны быть у администратора
-- Предположим, что администратору должны быть предоставлены все возможные права на все таблицы
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO administrator;

-- Права для неавторизованных пользователей
REVOKE ALL ON Users FROM public; -- Убираем все права на таблицу Users
