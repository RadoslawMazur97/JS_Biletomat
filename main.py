# Import the required Libraries
from tkinter import *
import time
import os
import sys
from decimal import *
import copy
import random

listadowzwolonych = [0.01, 0.02, 0.05, 0.10, 0.20, 0.50, 1, 2, 5, 10, 20, 50]
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

class Moneta:
    __waluta = 'PLN'
    __wartosc = 0

    def __init__(self, val):
        allowed = [0.01, 0.02, 0.05, 0.10, 0.20, 0.50, 1, 2, 5, 10, 20, 50]
        if val in allowed:
           # print(val)
            self.__wartosc = Decimal(val)
        else:
            raise ZlyNominalExcepion('Brak takiego nominalu')

    def get_wartosc(self):
        return self.__wartosc

    def get_waluta(self):
        return self.__waluta


class PrzechowywaczMonet:
    __lista = []
    lista2 =[]
    def __init__(self, obsluga,l):
        self.__obsluga = obsluga
        self.__lista=l

    def dodajMonete(self, moneta):
        if isinstance(moneta, Moneta):
            if moneta.get_waluta() in self.__obsluga:
                self.__lista.append(moneta)
            else:
                raise NieznanaWalutaException()
        else:
            print('Przeslany obiekt nie jest monetą')
    def lacznaSuma(self):
        sum_ = 0
        for x in self.__lista:
            sum_ = sum_ + x.get_wartosc()
        return Decimal(sum_)

    def zwrocNominal(self, val):
        for x in self.__lista:
            if x.get_wartosc() == Decimal(val):
                self.__lista.remove(x)
                return x
    def zwrocliste(self):
        return self.__lista

getcontext().prec = 4

tmp_list1 = []
tmp_list2 = []
l = [random.choice(listadowzwolonych) for x in range(100)]  # Randomowa lista nominalow znajdujacych sie w biletomacie
Biletomat = PrzechowywaczMonet('PLN',tmp_list1)
for i in l:
    Biletomat.dodajMonete(Moneta(i))
print(Biletomat.lacznaSuma())

WrzuconeMonety = PrzechowywaczMonet('PLN',tmp_list2)

cwd = os.getcwd()
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

    def aktywuj(self):
        self.Ticket_label.grid(row=self.row, column=self.col, sticky="NSEW", padx=2, pady=20)
        self.counter_disp.grid(row=self.row, column=2)
        self.ticket_add.grid(row=self.row, column=3, sticky="NSEW", padx=2, pady=50)
        self.ticket_substract.grid(row=self.row, column=1, sticky="NSEW", padx=2, pady=50)

    def forget(self):
        # self.Ticket_button.grid_forget()
        self.counter_disp.grid_forget()

    def grid_hide(widget):
        widget._grid_info = widget.grid_info()
        widget.grid_remove()

    def grid_show(widget):
        widget.grid(**widget._grid_info)

def WydajReszte(Biletomat,reszta):
    l =[]
    l2 =[]
    listamonet=Biletomat.zwrocliste()
    print("1:")
    print(Biletomat.lacznaSuma())
    for i in listamonet:
        l.append(i.get_wartosc())
    l.sort(reverse=True)

    print(l)
    for i in l:
        reszta=round(reszta,2)
        i=round(i,2)
        #print(i.compare(reszta))
        if i <= reszta:
            print("printuje i")
            print(float(i))
            reszta -=float(i)
            l2.append(i)
    if reszta == 0:
        print("Wydano reszte")
        for i in l2:
            print(i)
            print(Biletomat.zwrocNominal(i))
        return True
    else:
        print("reszty nie wydano")
        return False


def Bilety_Ulgowe(lista):
    a, b, c, d, e, f = lista
    widget_forget()
    # window.geometry("500x500")
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
                      command=lambda: Summary(lista, True),
                      bg="#231697",
                      borderwidth=5,
                      relief="raised",
                      font=myfont,
                      fg="white",
                      activebackground='#3974BB',
                      ).grid(row=3, column=1, sticky="NSEW", columnspan=3, padx=2, pady=20)


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
                      command=lambda: Summary(lista, False),
                      bg="#231697",
                      borderwidth=5,
                      relief="raised",
                      font=myfont,
                      fg="white",
                      activebackground='#3974BB',
                      ).grid(row=3, column=1, sticky="NSEW", columnspan=3, padx=2, pady=20)


def widget_forget():
    for i in window.grid_slaves():
        i.grid_forget()


def clear_widgets():
    for widget in window.winfo_children():
        widget.destroy()


def Summary(lista, flaga):
    global tmp
    coins_counter = IntVar()
    coins_counter.set(1)

    def display_coins(czy_aktywny="normal"):
        def onClick_addfun():
            coins_counter.set(coins_counter.get() + 1)
        def onClick_substract():
            if coins_counter.get() == 1:
                return
            coins_counter.set(coins_counter.get() - 1)

        i = 0
        for c in listadowzwolonych:
            if(i<6):
                colnum=3
                rownum=i+1
            else:
                colnum=5
                rownum =i-5
            Button(window,
                   text="Wrzuć " + str(c) + " zł",
                   command=lambda c=c: Refresh_sum(float(c)),
                   bg="#231697",
                   borderwidth=5,
                   relief="raised",
                   font=myfont,
                   fg="white",
                   state=czy_aktywny
                   ).grid(row=rownum, column=colnum, sticky="NSEW", padx=2, pady=20)
            i += 1

        Label(window,
              text="Wybierz ilosc Monet lub bankontow:",
              bg="#231697",
              borderwidth=5,
              relief="raised",
              font=myfont,
              fg="white",
              ).grid(row=0,column=1, sticky="NSEW", padx=2, pady=20, columnspan=2)
        counter_money = Label(window,
                                  textvariable=coins_counter,
                                  relief="raised",
                                  bg="#231697",
                                  font=myfont,
                                  fg="white"
                                  ).grid(row=0,column=4, sticky="NSEW", padx=2, pady=20)
        counter_money_add = Button(window,
                                 text="+",
                                 command= lambda: onClick_addfun(),
                                 borderwidth=5,
                                 relief="raised",
                                 bg="#231697",
                                 font=myfont,
                                 fg="white",
                                 activebackground='#3974BB',

                                 ).grid(row=0,column=5, sticky="NSEW", padx=2, pady=20)
        counter_money_substract = Button(window,
                                       text="-",
                                       bg="#231697",
                                       borderwidth=5,
                                       relief="raised",
                                       font=myfont,
                                       fg="white",
                                       activebackground='#3974BB',
                                       command=lambda: onClick_substract(),
                                       ).grid(row=0,column=3, sticky="NSEW", padx=2, pady=20)

    widget_forget()
    sum = DoubleVar()
    test = StringVar()
    reszta = StringVar()
    reszta.set("0.00 zl")
    t = 0
    a, b, c, d, e, f = lista
    if (flaga == True):
        a = a.ticket_counter.get() * price_20_minutes / 2
        b = b.ticket_counter.get() * price_40_minutes / 2
        c = c.ticket_counter.get() * price_60_minutes / 2
        d = d.ticket_counter.get() * price_20_minutes
        e = e.ticket_counter.get() * price_40_minutes
        f = f.ticket_counter.get() * price_60_minutes
        tmp = [a, b, c, d, e, f]
    elif (flaga == False):
        a = a.ticket_counter.get() * price_20_minutes
        b = b.ticket_counter.get() * price_40_minutes
        c = c.ticket_counter.get() * price_60_minutes
        d = d.ticket_counter.get() * price_20_minutes / 2
        e = e.ticket_counter.get() * price_40_minutes / 2
        f = f.ticket_counter.get() * price_60_minutes / 2
        tmp = [a, b, c, d, e, f]
    tmp_sum = WrzuconeMonety.lacznaSuma()
    print("Laczna sumna tmp_Sum")
    print(tmp_sum)
    for i in tmp:
        t = t + i

    t = t - float(tmp_sum)
    t2 = '{:.2f}'.format(t) + " zl"
    test.set(t2)

    def Refresh_sum(value):
        ilosc_wrzuconych=coins_counter.get()
        coins_counter.set(1)

        print(value)
        for i in range(ilosc_wrzuconych):
            WrzuconeMonety.dodajMonete(Moneta(value))

        print(WrzuconeMonety.lacznaSuma())

        #print(tmp_sum)
        sum_float = float(test.get().split(" ")[0]) - ilosc_wrzuconych*value
        test.set('{:.2f}'.format(sum_float) + " zl")
        if (sum_float) <= 0:
            display_coins("disabled")
            test.set("0.00 zl")
            sum_float = sum_float * -1
            reszta.set('{:.2f}'.format(sum_float) + " zl")
            czy_wydano_reszte=WydajReszte(Biletomat,sum_float)
            if czy_wydano_reszte == False:
                print("Tylko odliczona kwota")
                for k in WrzuconeMonety.zwrocliste():
                    WrzuconeMonety.zwrocNominal(k.get_wartosc())
            #WydajReszte(Biletomat.zwrocliste(),sum_float)

          #  if (sum_float>Biletomat.lacznaSuma()):
              #  print("nie da rady")

    suma_display_text = Label(window,
                              text="Pozostalo do zaplaty:",
                              bg="#231697",
                              borderwidth=5,
                              relief="raised",
                              font=myfont,
                              fg="white",
                              )
    suma_display_text.grid(row=1, column=1, sticky="NSEW", columnspan=2, padx=2, pady=20)
    suma_display = Label(window,
                         textvariable=test,
                         bg="#231697",
                         borderwidth=5,
                         relief="raised",
                         font=myfont,
                         fg="white",
                         )
    suma_display.grid(row=2, column=1, sticky="NSEW", columnspan=2, padx=2, pady=20)
    reszta_display_text = Label(window,
                                text="Reszta:",
                                bg="#231697",
                                borderwidth=5,
                                relief="raised",
                                font=myfont,
                                fg="white",
                                )
    reszta_display_text.grid(row=3, column=1, sticky="NSEW", columnspan=2, padx=2, pady=20)
    reszta_display = Label(window,
                           textvariable=reszta,
                           bg="#231697",
                           borderwidth=5,
                           relief="raised",
                           font=myfont,
                           fg="white",
                           )
    reszta_display.grid(row=4, column=1, sticky="NSEW", columnspan=2, padx=2, pady=20)
    Dodaj_Bilet = Button(window,
                         text="Dodaj Bilet",
                         command=lambda: Start(listanormalne, listaulgowe),
                         bg="#231697",
                         borderwidth=5,
                         relief="raised",
                         font=myfont,
                         fg="white",
                         )
    Dodaj_Bilet.grid(row=0, column=0, sticky="NSEW", padx=2, pady=20)

    display_coins()
    print(sum)


def Start(listanormalne, listaulgowe):
    widget_forget()
    wybor_biletu_label = Label(window,
                               text="Wybierz rodzaj biletu:",
                               borderwidth=5,
                               relief="raised",
                               bg="#140787",
                               font=myfont,
                               fg="white",
                               activebackground='#3974BB',
                               ).grid(row=0, column=1, sticky="NSEW", columnspan=2, padx=20, pady=35)

    button_bilet_normalny = Button(window,
                                   text="Bilet Normalny",
                                   command=lambda: Bilety_Normalne(listanormalne),
                                   borderwidth=5,
                                   relief="raised",
                                   bg="#231697",
                                   font=myfont,
                                   fg="white",
                                   activebackground='#3974BB',
                                   ).grid(row=1, column=1, sticky="NSEW", padx=20, pady=35)
    button_bilet_ulgowy = Button(window,
                                 text="Bilet Ulgowy",
                                 command=lambda: Bilety_Ulgowe(listaulgowe),
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
# window.resizable(False,False)
# window.iconbitmap("C:\\Users\\RXKW46\\Documents\\JS\\ikona.ico")
# window.iconbitmap("ikona.ico")
print("tst")
print(cwd)
window.title("Biletomat MPK")
myfont = ("Rubik", 15)


# filename = PhotoImage(file="C:\\Users\\RXKW46\\Documents\\JS\\tlo2.png")
# filename = PhotoImage(file = ".\\Documents\JS\\tlo.png")
# background_label = Label(window, image=filename)
# background_label.place(x=1, y=1, relwidth=1, relheight=1)
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


listanormalne, listaulgowe = config()
Start(listanormalne, listaulgowe)


def Restart():
    listanormalne, listaulgowe = config()
    Start(listanormalne, listaulgowe)


window.mainloop()