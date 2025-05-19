import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, 
                             QPushButton, QHBoxLayout)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPalette, QColor

class ClientesWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent_window = parent
        self.setWindowTitle("Módulo de Clientes")
        self.resize(900, 600)
        
        # Establecer el color de fondo turquesa
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor("#45B5AA"))
        self.setPalette(palette)
        
        # Widget central y layout principal
        central_widget = QWidget()
        main_layout = QVBoxLayout(central_widget)
        
        # Título y botón de regresar
        title_layout = QHBoxLayout()
        
        # Botón de regresar
        back_button = QPushButton("Regresar")
        back_button.setStyleSheet("""
            QPushButton {
                background-color: #f0ad4e;
                color: white;
                border-radius: 5px;
                padding: 5px 10px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #ec971f;
            }
        """)
        back_button.clicked.connect(self.go_back_to_main)
        title_layout.addWidget(back_button)
        
        # Título
        title_label = QLabel("Gestión de Clientes")
        title_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        title_layout.addWidget(title_label)
        title_layout.addStretch()
        
        main_layout.addLayout(title_layout)
        
        # Mensaje de placeholder
        placeholder_label = QLabel("Módulo de Clientes - En desarrollo")
        placeholder_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        placeholder_label.setStyleSheet("font-size: 24px; color: #333333;")
        main_layout.addWidget(placeholder_label)
        
        self.setCentralWidget(central_widget)
    
    def go_back_to_main(self):
        """Cierra esta ventana y vuelve a mostrar la ventana principal"""
        if self.parent_window:
            self.parent_window.show()
        self.hide()
    
    def closeEvent(self, event):
        """Captura el evento de cierre de ventana para volver a la principal"""
        self.go_back_to_main()
        event.ignore()

# Solo ejecutar si se llama directamente
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ClientesWindow()
    window.show()
    sys.exit(app.exec())