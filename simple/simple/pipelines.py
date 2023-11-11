
from itemadapter import ItemAdapter
import pymysql

class SimplePipeline:
    
    def process_item(self, item, spider):
        

        
        with open('book.json','a',encoding='utf-8')as fp:
            
            fp.write(str(item))
        
        
        return item

class Mysqlpipeline:
    def process_item(self, item, spider):
        
        job_name = item['job_name']

        job_location = item['job_location']

        education_background = item['education_background']

        job_class = item['job_class']

        database = pymysql.connect(host="localhost", port=3306, user="root", password="123456", db="hw_job", charset="utf8")

        cursor = database.cursor()

        cursor.execute('insert into hw(job_name, job_location, education_background, job_class) values(%s,%s,%s,%s)',(job_name, job_location, education_background, job_class))
        
        database.commit()

        cursor.close()

        database.close()

        return item