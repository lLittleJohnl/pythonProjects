##########################################################################################
# Automação para Regras de Descarte - Ericsson OSS
# 
# Original Version: TIM (Joao Vitor Correia Pessoa) - 14/02/2023
# Last Update Change Log: TIM (Joao Vitor Correia Pessoa) - 15/02/2023
##########################################################################################

### PSEUDOCÓDIGO ###

""" 
Início

1. Acessar o back-end do portal de automações
2. Clicar em avançado e depois no link
3. Abrir uma nova aba e acessar o portal de automações
4. Passar o usuário e senha e clicar em login
5. Clicar em Descarte de coleta
6. Clicar em Regras de Descarte
7. Acessar o Agent especificado
8. Preecher as informações
9. Clicar em Adicionar regra
10. Clicar em salvar

Fim
"""

### BIBLIOTECAS ###

import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService

### VARIAVEIS GLOBAIS ###

username = "F8085167"
password = "Tim@1234"
url_automation_portal = "http://10.216.127.48:32001/home"
url_backend_portal = "https://10.216.127.48:31000/"
regras_de_descarte = "/html/body/app-root/app-home/div/div[1]/div[2]/div[12]/div[2]/a"
login_button = "/html/body/app-root/app-login/div/div/div/div/div[2]/form/div[3]/button"
descarte_em_coleta = "/html/body/app-root/app-home/div/div[1]/div[2]/div[12]/div[1]/div[1]"
salvar = "/html/body/app-root/app-home/div/div[2]/div/app-descarte-coleta/app-regras-edit/div/div/div[2]/div[4]/div[2]/button"
local_do_arquivo = r"C:\Users\f8085167\Documents\vscode_projects\python\regras_descarte\base.xlsx"
nokia_netact = "/html/body/app-root/app-home/div/div[2]/div/app-regras-descarte/div/div/div[3]/div/div/div/div/div[2]/div/table/tbody/tr[5]/td[7]/button[2]"

### CONFIGURANDO DRIVER ###

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
service = ChromeService(executable_path=r"C:\Users\f8085167\Documents\vscode_projects\python\regras_descarte\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)
driver.implicitly_wait(15)

### ACESSANDO A PÁGINA ###

driver.get(url_backend_portal)
driver.find_element(By.XPATH, "//*[@id=\"details-button\"]").click()
driver.find_element(By.XPATH, "//*[@id=\"proceed-link\"]").click()

driver.switch_to.new_window('tab')
driver.get(url_automation_portal)
driver.find_element(By.ID, "inputEmail").send_keys(username)
driver.find_element(By.ID, "inputPassword").send_keys(password)

driver.find_element(By.XPATH, login_button).click()
driver.find_element(By.XPATH, descarte_em_coleta).click()
driver.find_element(By.XPATH, regras_de_descarte).click()
driver.find_element(By.XPATH, nokia_netact).click()

base = pd.read_excel(local_do_arquivo)

for x, agent in enumerate(base["AGENT"]):

    summary = base.loc[x, "SUMMARY"]
    summary_path = "/html/body/app-root/app-home/div/div[2]/div/app-descarte-coleta/app-regras-edit/div/div/div[2]/div[3]/div/div[2]/div/div/div[1]/div/div/input"
    adicionar_regra = "/html/body/app-root/app-home/div/div[2]/div/app-descarte-coleta/app-regras-edit/div/div/div[2]/div[3]/div/div[4]/button"

    driver.find_element(By.XPATH, summary_path).send_keys(summary)

    if x == 0:

        comparador_path_1 = "/html/body/app-root/app-home/div/div[2]/div/app-descarte-coleta/app-regras-edit/div/div/div[2]/div[3]/div/div[2]/div/div/div[4]/div/div/ng-select/div/div/div[3]"
        comparador_path_2 = "/html/body/app-root/app-home/div/div[2]/div/app-descarte-coleta/app-regras-edit/div/div/div[2]/div[3]/div/div[2]/div/div/div[4]/div/div/ng-select/ng-dropdown-panel/div/div[2]/div[1]"
        severity_path_1 = "/html/body/app-root/app-home/div/div[2]/div/app-descarte-coleta/app-regras-edit/div/div/div[2]/div[3]/div/div[2]/div/div/div[5]/div/div/ng-select/div/div/div[3]"
        severity_path_2 = "/html/body/app-root/app-home/div/div[2]/div/app-descarte-coleta/app-regras-edit/div/div/div[2]/div[3]/div/div[2]/div/div/div[5]/div/div/ng-select/ng-dropdown-panel/div/div[2]/div[3]"
        
        driver.find_element(By.XPATH, comparador_path_1).click()
        driver.find_element(By.XPATH, comparador_path_2).click()

        driver.find_element(By.XPATH, severity_path_1).click()
        driver.find_element(By.XPATH, severity_path_2).click()
        

    else:
        
        comparador_path_1 = "/html/body/app-root/app-home/div/div[2]/div/app-descarte-coleta/app-regras-edit/div/div/div[2]/div[3]/div/div[2]/div/div/div[4]/div/div/ng-select/div/div/div[2]"
        comparador_path_2 = "/html/body/app-root/app-home/div/div[2]/div/app-descarte-coleta/app-regras-edit/div/div/div[2]/div[3]/div/div[2]/div/div/div[4]/div/div/ng-select/ng-dropdown-panel/div/div[2]/div[1]"
        severity_path_1 = "/html/body/app-root/app-home/div/div[2]/div/app-descarte-coleta/app-regras-edit/div/div/div[2]/div[3]/div/div[2]/div/div/div[5]/div/div/ng-select/div/div/div[2]"
        severity_path_2 = "/html/body/app-root/app-home/div/div[2]/div/app-descarte-coleta/app-regras-edit/div/div/div[2]/div[3]/div/div[2]/div/div/div[5]/div/div/ng-select/ng-dropdown-panel/div/div[2]/div[3]"

        driver.find_element(By.XPATH, comparador_path_1).click()
        driver.find_element(By.XPATH, comparador_path_2).click()
        
        driver.find_element(By.XPATH, severity_path_1).click()
        driver.find_element(By.XPATH, severity_path_2).click()
        
    driver.find_element(By.XPATH, adicionar_regra).click()
       
# Salvar
driver.find_element(By.XPATH, salvar).click()
time.sleep(100)

driver.quit()