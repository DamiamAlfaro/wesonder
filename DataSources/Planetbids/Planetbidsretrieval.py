from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



# Scrolls down within the table container
def scroll_table_container(container, scroll_pause_time=1):
    last_height = driver.execute_script("return arguments[0].scrollHeight", container)
    
    while True:
        # Scroll down by a small amount within the container
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", container)
        
        # Wait to load the new content
        time.sleep(scroll_pause_time)
        
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return arguments[0].scrollHeight", container)
        if new_height == last_height:
            break
        last_height = new_height


# Input: bids list after scroll and each's general information
def getting_bid_general_information(self):
	bids_general_info = []
	for index in range(len(self)):
		try:
			current_bids = driver.find_element(By.CLASS_NAME,"table-overflow-container")
			bids = current_bids.find_elements(By.TAG_NAME,"tr")[2:4]

			print(f"{index}: {bids[index].text}")

			bids[index].click()
			WebDriverWait(driver,10).until(EC.presence_of_element_located((By.TAG_NAME,"h3")))
			try:
				element = driver.find_element(By.CLASS_NAME,"bid-detail-wrapper")
				bids_general_info.append(element.text.split("\n"))
			except Exception as exc:
				print("\nThere is something wrong with reading the general info\n")
				print(exc)

			driver.back()
			WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME,'table-overflow-container')))
		except Exception as exe:
			print("\nThere is something wrong with getting_bid_general_information\n")

	return bids_general_info


# Input: bid line items
def getting_bid_line_items(self):
	bids_line_items = []
	for index in range(len(self)):
		try:
			current_bids = driver.find_element(By.CLASS_NAME,"table-overflow-container")
			bids = current_bids.find_elements(By.TAG_NAME,"tr")[2:4]
			print(f"{index}: {bids[index].text}")

			bids[index].click()
			WebDriverWait(driver,10).until(EC.presence_of_element_located((By.TAG_NAME,"h3")))
			try:
				element = driver.find_element(By.CLASS_NAME,"bidLineItems")
				element.click()
				WebDriverWait(driver,10).until(EC.presence_of_element_located((By.)))
			except Exception as exc:
				print("\nThere is something wrong with getting the line items")
				print(exc)
			driver.back()
			driver.back()
			WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME,'table-overflow-container')))
		except Exception as exe:
			print("\nThere is soemthing wrong with getting_bid_line_items")







if __name__ == '__main__':
	driver = webdriver.Chrome()
	driver.get("https://vendors.planetbids.com/portal/28159/bo/bo-search")
	driver.implicitly_wait(10)

	# Identifies if the total number of bids in the municipality increased
	total_bids = driver.find_element(By.CLASS_NAME,"bids-table-filter-message") # int

	# Table container with all bids in the municipality's planetbids portal
	current_bids = driver.find_element(By.CLASS_NAME,"table-overflow-container") # element

	# Scrolls down through the table of bids (necessary to forbid overlooking data)
	#scroll_table_container(current_bids)

	# After scrolling, we put all bids in the webpage into a list; n bids
	bids = current_bids.find_elements(By.TAG_NAME,"tr")[2:4] # int

	# Acknowledges current window (we will be changing windows multiple times)
	main_window = driver.current_window_handle

	#getting_bid_general_information(bids)
	getting_bid_line_items(bids)












