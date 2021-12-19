# Import the required Libraries
from tkinter import *
import time

price_20_minutes = 4
price_40_minutes = 7
price_60_minutes = 8
window = Tk()


class my_ticket:
    Ticket_label = Label
    counter_disp = Label
    ticket_add = Button
    ticket_substract = Button
    ticket_counter = IntVar()

    def __init__(self, bilet_name, my_row, my_col):
        self.ticket_counter = IntVar()
        self.name = bilet_name
        self.row = my_row
        self.col = my_col
        self.Ticket_label = Label(window,
                                  text=self.name,
                                  borderwidth=5,
                                  relief="raised",
                                  bg="Gray"
                                  )
        self.counter_disp = Label(window, padx=2, pady=2, textvariable=self.ticket_counter)
        self.ticket_add = Button(window,
                            text="+",
                            command=self.onClick_addfun,
                            borderwidth=5,
                            relief="raised",
                            bg="Gray"

                            )
        self.ticket_substract = Button(window,
                                  text="-",
                                  command=self.onClick_substract,
                                  )
        print("Utworzono")

    def onClick_addfun(self, event=None):
        self.ticket_counter.set(self.ticket_counter.get() + 1)

    def onClick_substract(self, event=None):
        if self.ticket_counter.get() == 0:
            return
        self.ticket_counter.set(self.ticket_counter.get() - 1)

    def aktywuj(self):
        self.Ticket_label.grid(row=self.row, column=self.col, sticky="NSEW", padx=2, pady=20)
        self.counter_disp.grid(row=self.row, column=2)
        self.ticket_add.grid(row=self.row, column=1, sticky="NSEW", padx=2, pady=50)
        self.ticket_substract.grid(row=self.row, column=3, sticky="NSEW", padx=2, pady=50)

    def forget(self):
        # self.Ticket_button.grid_forget()
        self.counter_disp.grid_forget()

    def grid_hide(widget):
        widget._grid_info = widget.grid_info()
        widget.grid_remove()

    def grid_show(widget):
        widget.grid(**widget._grid_info)


def Bilety_Ulgowe(lista):
    a, b, c, d, e, f = lista
    widget_forget()
    window.geometry("500x500")
    a.aktywuj()
    b.aktywuj()
    c.aktywuj()
    tmp = [d, e, f, a, b, c]
    normalne = Button(window,
                        text="Bilety Normalne",
                        # command=print(Bilet20min_ulg.ticket_counter.get())
                        #  command= Bilety_Ulgowe
                        command=lambda: Bilety_Normalne(tmp)
                        ).grid(row=3, column=0, sticky="NSEW", padx=2, pady=20)
    platnosc = Button(window,
                        text="Platnosc",
                        command=lambda: Summary(lista,True)
                        ).grid(row=3, column=1, sticky="NSEW",columnspan=3, padx=2, pady=20)

def Bilety_Normalne(lista):
    a, b, c, d, e, f = lista
    widget_forget()
    #  clear_widgets()
    window.geometry("500x500")
    a.aktywuj()
    b.aktywuj()
    c.aktywuj()
    tmp = [d, e, f, a, b, c]
    ulgowe = Button(window,
                        text="Bilety Ulgowe",
                        # command=print(Bilet20min_ulg.ticket_counter.get())
                        #  command= Bilety_Ulgowe
                        command=lambda: Bilety_Ulgowe(tmp)
                        ).grid(row=3, column=0, sticky="NSEW", padx=2, pady=20)
    Platnosc = Button(window,
                        text="Platnosc",
                        command=lambda: Summary(lista,False)
                        ).grid(row=3, column=1, sticky="NSEW",columnspan=3, padx=2, pady=20)

def widget_forget():
    for i in window.grid_slaves():
        i.grid_forget()
        # i.grid()
   # if flaga == True:
  #      Bilety_Normalne()
 #   else:
  #      Bilety_Ulgowe()


def clear_widgets():
    for widget in window.winfo_children():
        widget.destroy()

def Summary(lista,flaga):
    widget_forget()
    sum = DoubleVar()
    a, b, c, d, e, f = lista
    if(flaga==True):
        a=a.ticket_counter.get()*price_20_minutes/2
        b=b.ticket_counter.get()*price_40_minutes/2
        c=c.ticket_counter.get()*price_60_minutes/2
        d=d.ticket_counter.get()*price_20_minutes
        e=e.ticket_counter.get()*price_40_minutes
        f=f.ticket_counter.get()*price_60_minutes
        tmp=[a,b,c,d,e,f]
    elif(flaga==False)    :
        a=a.ticket_counter.get()*price_20_minutes
        b=b.ticket_counter.get()*price_40_minutes
        c=c.ticket_counter.get()*price_60_minutes
        d=d.ticket_counter.get()*price_20_minutes/2
        e=e.ticket_counter.get()*price_40_minutes/2
        f=f.ticket_counter.get()*price_60_minutes/2
        tmp=[a, b, c, d, e, f]
    for i in tmp:
        sum.set(sum.get()+i)
    suma_button= Label(window, padx=2, pady=2, textvariable=sum)
    suma_button.grid(row=0, column=0, sticky="NSEW",columnspan=3, padx=2, pady=20)

    print(sum)

def Start():
    Bilet20min = my_ticket("Bilet 20 minutowy\n" + '{:.2f}'.format(price_20_minutes) + "zł", 0, 0, )
    Bilet40min = my_ticket("Bilet 40 minutowy\n" + '{:.2f}'.format(price_40_minutes) + "zł", 1, 0, )
    Bilet60min = my_ticket("Bilet 60 minutowy\n" + '{:.2f}'.format(price_60_minutes) + "zł", 2, 0, )
    Bilet20min_ulg = my_ticket("Bilet 20 minutowy\n" + '{:.2f}'.format(price_20_minutes / 2) + "zł", 0, 0, )
    Bilet40min_ulg = my_ticket("Bilet 40 minutowy\n" + '{:.2f}'.format(price_40_minutes / 2) + "zł", 1, 0, )
    Bilet60min_ulg = my_ticket("Bilet 60 minutowy\n" + '{:.2f}'.format(price_60_minutes / 2) + "zł", 2, 0, )
    listanormalne=[Bilet20min,Bilet40min,Bilet60min,Bilet20min_ulg,Bilet40min_ulg,Bilet60min_ulg]
    listaulgowe=[Bilet20min_ulg,Bilet40min_ulg,Bilet60min_ulg,Bilet20min,Bilet40min,Bilet60min]

    button_bilet_normalny = Button(window,
                                   text="Bilet Normalny",
                                   command =lambda:Bilety_Normalne(listanormalne),
                                   ).grid(row=0, column=0, sticky="NSEW", padx=20, pady=50)
    button_bilet_ulgowy = Button(window,
                                 text="Bilet Ulgowy",
                                 command=lambda:Bilety_Ulgowe(listaulgowe)
                                 ).grid(row=0, column=1, sticky="NSEW", padx=20, pady=50)


# Set the geometry of the Tkinter frame
window.geometry("250x150")
window.configure(background="#856ff8")

Grid.rowconfigure(window, 0, weight=1)
Grid.rowconfigure(window, 1, weight=1)
Grid.rowconfigure(window, 2, weight=1)
Grid.rowconfigure(window, 3, weight=1)
Grid.columnconfigure(window, 0, weight=1)
Grid.columnconfigure(window, 1, weight=1)
Grid.columnconfigure(window, 2, weight=1)
Grid.columnconfigure(window, 3, weight=1),
# button_list = [button_bilet_normalny]
Start()

window.mainloop()
