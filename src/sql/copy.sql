COPY tractors 
FROM '/Users/m4ks0n/study/IU7/sem6/dbcourse/bmstu-iu7-sem6-bdcoursework/doc/testdata/tractors.csv'
DELIMITER ','
CSV HEADER;

COPY assemblylines
FROM '/Users/m4ks0n/study/IU7/sem6/dbcourse/bmstu-iu7-sem6-bdcoursework/doc/testdata/assemblylines.csv'
DELIMITER ','
CSV HEADER;

COPY details
FROM '/Users/m4ks0n/study/IU7/sem6/dbcourse/bmstu-iu7-sem6-bdcoursework/doc/testdata/details.csv'
DELIMITER ','
CSV HEADER;

COPY users
FROM '/Users/m4ks0n/study/IU7/sem6/dbcourse/bmstu-iu7-sem6-bdcoursework/doc/testdata/users.csv'
DELIMITER ','
CSV HEADER;
