#Import the required Libraries
from tkinter import *


price_20_minutes = 4
price_40_minutes = 7
price_60_minutes = 8
window = Tk()
class My_Ticket:
   ticket_counter = IntVar()
   def __init__(self,bilet_name,my_row,my_col):
      self.name=bilet_name
      self.row=my_row
      self.col=my_col
      Button(window,text=bilet_name).grid(row=my_row,column=my_col,sticky="NSEW",padx=5,pady=20)
      counter_disp = Label(window, padx=15, pady=5, textvariable=self.ticket_counter).grid(row=0, column=2)
      ticket_add=Button(window,
      text="+",
      command=lambda: onClick_addfun(),
      ).grid(row=0, column=1, sticky="NSEW", padx=5, pady=50)


   def onClick_addfun(event=None):
      ticket_counter.set(counter.get() + 1)



def Bilety_Ulgowe():
   for widget in window.winfo_children():
      widget.destroy()

   counter_20min = Label(window, padx=15, pady=5 ,textvariable=counter).grid(row=0,column=2)
   counter_40min = Label(window, padx=15, pady=5, textvariable=counter).grid(row=1, column=2)
   counter_60min = Label(window, padx=15, pady=5, textvariable=counter).grid(row=2, column=2)

   button_Bilet_ulgowy_20 = Button(window,
      text="Bilet 20 minutowy\n"+'{:.2f}'.format(price_20_minutes/2)+"zł",
      ).grid(row=0, column=0, sticky="NSEW", padx=5, pady=20)
   button_Bilet_ulgowy_20_add = Button(window,
      text="+",
      command=onClick_add,
      ).grid(row=0, column=1, sticky="NSEW", padx=5, pady=50)
   button_Bilet_ulgowy_20_substract = Button(window,
      text="-",
      command=onClick_substract,
      ).grid(row=0, column=3, sticky="NSEW",padx=5, pady=50)
   button_Bilet_ulgowy_40 = Button(window,
      text="Bilet 40 minutowy\n"+'{:.2f}'.format(price_40_minutes/2)+"zł",
      #command=write_text,
      ).grid(row=1, column=0, sticky="NSEW", padx=5, pady=5)
   button_Bilet_ulgowy_60 = Button(window,
      text="Bilet 60 minutowy\n"+'{:.2f}'.format(price_60_minutes/2)+"zł",
      # command=write_text,
      ).grid(row=2, column=0, sticky="NSEW", padx=5, pady=5)

def Bilety_Normalne():
   for widget in window.winfo_children():
      widget.destroy()
   #ticket_counter = IntVar()
   Bilet1= My_Ticket("Bilet 20 minutowy\n"+'{:.2f}'.format(price_20_minutes)+"zł",0,0,)







#Set the geometry of the Tkinter frame
window.geometry("250x250")
counter = IntVar()

def onClick_add(event=None):
    counter.set(counter.get() + 1)

def onClick_substract(event=None):
   if counter.get()==0:
      return
   counter.set(counter.get() - 1)

Grid.rowconfigure(window,0,weight=1)
Grid.rowconfigure(window,1,weight=1)
Grid.rowconfigure(window,2,weight=1)
Grid.columnconfigure(window,0,weight=1)
Grid.columnconfigure(window,1,weight=1)
Grid.columnconfigure(window,2,weight=1)
Grid.columnconfigure(window,3,weight=1),
#button_list = [button_bilet_normalny]
button_bilet_normalny= Button(window,
      text="Bilet Normalny",
      command=Bilety_Normalne,
      ).grid(row=0,column=0, sticky = "NSEW",padx=5,pady=50)
button_bilet_ulgowy= Button(window,
      text="Bilet Ulgowy",
      command=Bilety_Ulgowe
      ).grid(row=0,column=1, sticky = "NSEW",padx=5,pady=50)

window.mainloop()