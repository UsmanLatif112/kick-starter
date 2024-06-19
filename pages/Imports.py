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
from resources.resourcces import ProfileResources, MessageResources


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





websites = [
    "https://www.google.com",
    "https://www.facebook.com",
    "https://www.youtube.com",
    "https://www.amazon.com",
    "https://www.wikipedia.org",
    "https://www.twitter.com",
    "https://www.instagram.com",
    "https://www.linkedin.com",
    "https://www.ebay.com",
    "https://www.reddit.com",
    "https://www.netflix.com",
    "https://www.microsoft.com",
    "https://www.apple.com",
    "https://www.tumblr.com",
    "https://www.quora.com",
    "https://www.github.com",
    "https://www.stackoverflow.com",
    "https://www.medium.com",
    "https://www.nytimes.com",
    "https://www.bbc.com",
    "https://www.cnn.com",
    "https://www.foxnews.com",
    "https://www.theguardian.com",
    "https://www.nbcnews.com",
    "https://www.forbes.com",
    "https://www.bloomberg.com",
    "https://www.imdb.com",
    "https://www.rottentomatoes.com",
    "https://www.tripadvisor.com",
    "https://www.booking.com",
    "https://www.airbnb.com",
    "https://www.zillow.com",
    "https://www.homedepot.com",
    "https://www.walmart.com",
    "https://www.target.com",
    "https://www.bestbuy.com",
    "https://www.costco.com",
    "https://www.etsy.com",
    "https://www.pinterest.com",
    "https://www.weather.com"
]



messagess = [
    "Hello, I'm Teresa, an expert in fundraising for businesses like yours. My method is truly unique, requiring no time or effort on your part. It avoids selling equity or taking out expensive loans. Plus, there's no retainer fee, and if we don't raise funds, you owe us nothing. Interested in discussing this?",
    "Hi, I'm Teresa. I specialize in helping companies like yours with fundraising. My unique approach requires zero time or effort from you and doesn't involve selling equity or costly loans. No retainer fees are needed, and if we don't succeed, you pay nothing. Would you like to know more about my approach?",
    "Greetings, I'm Teresa. My expertise is in fundraising for businesses such as yours. My distinctive method requires no time or effort from you and avoids selling equity or expensive loans. There's no upfront payment for our services, and if we don’t raise funds, you owe us nothing. Are you open to a conversation with one of my Account Managers?",
    "Hi there, I'm Anna. I specialize in company fundraising with a unique approach that demands no time or effort from you. We don't involve equity sales or high-cost loans. Best of all, no retainer fees, and you only pay if we succeed. Would you be willing to speak with an Account Manager?",
    "Hello, my name is Samantha. I focus on fundraising for companies like yours with a unique approach that requires no time or effort from you. We don't sell equity or take costly loans, and there's no retainer. If we don’t raise money, you pay nothing. Open to chatting with an Account Manager?",
    "Hi, I'm Jennifer, a fundraising specialist for businesses like yours. My approach is unique—no time or effort required from you, no equity selling, no costly loans. Plus, there's no retainer fee, and if we don't raise funds, you owe nothing. Would you like to speak with an Account Manager?",
    "I'm Leslie. I have a unique fundraising approach for companies like yours that requires no time or effort on your part. There's no selling equity or taking expensive loans involved. Additionally, no retainer fees are needed, and if we don’t succeed, you pay nothing. Can we arrange a call with an Account Manager?",
    "Hi, I'm Hannah. My specialty is fundraising for companies such as yours with a unique method that requires no effort or time from you. We don't sell equity or involve costly loans. There's no retainer, and if we don’t raise money, you owe us nothing. Would you be open to talking with an Account Manager?",
    "Hey there, I'm Sarah. I specialize in raising funds for companies like yours using a unique approach that requires no effort or time on your part. We avoid selling equity or taking on expensive loans. Plus, no retainer is needed, and if we don’t raise funds, you pay nothing. Interested in a chat with an Account Manager?",
    "Hello, my name is Cindy. I focus on helping companies like yours with fundraising. My unique approach doesn't require any time or effort from you and avoids selling equity or expensive loans. No retainer fees are needed, and if we don't raise funds, you owe nothing. Can we set up a meeting with an Account Manager?",
    "Hi, I'm Karen. I specialize in fundraising for businesses like yours. My method is unique and requires no effort or time from you. It doesn't involve selling equity or taking costly loans. There's no retainer fee, and if we don't succeed, you pay nothing. Open to a discussion with an Account Manager?",
    "Hello, I'm Mia. My expertise is in fundraising for companies such as yours with a unique approach that needs no effort or time from you. We avoid equity sales and costly loans. Plus, there's no retainer, and if we don’t raise money, you owe nothing. Would you like to talk with an Account Manager?",
    "Hi there, I'm Ava. I specialize in company fundraising using a unique method that requires no time or effort on your part. We don't involve selling equity or taking out expensive loans. Best of all, no retainer fees, and you only pay if we succeed. Interested in speaking with an Account Manager?",
    "Hello, my name is Jessica. I focus on fundraising for companies like yours with a unique approach that requires no time or effort from you. We don't sell equity or take on costly loans, and there's no retainer. If we don’t raise funds, you pay nothing. Open to a conversation with an Account Manager?",
    "Hi, I'm Charlotte. I specialize in fundraising for companies like yours. My unique approach requires no time or effort from you, and it doesn't involve selling equity or taking out expensive loans. Plus, there's no retainer fee, and if we don't succeed, you pay nothing. Can we arrange a call with an Account Manager?",
    "Hello, I'm Janet. I have a unique approach to fundraising for businesses like yours that requires no effort or time from you. We avoid selling equity or costly loans. Additionally, no retainer fees are needed, and if we don’t raise money, you owe nothing. Would you like to talk with an Account Manager?",
    "Hi, I'm Maria. My specialty is fundraising for companies such as yours using a unique method that needs no effort or time from you. We don't involve selling equity or taking expensive loans. There's no retainer, and if we don’t raise funds, you pay nothing. Interested in a chat with an Account Manager?",
    "Greetings, I'm Sandra. I specialize in fundraising for businesses like yours with a unique approach that requires no effort or time from you. We avoid equity sales and costly loans. Plus, there's no retainer fee, and if we don’t raise money, you owe us nothing. Open to a discussion with an Account Manager?",
    "Hello, my name is Liz. I focus on helping companies like yours with fundraising. My unique approach doesn't require any effort or time from you and avoids selling equity or costly loans. No retainer fees are needed, and if we don't succeed, you pay nothing. Would you be open to talking with an Account Manager?",
    "Hi, I'm Joanne. I specialize in fundraising for businesses like yours. My method is truly unique and requires no time or effort on your part. It doesn't involve selling equity or taking out costly loans. There's no retainer fee, and if we don't raise funds, you owe nothing. Interested in speaking with an Account Manager?"
]


keywords = [
    "Adventure",
    "Innovation",
    "Sustainability",
    "Blockchain",
    "Wellness",
    "Cryptocurrency",
    "Renewable energy",
    "Artificial intelligence",
    "Urban farming",
    "Mindfulness",
    "Quantum computing",
    "Autonomous vehicles",
    "Cybersecurity",
    "Augmented reality",
    "Climate change",
    "Space exploration",
    "Digital marketing",
    "Remote work",
    "Virtual reality",
    "Biodegradable products",
    "Smart homes",
    "Genetic engineering",
    "Social media",
    "E-commerce",
    "Machine learning",
    "Organic food",
    "Fintech",
    "Internet of Things (IoT)",
    "Green technology",
    "Big data",
    "Health tech",
    "Renewable resources",
    "Cloud computing",
    "E-learning",
    "Eco-tourism",
    "Edtech",
    "Personalized medicine",
    "3D printing",
    "Nanotechnology",
    "Electric vehicles",
    "Wearable technology",
    "Circular economy",
    "Smart cities",
    "Digital transformation",
    "Biodiversity",
    "Telehealth",
    "Renewable energy sources",
    "Sustainable fashion",
    "Blockchain technology",
    "Artificial neural networks"
]
