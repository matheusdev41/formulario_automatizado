#importações de bibliotecas
 
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import openpyxl


#inicialização do selenium / guardando em uma variável driver
driver = webdriver.Chrome()

#1 - abrir / navegar até o site https://contabilidade-devaprender.netlify.app/
driver.get('https://contabilidade-devaprender.netlify.app/')
sleep(5)

#2 - Digitar o e-email
email = driver.find_element(By.XPATH,'//input[@id="email"]')
sleep(2)
email.send_keys('admin@contabilidade.com')#função do selinium que te permite escrever algo 
#3 - Digitar a senha 
senha = driver.find_element(By.XPATH,'//input[@id="senha"]')
sleep(2)
senha.send_keys('123456')
#4 - Clicar em entrar 
botao_entrar = driver.find_element(By.XPATH, '//button[@id="Entrar"]')
sleep(2)
botao_entrar.click()
sleep(5)
#5 - Extrair informações da planilha 
empresas = openpyxl.load_workbook('./empresas.xlsx') #guarndando a planilha na variável empresas
pagina_empresas = empresas["dados empresas"] #localizando a página que vou usar no excel

for linha in pagina_empresas.iter_rows(min_row=2, values_only=True): #inter_rows() usado para acessar cada uma das linhas min_row quer dizer a linha mínima que ele deve iniciar a leitura =True, irá me retornar apenas os valores
    nome_empresa, email, telefone, endereco, cnpj, area_atuacao, quantidade_de_funcionarios, data_de_funcacao = linha

#6 - Clicar em cada campo e preencher 

    driver.find_element(By.ID, "nomeEmpresa").send_keys(nome_empresa) 
    sleep(1)
    driver.find_element(By.ID, "emailEmpresa").send_keys(email)
    sleep(1)
    driver.find_element(By.ID, "telefoneEmpresa").send_keys(telefone)
    sleep(1)
    driver.find_element(By.ID, "enderecoEmpresa").send_keys(endereco)
    sleep(1)
    driver.find_element(By.ID, "cnpj").send_keys(cnpj)
    sleep(1)
    driver.find_element(By.ID, "areaAtuacao").send_keys(area_atuacao)
    sleep(1)
    driver.find_element(By.ID, "numeroFuncionarios").send_keys(quantidade_de_funcionarios)
    sleep(1)
    driver.find_element(By.ID, "dataFundacao").send_keys(data_de_funcacao)
    sleep(1)

#7 - clicar em cadastrar 
    botao_cadastrar = driver.find_element(By.ID,'Cadastrar')
    sleep(2)
    botao_cadastrar.click()
    sleep(5)

#8 - Repito passo 5 e 6 




