from PyQt6.QtWidgets import (QMainWindow, QLabel, QPushButton, QVBoxLayout, 
                             QHBoxLayout, QWidget, QGridLayout)
from PyQt6.QtGui import QFont, QIcon, QPixmap
from PyQt6.QtCore import Qt, QSize

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana principal
        self.setWindowTitle("Farma PLUS - Principal")
        self.setFixedSize(800, 600)
        self.setStyleSheet("background-color: #17A398;")  # Color turquesa
        
        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout principal vertical
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(20)

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

        # Título FARMA PLUS+
        title_label = QLabel("FARMA PLUS +")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setFont(QFont("Arial", 28, QFont.Weight.Bold))
        title_label.setStyleSheet("color: black;")
        main_layout.addWidget(title_label)

        # Grid para las 4 secciones
        grid_layout = QGridLayout()
        grid_layout.setSpacing(30)
        
        # Estilo común para los módulos
        module_style = """
            QWidget {
                background-color: #17A398;
                border-radius: 10px;
            }
            QLabel {
                color: black;
                font-weight: bold;
            }
        """
        
        # Función para crear un módulo
        def create_module(title, icon_path, row, col):
            module_widget = QWidget()
            module_widget.setFixedSize(250, 200)
            module_widget.setStyleSheet(module_style)
            module_widget.setCursor(Qt.CursorShape.PointingHandCursor)  # Cambia el cursor al pasar por encima
            
            module_layout = QVBoxLayout(module_widget)
            module_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
            
            # Título del módulo
            title_label = QLabel(title)
            title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            title_label.setFont(QFont("Arial", 16, QFont.Weight.Bold))
            module_layout.addWidget(title_label)
            
            # Icono del módulo
            icon_label = QLabel()
            icon_pixmap = QPixmap(icon_path)
            if not icon_pixmap.isNull():
                icon_label.setPixmap(icon_pixmap.scaled(80, 80, Qt.AspectRatioMode.KeepAspectRatio))
            else:
                # Si no hay icono disponible, mostrar un placeholder
                icon_label.setText("🔍")
                icon_label.setFont(QFont("Arial", 40))
                icon_label.setStyleSheet("color: black;")
            
            icon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            module_layout.addWidget(icon_label)
            
            grid_layout.addWidget(module_widget, row, col)
            
            return module_widget
        
        # Crear los cuatro módulos
        ventas_module = create_module("VENTAS", "images/venta.png", 0, 0)
        clientes_module = create_module("CLIENTES", "images/cliente.png", 0, 1)
        inventario_module = create_module("INVENTARIO", "images/inventario.png", 1, 0)
        proveedores_module = create_module("PROVEEDORES", "images/proveedor.png", 1, 1)
        
        # Conectar eventos de clic (se pueden implementar después)
        ventas_module.mousePressEvent = lambda event: self.open_module("ventas")
        clientes_module.mousePressEvent = lambda event: self.open_module("clientes")
        inventario_module.mousePressEvent = lambda event: self.open_module("inventario")
        proveedores_module.mousePressEvent = lambda event: self.open_module("proveedores")
        
        # Agregar el grid al layout principal
        main_layout.addLayout(grid_layout)
        main_layout.addStretch()

    def logout(self):
        from login import LoginWindow  # Importación dentro de la función para evitar el ciclo
        """Cerrar sesión y volver al login"""
        self.login_window = LoginWindow()
        self.login_window.show()
        self.close()
        
    # abrir cada modulo, hacer lo mismo para el resto de modulos
    def open_module(self, module_name):
        """Abre el módulo seleccionado"""
        print(f"Abriendo módulo: {module_name}")