"""This File contains all the locators all the elements of different pages
If in futur the UI of the website will change we can change the locators from here
"""
from selenium.webdriver.common.by import By


class ProfileResources:
    side_modal = '//*[@id="react-consent-modal"]//*[@class="flex flex-column radius6px shadow-3 bg-white"]'
    side_modal_cross = '//*[@id="react-consent-modal"]//*[@class="flex flex-column radius6px shadow-3 bg-white"]/button'
    Discover_Page_btn = '//*[@class="relative global-nav-container"]//*[@class="react-aria-Group"]//div[contains(normalize-space(), "Discover")]//*[@class="category-link block"]/a'
    Discover_Page = '//*[@id="main_content"]//*[@class="grid-container"][contains(normalize-space(), "Explore")]'
    project_url = '//*[@class="relative discovery-project-card"]//span[@class="card-title type-20 medium lh24px clamp-1 mb0 relative"]/a'
    load_more_btn = '//*[@id="main_content"]//*[@class="load_more mt3"]/a[@class="bttn bttn-primary theme--create bttn-medium"]'


class MessageResources:
    See_More_btn = '//*[@id="content-wrap"]//*[@class="NS_projects__description_section m-auto"]//*[@class="col col-4 js-rewards-column max-w62 sticky-rewards"]//*[@class="pl1"][contains(normalize-space(), "See more")]'
    

