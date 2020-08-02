import os, unittest,time

from selenium import webdriver
from myStore import myStoreDriverWeb,myStorePage

d = myStoreDriverWeb.myStoreDriverWeb
p = myStorePage.myStorePage

class myStoreTest(unittest.TestCase):
    # driver = webdriver.Chrome(executable_path="chromedriver")
    driver = webdriver.Chrome()

    def setUp(self):
        d.criarDriver(self)

    def test_RealizarCompraOnline(self):
        p.autenticacao(self,"teste.nove@mail.com","abc@12345")
        p.escolherCategoria(self)
        p.escolherProduto(self)
        p.etapa1_AdcionarAoCarrinho(self)
        p.etapa2_Summary(self)
        p.etapa3_Address(self)
        p.etapa4_Shipping(self)
        p.etapa5_Payment(self)
        p.deslogar(self)

    def tearDown(self):
        d.fecharDriver(self)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(myStoreTest)
    unittest.TextTestRunner(verbosity=2).run(suite)