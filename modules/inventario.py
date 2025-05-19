import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, 
                            QVBoxLayout, QHBoxLayout, QWidget, QTableWidget, QTableWidgetItem, 
                            QDialog, QDateEdit, QMessageBox, QHeaderView)
from PyQt6.QtCore import Qt, QDate
from PyQt6.QtGui import QPalette, QColor


class ProductDialog(QDialog):
    def __init__(self, parent=None, product_data=None):
        super().__init__(parent)
        self.setWindowTitle("Registrar / Editar Producto")
        self.resize(400, 400)
        
        self.layout = QVBoxLayout()
    
        # Campos del formulario
        self.codigo_label = QLabel("Código:")
        self.codigo_input = QLineEdit()
        
        self.nombre_label = QLabel("Nombre:")
        self.nombre_input = QLineEdit()
        
        self.categoria_label = QLabel("Categoría:")
        self.categoria_input = QLineEdit()
        
        self.stock_actual_label = QLabel("Stock Actual:")
        self.stock_actual_input = QLineEdit()
        
        self.stock_minimo_label = QLabel("Stock Mínimo:")
        self.stock_minimo_input = QLineEdit()
        
        self.precio_venta_label = QLabel("Precio Venta:")
        self.precio_venta_input = QLineEdit()
        
        self.precio_compra_label = QLabel("Precio Compra:")
        self.precio_compra_input = QLineEdit()
        
        self.proveedor_label = QLabel("Proveedor:")
        self.proveedor_input = QLineEdit()
        
        self.vencimiento_label = QLabel("Vencimiento:")
        self.vencimiento_input = QDateEdit()
        self.vencimiento_input.setCalendarPopup(True)
        self.vencimiento_input.setDate(QDate.currentDate())
        
        self.fecha_registro_label = QLabel("Fecha Registro:")
        self.fecha_registro_input = QDateEdit()
        self.fecha_registro_input.setCalendarPopup(True)
        self.fecha_registro_input.setDate(QDate.currentDate())
        
        # Botones
        self.button_layout = QHBoxLayout()
        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.setStyleSheet("QPushButton { background-color: #ff6961; border-radius: 5px; padding: 5px; }")
        self.cancel_button.clicked.connect(self.reject)
        
        self.ok_button = QPushButton("OK")
        self.ok_button.setStyleSheet("QPushButton { background-color: #77dd77; border-radius: 5px; padding: 5px; }")
        self.ok_button.clicked.connect(self.accept)
        
        self.button_layout.addWidget(self.cancel_button)
        self.button_layout.addWidget(self.ok_button)
        
        # Añadir widgets al layout
        self.layout.addWidget(self.codigo_label)
        self.layout.addWidget(self.codigo_input)
        self.layout.addWidget(self.nombre_label)
        self.layout.addWidget(self.nombre_input)
        self.layout.addWidget(self.categoria_label)
        self.layout.addWidget(self.categoria_input)
        self.layout.addWidget(self.stock_actual_label)
        self.layout.addWidget(self.stock_actual_input)
        self.layout.addWidget(self.stock_minimo_label)
        self.layout.addWidget(self.stock_minimo_input)
        self.layout.addWidget(self.precio_venta_label)
        self.layout.addWidget(self.precio_venta_input)
        self.layout.addWidget(self.precio_compra_label)
        self.layout.addWidget(self.precio_compra_input)
        self.layout.addWidget(self.proveedor_label)
        self.layout.addWidget(self.proveedor_input)
        self.layout.addWidget(self.vencimiento_label)
        self.layout.addWidget(self.vencimiento_input)
        self.layout.addWidget(self.fecha_registro_label)
        self.layout.addWidget(self.fecha_registro_input)
        self.layout.addLayout(self.button_layout)
        
        self.setLayout(self.layout)
        
        # Si se proporcionan datos, llenar el formulario
        if product_data:
            self.populate_form(product_data)
    
    def populate_form(self, product_data):
        self.codigo_input.setText(product_data.get('codigo', ''))
        self.nombre_input.setText(product_data.get('nombre', ''))
        self.categoria_input.setText(product_data.get('categoria', ''))
        self.stock_actual_input.setText(str(product_data.get('stock_actual', '')))
        self.stock_minimo_input.setText(str(product_data.get('stock_minimo', '')))
        self.precio_venta_input.setText(str(product_data.get('precio_venta', '')))
        self.precio_compra_input.setText(str(product_data.get('precio_compra', '')))
        self.proveedor_input.setText(product_data.get('proveedor', ''))
        
        if 'vencimiento' in product_data:
            self.vencimiento_input.setDate(product_data['vencimiento'])
        if 'fecha_registro' in product_data:
            self.fecha_registro_input.setDate(product_data['fecha_registro'])
    
    def get_product_data(self):
        return {
            'codigo': self.codigo_input.text(),
            'nombre': self.nombre_input.text(),
            'categoria': self.categoria_input.text(),
            'stock_actual': self.stock_actual_input.text(),
            'stock_minimo': self.stock_minimo_input.text(),
            'precio_venta': self.precio_venta_input.text(),
            'precio_compra': self.precio_compra_input.text(),
            'proveedor': self.proveedor_input.text(),
            'vencimiento': self.vencimiento_input.date(),
            'fecha_registro': self.fecha_registro_input.date()
        }


class InventarioWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent_window = parent
        self.setWindowTitle("Módulo de Inventario")
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
        back_button.clicked.connect(self.back)
        title_layout.addWidget(back_button)
        
        # Título
        title_label = QLabel("Gestión de Inventario")
        title_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        title_layout.addWidget(title_label)
        title_layout.addStretch()
        
        main_layout.addLayout(title_layout)
        
        # Barra de búsqueda
        search_layout = QHBoxLayout()
        
        self.nombre_input = QLineEdit()
        self.nombre_input.setPlaceholderText("Nombre")
        
        self.codigo_input = QLineEdit()
        self.codigo_input.setPlaceholderText("Código")
        
        self.categoria_input = QLineEdit()
        self.categoria_input.setPlaceholderText("Categoría")
        
        self.proveedor_input = QLineEdit()
        self.proveedor_input.setPlaceholderText("Proveedor")
        
        self.buscar_button = QPushButton("Buscar")
        self.buscar_button.setStyleSheet("QPushButton { background-color: white; border-radius: 5px; padding: 5px; }")
        self.buscar_button.clicked.connect(self.buscar_productos)
        
        self.listar_button = QPushButton("Listar Todo")
        self.listar_button.setStyleSheet("QPushButton { background-color: white; border-radius: 5px; padding: 5px; }")
        self.listar_button.clicked.connect(self.listar_todos)
        
        search_layout.addWidget(self.nombre_input)
        search_layout.addWidget(self.codigo_input)
        search_layout.addWidget(self.categoria_input)
        search_layout.addWidget(self.proveedor_input)
        search_layout.addWidget(self.buscar_button)
        search_layout.addWidget(self.listar_button)
        
        main_layout.addLayout(search_layout)
        
        # Botones de acción
        action_layout = QHBoxLayout()
        
        self.registrar_button = QPushButton("Registrar Producto")
        self.registrar_button.setStyleSheet("QPushButton { background-color: white; border-radius: 5px; padding: 10px; }")
        self.registrar_button.clicked.connect(self.registrar_producto)
        
        self.editar_button = QPushButton("Editar Producto")
        self.editar_button.setStyleSheet("QPushButton { background-color: white; border-radius: 5px; padding: 10px; }")
        self.editar_button.clicked.connect(self.editar_producto)
        
        self.eliminar_button = QPushButton("Eliminar Producto")
        self.eliminar_button.setStyleSheet("QPushButton { background-color: white; border-radius: 5px; padding: 10px; }")
        self.eliminar_button.clicked.connect(self.eliminar_producto)
        # Agregar el botón de limpiar
        self.limpiar_button = QPushButton("Limpiar")
        self.limpiar_button.setStyleSheet("""
            QPushButton { 
                background-color: #d9534f; 
                color: white;
                border-radius: 5px; 
                padding: 10px; 
            }
            QPushButton:hover { 
                background-color: #c9302c; 
            }
        """)
        self.limpiar_button.clicked.connect(self.limpiar_inventario)
        
        action_layout.addWidget(self.registrar_button)
        action_layout.addWidget(self.editar_button)
        action_layout.addWidget(self.eliminar_button)
        action_layout.addWidget(self.limpiar_button)
        
        main_layout.addLayout(action_layout)
        
        # Tabla de inventario
        self.table = QTableWidget()
        self.table.setColumnCount(10)
        self.table.setHorizontalHeaderLabels([
            "Código", "Nombre", "Categoría", "Stock Actual", "Stock Mínimo",
            "Precio Venta", "Precio Compra", "Proveedor", "Vencimiento", "Fecha Registro"
        ])
        
        # Configurar el comportamiento de la tabla
        self.table.setAlternatingRowColors(True)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        
        main_layout.addWidget(self.table)
        
        self.setCentralWidget(central_widget)
        
        # Datos de ejemplo
        self.productos = []
        self.agregar_datos_ejemplo()
        self.actualizar_tabla()
    
    def agregar_datos_ejemplo(self):
        # Agregar algunos datos de ejemplo
        self.productos = [
            {
                'codigo': 'a', 'nombre': 'a', 'categoria': 'a', 
                'stock_actual': 'a', 'stock_minimo': 'a', 
                'precio_venta': 'a', 'precio_compra': 'a', 
                'proveedor': 'a', 'vencimiento': QDate.currentDate(), 
                'fecha_registro': QDate.currentDate()
            },
            {
                'codigo': 'b', 'nombre': 'b', 'categoria': 'medicina', 
                'stock_actual': 'b', 'stock_minimo': 'b', 
                'precio_venta': 'b', 'precio_compra': 'b', 
                'proveedor': 'b', 'vencimiento': QDate.currentDate(), 
                'fecha_registro': QDate.currentDate()
            },
            {
                'codigo': 'c', 'nombre': 'c', 'categoria': 'c', 
                'stock_actual': 'c', 'stock_minimo': 'c', 
                'precio_venta': 'c', 'precio_compra': 'c', 
                'proveedor': 'c', 'vencimiento': QDate.currentDate(), 
                'fecha_registro': QDate.currentDate()
            },
        ]
    
    def actualizar_tabla(self, productos_filtrados=None):
        productos_mostrados = productos_filtrados if productos_filtrados is not None else self.productos
        
        self.table.setRowCount(0)  # Limpiar tabla
        
        for row_index, producto in enumerate(productos_mostrados):
            self.table.insertRow(row_index)
            
            self.table.setItem(row_index, 0, QTableWidgetItem(producto['codigo']))
            self.table.setItem(row_index, 1, QTableWidgetItem(producto['nombre']))
            self.table.setItem(row_index, 2, QTableWidgetItem(producto['categoria']))
            self.table.setItem(row_index, 3, QTableWidgetItem(str(producto['stock_actual'])))
            self.table.setItem(row_index, 4, QTableWidgetItem(str(producto['stock_minimo'])))
            self.table.setItem(row_index, 5, QTableWidgetItem(str(producto['precio_venta'])))
            self.table.setItem(row_index, 6, QTableWidgetItem(str(producto['precio_compra'])))
            self.table.setItem(row_index, 7, QTableWidgetItem(producto['proveedor']))
            self.table.setItem(row_index, 8, QTableWidgetItem(producto['vencimiento'].toString("yyyy-MM-dd")))
            self.table.setItem(row_index, 9, QTableWidgetItem(producto['fecha_registro'].toString("yyyy-MM-dd")))
    
    def registrar_producto(self):
        dialog = ProductDialog(self)
        result = dialog.exec()
        
        if result == QDialog.DialogCode.Accepted:
            nuevo_producto = dialog.get_product_data()
            self.productos.append(nuevo_producto)
            self.actualizar_tabla()
            QMessageBox.information(self, "Éxito", "Producto registrado correctamente")
    
    def editar_producto(self):
        selected_rows = self.table.selectedItems()
        
        if not selected_rows:
            QMessageBox.warning(self, "Advertencia", "Por favor seleccione un producto para editar")
            return
        
        selected_row = selected_rows[0].row()
        producto_seleccionado = self.productos[selected_row]
        
        dialog = ProductDialog(self, producto_seleccionado)
        result = dialog.exec()
        
        if result == QDialog.DialogCode.Accepted:
            self.productos[selected_row] = dialog.get_product_data()
            self.actualizar_tabla()
            QMessageBox.information(self, "Éxito", "Producto editado correctamente")
    
    def eliminar_producto(self):
        selected_rows = self.table.selectedItems()
        
        if not selected_rows:
            QMessageBox.warning(self, "Advertencia", "Por favor seleccione un producto para eliminar")
            return
        
        selected_row = selected_rows[0].row()
        codigo_producto = self.productos[selected_row]['codigo']
        
        confirmation = QMessageBox.question(
            self, "Confirmar eliminación", 
            f"¿Está seguro que desea eliminar el producto {codigo_producto}?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        
        if confirmation == QMessageBox.StandardButton.Yes:
            self.productos.pop(selected_row)
            self.actualizar_tabla()
            QMessageBox.information(self, "Éxito", "Producto eliminado correctamente")
    
    def limpiar_inventario(self):
        """Función para limpiar la visualización de la tabla sin eliminar los productos"""
        if self.table.rowCount() == 0:
            QMessageBox.information(self, "Información", "La tabla ya está vacía")
            return
            
        # Simplemente vaciar la tabla sin modificar los datos subyacentes
        self.table.setRowCount(0)
        QMessageBox.information(self, "Éxito", "Tabla limpiada correctamente")
        # Los productos siguen almacenados en self.productos
        # Se pueden restaurar usando el botón "Listar Todo"

    def buscar_productos(self):
        nombre = self.nombre_input.text().lower()
        codigo = self.codigo_input.text().lower()
        categoria = self.categoria_input.text().lower()
        proveedor = self.proveedor_input.text().lower()
        
        productos_filtrados = []
        
        for producto in self.productos:
            if (nombre and nombre not in producto['nombre'].lower()):
                continue
            if (codigo and codigo not in producto['codigo'].lower()):
                continue
            if (categoria and categoria not in producto['categoria'].lower()):
                continue
            if (proveedor and proveedor not in producto['proveedor'].lower()):
                continue
            
            productos_filtrados.append(producto)
        
        self.actualizar_tabla(productos_filtrados)
    
    def listar_todos(self):
        self.nombre_input.clear()
        self.codigo_input.clear()
        self.categoria_input.clear()
        self.proveedor_input.clear()
        self.actualizar_tabla()

    def back(self):
        """Regresar y mostrar principal"""
        from principal import MainWindow   # Importación dentro de la función para evitar el ciclo
        
        # Crear y mostrar la ventana principal
        self.prin_window = MainWindow()
        self.prin_window.show()
        
        # Cerrar la ventana actual
        self.close()

# Solo ejecutar si se llama directamente
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InventarioWindow()
    window.show()
    sys.exit(app.exec())