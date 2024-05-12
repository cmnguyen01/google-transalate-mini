from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QTextEdit, QLineEdit, QWidget, QPushButton, QApplication, QComboBox
from googletrans import Translator, LANGUAGES
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        ##set minimum size
        self.setMinimumSize(865,400)

        ##input field
        self.input_field=QLineEdit(self)
        self.input_field.setGeometry(10,240,400,40)
        

        #select language
        self.input_language=QComboBox(self)
        self.input_language.setGeometry(10,140,400,40)

        #return language
        self.output_language=QComboBox(self)
        self.output_language.setGeometry(450,140,400,40)

        #output field
        self.output=QLineEdit(self)
        self.output.setGeometry(450,240,400,40)
        self.output.setReadOnly(True)

        #button
        self.button=QPushButton("translate",self)
        self.button.setGeometry(380,340,100,40)
        #self.button.clicked.connect(translateText(self.input_field.text,self.output.text,self.input_language.currentText,self.output_language.currentText))

        self.show()
        
def translateText(input,output,input_language,output_language):
    src_text=input
    src_lang=input_language
    dest_lang=output_language
    translation=Translator.translate(self=output,text=src_text,dest=dest_lang,src=src_lang)
    

def fillDropDowwn(self):
    pass

app=QApplication(sys.argv)

main_window=Window()

sys.exit(app.exec())
