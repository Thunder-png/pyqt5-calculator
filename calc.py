# Pyqt5 Kütüphaneleri import işlemi
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys


class Window(QMainWindow):

	def __init__(self):
		super().__init__()

		# Pencere Başlığı
		self.setWindowTitle("Hesap Makinesi")
		
		# Pencere ikonu
		self.setWindowIcon(QIcon('./assets/calculator.png'))

		# Pencerenin Geometrisi(x,y)
		self.setGeometry(100, 100, 360, 350)

		# calling method
		self.UiComponents()

		# Widget'ları gösterme
		self.show()

		# Widget lar için method
	def UiComponents(self):

		# Label oluşturma
		self.label = QLabel(self)

		# Oluşturulan Label için geometri ölçüleri
		self.label.setGeometry(5, 5, 350, 70)

		# Çok satırlı label oluşturma
		self.label.setWordWrap(True)

		# label için stylesheet ayarları
		self.label.setStyleSheet("QLabel"
								"{"
								"border : 4px solid black;"
								"background : white;"
								"}")

		# Label in ekran içinde hizalanma bilgisi
		self.label.setAlignment(Qt.AlignRight)

		# Font seçimi
		self.label.setFont(QFont('Arial', 15))


		# Ekrandaki buttonların oluşturulması
		# Push butonunun oluşturulması
		push1 = QPushButton("1", self)

		# buton geometrisinin ayarlanması
		push1.setGeometry(5, 150, 80, 40)

		# Push butonunun oluşturulması
		push2 = QPushButton("2", self)

		# buton geometrisinin ayarlanması
		push2.setGeometry(95, 150, 80, 40)

		# Push butonunun oluşturulması
		push3 = QPushButton("3", self)

		# buton geometrisinin ayarlanması
		push3.setGeometry(185, 150, 80, 40)

		# Push butonunun oluşturulması
		push4 = QPushButton("4", self)

		# buton geometrisinin ayarlanması
		push4.setGeometry(5, 200, 80, 40)

		# Push butonunun oluşturulması
		push5 = QPushButton("5", self)

		# buton geometrisinin ayarlanması
		push5.setGeometry(95, 200, 80, 40)

		# Push butonunun oluşturulması
		push6 = QPushButton("5", self)

		# buton geometrisinin ayarlanması
		push6.setGeometry(185, 200, 80, 40)

		# Push butonunun oluşturulması
		push7 = QPushButton("7", self)

		# buton geometrisinin ayarlanması
		push7.setGeometry(5, 250, 80, 40)

		# Push butonunun oluşturulması
		push8 = QPushButton("8", self)

		# buton geometrisinin ayarlanması
		push8.setGeometry(95, 250, 80, 40)

		# Push butonunun oluşturulması
		push9 = QPushButton("9", self)

		# buton geometrisinin ayarlanması
		push9.setGeometry(185, 250, 80, 40)

		# Push butonunun oluşturulması
		push0 = QPushButton("0", self)

		# buton geometrisinin ayarlanması
		push0.setGeometry(5, 300, 80, 40)

		# Eşittir Butonu
		# Push Button
		push_equal = QPushButton("=", self)

		# buton geometrisinin ayarlanması
		push_equal.setGeometry(275, 300, 80, 40)

		# Eşittir butonu için renk efekti
		c_effect = QGraphicsColorizeEffect()
		c_effect.setColor(Qt.blue)
		push_equal.setGraphicsEffect(c_effect)

		# Artı push buton
		push_plus = QPushButton("+", self)

		# buton geometrisinin ayarlanması
		push_plus.setGeometry(275, 250, 80, 40)

		# Eksi butonu
		push_minus = QPushButton("-", self)

		# buton geometrisinin ayarlanması
		push_minus.setGeometry(275, 200, 80, 40)

		# * Butonu
		push_mul = QPushButton("*", self)

		# buton geometrisinin ayarlanması
		push_mul.setGeometry(275, 150, 80, 40)

		# / butonu
		push_div = QPushButton("/", self)

		# buton geometrisinin ayarlanması
		push_div.setGeometry(185, 300, 80, 40)

		# . butonu
		push_point = QPushButton(".", self)

		# buton geometrisinin ayarlanması
		push_point.setGeometry(95, 300, 80, 40)


		# clear butonu
		push_clear = QPushButton("Clear", self)
		push_clear.setGeometry(5, 100, 200, 40)

		# del butonu
		push_del = QPushButton("Del", self)
		push_del.setGeometry(210, 100, 145, 40)

		# Düğmelerin her birine action ekleme
		push_minus.clicked.connect(self.action_minus)
		push_equal.clicked.connect(self.action_equal)
		push0.clicked.connect(self.action0)
		push1.clicked.connect(self.action1)
		push2.clicked.connect(self.action2)
		push3.clicked.connect(self.action3)
		push4.clicked.connect(self.action4)
		push5.clicked.connect(self.action5)
		push6.clicked.connect(self.action6)
		push7.clicked.connect(self.action7)
		push8.clicked.connect(self.action8)
		push9.clicked.connect(self.action9)
		push_div.clicked.connect(self.action_div)
		push_mul.clicked.connect(self.action_mul)
		push_plus.clicked.connect(self.action_plus)
		push_point.clicked.connect(self.action_point)
		push_clear.clicked.connect(self.action_clear)
		push_del.clicked.connect(self.action_del)


	def action_equal(self):

		# label metnini al
		equation = self.label.text()

		try:
			# ans tuşu al
			ans = eval(equation)

			# metni label a ayarlama
			self.label.setText(str(ans))

		except:
			# Metni label e yazdırma
			self.label.setText("Yanlış Giriş")

	def action_plus(self):
		# etiket metni ekleme
		text = self.label.text()
		self.label.setText(text + " + ")

	def action_minus(self):
		# etiket metni ekleme
		text = self.label.text()
		self.label.setText(text + " - ")

	def action_div(self):
		# etiket metni ekleme
		text = self.label.text()
		self.label.setText(text + " / ")

	def action_mul(self):
		# etiket metni ekleme
		text = self.label.text()
		self.label.setText(text + " * ")

	def action_point(self):
		# etiket metni ekleme
		text = self.label.text()
		self.label.setText(text + ".")

	def action0(self):
		# etiket metni ekleme
		text = self.label.text()
		self.label.setText(text + "0")

	def action1(self):
		# etiket metni ekleme
		text = self.label.text()
		self.label.setText(text + "1")

	def action2(self):
		# etiket metni ekleme
		text = self.label.text()
		self.label.setText(text + "2")

	def action3(self):
		# etiket metni ekleme
		text = self.label.text()
		self.label.setText(text + "3")

	def action4(self):
		# etiket metni ekleme
		text = self.label.text()
		self.label.setText(text + "4")

	def action5(self):
		# etiket metni ekleme
		text = self.label.text()
		self.label.setText(text + "5")

	def action6(self):
		# etiket metni ekleme
		text = self.label.text()
		self.label.setText(text + "6")

	def action7(self):
		# etiket metni ekleme
		text = self.label.text()
		self.label.setText(text + "7")

	def action8(self):
		# etiket metni ekleme
		text = self.label.text()
		self.label.setText(text + "8")

	def action9(self):
		# etiket metni ekleme
		text = self.label.text()
		self.label.setText(text + "9")

	def action_clear(self):
		# Label textini temizleme
		self.label.setText("")

	def action_del(self):
		# tek karakter silme
		text = self.label.text()
		print(text[:len(text)-1])
		self.label.setText(text[:len(text)-1])


# PyQt app ini oluşturma
App = QApplication(sys.argv)

# pencere oluşturma
window = Window()

# Uygulamayı başlat
sys.exit(App.exec())

