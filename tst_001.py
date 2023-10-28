import pyautogui
import unittest
import time
import os
import datetime
import pytest
from selenium import webdriver

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchWindowException
from selenium.common.exceptions import TimeoutException
import selenium

import pytest_html

horaGlobal = time.strftime("%H%M%S")

class TestRegistroGrimoldi(unittest.TestCase):

    
    def setUp(self):
        # Creamos una instancia del navegador 
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()
        # Accedemos a la página web de Grimoldi
       
        self.driver.get("https://www.grimoldi.com/registracion")
        
    def test_registro_fallido_email_invalido(self):
    
       
        nombre = self.driver.find_element(By.ID,"30")
        apellido = self.driver.find_element(By.ID,"29")
        email = self.driver.find_element(By.ID,"31")
        

        password = self.driver.find_element(By.ID,"51")
        confirmar_password = self.driver.find_element(By.ID,"51_2")
  
        boton_registrar = self.driver.find_element(By.ID,"formSubmit")

  
        nombre.send_keys("Juan")
        apellido.send_keys("Perez")
        email.send_keys("juan.perez") # Email sin dominio
        password.send_keys("123456")
        confirmar_password.send_keys("123456")
       

       
        boton_registrar.click()
  
    
        self.driver.find_element(By.ID, "31-error")
    
      
       
    def test_registro_fallido_password_no_coincidente(self):
       
        nombre = self.driver.find_element(By.ID,"30")
        apellido = self.driver.find_element(By.ID,"29")
        email = self.driver.find_element(By.ID,"31")
   
        
        password = self.driver.find_element(By.ID,"51")
        confirmar_password = self.driver.find_element(By.ID,"51_2")
  
        boton_registrar = self.driver.find_element(By.ID,"formSubmit")
       
        nombre.send_keys("Juan")
        apellido.send_keys("Perez")
        email.send_keys("juan.perez@gmail.com")
        
        password.send_keys("123456")
        confirmar_password.send_keys("654321") # Contraseña no coincide
        
        boton_registrar.click()
      
  
        self.driver.find_element(By.ID, "51_2-error")
    
    
    def test_registro_fallido_nombre_vacio(self):
       
        nombre = self.driver.find_element(By.ID,"30")
        apellido = self.driver.find_element(By.ID,"29")
        email = self.driver.find_element(By.ID,"31")
       

        password = self.driver.find_element(By.ID,"51")
        confirmar_password = self.driver.find_element(By.ID,"51_2")
  
        boton_registrar = self.driver.find_element(By.ID,"formSubmit")
    
      
        nombre.send_keys("") # Nombre vacío
        apellido.send_keys("Perez")
        email.send_keys("juan.perez@gmail.com")       
        password.send_keys("123456")
        confirmar_password.send_keys("123456")
    
       
        boton_registrar.click()
        
        self.driver.find_element(By.ID, "30-error")
        
    def tearDown(self):
       
        self.driver.implicitly_wait(3)
        folder = os.path.join("C:", "Users", "Lio", "Pictures", "Screenshots")
       
        now = datetime.datetime.now()
        file = os.path.join(folder, f"{self._testMethodName}_{now.strftime('%Y-%m-%d_%H-%M-%S')}.png")
       
        screenshot = pyautogui.screenshot()
        screenshot.save(file) 
if __name__ == "__main__":
    pytest.main(["--html=FigueroaLionel.html"])
    unittest.main()
