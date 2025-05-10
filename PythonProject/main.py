import sys
import socket
import threading
from PyQt5.QtWidgets import QApplication, QWidget
from ui_calculator import Ui_Form
from client_application_layer import prepare_message

# Fonction pour exécuter le serveur dans un thread séparé
def run_server():
    from server_transport_layer import start_server
    start_server()

class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.init_signals()

    def init_signals(self):
        # Connecter les boutons aux fonctions associées
        self.ui.Calculer.clicked.connect(self.calculate_result)
        self.ui.Reset.clicked.connect(self.reset_fields)

    def calculate_result(self):
        # Récupérer les valeurs saisies par l'utilisateur
        op1 = self.ui.lineEdit.text()
        operator = self.ui.lineEdit_2.text()
        op2 = self.ui.lineEdit_3.text()

        # Envoyer la requête au serveur et obtenir la réponse
        result = self.send_request_to_server(op1, op2, operator)

        # Afficher le résultat dans l'interface
        self.ui.lineEdit_4.setText(result)

    def send_request_to_server(self, op1, op2, operator):
        # Préparer le flux de bits à envoyer au serveur
        bitstream = prepare_message(op1, op2, operator)

        # Établir une connexion TCP avec le serveur
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(('localhost', 5000))  # On suppose que le serveur tourne en local sur le port 5000
            # Convertir le flux de bits en chaîne de caractères et l’envoyer
            bit_string = ''.join(str(bit) for bit in bitstream)
            s.sendall(bit_string.encode())

            # Recevoir la réponse du serveur
            response = s.recv(4096).decode()
            return response

    def reset_fields(self):
        # Réinitialiser les champs de saisie et de résultat
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit_3.clear()
        self.ui.lineEdit_4.clear()

if __name__ == "__main__":
    # Démarrer le serveur dans un thread séparé pour ne pas bloquer l’interface
    server_thread = threading.Thread(target=run_server)
    server_thread.daemon = True  # Le thread se termine avec l’arrêt de l’application principale
    server_thread.start()

    # Créer et lancer l’application PyQt5
    app = QApplication(sys.argv)
    window = CalculatorApp()
    window.show()

    sys.exit(app.exec_())
