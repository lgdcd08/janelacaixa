import sys
#importar os componentes para a construção da janela
from PyQt5.QtWidgets import QApplication, QLineEdit,QPushButton, QTableView,QVBoxLayout,QHBoxLayout,QWidget,QLabel
#CONTRUÇÃO DA CLASSE JANELA COM O NOME DE CAIXA
class Caixa(QWidget):
    #Criação do metodo ___init__ que inicia a janela e exibe ela em tela
    def __init__(self):
        super().__init__()
        #vamos definir a posição e o tamanho da tela
        self.setGeometry(0,30,1000,800)

        #vamos definir o titulo d nossa janela
        self.setWindowTitle("Caixa da loja")

        #Vamos criar as labels que representam as colunas esquerda e direita

        #Label da esquerda
        self.label_coluna_esquerda = QLabel()
        self.label_coluna_esquerda.setStyleSheet("QLabel{background-color:#0c0}")
        

        #label da direita
        self.label_coluna_direita =QLabel()
        self.label_coluna_direita.setStyleSheet("QLabel{background-color:#0000ff}")


        #criar o lyout horizontal para as colunas
        self.h_layout = QHBoxLayout()

        #Vamos adicionar as colunas da esquerda e direita ao layout horizontal
        self.h_layout.addWidget(self.label_coluna_esquerda)
        self.h_layout.addWidget(self.label_coluna_direita)

        #Adicionar o layout na tela
        self.setLayout(self.h_layout)
app = QApplication(sys.argv)
cx = Caixa()
cx.show()
app.exec_()