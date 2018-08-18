import pymysql as sql

sc=sql.conect('localhost','root','Zend','college')

cursor=sc.cursor()

sql="""INSERT INTO EMPOYEE(FIRST NAME,LAST NAME,AGE,SEX,INCOME)
VALUES('Mac','Mohan',20,'M',2000)"""

cursor.execute(sql)

#disconnect froom server
db.close()
