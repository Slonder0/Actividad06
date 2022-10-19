from PySide2.QtWidgets import QMainWindow
from ui_mainwindow import Ui_MainWindow
from administradora import Administradora
from particula import Particula
from PySide2.QtCore import Slot

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        
        self.administrador = Administradora()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Agregar_final.clicked.connect(self.agregar_final)
        self.ui.Agregar_Inicio.clicked.connect(self.agregar_inicio)
        self.ui.Mostrar.clicked.connect(self.ver)
    
    @Slot()   
    def ver(self):
        self.ui.Print.clear()
        self.ui.Print.insertPlainText(str(self.administrador))    
        
        
        
    @Slot()   
    def agregar_final(self):
        ID = self.ui.ID_spinBox.value()
        OrigenX = self.ui.OrigenX_spinBox.value()
        OrigenY = self.ui.OrigenY_spinBox.value()
        DestinoX = self.ui.DestinoX_spinBox.value()
        DestinoY = self.ui.DestinoY_spinBox.value()
        Red = self.ui.Red_spinBox.value()
        Green = self.ui.Green_spinBox.value()
        Blue = self.ui.Blue_spinBox.value()
        
        
        particula1 = Particula(ID,OrigenX,OrigenY,DestinoX,DestinoY)
        self.administrador.agregar_final(particula1)
    
    @Slot()    
    def agregar_inicio(self):
        ID = self.ui.ID_spinBox.value()
        OrigenX = self.ui.OrigenX_spinBox.value()
        OrigenY = self.ui.OrigenY_spinBox.value()
        DestinoX = self.ui.DestinoX_spinBox.value()
        DestinoY = self.ui.DestinoY_spinBox.value()
        Red = self.ui.Red_spinBox.value()
        Green = self.ui.Green_spinBox.value()
        Blue = self.ui.Blue_spinBox.value()
        
        particula1 = Particula(ID,OrigenX,OrigenY,DestinoX,DestinoY)
        self.administrador.agregar_inicio(particula1)
        