drop table if EXISTS tractors CASCADE;
create table if not exists tractors
(
    id int,
    model VARCHAR(64),
    release_year INT,
    enginetype VARCHAR(64),
    enginemodel VARCHAR(64),
    enginepower INT,
    fronttiresize INT,
    backtiresize INT,
    wheelsamount INT,
    tankcapacity INT,
    ecologicalstandart VARCHAR(64),
    length FLOAT,
    width FLOAT,
    cabinheight FLOAT
);

drop table if exists assemblylines CASCADE;
create table if not exists assemblylines
(
    id int,
    name VARCHAR(64),
    length FLOAT,
    height FLOAT,
    width FLOAT,
    status VARCHAR(64),
    production INT,
    downtime INT,
    inspectionsamountperyear INT,
    lastinspectiondate date,
    nextinspectiondate date,
    defectrate int
);

drop table if exists tractor_line CASCADE;
create table if not exists tractor_line
(
    tractorid int,
    lineid int
);

drop table if exists details CASCADE;
create table if not exists details
(
    id int,
    name VARCHAR(64),
    country VARCHAR(64),
    amount INT,
    price FLOAT,
    length INT,
    height INT,
    width INT
);

drop table if exists line_detail CASCADE;
create table if not exists line_detail
(
    lineid int,
    detailid int
);

drop table if exists users CASCADE;
create table if not exists users
(
    id int,
    name VARCHAR(64),
    surname VARCHAR(64),
    fatherame VARCHAR(64),
    department VARCHAR(64),
    email VARCHAR(64),
    password nchar(64),
    dateofbirth date,
    sex VARCHAR(64),
    role VARCHAR(64)
);

drop table if exists detailorders CASCADE;
create table if not exists detailorders
(
    id int,
    userid int,
    requestid int, 
    status VARCHAR(64),
    totalprice float,
    orderdate timestamp
);

drop table if exists order_detail CASCADE;
create table if not exists order_detail
(
    orderid int,
    detailid int,
    detailsamount int
);

drop table if exists servicerequests CASCADE;
create table if not exists servicerequests
(
    id int,
    lineid int,
    userid int,
    requestdate timestamp,
    status VARCHAR(64),
    type VARCHAR(64),
    description text
);

drop table if exists servicereports CASCADE;
create table if not exists servicereports
(
    id int,
    lineid int,
    userid int, 
    requestid int, 
    opendate timestamp,
    closedate timestamp,
    totalprice float,
    description text
);