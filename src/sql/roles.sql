-- Создание ролей (пользователей) с паролями
CREATE ROLE operator_production WITH 
NOSUPERUSER 
NOCREATEDB 
NOCREATEROLE 
CONNECTION LIMIT -1 
LOGIN 
PASSWORD 'operator';

CREATE ROLE service_specialist WITH 
NOSUPERUSER 
NOCREATEDB 
NOCREATEROLE 
CONNECTION LIMIT -1 
LOGIN 
PASSWORD 'specialist';

CREATE ROLE administrator WITH 
SUPERUSER 
CREATEDB 
CREATEROLE 
CONNECTION LIMIT -1 
LOGIN 
PASSWORD 'admin';

CREATE ROLE unauthorized_user WITH
NOSUPERUSER 
NOCREATEDB
NOCREATEROLE 
CONNECTION LIMIT -1;

-- Назначение прав ролям
GRANT SELECT ON 
tractors, 
assemblylines, 
servicereports, 
servicerequests, 
tractor_line 
TO operator_production;

GRANT UPDATE ON 
assemblylines, 
servicerequests
TO operator_production;

GRANT INSERT ON 
servicerequests
TO operator_production;

GRANT SELECT ON 
tractors, 
assemblylines, 
servicerequests, 
servicereports, 
details, 
detailorders, 
order_detail,
tractor_line,
line_detail
TO service_specialist;

GRANT UPDATE ON 
detailorders, 
servicereports, 
order_detail
TO service_specialist;

GRANT INSERT ON 
servicereports, 
detailorders,
order_detail
TO service_specialist;

GRANT ALL PRIVILEGES ON 
ALL TABLES 
IN SCHEMA public 
TO administrator;
