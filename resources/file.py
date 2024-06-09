import csv
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

# Selenium WebDriver Configuration
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

# Open the target URL
url = 'https://www.kickstarter.com/discover'
driver.get(url)

# CSV file setup
csv_file = 'kickstarter_projects.csv'

# Check if URL is already in the CSV
def is_url_in_csv(url, csv_filename):
    try:
        with open(csv_filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if url in row:
                    return True
    except FileNotFoundError:
        open(csv_filename, 'a', newline='', encoding='utf-8').close()  # Create file if it does not exist
    return False

# Save a new URL to the CSV
def save_url_to_csv(url, csv_filename):
    with open(csv_filename, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([url])

# XPath selectors
project_card_xpath = "//*[@class='relative discovery-project-card']//span[@class='card-title type-20 medium lh24px clamp-1 mb0 relative']/a"
load_more_button_xpath = "//*[@id='main_content']//*[@class='load_more mt3']/a[@class='bttn bttn-primary theme--create bttn-medium']"

# Main scraping loop
while True:
    # Find all project cards
    project_cards = driver.find_elements_by_xpath(project_card_xpath)
    for card in project_cards:
        project_url = card.get_attribute('href')
        if not is_url_in_csv(project_url, csv_file):
            save_url_to_csv(project_url, csv_file)
    
    # Try to click the 'Load More' button
    try:
        load_more_button = driver.find_element_by_xpath(load_more_button_xpath)
        driver.execute_script("arguments[0].click();", load_more_button)
        # Wait for new projects to load; adjust the sleep time based on your connection speed
        time.sleep(5)
    except NoSuchElementException:
        print("No more 'Load More' button found or end of the list reached.")
        break

# Close the browser
driver.quit()

print("Scraping complete. Data saved to CSV.")