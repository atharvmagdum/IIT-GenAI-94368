# import required packages
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options #Libraries

# start the selenium browser session
chrome_options = Options() #Set of chrome settings
chrome_options.add_argument("--headless") #  Performs everything without opening browser window
driver = webdriver.Chrome(options=chrome_options) # Opens in Chrome Browser

# load desired page in the browser
driver.get("https://www.sunbeaminfo.in/internship ")

print("Page Title:", driver.title)

# define wait strategy
driver.implicitly_wait(1)

# interact with web controls
table_body = driver.find_element(By.TAG_NAME, "tbody")
table_rows = table_body.find_elements(By.TAG_NAME, "tr")
for row in table_rows:
    # print(row.text)
    cols = row.find_elements(By.TAG_NAME, "td")
    info = {
        "sr": cols[0].text,
        "batch": cols[1].text,
        "batch duration": cols[2].text,
        "start date": cols[3].text,
        "end date": cols[4].text,
        "time": cols[5].text,
        "fees": cols[6].text
    }
    print(info)

# stop the session
driver.quit()