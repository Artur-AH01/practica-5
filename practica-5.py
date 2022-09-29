from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import HtmlTestRunner
import unittest
import time

class Shopping(unittest.TestCase):
       cat = {
          '//*[@id="itemc"]',
          '//*[@id="itemc"]'


       }
    
       def setUp(self):
              self._Driver = webdriver.Chrome("./chromedriver_win32/chromedriver.exe")
              self._Driver.maximize_window()
              self._Driver.get('https://www.demoblaze.com/index.html')
              print("entro")
       def test_all(self):
              print("registro")
              #registro en la web
              actions = ActionChains(self._Driver)
              """ action = self._Driver.find_element(By.ID, "signin2").click()
              time.sleep(2)
              action = self._Driver.find_element(By.ID, "sign-username")
              #pasamos nombre de usuario
              self._Driver.find_element(By.ID, "sign-username").send_keys("artur-in")
              time.sleep(2)
              password = self._Driver.find_element(By.ID, "sign-password")
              #pasamos contraseñ
              password.send_keys("a")
              time.sleep(2)
              #click en el boton de registro
              button = self._Driver.find_element(By.XPATH, "//*[@id='signInModal']/div/div/div[3]/button[2]")
              button.click()
              time.sleep(2)
              #aceptar alerta
              action = self._Driver.switch_to.alert.accept()
              time.sleep(2)
              button = self._Driver.find_element(By.XPATH, "//*[@id='signInModal']/div/div/div[3]/button[1]")
              button.click()
              print("registro acabo")
              time.sleep(2) """
              ####################################################################
              #iniciamos inicio de sesion
              print("inicio sesion")
              action = self._Driver.find_element(By.ID, "login2").click()
              time.sleep(2)
              action = self._Driver.find_element(By.ID, "loginusername")
              #pasamos parametros de sesion 
              self._Driver.find_element(By.ID, "loginusername").send_keys("artur-in")
              time.sleep(2)
              password = self._Driver.find_element(By.ID, "loginpassword")
              password.send_keys("a")
              time.sleep(2)
              button = self._Driver.find_element(By.XPATH, "//*[@id='logInModal']/div/div/div[3]/button[2]")
              button.click()
              #confirmacion inicio sesion
              print("inicio sesion")
              time.sleep(2)
              ##################################
              #añadir productos al carrito 
              self._Driver.find_element(By.LINK_TEXT, "Samsung galaxy s6").click()
              time.sleep(2)
              self._Driver.find_element(By.LINK_TEXT, "Add to cart").click()
              time.sleep(3)
              #Aceptar Alerta que tenga texto en especifico
              #assert self._Driver.switch_to.alert.text == "Product added"
              action = self._Driver.switch_to.alert.accept()
              time.sleep(3)
              self._Driver.find_element(By.ID, "nava").click()
              time.sleep(2)
              self._Driver.find_element(By.LINK_TEXT, "Nokia lumia 1520").click()
              time.sleep(2)
              self._Driver.find_element(By.LINK_TEXT, "Add to cart").click()
              time.sleep(2)
              action = self._Driver.switch_to.alert.accept()
              time.sleep(2)
              self._Driver.find_element(By.ID, "nava").click()
              time.sleep(2)
              ############################
              #Se añaden las laptop

              self._Driver.find_element(By.LINK_TEXT, "Laptops").click()
              time.sleep(2)
              self._Driver.find_element(By.LINK_TEXT, "Sony vaio i5").click()
              time.sleep(2)
              self._Driver.find_element(By.LINK_TEXT, "Add to cart").click()
              time.sleep(2)
              action = self._Driver.switch_to.alert.accept()
              time.sleep(2)
              self._Driver.find_element(By.ID, "nava").click()
              time.sleep(2)
              self._Driver.find_element(By.LINK_TEXT, "Laptops").click()
              time.sleep(2)
              self._Driver.find_element(By.LINK_TEXT, "Sony vaio i7").click()
              time.sleep(2)
              self._Driver.find_element(By.LINK_TEXT, "Add to cart").click()
              time.sleep(2)
              action = self._Driver.switch_to.alert.accept()
              time.sleep(2)
              self._Driver.find_element(By.ID, "nava").click()
              time.sleep(2)
              print("se añadieron las laptop")
              print("agregamos monitores")
              #########
              #Se añaden monitores
              self._Driver.find_element(By.LINK_TEXT, "Monitors").click()
              time.sleep(2)
              self._Driver.find_element(By.LINK_TEXT, "Apple monitor 24").click()
              time.sleep(2)
              self._Driver.find_element(By.LINK_TEXT, "Add to cart").click()
              time.sleep(2)
              action = self._Driver.switch_to.alert.accept()
              time.sleep(2)
              self._Driver.find_element(By.ID, "nava").click()
              time.sleep(2)
              self._Driver.find_element(By.LINK_TEXT, "Monitors").click()
              time.sleep(2)
              self._Driver.find_element(By.LINK_TEXT, "ASUS Full HD").click()
              time.sleep(2)
              self._Driver.find_element(By.LINK_TEXT, "Add to cart").click()
              time.sleep(2)
              action = self._Driver.switch_to.alert.accept()
              time.sleep(2)
              print("se añadieron los monitores")
              ################
              #Vamos al carrito
              self._Driver.find_element(By.LINK_TEXT, "Cart").click()
              time.sleep(10)
              time.sleep(10)
              time.sleep(10)

    #self._Driver.quit()

if __name__ == '__main__':
       unittest.main()