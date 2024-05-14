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
        self.input_field.setText("default")
        

        #select language
        self.input_language=QComboBox(self)
        self.input_language.setGeometry(10,140,400,40)

        #return language
        self.output_language=QComboBox(self)
        self.output_language.setGeometry(450,140,400,40)
        self.fillDropDowwn()
        self.input_language.setCurrentText('english')

        #output field
        self.output=QLineEdit(self)
        self.output.setGeometry(450,240,400,40)
        self.output.setReadOnly(True)

        #button
        self.button=QPushButton("translate",self)
        self.button.setGeometry(380,340,100,40)
        
        self.button.clicked.connect(lambda:self.translateText(self.input_field.text(),self.output.text(),self.input_language.currentText(),self.output_language.currentText()))
        #self.button.clicked.connect(lambda:sayhello(self.input_field.text()))
        self.button.show()
        self.show()
        
    def translateText(self,input,output,input_language,output_language):
        src_text=input
        #convert to abreviation
        src_lang=self.returnabr(input_language)
        dest_lang=self.returnabr(output_language)
        #run translator method
        translation=Translator()
        outputtext=translation.translate(text=src_text,dest=dest_lang,src=src_lang)
        self.output.setText(outputtext.text)
        
        
   

    def fillDropDowwn(self):
        for lang in LANGUAGES.values():
            self.input_language.addItem(lang)
            self.output_language.addItem(lang)
    #function for 
    def returnabr(self,lang):
        for abr,lan in LANGUAGES.items():
            if lang==lan:
                return abr

app=QApplication(sys.argv)

main_window=Window()

sys.exit(app.exec())
