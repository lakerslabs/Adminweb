# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 11:44:50 2020

@author: eduardo.berga
"""


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select

from selenium.webdriver.support import expected_conditions as EC

import win32com.client as win32
import win32print
from selenium import webdriver
import time
import openpyxl
import math
import autoit



# # workbook  = openpyxl.load_workbook(r'C:\Users\eduardo.berga\Desktop\RunPy.xlsm')
# workbook  = openpyxl.load_workbook(r'X:\Logistica\1. Logistica Interno\Historiales_de_Logistica\ImportacionMasiva_Pruebas.xlsx')
# workbook.save(r'C:\borrar\ImportacionMasiva_Pruebas.xlsx') 

# print('RunPy.xlsm  se ejecuto correctamente')

options = webdriver.ChromeOptions()
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('--headless')
browser = webdriver.Chrome(executable_path= r'C:\Users\eduardo.berga\AppData\Local\Programs\Python\Python38\chromedriver.exe', options=options)		
# browser = webdriver.Chrome(executable_path= r'C:\Users\seincomp\AppData\Local\anaconda3\chromedriver.exe', options=options)
browser.get('https://andreanionline.com/login')
browser.maximize_window()
try:
    element = WebDriverWait(browser, 200).until(EC.presence_of_element_located((By.ID,'main')))
    search_button = browser.find_element_by_id('loginButton')
    search_button.click()
except:
    print('Error al cargar el elemento >> loginButton <<\n')
    
try:
    element = WebDriverWait(browser, 200).until(EC.presence_of_element_located((By.ID,'username')))
    search_textinput = browser.find_element_by_id ('username')
    search_textinput.send_keys('xlshop@xl.com.ar')
    search_textinput = browser.find_element_by_id ('password')
    search_textinput.send_keys('Elarge,123')
    time.sleep(2)
    search_button = browser.find_element_by_xpath ('/html/body/div[2]/div/div[2]/form/div[4]/div[3]/button')
    search_button.click()
except:
    print('Error en la linea 157')

print('La ecucion fue un exito')
