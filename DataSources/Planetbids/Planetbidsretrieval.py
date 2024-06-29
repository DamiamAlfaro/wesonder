from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://vendors.planetbids.com/portal/28159/bo/bo-search")

title = driver.title

driver.implicitly_wait(100)

# Needed to check for any new bids
#totalMunicipalityBids = driver.find_element(By.CLASS_NAME, 'bids-table-filter-message')

# Tabulation of bids
start = driver.find_element(By.ID,"ember20")

firstclass = start.find_element(By.CLASS_NAME,"table-overflow-container")

tabulationStart = firstclass.find_elements(By.TAG_NAME,"table")

selectedTableElement = tabulationStart[1]

tableBody = selectedTableElement.find_element(By.TAG_NAME,"tbody")

bidsTable = tableBody.find_elements(By.TAG_NAME,"tr")

def scrollWebpage(container):
	driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", container)

rowCount = 0
newCount = len(bidsTable)

while newCount > rowCount:
	rowCount = newCount
	scrollWebpage(firstclass)
	time.sleep(5)
	newCount = len(bidsTable)
	print(len(bidsTable))


























