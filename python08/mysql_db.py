import pymysql


def read(code):
    conn = pymysql.connect(host='localhost', port=3366, user='root', passwd='1234',
                           db='finance', charset='utf8')

    print('연결 성공', conn)

    curs = conn.cursor()

    sql = f"select * from finance where code = {code}"
    curs.execute(sql)

    rows = curs.fetchall()

    conn.close()
    return rows


def create(code, name, now, high, low):
    conn = pymysql.connect(host='localhost', port=3366, user='root', passwd='1234',
                           db='finance', charset='utf8')

    print('연결 성공', conn)

    curs = conn.cursor()

    sql = f"insert into finance values ('{code}', '{name}', '{now}', '{high}', '{low}')"
    curs.execute(sql)

    conn.commit()

    conn.close()


def update(code, name, now, high, low):
    conn = pymysql.connect(host='localhost', port=3366, user='root', passwd='1234',
                           db='finance', charset='utf8')

    print('연결 성공', conn)

    curs = conn.cursor()

    sql = f"update finance set name = '{name}', now = '{now}', high = '{high}', low = '{low}' where code = '{code}'"
    curs.execute(sql)

    conn.commit()

    conn.close()


def delete(code):
    conn = pymysql.connect(host='localhost', port=3366, user='root', passwd='1234',
                           db='finance', charset='utf8')

    print('연결 성공', conn)

    curs = conn.cursor()

    sql = f"delete from finance where code = {code}"
    curs.execute(sql)

    conn.commit()

    conn.close()
