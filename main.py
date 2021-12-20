# Import the required Libraries
from tkinter import *
import time
import os
cwd = os.getcwd()
coins = {
    "0,10 zl" : 0.10,
    "0,20 zl" : 0.20,
    "0,50 zl" : 0.50,
    "1,00 zl" : 1,
    "2,00 zl" : 2,
    "5,00 zl" : 5

}
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
                                bg="#231697",
                                font=myfont,
                                fg="white",
                                  )
        self.counter_disp = Label(window,
                            padx=2, 
                            pady=2, 
                            textvariable=self.ticket_counter,
                            relief="raised",
                            bg="#231697",
                            font=("Rubik",20),
                            fg="white"
                            )
        self.ticket_add = Button(window,
                            text="+",
                            command=self.onClick_addfun,
                            borderwidth=5,
                            relief="raised",
                            bg="#231697",
                            font=myfont,
                            fg="white",
                            activebackground='#3974BB',

                            )
        self.ticket_substract = Button(window,
                            text="-",
                            bg="#231697",
                            borderwidth=5,
                            relief="raised",
                            font=myfont,
                            fg="white",
                            activebackground='#3974BB',
                            command=self.onClick_substract,
                                  )

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
    #window.geometry("500x500")
    a.aktywuj()
    b.aktywuj()
    c.aktywuj()
    tmp = [d, e, f, a, b, c]
    normalne = Button(window,
                        text="Bilety Normalne",
                        command=lambda: Bilety_Normalne(tmp),
                        bg="#231697",
                        borderwidth=5,
                        relief="raised",
                        font=myfont,
                        fg="white",
                        activebackground='#3974BB',
                        ).grid(row=3, column=0, sticky="NSEW", padx=2, pady=20)
    platnosc = Button(window,
                        text="Platnosc",
                        command=lambda: Summary(lista,True),
                        bg="#231697",
                        borderwidth=5,
                        relief="raised",
                        font=myfont,
                        fg="white",
                        activebackground='#3974BB',
                        ).grid(row=3, column=1, sticky="NSEW",columnspan=3, padx=2, pady=20)

def Bilety_Normalne(lista):
    a, b, c, d, e, f = lista
    widget_forget()
    #  clear_widgets()
   # window.geometry("500x500")
    a.aktywuj()
    b.aktywuj()
    c.aktywuj()
    tmp = [d, e, f, a, b, c]
    ulgowe = Button(window,
                        text="Bilety Ulgowe",
                        command=lambda: Bilety_Ulgowe(tmp),
                        bg="#231697",
                        borderwidth=5,
                        relief="raised",
                        font=myfont,
                        fg="white",
                        activebackground='#3974BB',
                        ).grid(row=3, column=0, sticky="NSEW", padx=2, pady=20)
    Platnosc = Button(window,
                        text="Platnosc",
                        command=lambda: Summary(lista,False),
                        bg="#231697",
                        borderwidth=5,
                        relief="raised",
                        font=myfont,
                        fg="white",
                        activebackground='#3974BB',
                        ).grid(row=3, column=1, sticky="NSEW",columnspan=3, padx=2, pady=20)

def widget_forget():
    for i in window.grid_slaves():
        i.grid_forget()

def clear_widgets():
    for widget in window.winfo_children():
        widget.destroy()

def Summary(lista,flaga):
    
    def display_coins():
     for i,(key,value) in enumerate(coins.items()):
        print(value)
        Button(window,
                text=key,
                command = lambda:Refresh_sum(value),
                bg="#231697",
                borderwidth=5,
                relief="raised",
                font=myfont,
                fg="white",
        ).grid(row=i,column=3,sticky="NSEW",padx=2,pady=20)
        print(value)
    widget_forget()
    sum = DoubleVar()
    test = StringVar()
    t=0
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
        t=t+i
        t2='{:.2f}'.format(t) + " zl"
        #t2.fromat()
        #'{:.2f}'.format(price_60_minutes)
        test.set(t2)
        sum.set(sum.get()+i)
    def Refresh_sum(value):
        #current_sum = test.get()
        sum_float=float(test.get().split(" ")[0]) - value
        #sum_float = sum_float - value
       # current_sum='{:.2f}'.format(sum_float) + " zl"
        test.set('{:.2f}'.format(sum_float) + " zl")

    suma_display_text= Label(window,
                    text="Pozostalo do zaplaty:",
                    bg="#231697",
                    borderwidth=5,
                    relief="raised",
                    font=myfont,
                    fg="white",
                    )
    suma_display_text.grid(row=1, column=1, sticky="NSEW",columnspan=2, padx=2, pady=20)
    suma_display= Label(window,
                    textvariable=test,
                    bg="#231697",
                    borderwidth=5,
                    relief="raised",
                    font=myfont,
                    fg="white",
                    )
    suma_display.grid(row=2, column=1, sticky="NSEW",columnspan=2, padx=2, pady=20)
   # button_2_zlote= Button(window,
    #                text="2.00 zl",
    #                bg="#231697",
    #                borderwidth=5,
     #               relief="raised",
     #               font=myfont,
     #               fg="white",
     #               command =lambda: Refresh_sum(2)
     #               )
    #button_2_zlote.grid(row=0, column=3, sticky="NSEW",columnspan=2, padx=2, pady=20)
    display_coins()
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
    wybor_biletu_label = Label(window,
                                    text= "Wybierz rodzaj biletu:",
                                    borderwidth=5,
                                    relief="raised",
                                    bg="#140787",
                                    font=myfont,
                                    fg="white",
                                    activebackground='#3974BB',
                                    ).grid(row=0,column=1,sticky = "NSEW", columnspan=2,padx=20,pady=35)   

    button_bilet_normalny = Button(window,
                                    text="Bilet Normalny",
                                    command =lambda:Bilety_Normalne(listanormalne),
                                    borderwidth=5,
                                    relief="raised",
                                    bg="#231697",
                                    font=myfont,
                                    fg="white",
                                    activebackground='#3974BB',
                                   ).grid(row=1, column=1, sticky="NSEW", padx=20, pady=35)
    button_bilet_ulgowy = Button(window,
                                    text="Bilet Ulgowy",
                                    command=lambda:Bilety_Ulgowe(listaulgowe),
                                    borderwidth=5,
                                    relief="raised",
                                    bg="#231697",
                                    font=myfont,
                                    fg="white",
                                    activebackground='#3974BB',
                                 ).grid(row=1, column=2, sticky="NSEW", padx=20, pady=35)


# Set the geometry of the Tkinter frame
window.geometry("850x650")
window.configure(background="#231697")
#window.resizable(False,False)
window.iconbitmap("C:\\Users\\RXKW46\\Documents\\JS\\ikona.ico")
#window.iconbitmap("ikona.ico")
print("tst")
print(cwd)
window.title("Biletomat MPK")
myfont=("Rubik",15)
filename = PhotoImage(file = "C:\\Users\\RXKW46\\Documents\\JS\\tlo2.png")
#filename = PhotoImage(file = ".\\Documents\JS\\tlo.png")
background_label = Label(window, image=filename)
background_label.place(x=1, y=1, relwidth=1, relheight=1)

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