COPY tractors (model, release_year, enginetype, enginepower, fronttiresize, backtiresize, wheelsamount, tankcapacity, ecologicalstandart, length, width, cabinheight)
FROM '/Users/m4ks0n/study/IU7/sem6/dbcourse/bmstu-iu7-sem6-bdcoursework/doc/testdata/tractors.csv'
DELIMITER ','
CSV HEADER;


COPY assemblylines (name, length, height, width, status, production, downtime, inspectionsamountperyear, lastinspectiondate, nextinspectiondate, defectrate)
FROM '/Users/m4ks0n/study/IU7/sem6/dbcourse/bmstu-iu7-sem6-bdcoursework/doc/testdata/assemblylines.csv'
DELIMITER ','
CSV HEADER;


COPY details (name, country, amount, price, length, height, width)
FROM '/Users/m4ks0n/study/IU7/sem6/dbcourse/bmstu-iu7-sem6-bdcoursework/doc/testdata/details.csv'
DELIMITER ','
CSV HEADER;

COPY "user" (name, surname, fathername, department, email, hashed_password, dateofbirth, sex, role, is_active, is_superuser, is_verified)
FROM '/Users/m4ks0n/study/IU7/sem6/dbcourse/bmstu-iu7-sem6-bdcoursework/doc/testdata/users.csv'
DELIMITER ','
CSV HEADER;

COPY line_detail (lineid, detailid)
FROM '/Users/m4ks0n/study/IU7/sem6/dbcourse/bmstu-iu7-sem6-bdcoursework/doc/testdata/line_detail.csv'
DELIMITER ','
CSV HEADER;

COPY tractor_line (tractorid, lineid)
FROM '/Users/m4ks0n/study/IU7/sem6/dbcourse/bmstu-iu7-sem6-bdcoursework/doc/testdata/tractor_line.csv'
DELIMITER ','
CSV HEADER;

COPY servicerequests (lineid, userid, requestdate, status, type, description)
FROM '/Users/m4ks0n/study/IU7/sem6/dbcourse/bmstu-iu7-sem6-bdcoursework/doc/testdata/requests.csv'
DELIMITER ','
CSV HEADER;

COPY servicereports (lineid, userid, requestid, opendate, closedate, totalprice, description)
FROM '/Users/m4ks0n/study/IU7/sem6/dbcourse/bmstu-iu7-sem6-bdcoursework/doc/testdata/report.csv'
DELIMITER ','
CSV HEADER;

COPY detailorders (userid, status, totalprice, orderdate)
FROM '/Users/m4ks0n/study/IU7/sem6/dbcourse/bmstu-iu7-sem6-bdcoursework/doc/testdata/orders.csv'
DELIMITER ','
CSV HEADER;

COPY order_detail (orderid, detailid, detailsamount)
FROM '/Users/m4ks0n/study/IU7/sem6/dbcourse/bmstu-iu7-sem6-bdcoursework/doc/testdata/order_detail.csv'
DELIMITER ','
CSV HEADER;
