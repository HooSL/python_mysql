import mysql.connector
from mysql.connector import connection
from mysql.connector.errors import DatabaseError, Error
from mysql_connection import get_connection
#연결하는 코드
#try 라고 나오면 들여쓰기 되어있는 문장들을 실행하라는 뜻
try:
    connection = get_connection()

    # 튜플로 원하는 값 액세스하기
    query = ''' select * 
                from test
                where id = %s;'''
    param = (3,)

    cursor = connection.cursor()

    cursor.execute(query,param)

    # select문은 아래 내용이 필요하다.
    record_list = cursor.fetchall()
    print(record_list)

    #데이터 하나씩 액세스해서 보기
    for row in record_list:
        print('id = ',row[0])
        print('name = ',row[1])
        print('date = ',row[2].isoformat())

#위의 코드를 실행하다가 문제가 생시면 except를 실행하라는 뜻
except Error as e :
    print('Error while connecting to MySQL',e)
#finally는 try에서 에러가 나든 안나든 무조건 실행하라는 뜻
finally :
    cursor.close()
    if connection.is_connected():
        connection.close()
        print('MySQL connection is closed')
    else:
        print('connection does not exist')