# Import the required Libraries
from tkinter import *
import time
import os
import sys
from decimal import *
import copy
import random
import interface
sum_test_purposes = 0

#interface.window = Tk()
#myfont = ("Rubik", 15)
#filename = PhotoImage(file="C:\\Users\\RXKW46\\Documents\\JS\\tlo2.png")
#interface.window.iconbitmap("C:\\Users\\RXKW46\\Documents\\JS\\ikona.ico")
# background_label = Label(top, image=filename)
#label1 = Label(interface.window, image=filename)
#label1.place(x=0, y=0)
price_20_minutes = 4
price_40_minutes = 7
price_60_minutes = 8
getcontext().prec = 4
allowed_coins_bills = [0.01, 0.02, 0.05, 0.10, 0.20, 0.50, 1, 2, 5, 10, 20, 50]

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
        self.Ticket_label = Label(interface.window,
                                  text=self.name,
                                  borderwidth=5,
                                  relief="raised",
                                  bg="#231697",
                                  font=interface.myfont,
                                  fg="white",
                                  )
        self.counter_disp = Label(interface.window,
                                  padx=2,
                                  pady=2,
                                  textvariable=self.ticket_counter,
                                  relief="raised",
                                  bg="#231697",
                                  font=("Rubik", 20),
                                  fg="white"
                                  )
        self.ticket_add = Button(interface.window,
                                 text="+",
                                 command=self.onClick_addfun,
                                 borderwidth=5,
                                 relief="raised",
                                 bg="#231697",
                                 font=interface.myfont,
                                 fg="white",
                                 activebackground='#3974BB',

                                 )
        self.ticket_substract = Button(interface.window,
                                       text="-",
                                       bg="#231697",
                                       borderwidth=5,
                                       relief="raised",
                                       font=interface.myfont,
                                       fg="white",
                                       activebackground='#3974BB',
                                       command=self.onClick_substract,
                                       )
    def get_name(self):
        return self.name

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




def config():
    Grid.rowconfigure(interface.window, 0, weight=1)
    Grid.rowconfigure(interface.window, 1, weight=1)
    Grid.rowconfigure(interface.window, 2, weight=1)
    Grid.rowconfigure(interface.window, 3, weight=1)
    Grid.rowconfigure(interface.window, 4, weight=1)
    Grid.rowconfigure(interface.window, 5, weight=1)
    Grid.rowconfigure(interface.window, 6, weight=1)
    Grid.rowconfigure(interface.window, 7, weight=1)
    Grid.rowconfigure(interface.window, 8, weight=1)
    Grid.rowconfigure(interface.window, 9, weight=1)
    Grid.rowconfigure(interface.window, 10, weight=1)
    Grid.rowconfigure(interface.window, 11, weight=1)
    Grid.rowconfigure(interface.window, 12, weight=1)

    Grid.columnconfigure(interface.window, 0, weight=1)
    Grid.columnconfigure(interface.window, 1, weight=1)
    Grid.columnconfigure(interface.window, 2, weight=1)
    Grid.columnconfigure(interface.window, 3, weight=1),
    Grid.columnconfigure(interface.window, 4, weight=1),
    Grid.columnconfigure(interface.window, 5, weight=1),
    Grid.columnconfigure(interface.window, 6, weight=1),

    Bilet20min = my_ticket("Bilet 20 minutowy\n" + '{:.2f}'.format(price_20_minutes) + "zł", 0, 0, )
    Bilet40min = my_ticket("Bilet 40 minutowy\n" + '{:.2f}'.format(price_40_minutes) + "zł", 1, 0, )
    Bilet60min = my_ticket("Bilet 60 minutowy\n" + '{:.2f}'.format(price_60_minutes) + "zł", 2, 0, )
    Bilet20min_ulg = my_ticket("Bilet 20 minutowy\n" + '{:.2f}'.format(price_20_minutes / 2) + "zł", 0, 0, )
    Bilet40min_ulg = my_ticket("Bilet 40 minutowy\n" + '{:.2f}'.format(price_40_minutes / 2) + "zł", 1, 0, )
    Bilet60min_ulg = my_ticket("Bilet 60 minutowy\n" + '{:.2f}'.format(price_60_minutes / 2) + "zł", 2, 0, )
    return [Bilet20min, Bilet40min, Bilet60min, Bilet20min_ulg, Bilet40min_ulg, Bilet60min_ulg], [Bilet20min_ulg,
                                                                                                  Bilet40min_ulg,
                                                                                                  Bilet60min_ulg,
                                                                                                  Bilet20min,
                                                                                                  Bilet40min,
                                                                                                  Bilet60min]


def Bilety_Ulgowe(list):
    a, b, c, d, e, f = list  # Unpack list of tickets
    interface.widget_forget()  # forget previous buttons
    a.activate()  # display tickets
    b.activate()
    c.activate()
    tmp_list_tickets = [d, e, f, a, b,
                        c]  # tmp list of tickets, which allows to send them to another function to proper count sum price
    interface.wyswietlulgowe(list, tmp_list_tickets)



def Bilety_Normalne(list):
    a, b, c, d, e, f = list  # Unpack list of tickets
    interface.widget_forget()  # forget previous buttons
    a.activate()
    b.activate()
    c.activate()
    tmp_list_tickets = [d, e, f, a, b,
                        c]  # tmp_list_tickets list of tickets, which allows to send them to another function to proper count sum price
    interface.wyswietnormalne(list, tmp_list_tickets)


def Restart():
    interface.widget_forget()
    l = []
    temp = WrzuconeMonety.return_list()
    for k in temp:
        l.append(k.get_value())
    for i in l:
        WrzuconeMonety.return_Nominal(i)
    # clear_w()
    # WrzuconeMonety = Money_Storage('PLN', [])
    listanormalne, listaulgowe = config()
    interface.Start(listanormalne, listaulgowe)


def returnChange(Biletomat, reszta):
    l = []
    l2 = []
    o = []
    listamonet = Biletomat.return_list()
    print("1:")
    print(Biletomat.Sum())
    for i in listamonet:
        l.append(i.get_value())
    l.sort(reverse=True)
    print("printuje reszte")
    print(reszta)
    r = round(reszta, 2)
    if r == 0:
        print("wchodze tu")
        return True, [0]

    for i in l:
        k = round(i, 2)
        r=round(r,2)
        if k <= r:
            r -= float(k)
            l2.append(i)
            if r == 0:
                print("Wydano reszte")
                for i in l2:
                    o.append(Biletomat.return_Nominal(i).get_value())
                print(Biletomat.Sum())
                return True, o
    else:
        print("reszty nie wydano")
        return False, []


def Refresh_sum(value, coins_counter, sum_string, change,dictionary):  # function to refresh sum after throw a coin into machine
    print("jestem w refesz szum")
    print(dictionary)
    coins_thrown_in_counter = coins_counter.get()
    coins_counter.set(1)
    for i in range(coins_thrown_in_counter):
        WrzuconeMonety.add_Coin_or_Bill(Coin_Bill(value))
    sum_float = float(sum_string.get().split(" ")[0]) - coins_thrown_in_counter * value

    sum_string.set('{:.2f}'.format(sum_float) + " zl")
    if sum_float <= 0:
        interface.display_coins(sum_string, change, dictionary,"disabled")  # if sum <=0 then no more coins are allowed to be thrown in
        sum_string.set("0.00 zl")
        if sum_float < 0:
            sum_float = sum_float * -1
            print("sumFloat")
            print(sum_float)
        change.set('{:.2f}'.format(sum_float) + " zl")
        change_to_be_returned_bool, w = returnChange(Biletomat, sum_float)
        print(change_to_be_returned_bool)
        if w == [] and change_to_be_returned_bool == False:
            l = WrzuconeMonety.return_list()
            for i in l:
                w.append(i.get_value())

        finish(change_to_be_returned_bool, w,dictionary)
        interface.Summary_display(sum_string, change,"disabled")


def finish(change_to_be_returned_bool, text,dictionary):
    if change_to_be_returned_bool == True:
        t = "Wydano reszte:\n "
        l = WrzuconeMonety.return_list()
        for k in l:
            Biletomat.add_Coin_or_Bill(k)
    elif change_to_be_returned_bool == False:
        t = "Tylko odliczona kwota, zwrocono : \n"
    tmp2 = []
    for k in text:
        tmp2.append(str(float(k)) + " zl ")
    print(tmp2)
    tmp = ' '.join(item for item in tmp2)
    change_info_text = StringVar()
    change_info_text.set(t + tmp)
    purchased_tickets_text = StringVar()

    print(Biletomat.Sum())
    d=copy.deepcopy(dictionary)
    for key, value in d.items():
        if value == 0:
            dictionary.pop(key)
            continue
    t3 ='\n'.join(str(value)+ "x"+key  for key,value in dictionary.items())
    purchased_tickets_text.set("Zakupione bilety:\n" +t3)
    print(dictionary)
    change_info = Label(interface.window,
                        textvariable=change_info_text,
                        relief="raised",
                        bg="#231697",
                        font=interface.myfont,
                        fg="white",
                        borderwidth=5,
                        ).grid(row=5, column=1, sticky="NSEW", padx=2, pady=20, columnspan=2, rowspan=2)
    Purchased_tickets = Label(interface.window,
                        textvariable=purchased_tickets_text,
                        relief="raised",
                        bg="#231697",
                        font=interface.myfont,
                        fg="white",
                        borderwidth=5,
                        ).grid(row=2, column=0, sticky="NSEW", padx=2, pady=20,  rowspan=5)




def Summary(lista, flaga):
    change_info = StringVar()
    change_info.set("0.00 zl")
    coins_counter = IntVar()
    coins_counter.set(1)
    interface.widget_forget()
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
    ticket_name_price_dictionary ={}
    for i in lista:
        ticket_name_price_dictionary[i.get_name()] = i.ticket_counter.get()
    tmp_sum = WrzuconeMonety.Sum()
    print("printujetmp_sum")
    print(tmp_sum)
    print("printuje tmp1:")
    tmp = 0
    print(tmp)
    for i in tmp_list:
        tmp = tmp + i
    tmp = tmp - float(tmp_sum)  # sum calculation
    print("printujetmp2")
    print(tmp)
    tmp2 = '{:.2f}'.format(tmp) + " zl"
    global sum_test_purposes
    sum_test_purposes=tmp
    sum_string.set(tmp2)
    interface.display_coins(sum_string, change,ticket_name_price_dictionary)
    interface.Summary_display(sum_string, change)


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
    interface.window.geometry("850x650")
    interface.window.configure(background="#231697")
    # interface.window.resizable(False,False)
    # interface.window.iconbitmap("ikona.ico")
    interface.window.title("Biletomat MPK")
    interface.Start(listanormalne, listaulgowe)

    interface.window.mainloop()


