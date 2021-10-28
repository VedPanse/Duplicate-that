from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
chrome_driver_path = "/Users/vedpanse/Desktop/Develope/chromedriver"

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")

URL = input("Enter the URL you want to scan: ")
file_name = input("Please enter the name of HTML file (ignore the '.html' extension): ")

driver = webdriver.Chrome(executable_path=chrome_driver_path, chrome_options=options)
driver.get(URL)

src = driver.page_source
driver.close()
f = open(f"{file_name}.html", "w")
f.write(src)
f.close()
