CREATE database database1;
USE database1;
CREATE TABLE example(
id INT NOT NULL AUTO_INCREMENT, 
PRIMARY KEY(id),
 name VARCHAR(30), 
 age INT);
INSERT INTO example (name,age) VALUES ('flanders',25);
-- http://www.linuxhomenetworking.com/wiki/index.php/Quick_HOWTO_:_Ch34_:_Basic_MySQL_Configuration
GRANT ALL PRIVILEGES ON *.* to 'icesi'@'192.168.131.100' IDENTIFIED by '12345';
