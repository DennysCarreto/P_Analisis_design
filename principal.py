from PyQt6.QtWidgets import QMainWindow, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QWidget
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

#from login import LoginWindow  

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Farma PLUS - Principal")
        self.setFixedSize(600, 400)
        
        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout principal vertical
        main_layout = QVBoxLayout(central_widget)

        # Layout superior para el botón de cerrar sesión
        top_layout = QHBoxLayout()
        top_layout.addStretch()  # poner el botón a la derecha

        logout_button = QPushButton("Cerrar sesión")
        logout_button.setFixedSize(120, 35)
        logout_button.setStyleSheet("""
            QPushButton {
                background-color: #d9534f;
                color: white;
                border-radius: 5px;
                font-size: 13px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #c9302c;
            }
        """)
        logout_button.clicked.connect(self.logout)
        top_layout.addWidget(logout_button)

        # Agrega el layout superior al layout principal
        main_layout.addLayout(top_layout)

        # Etiqueta de bienvenida centrada
        welcome_label = QLabel("¡Bienvenido a Farma PLUS!")
        welcome_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        welcome_label.setFont(QFont("Arial", 20, QFont.Weight.Bold))
        main_layout.addStretch()
        main_layout.addWidget(welcome_label)
        main_layout.addStretch()

    def logout(self):
        from login import LoginWindow  # Importación dentro de la función para evitar el ciclo
        """Cerrar sesión y volver al login"""
        self.login_window = LoginWindow()
        self.login_window.show()
        self.close()