import matplotlib.pyplot as plt
import math
import sys
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QListWidgetItem


class Graph(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('test.ui', self)
        self.pushButton.clicked.connect(self.push)
        self.ℏ = 6.62607015 * (10 ** -34)  # постоянная планка
        # self.m2 = float(input("Введите эффективную массу электрона для второго графика: "))
        #self.T = [0, 25, 50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 375, 400]
        # self.T2 = [0, 5, 30, 55, 80, 105, 130, 155, 180, 205, 230, 255, 280, 305, 330, 355, 380]
        self.k = 1.380649 * (10 ** (-23))
        # self.E = float(input("Введите ширину запрещенной зоны для первого графика (эВ): "))
        # self.E2 = float(input("Введите ширину запрещенной зоны для второго графика (эВ): "))
        self.T = []
        self.p = []
        self.p2 = []

        # x = np.arange(-10, 10.01, 0.01)

        # for j in range(len(T2)):
        #    p2.append((((T2[j] * k * 2 * m2)**3/2)/(4 * (math.pi**3/2) * ℏ**3)) * (2.718**((E2 * 1.602176634*10**-19)/2 * k * T2[j])))

    def push(self):
        self.E = float(self.EText.toPlainText())
        self.m = float(self.MText.toPlainText())
        self.Tmin = float(self.TMinimumText.toPlainText())
        self.Tmax = float(self.TMaximumText.toPlainText())
        for j in range(int(self.Tmin), int(self.Tmax), 25):
            self.T.append(j)
        # self.line1.remove()
        for i in range(len(self.T)):
            self.p.append((((self.T[i] * self.k * 2 * self.m) ** 3 / 2) / (4 * (math.pi ** 3 / 2) * self.ℏ ** 3)) *
                          (2.718 ** ((self.E * 1.602176634 * 10 ** -19) / 2 * self.k * self.T[i])))
        plt.plot(self.T, self.p)
        # self.line1 = plt.plot(self.T, self.p)
        plt.savefig('mainGraph')
        #plt.show()
        j = 0
        i = 0
        self.T = []
        self.p = []
        self.label.setPixmap(QPixmap('mainGraph.png'))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    op = Graph()
    op.show()
    sys.exit(app.exec_())
