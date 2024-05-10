COPY tractors 
FROM '/Users/m4ks0n/study/IU7/sem5/bmstu-sem5-db/lab_01/tables/actors.csv'
DELIMITER ','
CSV HEADER;

COPY assemblylines
FROM '/Users/m4ks0n/study/IU7/sem5/bmstu-sem5-db/lab_01/tables/companies.csv'
DELIMITER ','
CSV HEADER;

COPY details
FROM '/Users/m4ks0n/study/IU7/sem5/bmstu-sem5-db/lab_01/tables/directors.csv'
DELIMITER ','
CSV HEADER;

COPY detailorders
FROM '/Users/m4ks0n/study/IU7/sem5/bmstu-sem5-db/lab_01/tables/films.csv'
DELIMITER ','
CSV HEADER;

COPY users
FROM '/Users/m4ks0n/study/IU7/sem5/bmstu-sem5-db/lab_01/tables/played.csv'
DELIMITER ','
CSV HEADER;

COPY servicerequests
FROM '/Users/m4ks0n/study/IU7/sem5/bmstu-sem5-db/lab_01/tables/played.csv'
DELIMITER ','
CSV HEADER;

COPY servicereports
FROM '/Users/m4ks0n/study/IU7/sem5/bmstu-sem5-db/lab_01/tables/played.csv'
DELIMITER ','
CSV HEADER;

COPY order_detail
FROM '/Users/m4ks0n/study/IU7/sem5/bmstu-sem5-db/lab_01/tables/played.csv'
DELIMITER ','
CSV HEADER;

COPY tractor_line
FROM '/Users/m4ks0n/study/IU7/sem5/bmstu-sem5-db/lab_01/tables/played.csv'
DELIMITER ','
CSV HEADER;

COPY line_detail
FROM '/Users/m4ks0n/study/IU7/sem5/bmstu-sem5-db/lab_01/tables/played.csv'
DELIMITER ','
CSV HEADER;