from time import sleep
from myStore import myStoreDriverWeb,myStoreVariables,basePage

d = myStoreDriverWeb.myStoreDriverWeb
v = myStoreVariables
p = basePage.BasePage

xpath = "XPATH"
id = "ID"
name = "NAME"
className = "CLASS"
dirMyStore = '../evidencias/MyStoreOnline'

class myStorePage():
    def autenticacao(self, email, senha):
        p.clicar(self,className,v.labelSignIn)
        p.escrever(self,id,v.campoEmail, email)
        p.escrever(self,id,v.campoSenha, senha)
        p.clicar(self,id,v.botaoSignIn)

    def escolherCategoria(self):
        p.clicar(self,xpath,v.labelWomen)
        p.scrollDown(self,"550")

    def escolherProduto(self):
        p.clicar(self, xpath, v.imgFadedShortSleeveTshirts)
        p.switchToFrame(self, xpath, v.iFrame_FadedShortSleeveTshirts)
        p.checkIfElementIsVisible(self, xpath, v.txt_FadedShortSleeveTshirts)

    def etapa1_AdcionarAoCarrinho(self):
        p.clicar(self,name,v.botaoAddToCart)