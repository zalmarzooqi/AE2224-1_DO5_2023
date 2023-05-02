import pandas as pd
import matplotlib.pyplot as plt
import os

excel_path = r"C:\Users\Thomas\Documents\uninhb_sorted - colored - Copy.xlsx"

cols = ["Al At%", "Cu At%", "Mg At%", "Fe At%", "Mn At%", "Si At%", "O At%", "Class"]

data = pd.read_excel(excel_path, sheet_name="Secondary", usecols=cols)

class_a = data[data.Class == "A"]
class_b = data[data.Class == "B"]
class_c = data[data.Class == "C"]
class_d = data[data.Class == "D"]
class_e = data[data.Class == "E"]
class_f = data[data.Class == "F"]

for i in range(len(cols)-1):
    plt.boxplot(class_a.iloc[0:-1, i], sym="", positions=[1], labels="A")
    plt.boxplot(class_b.iloc[0:-1, i], sym="", positions=[2], labels="B")
    plt.boxplot(class_c.iloc[0:-1, i], sym="", positions=[3], labels="C")
    plt.boxplot(class_d.iloc[0:-1, i], sym="", positions=[4], labels="D")
    plt.boxplot(class_e.iloc[0:-1, i], sym="", positions=[5], labels="E")
    plt.boxplot(class_f.iloc[0:-1, i], sym="", positions=[6], labels="F")
    # plt.ylim(0, 100)
    plt.xlabel("Class")
    # plt.axes("A")
    plt.title(cols[i])
    plt.show()
