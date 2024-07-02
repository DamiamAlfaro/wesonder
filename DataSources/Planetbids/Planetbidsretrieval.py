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
			# We need to refer to the initial bid tabulation each time in order to forbid
			# going astray
			current_bids = driver.find_element(By.CLASS_NAME,"table-overflow-container")
			bids = current_bids.find_elements(By.TAG_NAME,"tr")[2:4]

			# Just checking you know
			print(f"{index}: {bids[index].text}")

			# Clicks every <tr> element within the tabulation in the main page
			bids[index].click()

			# This is just a signal that checks if the click() was successful
			# The 'h3' is the first printable element found in the clicked tab
			WebDriverWait(driver,10).until(EC.presence_of_element_located((By.TAG_NAME,"h3")))
			try:
				# Apparently this is where all general info text is found...
				element = driver.find_element(By.CLASS_NAME,"bid-detail-wrapper")

				# Storing them into a list	
				bids_general_info.append(element.text.split("\n"))

			# We want to see if something is wrong without stoping the code, right?
			except Exception as exc:
				print("\n!!!")
				print("\nThere is something wrong with reading the general info\n")
				print("\n!!!\n")
				print(exc)

			# Remember that we need to go back for the next iteration to work
			driver.back()

			# Again, this is to check that each action worked
			WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME,'table-overflow-container')))
		except Exception as exe:
			print("\nThere is something wrong with getting_bid_general_information\n")

	# The list that will later be use for analysis
	return bids_general_info


# Input: bid line items
def getting_bid_line_items(self):

	# Where bid line items will be stored separated by a "\n"
	bids_line_items = []
	for index in range(len(self)):
		try:
			current_bids = driver.find_element(By.CLASS_NAME,"table-overflow-container")
			bids = current_bids.find_elements(By.TAG_NAME,"tr")[2:4]
			print(f"{index}: {bids[index].text}")

			# Clicks a bid <tr> element
			bids[index].click()

			# This is just a signal to make sure the click() worked
			WebDriverWait(driver,10).until(EC.presence_of_element_located((By.TAG_NAME,"h3")))

			# Why "try"? Because we are trying to collect every bid data, we want to be notified 
			# in case of any issues without breaking the code mon ami...
			try:
				# 
				element = driver.find_element(By.CLASS_NAME,"bidLineItems")
				element.click()
				element2 = driver.find_element(By.CLASS_NAME,"bid-line-items")
				bids_line_items.append(element2.text.split("\n"))

			except Exception as exc:
				print("\n!!!")
				print("\nThere is something wrong with getting the line items")
				print("\n!!!\n")
				print(exc)

			# Double because we are clicking twice; basically, every click(), one back()
			driver.back()
			driver.back()
			WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME,'table-overflow-container')))
		except Exception as exe:
			print("\nThere is soemthing wrong with getting_bid_line_items")

	return bids_line_items


def bid_results(self):
	
	# Where bid results will be stored
	bid_results_general = []


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

	'''
	The reason we will do this lists separated is because we want to broke things apart,
	i.e. compartmentalize each procedure and step in order to facilitate optimization in
	the nearby future upon each step at a time.
	'''

	# A list containing text of the general information of the bid broken by '\n'
	#getting_bid_general_information(bids)

	# A list containing text of the line items of the bid broken by '\n'
	#getting_bid_line_items(bids)














