from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage():

    def clicar(self, tipoEl, el):
        if tipoEl == "ID" or tipoEl.__eq__("id"):
            self.driver.find_element_by_id(el).click()
        elif tipoEl == "NAME" or tipoEl.__eq__("name"):
            self.driver.find_element_by_name(el).click()
        elif tipoEl == "XPATH" or tipoEl.__eq__("xpath"):
            self.driver.find_element_by_xpath(el).click()
        elif tipoEl == "CLASS" or tipoEl.__eq__("class"):
            self.driver.find_element_by_class_name(el).click()
    sleep(1)

    def selectElement(self, tipoEl, el):
        if tipoEl == "ID" or tipoEl.__eq__("id"):
            self.driver.find_element_by_id(el).click()
        elif tipoEl == "NAME" or tipoEl.__eq__("name"):
            self.driver.find_element_by_name(el).click()
        elif tipoEl == "XPATH" or tipoEl.__eq__("xpath"):
            self.driver.find_element_by_xpath(el).click()
        elif tipoEl == "CLASS" or tipoEl.__eq__("class"):
            element = self.driver.find_element_by_class_name(el)
            self.driver.execute_script("arguments[0].style.border=arguments[1]", element, "solid 4px red")

    def waitElementClickable(self,tipoEl,el):
        button = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.dismiss')))
        button.click()

        if tipoEl == "ID" or tipoEl.__eq__("id"):
            element = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.id, el)))
            element.click()
        elif tipoEl == "NAME" or tipoEl.__eq__("name"):
            element = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.name, el)))
            element.click()
        elif tipoEl == "XPATH" or tipoEl.__eq__("xpath"):
            element = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.xpath, el)))
            element.click()
        elif tipoEl == "CLASS" or tipoEl.__eq__("class"):
            element = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.className, el)))
            element.click()
        sleep(1)

    def escrever(self, tipoEl, el, texto):
        if tipoEl == "ID" or tipoEl.__eq__("id"):
            self.driver.find_element_by_id(el).send_keys(texto)
        elif tipoEl == "NAME" or tipoEl.__eq__("name"):
            self.driver.find_element_by_name(el).send_keys(texto)
        elif tipoEl == "XPATH" or tipoEl.__eq__("xpath"):
            self.driver.find_element_by_xpath(el).send_keys(texto)
        elif tipoEl == "CLASS" or tipoEl.__eq__("class"):
            self.driver.find_element_by_class_name(el).send_keys(texto)
        sleep(1)

    def validarTexto(self,tipoEl,el,texto):
        sleep(1)
        if tipoEl == "ID" or tipoEl.__eq__("id"):
            txt = self.driver.find_element_by_id(el).text
            assert texto == txt
        elif tipoEl == "NAME" or tipoEl.__eq__("name"):
            txt = self.driver.find_element_by_name(el).text
            assert texto == txt
        elif tipoEl == "XPATH" or tipoEl.__eq__("xpath"):
            txt = self.driver.find_element_by_xpath(el).text
            assert texto == txt
        elif tipoEl == "CLASS" or tipoEl.__eq__("class"):
            txt = self.driver.find_element_by_class_name(el).text
            assert texto == txt
        sleep(1)

    def scrollDown(self,altura):
        sleep(1)
        if altura == "100" or altura.__eq__("100"):
            self.driver.execute_script("window.scrollTo(0, 100)")
        elif altura == "200" or altura.__eq__("200"):
            self.driver.execute_script("window.scrollTo(0, 200)")
        elif altura == "300" or altura.__eq__("300"):
            self.driver.execute_script("window.scrollTo(0, 300)")
        elif altura == "400" or altura.__eq__("400"):
            self.driver.execute_script("window.scrollTo(0, 400)")
        elif altura == "550" or altura.__eq__("550"):
            self.driver.execute_script("window.scrollTo(0, 550)")
        sleep(1)

    def checkIfElementIsVisible(self,tipoEl,el):
        sleep(1)
        if tipoEl == "ID" or tipoEl.__eq__("id"):
            self.driver.find_element_by_id(el).is_displayed()
        elif tipoEl == "NAME" or tipoEl.__eq__("name"):
            self.driver.find_element_by_name(el).is_displayed()
        elif tipoEl == "XPATH" or tipoEl.__eq__("xpath"):
            self.driver.find_element_by_xpath(el).is_displayed()
        elif tipoEl == "CLASS" or tipoEl.__eq__("class"):
            self.driver.find_element_by_class_name(el).is_displayed()
        sleep(1)

    def ScrollDownTheEndOfThePage(self):
        sleep(1)
        self.driver.execute_script("window.scrollTo (0, document.body.scrollHeight)")
        sleep(1)

    def switchToFrame(self,tipoEl,el):
        sleep(3)
        if tipoEl == "ID" or tipoEl.__eq__("id"):
            iframe = self.driver.find_element_by_id(el)
            self.driver.switch_to.frame(iframe)
        elif tipoEl == "NAME" or tipoEl.__eq__("name"):
            iframe = self.driver.find_element_by_name(el)
            self.driver.switch_to.frame(iframe)
        elif tipoEl == "XPATH" or tipoEl.__eq__("xpath"):
            iframe = self.driver.find_element_by_xpath(el)
            self.driver.switch_to.frame(iframe)
        elif tipoEl == "CLASS" or tipoEl.__eq__("class"):
            iframe = self.driver.find_element_by_class_name(el)
            self.driver.switch_to.frame(iframe)
        sleep(1)

    def esperar(self, t):
        if t > 0:
            sleep(t)
        else:
            sleep(1)

    def returnToWindowPrincipal(self):
        sleep(2)
        # Retorna para a janela principal (fora do iframe)
        self.driver.switch_to.default_content()
        sleep(2)