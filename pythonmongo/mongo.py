from pymongo import MongoClient
import pymysql
#my_client = MongoClient('mongodb+srv://root:1234@neotubekids.e68cc.mongodb.net/project?retryWrites=true&w=majority')
my_client = MongoClient('localhost:27017')


def insert(col):
    print("id: ", end='')
    pid = input()
    print('pw: ', end='')
    pw = input()
    print('name: ', end='')
    name = input()
    print('tel: ', end='')
    tel = input()
    col.insert_one({"id": pid, "pw": pw, "name": name, "tel": tel})


def read(col):
    if col.find_one() is None:
        print("found no documents")
        return
    for x in col.find():
        print(x)


def to_mysql(col):
    if col.find_one() is None:
        return
    conn = pymysql.connect(host='localhost', port=3366, user='root', passwd='1234',
                           db='shop', charset='utf8')
    curs = conn.cursor()

    for x in col.find():
        sql = f'''insert into member values ('{x["id"]}', '{x["pw"]}', '{x["name"]}', '{x["tel"]}')'''
        curs.execute(sql)

    conn.commit()
    curs.close()
    conn.close()


if __name__ == '__main__':
    mydb = my_client['project']
    if mydb.get_collection('member') is None:
        mydb.create_collection('member')
    mycol = mydb['member']

    while True:
        print('1:insert 2:read 3:import_mysql 4:drop 0:exit>>', end='')
        s = input()
        if s == '1':
            insert(mycol)
        elif s == '2':
            read(mycol)
        elif s == '3':
            to_mysql(mycol)
        elif s == '4':
            mydb.drop_collection('member')
            mydb.create_collection('member')
            print('drop')
        elif s == '0':
            break
