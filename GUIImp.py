from inputTest import *
from tkinter import *
from tkinter.ttk import *

from pandas import array

root = Tk()
root.title("Laptop Store")

# Full Screen Window
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
h = h - 65
root.geometry("%dx%d+0+0" % (w, h))

#   Header
frameHeader = Frame(root, borderwidth=20, relief=GROOVE)
frameHeader.pack(pady=20,ipadx=w)
lblHeader = Label(frameHeader, font=("arial", 44, 'bold'), text="Search Laptops")
lblHeader.pack()

#   Frame for inputs
frameTop = Frame(root, borderwidth=10)
frameTop.pack()

# ram
lblRam = Label(frameTop, font=("arial", 14, 'bold'), text="    Ram:")
lblRam.pack(side=LEFT)

comboRam = Combobox(frameTop, font=("arial", 12))
comboRam['values'] = ("2GB", "4GB", "8GB")
comboRam.set("select")
comboRam.pack(side=LEFT)

# Storage
lblStorage = Label(frameTop, font=("arial", 14, 'bold'), text="    Storage:")
lblStorage.pack(side=LEFT)

comboStorage = Combobox(frameTop, font=("arial", 12))
comboStorage['values'] = ("1000GB","512GB","500GB","64GB")
comboStorage.set("select")
comboStorage.pack(side=LEFT)

# Clock Speed
lblClockSpeed = Label(frameTop, font=("arial", 14, 'bold'), text="    Clock Speed:")
lblClockSpeed.pack(side=LEFT)

comboClkSpeed = Combobox(frameTop, font=("arial", 12))
comboClkSpeed['values'] = ("1.60GHz","1.80GHz","2GHz","2.20GHz","2.50GHz","2.70GHz")
comboClkSpeed.set("select")
comboClkSpeed.pack(side=LEFT)

# Price
lblPrice = Label(frameTop, font=("arial", 14, 'bold'), text="    Price:")
lblPrice.pack(side=LEFT)

comboPrice = Combobox(frameTop, font=("arial", 12))
comboPrice['values'] = ("20000-35000","35001-50000","50001-65000","65001-80000")
comboPrice.set("select The Price in TAKA")
comboPrice.pack(side=LEFT)


# submit
varRam=""
varStorage=""
varClockSpeed=""
varPrice=""

def print_me():
    varRam = comboRam.get()
    varRam = varRam.split("GB")
    varRam = int(varRam[0])/10

    varStorage = comboStorage.get().split("GB")
    varStorage = int(varStorage[0])
    varStorage = varStorage / 1000

    varClockSpeed=comboClkSpeed.get().split("GHz")
    varClockSpeed=float(varClockSpeed[0])
    varClockSpeed=varClockSpeed/3

    varPrice = comboPrice.get().split("-")
    varPrice = (float(varPrice[0]) + float(varPrice[1]))/2
    varPrice = varPrice/90000

    print(str(varRam) + " " + str(varStorage) + " " + str(varClockSpeed) + " " + str(varPrice))

    from inputTest import think
    total = array([varClockSpeed, varRam, varStorage, varPrice])
    prediction=think(total)
    print(prediction)

    prediction=prediction.tolist()
    demo=prediction
    print(type(prediction))
    prBig = float(prediction[0]) + 0.01
    prBig=str(prBig)
    prSmall = float(demo[0]) - 0.01
    prSmall=str(prSmall)

    from dbsql import func
    result=func(prBig,prSmall)

    j = 0
    anotherList = list()
    while j < 9:
        anotherList.insert(j, result[j])
        j = j + 1

    ViewTable(anotherList)

      # view the table with data
    # print(neural_net.think(array([v1, v2, v3, v4])))

#  style for button
style = Style()
style.configure('TButton', font=('calibri', 20, 'bold'), borderwidth='4')
style.map('TButton')

#  Search button
submitframe = Frame(root)
submitframe.pack()
btn = Button(submitframe, text="Search")
btn["command"] = print_me
btn.pack()

# table frame

#tableframe = Frame(root, borderwidth=10, relief=RIDGE)
#tableframe.pack(padx=8,pady=8, ipadx=w)

tableframe = Frame(root, borderwidth=10, relief=RIDGE)
tableframe.pack(padx=8, pady=8, ipadx=w)
canvas = Canvas(tableframe)
canvas.grid(row=0, column=0, sticky="news", ipadx=w)
frameLabel = Frame(canvas)
canvas.create_window((0, 0), window=frameLabel, anchor='nw')

def ViewTable(anotherList):

    list = frameLabel.winfo_children()
    for l in list:
        l.destroy()
    #  Table Column Titles
    Label(frameLabel, text=" Model ", font=("arial", 14, 'bold', UNDERLINE), relief=FLAT).grid(row=0, column=0)
    Label(frameLabel, text=" Clock Speed", font=("arial", 14, 'bold', UNDERLINE), relief=FLAT).grid(row=0, column=2)
    Label(frameLabel, text=" RAM ", font=("arial", 14, 'bold', UNDERLINE), relief=FLAT).grid(row=0, column=4)
    Label(frameLabel, text=" Storage ", font=("arial", 14, 'bold', UNDERLINE), relief=FLAT).grid(row=0, column=6)
    Label(frameLabel, text=" PRICE(TK) ", font=("arial", 14, 'bold', UNDERLINE), relief=FLAT).grid(row=0, column=8)

    #  Table data from data list


    for index, dat in enumerate(anotherList):
        Label(frameLabel, text=dat[0], font=("arial", 14, 'bold'), relief=FLAT).grid(row=index + 1, column=0)
        Label(frameLabel, text="-----", font=("arial", 14), relief=FLAT).grid(row=index + 1, column=1)
        Label(frameLabel, text=dat[1], font=("arial", 14, 'bold'), relief=FLAT).grid(row=index + 1, column=2)
        Label(frameLabel, text="-----", font=("arial", 14), relief=FLAT).grid(row=index + 1, column=3)
        Label(frameLabel, text=dat[2], font=("arial", 14, 'bold'), relief=FLAT).grid(row=index + 1, column=4)
        Label(frameLabel, text="-----", font=("arial", 14), relief=FLAT).grid(row=index + 1, column=5)
        Label(frameLabel, text=dat[3], font=("arial", 14, 'bold'), relief=FLAT).grid(row=index + 1, column=6)
        Label(frameLabel, text="-----", font=("arial", 14), relief=FLAT).grid(row=index + 1, column=7)
        Label(frameLabel, text=dat[4], font=("arial", 14, 'bold'), relief=FLAT).grid(row=index + 1, column=8)
    count = len(anotherList)
    lblCount.config(text=count)
# bottom frame
frameBottom = Frame(root, borderwidth=10, relief=GROOVE)
frameBottom.pack(ipadx=w, side=BOTTOM)
lblSt = Label(frameBottom, text="*** ", font=("arial", 14, 'bold'))
lblSt.pack(side=LEFT)
lblCount = Label(frameBottom, text='0', font=("arial", 14, 'bold'))
lblCount.pack(side=LEFT)
lblDF = Label(frameBottom, font=("arial", 14, 'bold'), text=" Laptops Found ***")
lblDF.pack(side=LEFT)


root.mainloop()
