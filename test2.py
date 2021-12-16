import mysql.connector
from mysql_connection import get_connection
try:
    #1. DB에 연결
    connection = get_connection()

    name = 'Harry'
    #date = '2021-12-15'

    #2. 쿼리문 만들고
    query = '''insert into test(name)
                values(%s);'''
    #2-1. 파이썬에서 튜플을 만들때 데이터가 1개인 경우에는 ,를 꼭 작성해준다.
    record = (name,)

    #3. 커넥션으로부터 커서를 가져온다
    cursor = connection.cursor()

    #4. 쿼리문을 커서에 넣어서 실행한다.
    cursor.execute(query,record)

    #5. 커넥션을 커밋한다 -> 디비에 영구적으로 반영하라는 뜻
    connection.commit()

except mysql.connector.Error as e:
    print('Error',e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print('MySQL connection is closed')