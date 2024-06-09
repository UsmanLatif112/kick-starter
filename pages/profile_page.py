from pages.Imports import *
from pages.functions import *

def make_csv(filename: str, data, new=True):
    """make a csv file with the given filename
    and enter the data
    """
    mode = "w" if new else "a"
    with open(filename, mode, newline="", encoding='utf-8') as f:
        f.writelines(data)

def main_code():  
      
    # actions = ActionChains(driver)
    # csvv = HomePage(driver)
    
    # csvv.make_csv('Kick_Starter.csv', 'Project_URL\n')
    
    
    driver = get_undetected_chrome_browser('christoph')
    
    time.sleep(1)
    driver.get("https://google.com/")
    time.sleep(1)
    driver.maximize_window()
    time.sleep(1)
    driver.get("https://www.kickstarter.com/discover")
    time.sleep(1)
    
    # try:
    #     side_modall = HomePage(driver)
    #     side_modall.wait(ProfileResources.side_modal)
    #     time.sleep(2)
    #     side_modal_crosss = HomePage(driver)
    #     side_modal_crosss.click_btn(ProfileResources.side_modal_cross)
        
    # except:
    #     pass
    
    # try:         
    #     time.sleep(2)
    #     Discover_Page_btnn = HomePage(driver)
    #     Discover_Page_btnn.click_btn(ProfileResources.side_modal_cross)
    # except Exception as e:
    #     print(e)
        
    try:
        side_modall = HomePage(driver)
        side_modall.wait(ProfileResources.side_modal)
        time.sleep(2)
        side_modal_crosss = HomePage(driver)
        side_modal_crosss.click_btn(ProfileResources.side_modal_cross)
    except:
        pass
    
    # XPath selectors
    # project_card_xpath = "//*[@class='relative discovery-project-card']//span[@class='card-title type-20 medium lh24px clamp-1 mb0 relative']/a"
    project_card_xpath = ProfileResources.project_url
    # load_more_button_xpath = "//*[@id='main_content']//*[@class='load_more mt3']/a[@class='bttn bttn-primary theme--create bttn-medium']"
    load_more_button_xpath = ProfileResources.load_more_btn
    try:
        
        # Main scraping loop
        while True:
            # Find all project cards
            project_cards = driver.find_elements(By.XPATH, project_card_xpath)
            for card in project_cards:
                project_url = card.get_attribute('href')
                if not is_url_in_csv(project_url, csv_file):
                    print(project_url)
                    save_url_to_csv(project_url, csv_file)
                
            # Try to click the 'Load More' button
            try:
                time.sleep(2)
                load_more_button = driver.find_element(By.XPATH, load_more_button_xpath)
                ActionChains(driver).move_to_element(load_more_button).perform()
                time.sleep(2)
                load_more_button.click()
                time.sleep(30)
            except NoSuchElementException:
                crruent_url = driver.current_url
                print("No more 'Load More' button found or end of the list reached.")
                print(driver.current_url)
                
                break
    except Exception as e:
        print(e)
    # Close the browser
    driver.quit()

print("Scraping complete. Data saved to CSV.")
    
    
    
    
  