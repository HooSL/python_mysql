import mysql.connector
from datetime import datetime

try:
    #1. DB에 연결
    connection = mysql.connector.connect(host = ' ',database=' ',user=' ',password=' ')

    #2. 쿼리문 만들고

    current_time = datetime.now() #우리 컴퓨터의 시간을 가져온다(로컬 타임)실제론 이렇게 안한다

    query = '''insert into test(name,date)
                values(%s,%s);'''
    #2-1. 파이썬에서 튜플을 만들때 데이터가 1개인 경우에는 ,를 꼭 작성해준다. (데이터 여러개 집어넣기)
    record = [ ('qqq',current_time) ,('yyy',current_time),('ppp',current_time) ]

    #3. 커넥션으로부터 커서를 가져온다
    cursor = connection.cursor()

    #4. 쿼리문을 커서에 넣어서 실행한다.
    cursor.executemany(query,record)

    #5. 커넥션을 커밋한다 -> 디비에 영구적으로 반영하라는 뜻
    connection.commit()

except mysql.connector.Error as e:
    print('Error',e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print('MySQL connection is closed')