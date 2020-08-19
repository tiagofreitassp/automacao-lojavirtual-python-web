# automacao-lojavirtual-python-web
Scripts de automação web em uma Loja Virtual desenvolvido com Python, Unittest e Selenium.

### Cobertura dos testes:  ###

* Realizar compra online

## Tecnologias:
* [Python 3.8](https://www.python.org/)
* [unittest](https://docs.python.org/3/library/unittest.html)
* [Selenium](https://selenium-python.readthedocs.io/)
* [Pycharm](https://www.jetbrains.com/pt-br/pycharm/)
* [PyPI](https://pypi.org/project/selenium/)

## Dependências:
* Selenium
* OS
* Appium-Python-Client
* Time
* DocX
* Utilize o pip install para instalar via terminal os drivers dos navegadores.

## Instruções de execução:

###  - Plataforma
*Importante:

O projeto foi criado para executar no MacOS. Mas pode receber adaptacoes para executar no Windows e Linux caso nao execute bem fora do MacOS.

Recomendado utilizar o Intellij Idea, mas pode usar o Eclipse IDE, Visual Studio Code ou Spring Tools Suite.

###  - Fluxo
*Descricao: Este script ira executar uma compra online, seguindo o fluxo desde a escolha do produto ate a etapa de confirmacao da compra.

###  - Massas
*Descricao: 
Apos a execucao as imagens de evidencias sao armazenadas na pasta evidencias.

Para visualizar as evidencias no documento pode usar o MS Office Word ou o LibreOffice.

Antes de executar nao esqueca de trocar as massas por uma adequada. Nao ha problema em usar a massa disponivel na feature desde que verifique antes se o site nao apagou do banco de dados.

###  - Evidencias
*Descricao:
Apos a execucao as imagens de evidencias sao armazenadas na pasta evidencias.

Para visualizar as evidencias no documento pode usar o MS Office Word ou o LibreOffice

###  - Inicializar a automação
*Descricao:

Inserir as massas para teste na classe myStoreTest.

Abrir a classe myStoreTest.py no PyCharm