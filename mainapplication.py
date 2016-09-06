import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mBox
import pymongo
import pymysql

win=tk.Tk()
win.title("NB Gardens")

tabControl = ttk.Notebook(win)

tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Welcome')
tabControl.pack(expand=1, fill="both")

ttk.Label(tab1, text="WELCOME TO THE NB GARDENS MANAGEMENT SYSTEM\nNAVIGATE THROUGH THE SYSTEM USING\nTHE TABS ABOVE").grid(column =1, row=0)


tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text='Product Feedback')

tab3 = ttk.Frame(tabControl)
tabControl.add(tab3, text='Add a Product')

framing = ttk.LabelFrame(tab2, text=' NB Gardens Product Feedback System ')
framing.grid(column = 0, row = 0,padx = 10, pady = 10)

ttk.Label(framing, text="Feedback ID").grid(column =1, row=0)
idFeedback = tk.StringVar()
idFeedbackEntered=ttk.Entry(framing, width=20, textvariable = idFeedback)
idFeedbackEntered.grid(column = 2, row=0,padx = 10, pady = 10)
idFeedbackEntered.focus()

ttk.Label(framing, text="Product Name").grid(column =1, row=1)
productName = tk.StringVar()
productNameEntered = ttk.Entry(framing, width=20, textvariable = productName)
productNameEntered.grid(column = 2, row=1,padx = 10, pady = 10)

ttk.Label(framing, text="Description").grid(column =1, row=2)
description = tk.StringVar()
descriptionEntered = ttk.Entry(framing, width=20, textvariable = description)
descriptionEntered.grid(column = 2, row=2,padx = 10, pady = 10)

ttk.Label(framing, text="Product Rating").grid(column =1, row=3)
productRating = tk.StringVar()
productRatingEntered = ttk.Entry(framing, width=20, textvariable = productRating)
productRatingEntered.grid(column = 2, row=3, padx = 10, pady = 10)

ttk.Label(framing, text="Comments").grid(column =1, row=4)
comments = tk.StringVar()
commentsEntered = ttk.Entry(framing, width=20, textvariable = comments)
commentsEntered.grid(column = 2, row=4,padx = 10, pady = 10)

ttk.Label(framing, text="Customer Name").grid(column =1, row=5)
name = tk.StringVar()
nameEntered = ttk.Entry(framing, width=20, textvariable = name)
nameEntered.grid(column = 2, row=5,padx = 10, pady = 10)

ttk.Label(framing, text="Location").grid(column =1, row=6)
location = tk.StringVar()
locationEntered = ttk.Entry(framing, width=20, textvariable = location)
locationEntered.grid(column = 2, row=6,padx = 10, pady = 10)


def clickAndMsg():
    clickMe()
    _msgBox()
    
    
    
def _msgBox():
    mBox.showinfo('Feedback System!', 'Your feedback has been added, thank you!')

#button******************************
def clickMe():
    idFB = idFeedback.get()
    idPN = productName.get()
    idDe = description.get()
    idPR = productRating.get()
    idCo = comments.get()
    idNa = name.get()
    idLo = location.get()
    
    client = pymongo.MongoClient()
    db = client["ProductFeedbackNB"]

    collection = db["Products"]

    product = {}
    product["_idFeedback"] = idFB
    product["ProductName"] = idPN
    product["Description"] = idDe
    product["Product Rating"] = idPR
    product["Comments"] = idCo
    product["Customer"] = idNa
    product["Location"] = idLo


    try:
        collection.insert_one(product)
    
    except:
        print("Document already exists")
       
    
action = ttk.Button(framing, text="Submit", command = clickAndMsg)
action.grid(column=2, row=10,padx = 10, pady = 10)









framing2 = ttk.LabelFrame(tab3, text=' NB Gardens Product Addition System ')
framing2.grid(column = 0, row = 0, padx = 10, pady = 10)

ttk.Label(framing2, text="Product ID").grid(column =1, row=0)
idProduct = tk.StringVar()
idProductEntered=ttk.Entry(framing2, width=20, textvariable = idProduct)
idProductEntered.grid(column = 2, row=0,padx = 10, pady = 10)
idProductEntered.focus()

ttk.Label(framing2, text="Product Name").grid(column =1, row=1)
productName2 = tk.StringVar()
productName2Entered = ttk.Entry(framing2, width=20, textvariable = productName2)
productName2Entered.grid(column = 2, row=1,padx = 10, pady = 10)

ttk.Label(framing2, text="Price").grid(column =1, row=3)
price = tk.StringVar()
priceEntered = ttk.Entry(framing2, width=20, textvariable = price)
priceEntered.grid(column = 2, row=3, padx = 10, pady = 10)

ttk.Label(framing2, text="Description").grid(column =1, row=2)
description2 = tk.StringVar()
description2Entered = ttk.Entry(framing2, width=20, textvariable = description2)
description2Entered.grid(column = 2, row=2,padx = 10, pady = 10)

def clickAndMsg2():
    clickMe2()
    _msgBox2()
    
    
    
def _msgBox2():
    mBox.showinfo('Product Update!', 'Product has been added, thank you!')


def clickMe2():
    idProd = idProduct.get()
    idProdName = productName2.get()
    idPrice = price.get()
    idDe2 = description2.get()
    
    resultsofinput=[idProd, idProdName, idPrice, idDe2]
    
    db = pymysql.connect("localhost", "root", "password", "nbGardens3")

    cursor = db.cursor()


    sql="INSERT INTO Product (idProduct, ProductName, Price, Description) VALUES (\"" + str(resultsofinput[0]) + "\",\"" + str(resultsofinput[1]) + "\",\"" + str(resultsofinput[2]) + "\",\"" + str(resultsofinput[3])+ "\");"
    cursor.execute(sql)
    cursor.fetchall()
    db.commit()
    
    cursor.close()


action = ttk.Button(framing2, text="Submit", command = clickMe2)
action.grid(column=2, row=10,padx = 10, pady = 10)


























win.mainloop()