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
        p.checkIfElementIsVisible(self, xpath, v.txtFadedShortSleeveTshirts)

    def etapa1_AdcionarAoCarrinho(self):
        p.clicar(self,name,v.botaoAddToCart)
        p.returnToWindowPrincipal(self)
        p.clicar(self,xpath,v.botaoProceedToCheckout)

    def etapa2_Summary(self):
        p.checkIfElementIsVisible(self,id,v.txtShoppingCartSummary)
        sleep(6)
        p.scrollDown(self,"400")
        sleep(6)
        p.clicar(self,xpath,v.botaoSHOPPINGCARTSUMMARY_ProceedToCheckout)

    def etapa3_Address(self):
        p.checkIfElementIsVisible(self, className, v.txtAddress)
        p.scrollDown(self, "550")
        sleep(6)
        p.clicar(self,name,v.botaoAddress_ProceedToCheckout)

    def etapa4_Shipping(self):
        p.checkIfElementIsVisible(self, className, v.txtShipping)
        p.clicar(self,id,v.checkboxTermOfService)
        sleep(5)
        p.clicar(self,name,v.botaoShipping_ProceedToCheckout)

    def etapa5_Payment(self):
        p.checkIfElementIsVisible(self, className, v.txtPleaseChooseYourPaymentMethod)
        p.scrollDown(self, "300")
        p.clicar(self,className,v.botaoPayByBankWire)
        p.checkIfElementIsVisible(self, className, v.txtOrderSummary)
        p.clicar(self,xpath,v.botaoIconfirmMyOrder)
        p.checkIfElementIsVisible(self, className, v.txtOrderConfirmation)
        sleep(2)

    def deslogar(self):
        p.clicar(self,className,v.labelSignOut)
        p.checkIfElementIsVisible(self, id, v.campoEmail)
        p.checkIfElementIsVisible(self, id, v.campoSenha)
        sleep(2)