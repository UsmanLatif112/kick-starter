from pages.Imports import *
from drivers.driver import *

import pyautogui,random,time,csv


def random_mouse_movement(fixed_delay):
    # Automatically get screen resolution
    screen_width, screen_height = pyautogui.size()

    # Get current mouse position
    current_x, current_y = pyautogui.position()

    # Randomize x and y coordinates within the screen resolution
    end_x, end_y = random.randint(0, screen_width), random.randint(0, screen_height)

    # Number of intermediate points
    intermediate_points = random.randint(3, 6)

    # Generate intermediate points for more human-like movement
    points = [(current_x, current_y)]
    for _ in range(intermediate_points):
        intermediate_x = random.randint(min(current_x, end_x), max(current_x, end_x))
        intermediate_y = random.randint(min(current_y, end_y), max(current_y, end_y))
        points.append((intermediate_x, intermediate_y))
    points.append((end_x, end_y))

    for point in points:
        pyautogui.moveTo(point[0], point[1], duration=random.uniform(0.1, 0.3))

        # Apply fixed delay after each move
        time.sleep(fixed_delay)


def scroll_page(driver, fixed_delay):
    # Get the scroll height of the page
    scroll_height = driver.execute_script("return document.body.scrollHeight")
    scroll_position = driver.execute_script(
        "return window.pageYOffset"
    )  
    scroll_sequence = ["down"] * 5 + ["up"] * 5
    random.shuffle(scroll_sequence)  

    for scroll_direction in scroll_sequence:
        if scroll_direction == "down":
            # Scroll down
            scroll_position += random.randint(300, 500)
            # Ensure that we do not scroll past the bottom of the page
            scroll_position = min(scroll_position, scroll_height)
        else:
            # Scroll up
            scroll_position -= random.randint(300, 500)
            # Ensure that we do not scroll before the top of the page
            scroll_position = max(scroll_position, 0)

        # Execute the scroll
        driver.execute_script(f"window.scrollTo(0, {scroll_position});")

        # Fixed delay after the scroll
        time.sleep(fixed_delay)
        
class BasePage:
    def __init__(self, driver):
        self.driver = driver


class HomePage(BasePage):
    
    def click_btn(self, xpath: str):
        self.driver.find_element(By.XPATH, xpath).click()

    def enter_Name(self, xpath: str, clientname: str):
        self.driver.find_element(By.XPATH, xpath).send_keys(clientname)

    def enter_name_delay(self, xpath: str, clientname: str, delay=0.2):
        element = self.wait(xpath)
        element.clear()
        for char in clientname:
            element.send_keys(char)
            time.sleep(delay)

    def wait(self, xpath, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            return element
        except Exception as e:
            print(f"Element with XPath '{xpath}' not found within {timeout} seconds.")
            raise e

    def make_csv(self, filename: str, data):
        mode = "a"  # Always append to the existing file
        with open(filename, mode, newline="") as f:
            writer = csv.writer(f)
            writer.writerow(data)

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
        
        
        


  # mainpage = HomePage(driver)
    # mainpage.wait(ProfileResources.Main_login_page)
    
    # time.sleep(2)
    # email_fieldd = HomePage(driver)
    # email_fieldd.click_btn(ProfileResources.email_field)
    
    # time.sleep(2)
    # Usernamee = HomePage(driver)
    # Usernamee.enter_name_delay(ProfileResources.email_field, username)