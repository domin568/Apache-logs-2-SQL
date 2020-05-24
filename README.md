## Store your apache2 logs in your mysql database
# Setup
```
CREATE DATABASE logdb
CREATE USER â'loguser'@'localhost' IDENTIFIED BY 'passwd';
GRANT ALL PRIVILEGES ON logdb.* TO 'loguser'@'localhost';

CREATE TABLE access (
id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
ip VARCHAR (20),
identd VARCHAR (100),
userid VARCHAR (100),
date DATETIME,
requestType VARCHAR (20),
resourcePath VARCHAR (4000),
protocol VARCHAR (20),
status INT UNSIGNED,
bytesReturned INT UNSIGNED,
referer VARCHAR (2000),
userAgent VARCHAR (2000)
)
```
In your apache2 global configuration file e.g. apache2.conf
```
LogFormat "%h %l %u [%{%Y-%m-%d %H:%M:%S}t] \"%r\" %>s %O \"%{Referer}i\" \"%{User-Agent}i\"" combinedISOdatetime
```
In your host configuration file e.g the one in sites-enabled folder
```
CustomLog "|/path/to/logsToSql.py" combinedISOdatetime
```

#Result
![](result.png) 
