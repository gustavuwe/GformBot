from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
import pyperclip

navegador = webdriver.Chrome(executable_path=r'./chromedriver.exe')

navegador.get('https://docs.google.com/forms/d/e/1FAIpQLSdUwxgtiddg9IS9D7OPAgqDm6TdY0CHx6MW7292p7a5ZDhkXg/viewform')
time.sleep(5)
emailadress = "luislima@gmail.com"
i = 0
while i <= 10000:

    email = navegador.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div[1]/input')
    email.click()

    pyperclip.copy(emailadress)
    pyautogui.hotkey('ctrl', 'v')

    opcao = navegador.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div/div/div/div[2]/div/div/span/div/div[3]/label')
    opcao.click()

    submit = navegador.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div/span')
    submit.click()

    restart = navegador.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    restart.click()

    print(i,' votos contabilizados')
    i += 1

    if i > 10000:
        break
