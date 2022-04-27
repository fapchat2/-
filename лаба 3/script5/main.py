from keyring import delete_password
import re
import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
import design  # Это наш конвертированный файл дизайна


class MainWindow(QMainWindow, design.Ui_MainWindow):
    """Main Window."""
    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        # print(self.lineEdit.text())
        # print(self.pushButton.clicked.connect(StringFormatter().numbersToAsterisks(self.lineEdit.text())))
        self.pushButton.clicked.connect(self.printValue)
    def printValue(self):
        st = self.lineEdit.text()
        if(self.checkBox.isChecked()):
            st = StringFormatter().numbersToAsterisks(st)
        if(self.checkBox_2.isChecked() and self.radioButton.isChecked()):
            st = StringFormatter().sortByLength(st)
        if(self.checkBox_2.isChecked() and self.radioButton_2.isChecked()):
            st = StringFormatter().sortBylexicographicOrder(st)
        if(self.checkBox_3.isChecked()):
            st = StringFormatter().delete(self.spinBox.value(), st)  
        if(self.checkBox_4.isChecked()):
            st = StringFormatter().oneSpaceAmongTheChars(st)  
        print(st)




def replacer(match):
    return "*"
class StringFormatter:
    def delete(self, numb, text):
        return ' '.join(list(filter(lambda x: len(x) >= numb, text.split())))
    def numbersToAsterisks(self, str):        
        return re.sub(r'\d', replacer, str)    
    def oneSpaceAmongTheChars(self, str):
        lst = list(str)
        lst1 = []
        for i in range(len(lst)):
            if (re.match(r'\S', lst[i])):
                lst1.append(" " + lst[i])
            else:
                lst1.append(" ")
        return ' '.join(lst1)
    def sortByLength(self, st):
        lst = st.split()
        return ' '.join(sorted(lst, key=len))
    def sortBylexicographicOrder(self, str):
        words = str.split()
        words.sort()
        return ' '.join(words)


# print("Текст без слов, длина которых меньше {}: ".format(2) , StringFormatter().delete(2, "text ww t texttt t"))
# print("Текст со * вместо каждого числа: ",StringFormatter().numbersToAsterisks("ewq 22 qwe2"))
# print("Текст с пробельчиком после каждого символа: ",StringFormatter().oneSpaceAmongTheChars("ewq 22 qwe2"))
# print("Текст с сортировкой по размеру слова: ",StringFormatter().sortByLength("ewq wwwwwww 22 qwe2"))
# print("Текст сортировакой слов lexicographicOrder: ",StringFormatter().sortBylexicographicOrder("неггр негр гариолла рогилла Ваня ваня"))



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())