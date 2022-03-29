from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
import pyperclip

navegador = webdriver.Chrome(executable_path=r'./chromedriver.exe')

navegador.get('link here')
time.sleep(5)
emailadress = "email here" #if dont need email you can delete that variable and the variable "email"
i = 0
while i <= 10000:

    email = navegador.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div[1]/input')
    email.click()

    pyperclip.copy(emailadress)
    pyautogui.hotkey('ctrl', 'v')

    option = navegador.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div/div/div/div[2]/div/div/span/div/div[3]/label')
    option.click()

    submit = navegador.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div/span')
    submit.click()

    restart = navegador.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    restart.click()

    print(i,' counted votes')
    i += 1

    if i > 10000:
        break
