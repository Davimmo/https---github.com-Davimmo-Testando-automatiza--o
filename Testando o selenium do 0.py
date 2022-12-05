import time
from selenium.webdriver import Chrome
from time import sleep

url = 'https://curso-python-selenium.netlify.app/aula_03.html'

navegador = Chrome()

navegador.get(url)

sleep(1)

a = navegador.find_element_by_tag_name('a')

time.sleep(2)
for click in range(10):
    time.sleep(2)
    ps = navegador.find_elements_by_tag_name('p')
    time.sleep(2)
    a.click()
    time.sleep(2)
    print(f'Valor do ultimo p: {ps[-1].text} valor do click: {click}')
    time.sleep(2)
    print(f'Os valors são iguais {ps[-1].text == str(click)}')