import sys
from selenium import webdriver
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer  # QTimer'ı import ediyoruz
from trendyol_datapull import main  # trendyol_datapull fonksiyonunu içe aktarıyoruz

ortalama_fiyat = 0  # Başlangıçta 0, sonradan atanacak

class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.etiket1 = QtWidgets.QLabel("Fiyat Performans Bilgisayarı Bulma Aracı")
        self.etiket2 = QtWidgets.QLabel("Lütfen Almak İstediğiniz Bilgisayarın Ortalama Fiyatını Girin")
        self.etiket1.move(225, 30)
        self.etiket1.move(225, 45)

        self.button1 = QtWidgets.QPushButton("Başlat")
        self.button1.move(225, 60)

        self.textline = QtWidgets.QLineEdit()
        self.textline.move(225, 50)

        V_box = QtWidgets.QVBoxLayout()
        V_box.addWidget(self.etiket1)
        V_box.addWidget(self.etiket2)
        V_box.addStretch()
        V_box.addWidget(self.textline)
        V_box.addWidget(self.button1) 

        self.button1.clicked.connect(self.button1_click)

        self.setLayout(V_box)  
        self.show()

    def button1_click(self):
        global ortalama_fiyat
        ortalama_fiyat = int(self.textline.text())  # Text'i int'e çevir
        self.close()
        self.pencere2 = Pencere2()
        self.pencere2.show()

        main(ortalama_fiyat)
        self.pencere2.close()
        self.pencere3 = Pencere3()
        self.pencere3.show()

class Pencere2(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.etiket1 = QtWidgets.QLabel("Bilgisayarlar Taranıyor..Lütfen Bekleyin")
        self.etiket1.move(225, 30)

        V_box = QtWidgets.QVBoxLayout()
        V_box.addWidget(self.etiket1)
        V_box.addStretch()
        
        self.setLayout(V_box)
        self.setGeometry(700, 300, 300, 200)

class Pencere3(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        

    def init_ui(self):
        self.etiket1 = QtWidgets.QLabel("Uygun Bilgisayar Bulundu.")
        self.etiket1.move(225, 30)

        self.button2 = QtWidgets.QPushButton("Lİnki Aç")
        self.button2.move(225, 60)

        V_box = QtWidgets.QVBoxLayout()
        V_box.addWidget(self.etiket1)
        V_box.addStretch()

        V_box.addWidget(self.button2) 
        self.setLayout(V_box)
        
        self.setGeometry(700, 300, 300, 200)
        self.button2.clicked.connect(self.final_rul)

    def final_rul(self):
        # Tarayıcıyı burada başlat
        self.browser = webdriver.Edge()

        with open('data.txt', 'r') as file:
            url = str(file.read())
        self.browser.get(url)
    
    def closeEvent(self, event):
        # Tarayıcı başlatıldıysa kapat
        if hasattr(self, 'browser') and self.browser:
            self.browser.quit()
        event.accept()  



app = QtWidgets.QApplication(sys.argv)
pencere = Pencere()

sys.exit(app.exec_())
