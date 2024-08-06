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

COPY users
FROM '/Users/m4ks0n/study/IU7/sem6/dbcourse/bmstu-iu7-sem6-bdcoursework/doc/testdata/users.csv'
DELIMITER ','
CSV HEADER;
