from scrapy import cmdline
cmdline.execute("scrapy crawl icbc-us".split())



# #selenium测试
# from selenium import webdriver
# import time
#
# def main():
#     chrome_driver = 'E:\chromedriver\chromedriver.exe'  # chromedriver的文件位置
#     b = webdriver.Chrome(executable_path=chrome_driver)
#     #b = webdriver.Chrome()
#     b.get('https://www.baidu.com')
#     time.sleep(5)
#     b.quit()
#
# if __name__ == '__main__':
#     main()