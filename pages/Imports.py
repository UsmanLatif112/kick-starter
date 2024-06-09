# Import required modules
import csv,time, random
from pathlib import Path
from datetime import datetime
from drivers.driver import get_undetected_chrome_browser
import pyautogui
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
import contextlib
from .functions import BasePage
from datetime import datetime
from resources.resourcces import ProfileResources


# =================
from pathlib import Path
import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


# ==================================
from pages.functions import *
BASE_DIR = Path(__file__).resolve().parent
input_file = BASE_DIR / "input.csv"
output_file = BASE_DIR / "output.csv"