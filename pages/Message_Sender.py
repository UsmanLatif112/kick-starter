from pages.Imports import *
from pages.functions import *

def main_code_message_sending():
    csv_file_path = 'D:\\my\\New folder\\kick starter\\kickstarter_1800.csv'
        
    with open(csv_file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            try:
                Project_Urls = row[0]
                if not is_url_in_csvv(Project_Urls, csv_filee):
                    driver = get_undetected_chrome_browser('christoph')
                    driver.maximize_window()
                    driver.get("https://www.google.com/")
                    time.sleep(2)
                    try:
                        Search_barr = HomePage(driver)
                        Search_barr.click_btn(MessageResources.Search_bar)
                        time.sleep(1)
                        Search_bar_r = HomePage(driver)
                        keywordss = random.choice(keywords)
                        Search_bar_r.enter_name_delay(MessageResources.Search_bar, keywordss)
                        time.sleep(1)
                        ActionChains(driver).send_keys(Keys.ENTER).perform()
                    except:
                        print("searxh bar not found")
                        
                    gentle_human_like_scroll(driver, duration=5)
                    time.sleep(2)
                    random_mouse_movemen_t(3)
                    time.sleep(2)
                    website = random.choice(websites)
                    time.sleep(2)
                    driver.get(website)
                    time.sleep(2)
                    gentle_human_like_scroll(driver, duration=5)
                    time.sleep(2)
                    random_mouse_movemen_t(3)
                    time.sleep(2)
                    print(Project_Urls)
                    time.sleep(5)
                    driver.get(f"{Project_Urls}")
                    time.sleep(5) 
                    try:
                        side_modall = HomePage(driver)
                        side_modall.wait(ProfileResources.side_modal)
                        side_modal_crosss = HomePage(driver)
                        side_modal_crosss.click_btn(ProfileResources.side_modal_cross)
                    except Exception as e:
                        print(e)
                    time.sleep(2)
                    gentle_human_like_scroll(driver, duration=5)
                    time.sleep(2)
                    random_mouse_movemen_t(3)
                    time.sleep(2)
                    try:
                        see_more_e = driver.find_element(By.XPATH,'//*[@id="content-wrap"]//*[@class="NS_projects__description_section m-auto"]//*[@class="col col-4 js-rewards-column max-w62 sticky-rewards"]//*[@class="pl1"][contains(normalize-space(), "See more")]')
                        time.sleep(2)
                        ActionChains(driver).move_to_element(see_more_e).perform()
                        time.sleep(1)
                        see_more_e_e = HomePage(driver)
                        see_more_e_e.click_btn(MessageResources.See_More_btn)
                    except:
                        print("see more button not found")
                        continue
                    try:
                        modal_cancel_1 = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,'//*[@id="content-wrap"]//*[@class="shadow-low p4 max-h70vh auto-scroll-y clip"][contains(normalize-space(), "About the creator")]',)))
                        if modal_cancel_1:
                            Contact_me = driver.find_element(By.XPATH,'//*[@id="content-wrap"]//*[@class="shadow-low p4 max-h70vh auto-scroll-y clip"]//button[contains(normalize-space(), "Contact me")]')
                            time.sleep(2)
                            ActionChains(driver).move_to_element(Contact_me).perform()
                            time.sleep(1)
                            Contact_me.click()
                            time.sleep(2)
                            try:
                                Message_feild = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,'//*[@id="content-wrap"]//*[@class="shadow-low p4 max-h70vh auto-scroll-y clip"]//textarea[@placeholder="Type your message here"]',)))
                                if Message_feild:
                                    Message_feild.click()
                                    time.sleep(2)
                                    Message_feild_d = HomePage(driver)
                                    messages = random.choice(messagess)
                                    Message_feild_d.enter_name_delay(MessageResources.Message_feild_dd, messages)
                                    time.sleep(2)
                                    try:
                                        Send_message = driver.find_element(By.XPATH,'//*[@id="content-wrap"]//*[@class="shadow-low p4 max-h70vh auto-scroll-y clip"]//button[contains(normalize-space(), "Send Message")]')
                                        time.sleep(2)
                                        ActionChains(driver).move_to_element(Send_message).perform()
                                        time.sleep(2)
                                        Send_message.click()
                                    except:
                                        print("Sent messagebuton not found")
                                    try:
                                        Message_sent_pop = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH,'//*[@class="jGrowl-message"][contains(normalize-space(), "Your message has been sent!")]',)))
                                        save_url_to_csvv (Project_Urls, csv_filee)
                                    except:
                                        print("message not sent") 
                                        save_url_to_csvv_v (Project_Urls, csv_filee_e)    
                            except:
                                print("error in message typing")
                    except:
                        print("message modal not found")       
                    time.sleep(15)
                    websitee = random.choice(websites)
                    driver.get(websitee)
                    time.sleep(2)
                    gentle_human_like_scroll(driver, duration=5)
                    time.sleep(2)
                    random_mouse_movemen_t(3)
                    time.sleep(2)
                    driver.quit()
            except Exception as e:
                print(e)
                save_url_to_csvv_v (Project_Urls, csv_filee_e)
  