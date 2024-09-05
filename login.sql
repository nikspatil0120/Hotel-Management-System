DROP TABLE IF EXISTS login;

CREATE TABLE login
(
	Email_Address VARCHAR(250),
	Password VARCHAR(250) NOT NULL
);

INSERT INTO login (Email_Address, Password)
VALUES ('xyz@gmail.com', 'xyz@123');

SELECT * FROM login;
