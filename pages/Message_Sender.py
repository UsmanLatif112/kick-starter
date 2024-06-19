from pages.Imports import *
from pages.functions import *

def main_code_message_sending():
    driver = get_undetected_chrome_browser('christoph')
    driver.get("https://www.google.com/")
    time.sleep(1)
    csv_file_path = 'D:\\my\\New folder\\kick starter\\kickstarter_1800.csv'
        
    with open(csv_file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            try:
                Project_Urls = row[0]
                if not is_url_in_csvv(Project_Urls, csv_filee):
                    print(Project_Urls)
                    time.sleep(1)
                    driver.get(f"{Project_Urls}")
                    time.sleep(1)
                    driver.maximize_window()
                    time.sleep(1)
                    side_modall = HomePage(driver)
                    side_modall.wait(ProfileResources.side_modal)
                    time.sleep(2)
                    side_modal_crosss = HomePage(driver)
                    side_modal_crosss.click_btn(ProfileResources.side_modal_cross)
                    save_url_to_csvv (Project_Urls, csv_filee)
                    
            except Exception as e:
                print(e)
        
    driver.quit()
    # if not is_url_in_csv(project_url, csv_file):
    #     print(project_url)
    #     save_url_to_csv(project_url, csv_file)
    
    
    # ActionChains(driver).move_to_element(load_more_button).perform()           
                        
    # driver.quit()
    
    
    
  