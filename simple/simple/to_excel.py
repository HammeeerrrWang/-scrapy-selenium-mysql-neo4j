import pandas as pd
import pymysql

connection = pymysql.connect(host="localhost", port=3306, user="root", password="123456", db="hw_job", charset="utf8")

query = 'select * from hw'

df = pd.read_sql_query(query,connection)

connection.close()

excel_filename = r'C:\Users\wsy19\Desktop\找工作\实习\数据获取+数据库+可视化\neo4j相关\neo4j_data_all.xlsx'

df.to_excel(excel_filename, index=True)


