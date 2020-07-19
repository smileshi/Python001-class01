from random import randint
import pymysql
import pandas as pd
import random as rd

# for i in range(10):
#     print(i)
#     i = 5 

# for i in range(5):
#     age = rd.randint(20,60)
#     sql = "insert data_a(id, age) VALUES('" f'{i}' "','" f'{age}' "')"
#     print(sql)

def prepareData():        
    sql  =  'SELECT *  FROM movie_info'
    conn = pymysql.connect(
                host = "localhost",
                port = 3306,
                user = "root",
                password = "Welcome12",
                db = "test",
                charset = 'utf8mb4'
            )
    cursor = conn.cursor()
    for i in range(10):
        id = rd.randint(500,2000)
        age = rd.randint(20,60)
        sql = "insert data_a(id, age) VALUES('" f'{id}' "','" f'{age}' "')"    
        try:        
            cursor.execute(sql)        
            conn.commit()
        except:        
            conn.rollback()

    cursor.close()
    conn.close()
    # df = pd.read_sql(sql,conn)
    # print(df)
def readData():
    sql  =  'SELECT *  FROM data_a'
    conn = pymysql.connect(
                host = "localhost",
                port = 3306,
                user = "root",
                password = "XXXXX",
                db = "test",
                charset = 'utf8mb4'
            )
    df = pd.read_sql(sql,conn)
    return df

def readData2():
    sql  =  'SELECT *  FROM data_b'
    conn = pymysql.connect(
                host = "localhost",
                port = 3306,
                user = "root",
                password = "XXXXX",
                db = "test",
                charset = 'utf8mb4'
            )
    df = pd.read_sql(sql,conn)
    return df

def head10(data):
    result = data.head(10)
    print(result)

def getColumn(data, column):
    result = data[column]
    print(result)

def countByColumn(data, column):
    result = data[column].value_counts()
    print(result)

def filterData(data):    
    result = data[ ( data['id']<1000 ) & ( data['age']>30 )]
    print(result)

def groupData(data):
    result = data.groupby('id').agg({'order_id':'count'})
    print(result)

def mergeData(data1, data2):
    result = pd.merge(data1, data2, on= 'id', how='inner')
    print(result)

def unionData(data1, data2):
    result = pd.concat([data1, data2])
    print(result)

def deleteRow(data):
    result = data.drop(data[data['id']==10].index,axis=0)
    print(result)

def deleteColumn(data):
    del data['order_id']
    print(data)

if __name__ == "__main__":
    #1
    data = readData()
    data2 = readData2()
    #2
    head10(data)
    # 3
    getColumn(data, 'id')
    # 4
    countByColumn(data, 'id')
    # 5
    filterData(data)
    # 6
    groupData(data)
    # 7
    mergeData(data, data2)
    # 8
    unionData(data, data2)
    # 9
    deleteRow(data)
    # 10
    deleteColumn(data2)
    
