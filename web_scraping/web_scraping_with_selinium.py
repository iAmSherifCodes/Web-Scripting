from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service("C:\\Users\\SHERIF\\Downloads\\chromedriver_win32\\chromedriver.exe")


def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(service=service, options=options)
    driver1 = webdriver.Chrome(service=service, options=options)
    driver1.get("https://developer.mozilla.org/en-US")
    driver.get("https://www.thenetnaija.net/videos/movies/4751-john-wick-chapter-2-2017")
    driver_list = [driver, driver1]
    return driver_list


def main():
    driver = get_driver()
    element1 = driver[1].find_element(by="xpath", value='//*[@id="content"]/div/div[1]/section/p')
    element = driver[0].find_element(by="xpath", value='//*[@id="content"]/div/div/div[2]/div[1]/main/h1')
    text = element.text
    text2 = element1.text
    return text + " \n" + text2


# //*[@id="content"]/div/div/div[2]/div[1]/main/h1
# https://www.thenetnaija.net/videos/movies/4751-john-wick-chapter-2-2017

print()
print(main())

