CREATE TABLE audition (
	ID int PRIMARY KEY AUTO_INCREMENT,
    studentName varchar(40),
    instrument varchar(25),
    etudeScore float,
    sightReadingScore float,
    totalScore float
);

SELECT * from audition;

INSERT INTO audition (studentName, instrument, etudeScore, sightReadingScore, totalScore)
VALUES ('Junhui Park', 'Flute', 60, 33, 93);

INSERT INTO audition (studentName, instrument, etudeScore, sightReadingScore, totalScore)
VALUES ('Shinyue Chen', 'Clarinet', 53.2, 36.3, 89.5);

INSERT INTO audition (studentName, instrument, etudeScore, sightReadingScore, totalScore)
VALUES ('Daichi Takimoto', 'French Horn', 59.5, 37.2, 96.7);

INSERT INTO audition (studentName, instrument, etudeScore, sightReadingScore, totalScore)
VALUES ('Jenevieve Groom', 'Saxophone', 50.6, 30.8, 81.4);

INSERT INTO audition (studentName, instrument, etudeScore, sightReadingScore, totalScore)
VALUES ('Audrey Mitchell', 'Euphonium', 60, 35, 95);

INSERT INTO audition (studentName, instrument, etudeScore, sightReadingScore, totalScore)
VALUES ('Olivia Ling', 'Flute', 55, 33, 88);

INSERT INTO audition (studentName, instrument, etudeScore, sightReadingScore, totalScore)
VALUES ('Esha Sajjan', 'Clarinet', 52.3, 34, 86.3);

INSERT INTO audition (studentName, instrument, etudeScore, sightReadingScore, totalScore)
VALUES ('Susanna Cho', 'Oboe', 60.25, 37, 97.25);

INSERT INTO audition (studentName, instrument, etudeScore, sightReadingScore, totalScore)
VALUES ('Samantha Mendez', 'Bassoon', 58, 36, 94);

INSERT INTO audition (studentName, instrument, etudeScore, sightReadingScore, totalScore)
VALUES ('Derek Lee', 'Trumpet', 59, 33, 92);

INSERT INTO audition (studentName, instrument, etudeScore, sightReadingScore, totalScore)
VALUES ('Jesse Crespo', 'Trumpet', 53.2, 34.3, 87.5);

INSERT INTO audition (studentName, instrument, etudeScore, sightReadingScore, totalScore)
VALUES ('Amelie Roy', 'Trombone', 52.9, 31.1, 84);

INSERT INTO audition (studentName, instrument, etudeScore, sightReadingScore, totalScore)
VALUES ('Issac Lee', 'Percussion', 60, 40, 100);

INSERT INTO audition (studentName, instrument, etudeScore, sightReadingScore, totalScore)
VALUES ('Emma Hoover', 'Percussion', 52.3, 31.2, 83.5);

INSERT INTO audition (studentName, instrument, etudeScore, sightReadingScore, totalScore)
VALUES ('Charles Buck', 'Tuba', 55.2, 33, 88.2);

INSERT INTO audition (studentName, instrument, etudeScore, sightReadingScore, totalScore)
VALUES ('Irene Tang', 'French Horn', 60, 40, 100);

DROP TABLE audition