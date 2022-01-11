# Import the required Libraries
from tkinter import *
import time
import os
import sys
from decimal import *
import copy
import random
window = Tk()
myfont = ("Rubik", 15)
class ZlyNominalExcepion(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class NieznanaWalutaException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class Coin_Bill:
    __currency = 'PLN'
    __value = 0

    def __init__(self, val):
        if val in allowed_coins_bills:
            self.__value = Decimal(val)
        else:
            raise ZlyNominalExcepion('Brak takiego nominalu')

    def get_value(self):
        return self.__value

    def get_waluta(self):
        return self.__currency


class Money_Storage:
    __Money_list = []

    def __init__(self, currency, l):
        self.__curr = currency
        self.__Money_list = l

    def add_Coin_or_Bill(self, Coin_or_Bill):
        if isinstance(Coin_or_Bill, Coin_Bill):
            if Coin_or_Bill.get_waluta() in self.__curr:
                self.__Money_list.append(Coin_or_Bill)
            else:
                raise NieznanaWalutaException()
        else:
            print('Przeslany obiekt nie jest monetą')

    def Sum(self):
        sum_ = 0
        for x in self.__Money_list:
            sum_ = sum_ + x.get_value()
        return Decimal(sum_)

    def return_Nominal(self, val):
        for x in self.__Money_list:
            if x.get_value() == Decimal(val):
                self.__Money_list.remove(x)
                return x

    def return_list(self):
        return self.__Money_list

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
                                  font=("Rubik", 20),
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

    def activate(self):
        self.Ticket_label.grid(row=self.row, column=self.col, sticky="NSEW", padx=2, pady=20)
        self.counter_disp.grid(row=self.row, column=2)
        self.ticket_add.grid(row=self.row, column=3, sticky="NSEW", padx=2, pady=50)
        self.ticket_substract.grid(row=self.row, column=1, sticky="NSEW", padx=2, pady=50)

price_20_minutes = 4
price_40_minutes = 7
price_60_minutes = 8        
getcontext().prec = 4
allowed_coins_bills = [0.01, 0.02, 0.05, 0.10, 0.20, 0.50, 1, 2, 5, 10, 20, 50]
def config():
        Grid.rowconfigure(window, 0, weight=1)
        Grid.rowconfigure(window, 1, weight=1)
        Grid.rowconfigure(window, 2, weight=1)
        Grid.rowconfigure(window, 3, weight=1)
        Grid.rowconfigure(window, 4, weight=1)
        Grid.rowconfigure(window, 5, weight=1)
        Grid.rowconfigure(window, 6, weight=1)
        Grid.rowconfigure(window, 7, weight=1)
        Grid.rowconfigure(window, 8, weight=1)
        Grid.rowconfigure(window, 9, weight=1)
        Grid.rowconfigure(window, 10, weight=1)
        Grid.rowconfigure(window, 11, weight=1)
        Grid.rowconfigure(window, 12, weight=1)

        Grid.columnconfigure(window, 0, weight=1)
        Grid.columnconfigure(window, 1, weight=1)
        Grid.columnconfigure(window, 2, weight=1)
        Grid.columnconfigure(window, 3, weight=1),
        Grid.columnconfigure(window, 4, weight=1),
        Grid.columnconfigure(window, 5, weight=1),
        Grid.columnconfigure(window, 6, weight=1),

        Bilet20min = my_ticket("Bilet 20 minutowy\n" + '{:.2f}'.format(price_20_minutes) + "zł", 0, 0, )
        Bilet40min = my_ticket("Bilet 40 minutowy\n" + '{:.2f}'.format(price_40_minutes) + "zł", 1, 0, )
        Bilet60min = my_ticket("Bilet 60 minutowy\n" + '{:.2f}'.format(price_60_minutes) + "zł", 2, 0, )
        Bilet20min_ulg = my_ticket("Bilet 20 minutowy\n" + '{:.2f}'.format(price_20_minutes / 2) + "zł", 0, 0, )
        Bilet40min_ulg = my_ticket("Bilet 40 minutowy\n" + '{:.2f}'.format(price_40_minutes / 2) + "zł", 1, 0, )
        Bilet60min_ulg = my_ticket("Bilet 60 minutowy\n" + '{:.2f}'.format(price_60_minutes / 2) + "zł", 2, 0, )
        # listanormalne = [Bilet20min, Bilet40min, Bilet60min, Bilet20min_ulg, Bilet40min_ulg, Bilet60min_ulg]
        return [Bilet20min, Bilet40min, Bilet60min, Bilet20min_ulg, Bilet40min_ulg, Bilet60min_ulg], [Bilet20min_ulg,
                                                                                                      Bilet40min_ulg,
                                                                                                      Bilet60min_ulg,
                                                                                                  Bilet20min,
                                                                                                  Bilet40min,
                                                                                                  Bilet60min]
def widget_forget():  # function to hide widgets
    for i in window.grid_slaves():
     i.grid_forget()
def clear_widgets():  # function to destroy widgets
    for widget in window.winfo_children():
        widget.destroy()                      
def wyswietlulgowe(list,tmp_list_tickets):
    normalne = Button(window,
                      text="Bilety Normalne",
                      command=lambda: Bilety_Normalne(tmp_list_tickets),
                      bg="#231697",
                      borderwidth=5,
                      relief="raised",
                      font=myfont,
                      fg="white",
                      activebackground='#3974BB',
                      ).grid(row=3, column=0, sticky="NSEW", padx=2, pady=20)
    platnosc = Button(window,
                      text="Platnosc",
                      command=lambda: Summary(list, True),
                      bg="#231697",
                      borderwidth=5,
                      relief="raised",
                      font=myfont,
                      fg="white",
                      activebackground='#3974BB',
                      ).grid(row=3, column=1, sticky="NSEW", columnspan=3, padx=2, pady=20)
def Bilety_Ulgowe(list):
    a, b, c, d, e, f = list  # Unpack list of tickets
    widget_forget()  # forget previous buttons
    a.activate()  # display tickets
    b.activate()
    c.activate()
    tmp_list_tickets = [d, e, f, a, b,
                        c]  # tmp list of tickets, which allows to send them to another function to proper count sum price
    wyswietlulgowe(list,tmp_list_tickets)
def wyswietnormalne(list,tmp_list_tickets):
    ulgowe = Button(window,
                    text="Bilety Ulgowe",
                    command=lambda: Bilety_Ulgowe(tmp_list_tickets),
                    bg="#231697",
                    borderwidth=5,
                    relief="raised",
                    font=myfont,
                    fg="white",
                    activebackground='#3974BB',
                    ).grid(row=3, column=0, sticky="NSEW", padx=2, pady=20)
    Platnosc = Button(window,
                      text="Platnosc",
                      command=lambda: Summary(list, False),
                      bg="#231697",
                      borderwidth=5,
                      relief="raised",
                      font=myfont,
                      fg="white",
                      activebackground='#3974BB',
                      ).grid(row=3, column=1, sticky="NSEW", columnspan=3, padx=2, pady=20)
def Bilety_Normalne(list):
    a, b, c, d, e, f = list  # Unpack list of tickets
    widget_forget()  # forget previous buttons
    a.activate()
    b.activate()
    c.activate()
    tmp_list_tickets = [d, e, f, a, b,
                        c]  # tmp_list_tickets list of tickets, which allows to send them to another function to proper count sum price
    wyswietnormalne(list,tmp_list_tickets)
def Restart():
    l=[]
    temp = WrzuconeMonety.return_list()
    for k in temp:
        l.append(k.get_value())
    for i in l:
        WrzuconeMonety.return_Nominal(i)
    #clear_w()
    #WrzuconeMonety = Money_Storage('PLN', [])
    listanormalne, listaulgowe = config()
    Start(listanormalne, listaulgowe)

def Start(listanormalne, listaulgowe):
    widget_forget()
    choose_ticket_label = Label(window,
                                text="Wybierz rodzaj biletu:",
                                borderwidth=5,
                                relief="raised",
                                bg="#140787",
                                font=myfont,
                                fg="white",
                                activebackground='#3974BB',
                                ).grid(row=0, column=1, sticky="NSEW", columnspan=2, padx=20, pady=35)

    button_normal_ticket = Button(window,
                                  text="Bilet Normalny",
                                  command=lambda: Bilety_Normalne(listanormalne),
                                  borderwidth=5,
                                  relief="raised",
                                  bg="#231697",
                                  font=myfont,
                                  fg="white",
                                  activebackground='#3974BB',
                                  ).grid(row=1, column=1, sticky="NSEW", padx=20, pady=35)
    button_halfprice_ticket = Button(window,
                                     text="Bilet Ulgowy",
                                     command=lambda: Bilety_Ulgowe(listaulgowe),
                                     borderwidth=5,
                                     relief="raised",
                                     bg="#231697",
                                     font=myfont,
                                     fg="white",
                                     activebackground='#3974BB',
                                     ).grid(row=1, column=2, sticky="NSEW", padx=20, pady=35)
def returnChange(Biletomat, reszta):
    l = []
    l2 = []
    listamonet = Biletomat.return_list()
    print("1:")
    print(Biletomat.Sum())
    for i in listamonet:
        l.append(i.get_value())
    l.sort(reverse=True)

    for i in l:
        reszta = round(reszta, 2)
        k = round(i, 2)
        # print(i.compare(reszta))
        if k <= reszta:
            print("printuje i")
            print(float(i))
            reszta -= float(i)
            l2.append(i)
    if reszta == 0:
        print("Wydano reszte")
        for i in l2:
            o =[]
            o.append(Biletomat.return_Nominal(i).get_value())
            print(Biletomat.return_Nominal(i).get_value())
        return True, o
    else:
        print("reszty nie wydano")
        return False


def Refresh_sum(value,coins_counter,sum_string,change):  # function to refresh sum after throw a coin into machine
    coins_thrown_in_counter = coins_counter.get()
    coins_counter.set(1)
    for i in range(coins_thrown_in_counter):
        WrzuconeMonety.add_Coin_or_Bill(Coin_Bill(value))
    sum_float = float(sum_string.get().split(" ")[0]) - coins_thrown_in_counter * value

    sum_string.set('{:.2f}'.format(sum_float) + " zl")
    if (sum_float) <= 0:
        display_coins(sum_string,change,"disabled")  # if sum <0 then no more coins are allowed to be thrown in
        sum_string.set("0.00 zl")
        sum_float = sum_float * -1
        change.set('{:.2f}'.format(sum_float) + " zl")
        change_to_be_returned_bool, o = returnChange(Biletomat, sum_float)
        print(o)
        #global change_info
    #    change_info.set("2222")
        if change_to_be_returned_bool == False:
            print("Tylko odliczona kwota")
            for k in WrzuconeMonety.return_list():
                WrzuconeMonety.return_Nominal(k.get_value())

def display_coins(sum_string,change,is_active="normal"):

    coins_counter = IntVar()
    coins_counter.set(1)
    change_info = StringVar()
    change_info.set("l22ala")
    def onClick_addfun():
        coins_counter.set(coins_counter.get() + 1)
    def onClick_substract():
        if coins_counter.get() == 1:
            return
        coins_counter.set(coins_counter.get() - 1)
    i = 0
    for c in allowed_coins_bills:  # Display coins/bills buttons
        if (i < 6):
            colnum = 3
            rownum = i + 1
        else:
            colnum = 5
            rownum = i - 5
        Button(window,
               text="Wrzuć " + str(c) + " zł",
               command=lambda c=c: Refresh_sum(float(c),coins_counter,sum_string,change),
               bg="#231697",
               borderwidth=5,
               relief="raised",
               font=myfont,
               fg="white",
               state=is_active
               ).grid(row=rownum, column=colnum, sticky="NSEW", padx=2, pady=20)
        i += 1


    Label(window,
          text="Wybierz ilosc Monet lub bankontow:",
          bg="#231697",
          borderwidth=5,
          relief="raised",
          font=myfont,
          fg="white",
          ).grid(row=0, column=1, sticky="NSEW", padx=2, pady=20, columnspan=2)
    counter_money = Label(window,
                          textvariable=coins_counter,
                          relief="raised",
                          bg="#231697",
                          font=myfont,
                          fg="white"
                          ).grid(row=0, column=4, sticky="NSEW", padx=2, pady=20)
    counter_money_add = Button(window,
                               text="+",
                               command=lambda: onClick_addfun(),
                               borderwidth=5,
                               relief="raised",
                               bg="#231697",
                               font=myfont,
                               fg="white",
                               activebackground='#3974BB',
                               ).grid(row=0, column=5, sticky="NSEW", padx=2, pady=20)
    counter_money_substract = Button(window,
                                     text="-",
                                     bg="#231697",
                                     borderwidth=5,
                                     relief="raised",
                                     font=myfont,
                                     fg="white",
                                     activebackground='#3974BB',
                                     command=lambda: onClick_substract(),
                                     ).grid(row=0, column=3, sticky="NSEW", padx=2, pady=20)
    change_info = Label(window,
                        textvariable=change_info,
                        relief="raised",
                        bg="#231697",
                        font=myfont,
                        fg="white",
                        borderwidth=5,
                        ).grid(row=5, column=1, sticky="NSEW", padx=2, pady=20, columnspan=2, rowspan=2)

def Summary_display(sum_string,change):
    sum_display_text = Label(window,
                             text="Pozostalo do zaplaty:",
                             bg="#231697",
                             borderwidth=5,
                             relief="raised",
                             font=myfont,
                             fg="white",
                             )
    sum_display_text.grid(row=1, column=1, sticky="NSEW", columnspan=2, padx=2, pady=20)
    sum_display = Label(window,
                        textvariable=sum_string,
                        bg="#231697",
                        borderwidth=5,
                        relief="raised",
                        font=myfont,
                        fg="white",
                        )
    sum_display.grid(row=2, column=1, sticky="NSEW", columnspan=2, padx=2, pady=20)
    change_display_text = Label(window,
                                text="Reszta:",
                                bg="#231697",
                                borderwidth=5,
                                relief="raised",
                                font=myfont,
                                fg="white",
                                )
    change_display_text.grid(row=3, column=1, sticky="NSEW", columnspan=2, padx=2, pady=20)
    change_display = Label(window,
                           textvariable=change,
                           bg="#231697",
                           borderwidth=5,
                           relief="raised",
                           font=myfont,
                           fg="white",
                           )
    change_display.grid(row=4, column=1, sticky="NSEW", columnspan=2, padx=2, pady=20)
    add_ticket = Button(window,
                        text="Dodaj Bilet",
                        command=lambda: Start(listanormalne, listaulgowe),
                        bg="#231697",
                        borderwidth=5,
                        relief="raised",
                        font=myfont,
                        fg="white",
                        )
    add_ticket.grid(row=0, column=0, sticky="NSEW", padx=2, pady=20)
    add_ticket = Button(window,
                        text="Zacznij od nowa",
                        command=lambda: Restart(),
                        bg="#231697",
                        borderwidth=5,
                        relief="raised",
                        font=myfont,
                        fg="white",
                        )
    add_ticket.grid(row=1, column=0, sticky="NSEW", padx=2, pady=20)

def Summary(lista, flaga):
    change_info = StringVar()
    change_info.set("0.00 zl")
    coins_counter = IntVar()
    coins_counter.set(1)
    widget_forget()
    a, b, c, d, e, f = lista
    sum = DoubleVar()
    sum_string = StringVar()
    change = StringVar()
    change.set("0.00 zl")
    

    if (flaga == True):
        a = a.ticket_counter.get() * price_20_minutes / 2
        b = b.ticket_counter.get() * price_40_minutes / 2
        c = c.ticket_counter.get() * price_60_minutes / 2
        d = d.ticket_counter.get() * price_20_minutes
        e = e.ticket_counter.get() * price_40_minutes
        f = f.ticket_counter.get() * price_60_minutes
        tmp_list = [a, b, c, d, e, f]  # temporary list to store tickets and their prices
    elif (flaga == False):
        a = a.ticket_counter.get() * price_20_minutes
        b = b.ticket_counter.get() * price_40_minutes
        c = c.ticket_counter.get() * price_60_minutes
        d = d.ticket_counter.get() * price_20_minutes / 2
        e = e.ticket_counter.get() * price_40_minutes / 2
        f = f.ticket_counter.get() * price_60_minutes / 2
        tmp_list = [a, b, c, d, e, f]  # temporary list to store tickets and their prices
    tmp_sum = WrzuconeMonety.Sum()
    tmp = 0
    for i in tmp_list:
        tmp = tmp + i

    tmp = tmp - float(tmp_sum)  # sum calculation
    tmp2 = '{:.2f}'.format(tmp) + " zl"
    sum_string.set(tmp2)
    display_coins(sum_string,change)
    Summary_display(sum_string,change)

tmp_list2 = []
tmp_list1 = []
random_generated_list_of_coins_bills = [random.choice(allowed_coins_bills) for x in
                                    range(100)]  # Randomowa lista nominalow znajdujacych sie w biletomacie
Biletomat = Money_Storage('PLN', tmp_list1)
for i in random_generated_list_of_coins_bills:
   Biletomat.add_Coin_or_Bill(Coin_Bill(i))
print(Biletomat.Sum())

WrzuconeMonety = Money_Storage('PLN', tmp_list2)

listanormalne, listaulgowe = config()
def main():





    window.geometry("850x650")
    window.configure(background="#231697")
    # window.resizable(False,False)
    # window.iconbitmap("C:\\Users\\RXKW46\\Documents\\JS\\ikona.ico")
    # window.iconbitmap("ikona.ico")
    window.title("Biletomat MPK")
    Start(listanormalne, listaulgowe)



    
    window.mainloop()


main()