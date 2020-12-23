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
        d.criarPastaEvidencia(self,dirMyStore)
        p.clicar(self,className,v.labelSignIn)
        p.escrever(self,id,v.campoEmail, email)
        p.escrever(self,id,v.campoSenha, senha)
        d.gerarScreenshot(self, dirMyStore, "Ev1")
        p.clicar(self,id,v.botaoSignIn)

    def escolherCategoria(self):
        p.clicar(self,xpath,v.labelWomen)
        p.scrollDown(self,"550")
        d.gerarScreenshot(self, dirMyStore, "Ev2")

    def escolherProduto(self):
        p.clicar(self, xpath, v.imgFadedShortSleeveTshirts)
        p.switchToFrame(self, xpath, v.iFrame_FadedShortSleeveTshirts)
        p.checkIfElementIsVisible(self, xpath, v.txtFadedShortSleeveTshirts)
        d.gerarScreenshot(self, dirMyStore, "Ev3")

    def etapa1_AdcionarAoCarrinho(self):
        p.clicar(self,name,v.botaoAddToCart)
        p.returnToWindowPrincipal(self)
        d.gerarScreenshot(self, dirMyStore, "Ev4")
        p.clicar(self,xpath,v.botaoProceedToCheckout)

    def etapa2_Summary(self):
        p.checkIfElementIsVisible(self,id,v.txtShoppingCartSummary)
        sleep(3)
        p.scrollDown(self,"400")
        sleep(6)
        d.gerarScreenshot(self, dirMyStore, "Ev5")
        p.clicar(self,xpath,v.botaoSHOPPINGCARTSUMMARY_ProceedToCheckout)

    def etapa3_Address(self):
        p.checkIfElementIsVisible(self, className, v.txtAddress)
        p.scrollDown(self, "550")
        sleep(6)
        d.gerarScreenshot(self, dirMyStore, "Ev6")
        p.clicar(self,name,v.botaoAddress_ProceedToCheckout)

    def etapa4_Shipping(self):
        p.checkIfElementIsVisible(self, className, v.txtShipping)
        d.gerarScreenshot(self, dirMyStore, "Ev7")
        p.clicar(self,id,v.checkboxTermOfService)
        sleep(5)
        d.gerarScreenshot(self, dirMyStore, "Ev8")
        p.clicar(self,name,v.botaoShipping_ProceedToCheckout)

    def etapa5_Payment(self):
        p.checkIfElementIsVisible(self, className, v.txtPleaseChooseYourPaymentMethod)
        p.scrollDown(self, "300")
        d.gerarScreenshot(self, dirMyStore, "Ev9")
        p.clicar(self,className,v.botaoPayByBankWire)
        p.checkIfElementIsVisible(self, className, v.txtOrderSummary)
        d.gerarScreenshot(self, dirMyStore, "Ev10")
        p.clicar(self,xpath,v.botaoIconfirmMyOrder)
        p.checkIfElementIsVisible(self, className, v.txtOrderConfirmation)
        d.gerarScreenshot(self, dirMyStore, "Ev11")
        sleep(2)

    def deslogar(self):
        p.clicar(self,className,v.labelSignOut)
        p.checkIfElementIsVisible(self, id, v.campoEmail)
        p.checkIfElementIsVisible(self, id, v.campoSenha)
        d.gerarScreenshot(self, dirMyStore, "Ev12")
        sleep(2)