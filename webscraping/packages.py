# import matplotlib.pyplot as plt
# plt.plot([1, 2, 3], [2, 4, 1])
# plt.title("graph")
# plt.xlabel("x")
# plt.ylabel("y")
# plt.show()
# import requests
# from bs4 import BeautifulSoup

# response = requests.get("https://stackoverflow.com/questions")
# soup = BeautifulSoup(response.text, "html.parser")

# questions = soup.select(".bb")
# print(type(questions[1].attrs))
# import requests
# from bs4 import BeautifulSoup

# response = requests.get("https://quotes.toscrape.com")
# soup = BeautifulSoup(response.text, "html.parser")

# result = soup.find_all("span", class_="text")
# for res in result:
#     print(res.getText())
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()
# driver.get("https://google.com")

# box = driver.find_element(By.NAME, "q")
# box.send_keys("Hello World")

# btn = driver.find_element(By.NAME, "btnK")
# btn.click()
