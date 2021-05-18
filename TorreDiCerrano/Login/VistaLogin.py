from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

from TorreDiCerrano.Cliente.controller.ControlloreCliente import ControlloreCliente
from TorreDiCerrano.Cliente.views.VistaCliente import VistaCliente
from TorreDiCerrano.ListaClienti.controller.ControlloreListaClienti import ControlloreListaClienti


class VistaLogin(QWidget):

    def __init__(self, parent=None):
        super(VistaLogin, self).__init__(parent)

        self.controllore = ControlloreListaClienti()

        self.font = QFont("Arial", 17)

        self.v_layout = QVBoxLayout()

        self.label_alto = QLabel("Inserisci i dati per il login")
        self.label_alto.setFont(self.font)
        self.v_layout.addWidget(self.label_alto)

        self.v_layout.addSpacing(10)

        self.label_email = QLabel("E-mail")
        self.label_email.setFont(self.font)
        self.v_layout.addWidget(self.label_email)

        self.campo_email = QLineEdit()
        self.v_layout.addWidget(self.campo_email)

        self.label_password = QLabel("Password")
        self.label_password.setFont(self.font)
        self.v_layout.addWidget(self.label_password)

        self.campo_password = QLineEdit()
        self.campo_password.setEchoMode(QLineEdit.Password)
        self.v_layout.addWidget(self.campo_password)

        self.v_layout.addSpacing(20)

        self.bottone_login = QPushButton("Login")
        self.bottone_login.setFont(self.font)
        self.bottone_login.setStyleSheet("background-color:#ccd9ff;")
        self.bottone_login.clicked.connect(self.login)
        self.v_layout.addWidget(self.bottone_login)

        self.setLayout(self.v_layout)
        self.resize(200, 200)
        self.setWindowTitle("Login")

    def login(self):
        email = self.campo_email.text()
        password = self.campo_password.text()

        if self.controllore.get_cliente_by_email(email) is not None:
            da_mostrare = self.controllore.get_cliente_by_email(email)
            if da_mostrare.password == password:
                self.vista_cliente = VistaCliente(ControlloreCliente(da_mostrare))
                self.vista_cliente.show()
                self.close()
            else:
                QMessageBox.critical(self, "Errore", "La password è errata", QMessageBox.Ok,
                                     QMessageBox.Ok)
        else:
            QMessageBox.critical(self, "Errore", "L'email inserita non è associata ad alcun cliente", QMessageBox.Ok,
                                 QMessageBox.Ok)



