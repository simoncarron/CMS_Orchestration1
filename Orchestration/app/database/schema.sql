drop table if exists cms;

create table cms (
  pkID integer primary key autoincrement
  ,name text
  ,management_ip_address text
  ,username text
  ,password text
);

INSERT INTO cms (name,management_ip_address,username,password)VALUES ('cms 01', '198.18.134.175', 'admin', 'dCloud123' );
INSERT INTO cms (name,management_ip_address,username,password)VALUES ('cms 02', '198.18.134.185', 'admin', 'dCloud123' );
INSERT INTO cms (name,management_ip_address,username,password)VALUES ('cms 03', '198.18.134.147', 'admin', 'dCloud123' );