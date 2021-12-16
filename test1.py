import mysql.connector
from mysql.connector import connection
from mysql.connector.errors import DatabaseError, Error
from mysql_connection import get_connection
#연결하는 코드
#try 라고 나오면 들여쓰기 되어있는 문장들을 실행하라는 뜻
try:
    connection = get_connection()

    if connection.is_connected():
        db_info = connection.get_server_info()
        print('MySQL info',db_info)
#위의 코드를 실행하다가 문제가 생시면 except를 실행하라는 뜻
except Error as e :
    print('Error while connecting to MySQL',e)
#finally는 try에서 에러가 나든 안나든 무조건 실행하라는 뜻
finally :
    if connection.is_connected():
        connection.close()
        print('MySQL connection is closed')
    else:
        print('connection does not exist')