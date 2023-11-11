import scrapy

from simple.items import SimpleItem 

import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scrapy.selector import Selector

class HwPhoneSpider(scrapy.Spider):
    name = "hw_phone"
    allowed_domains = ["www.career.huawei.com"]
    start_urls = ["https://career.huawei.com/reccampportal/portal5/campus-recruitment.html"]


    def __init__(self):
        
        self.driver = webdriver.Chrome()
        self.driver.wait = WebDriverWait(self.driver, 5)

    def parse(self, response):
        
        # self.driver.get(response.url)
        self.driver.get('https://career.huawei.com/reccampportal/portal5/campus-recruitment.html')
        for page_num in range(1, 5):  # 遍历4页
            
            time.sleep(5)
        # 等待页面加载完毕
            
            self.driver.wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="public-table"]')))
            
        # 获取更新后的网页源代码
            
            source = self.driver.page_source
            
            sel = Selector(text=source)

            jobs = sel.xpath('//div[@class="public-table"]')


            for job_name , job_location, education_background, job_class in zip(
                
                jobs.xpath('//div[@class="td"]/h6/text()').getall(), #职位名称

                jobs.xpath('//div[@id="jobList"]/div[4]/ul/li/a/div[2]/text()').getall(), #工作地

                jobs.xpath('//div[@class="th"]/p/text()').getall(),#教育背景

                jobs.xpath('//div[@class="th"][3]/text()').getall()#工作类型
            ):
                #传入pipeline
                yield {
                    
                    'job_name': job_name.strip(),
                    
                    'job_location': job_location.strip(),
                    
                    'education_background': education_background.strip(),

                    'job_class': job_class.strip()
                }
                
            self.driver.implicitly_wait(3)
            
            if page_num == 1:
                self.driver.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@class="fr module-page-switch"]/a')))
                self.driver.implicitly_wait(3)
                self.driver.execute_script("document.body.scrollTop += 1")#
                time.sleep(3)
                self.driver.find_element_by_xpath('//*[@class="fr module-page-switch"]/a').click()
                
            elif page_num == 2:                
                self.driver.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@class="fr module-page-switch"]/a[2]')))
                self.driver.implicitly_wait(3)
                self.driver.execute_script("document.body.scrollTop += 1") 
                time.sleep(3)              
                self.driver.find_element_by_xpath('//*[@class="fr module-page-switch"]/a[2]').click()

            elif page_num == 3:                
                self.driver.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@class="fr module-page-switch"]/a[2]')))
                self.driver.implicitly_wait(3)
                self.driver.execute_script("document.body.scrollTop += 1")      
                time.sleep(3)
                self.driver.find_element_by_xpath('//*[@class="fr module-page-switch"]/a[2]').click()
            else:
                
                break
            
        
        
        self.driver.close()