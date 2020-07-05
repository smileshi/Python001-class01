#学习笔记
## 1. exceptions
## 2.use pymysql to connect db
 2.1 pip install PyMysql
 ```python
 conn = pymysql.connect(
            host = "localhost",
            port = 3306,
            user = "root",
            password = "1234123",
            db = "test",
            charset = 'utf8mb4'
        )
    
	cursor = conn.cursor()
	sql = "insert movie_info(movie_name, movie_type, movie_plan_date) VALUES('" f'{film_name}' "','" f'{film_type}' "','" f'{plan_date}' "')"
	print(sql)
	try:        
		cursor.execute(sql)        
		conn.commit()
	except:        
		conn.rollback()
```	
## 3.scrapy-redis
pip install scrapy-redis
