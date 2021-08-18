import unittest
from selenium import webdriver

class HomePageTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"./chromedriver.exe")
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("http://demo-store.seleniumacademy.com/")
        
        

    def test_search_text_fiels(self): #Busca por ID
        search_field = self.driver.find_element_by_id("search")

    def test_search_text_field_by_name(self): #Busca por  name
        search_field = self.driver.find_element_by_name("q")

    def test_search_text_field_class_name(self): #Busca por class name
        search_field = self.driver.find_element_by_class_name("input-text")

    def test_search_button_enabled(self): #Busca por class name
        buttom = self.driver.find_element_by_class_name("button")

    def test_count_of_promo_banner_images(self):
        banner_list = self.driver.find_element_by_class_name("promos")
        banners = banner_list.find_elements_by_tag_name('img') # Crea variable con los elementos del objeto IMG por tag
        self.assertEqual(3, len(banners)) # Verifica validacion conteo de los elementos del objeto

    def test_vip_promo(self): #Busca por XPath - Tocar dale copiar y decirle para xpath en el sitio
        vip_promo = self.driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div/div[2]/div[1]/ul/li[2]/a/img')

    def test_shopping_cart(self):
        shopping_cart_icon = self.driver.find_element_by_css_selector("div.header-minicart span.icon")


    def  tearDown(self):  #Cerar la prueba - cerrar el navegador
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)