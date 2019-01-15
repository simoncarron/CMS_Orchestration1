drop table if exists cms;
create table cms (
  pkID integer primary key autoincrement
  ,name text
  ,management_ip_address text
  ,username text
  ,password text
);
INSERT INTO cms (text,management_ip_address,username,password)VALUES ('cms 01', '192.168.1.1', 'admin', 'admin' );
INSERT INTO cms (text,management_ip_address,username,password)VALUES ('cms 02', '192.168.1.2', 'admin', 'admin' );
INSERT INTO cms (text,management_ip_address,username,password)VALUES ('cms 03', '192.168.1.3', 'admin', 'admin' );

