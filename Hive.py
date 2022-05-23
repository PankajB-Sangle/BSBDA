sudo su hduser

cd

cd /usr/local/hadoop

start-dfs.sh

start-yarn.sh

 jps

 cd /usr/local/hive/bin

 ./hive

hive> show databases;

hive> use student

hive> show tables;

hive> CREATE EXTERNAL TABLE FlightInfo1( FID INT, Arrival STRING, Departure STRING)ROW FORMAT DELIMITED FIELDS TERMINATED BY ',';

hive> LOAD DATA LOCAL INPATH '/home/student/FlightInfo.csv' INTO TABLE FlightInfo1;Loading data to table student.flightinfo1

hive> DESCRIBE FlightInfo1;

hive> SELECT * FROM FlightInfo1;

hive> INSERT INTO FlightInfo1 VALUES (1002,'LA','Vegas');

hive> SELECT * FROM FlightInfo1;

hive> ALTER TABLE FlightInfo1 ADD COLUMNS (cust string);

hive> DESCRIBE FlightInfo1;

hive> INSERT INTO FlightInfo1 VALUES (1005,'LA','Vegas','Jake');

hive> SELECT * FROM FlightInfo1;

hive> CREATE EXTERNAL TABLE CustInfo1( CID INT, Name STRING, Age INT) ROW
FORMAT DELIMITED FIELDS TERMINATED BY ',';

hive> LOAD DATA LOCAL INPATH '/home/student/CustInfo.csv' INTO TABLE CustInfo1;
Loading data to table student.custinfo1

hive> DESCRIBE CustInfo1;

hive> SELECT * FROM CustInfo1;

hive> INSERT INTO FlightInfo1 VALUES (1006,'LA','Vegas','Jason');

hive> select c.cid, c.name, c.age, f.arrival ,f.departure from CustInfo1 c LEFT OUTER JOIN
FlightInfo1 f ON (c.name=f.cust);

hive> CREATE INDEX index_arrival ON TABLE FlightInfo1(Arrival) AS
'org.apache.hadoop.hive.ql.index.compact.CompactIndexHandler' WITH DEFERRED REBUILD;

hive> SHOW INDEX ON FlightInfo1;

hive> DROP INDEX index_arrival ON FlightInfo1;

