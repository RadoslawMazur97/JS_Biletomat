# Import the required Libraries
from tkinter import *
from decimal import *
import copy
import random
import interface
sum_test_purposes = 0 #variable for test purposes

try: #Try to set the graphics as a background and icon file if not the app will run with navy blue colour.
    filename = PhotoImage(file="tlo2.png")
    interface.window.iconbitmap("ikona.ico")
    background_label = Label(interface.window, image=filename)
    label1 = Label(interface.window, image=filename)
    label1.place(x=0, y=0)
except:
    print("unable to load graphic") 

# Set Price for the normal tickets    
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

class NiepoprawnaIloscMonetException(Exception):
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
    '''Class reponsible for Coin/Bill object creation'''
    __currency = 'PLN'
    __value = 0

    def __init__(self, val):
        '''Constructor'''
        if val in allowed_coins_bills:
            self.__value = Decimal(val)
        else:
            raise ZlyNominalExcepion('Brak takiego nominalu')

    def get_value(self):
        '''return value of coin'''
        return self.__value

    def get_waluta(self):
        '''return coin currency'''
        return self.__currency


class Money_Storage:
    '''Class which stores Coins/Bills'''
    __Money_list = []

    def __init__(self, currency, l):
        '''Constructor'''
        self.__curr = currency
        self.__Money_list = l

    def add_Coin_or_Bill(self, Coin_or_Bill):
        '''Add Coin or Bill to storage'''
        if isinstance(Coin_or_Bill, Coin_Bill):
            if Coin_or_Bill.get_waluta() in self.__curr:
                self.__Money_list.append(Coin_or_Bill)
            else:
                raise NieznanaWalutaException()
        else:
            print('Przeslany obiekt nie jest monetą')

    def Sum(self):
        '''Return Sum of coins/bill which Storage contain'''
        sum_ = 0
        for x in self.__Money_list:
            sum_ = sum_ + x.get_value()
        return Decimal(sum_)

    def return_Nominal(self, val):
        '''return the Coin/Bill from the Storage'''
        for x in self.__Money_list:
            if x.get_value() == Decimal(val):
                self.__Money_list.remove(x)
                return x

    def return_list(self):
        '''Returns the list of the coins/bill'''
        return self.__Money_list


class my_ticket:
    '''Class responsible for tikcet creation and dispaly'''
    Ticket_label = Label
    counter_disp = Label
    ticket_add = Button
    ticket_substract = Button
    ticket_counter = IntVar()

    def __init__(self, bilet_name, my_row, my_col):
        '''Constructor'''
        self.ticket_counter = IntVar()
        self.ticket_counter.set(0)
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
        '''Return name of the ticket'''
        return self.name

    def onClick_addfun(self, event=None):
        '''Increment tickets count'''
        self.ticket_counter.set(self.ticket_counter.get() + 1)

    def onClick_substract(self, event=None):
        '''Decrement tickets count'''
        if self.ticket_counter.get() == 0:
            return
        self.ticket_counter.set(self.ticket_counter.get() - 1)

    def activate(self):
        '''Display Tickets'''
        self.Ticket_label.grid(row=self.row, column=self.col, sticky="NSEW", padx=2, pady=20)
        self.counter_disp.grid(row=self.row, column=2)
        self.ticket_add.grid(row=self.row, column=3, sticky="NSEW", padx=2, pady=50)
        self.ticket_substract.grid(row=self.row, column=1, sticky="NSEW", padx=2, pady=50)




def config(): #config function
    '''Config function, renposible for setting grid, create tickets and return them as 2 lists'''
    for i in range(4): #Set grid config to proper display
        Grid.rowconfigure(interface.window, i, weight=1) 
        Grid.columnconfigure(interface.window, i, weight=1)
    # Create tickets and return them as a lists
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
    '''function which is unpacking list of reduced tickets and activate(display)them'''
    a, b, c, d, e, f = list  # Unpack list of tickets
    interface.widget_forget()  # forget previous buttons
    a.activate()  # display tickets
    b.activate()
    c.activate()
    tmp_list_tickets = [d, e, f, a, b,
                        c]  # tmp list of tickets, which allows to send them to another function to proper count sum price
    interface.wyswietlulgowe(list, tmp_list_tickets)



def Bilety_Normalne(list):
    '''function which is unpacking list of normal tickets and activate(display)them'''
    a, b, c, d, e, f = list  # Unpack list of tickets
    interface.widget_forget()  # forget previous buttons
    a.activate()
    b.activate()
    c.activate()
    tmp_list_tickets = [d, e, f, a, b,
                        c]  # tmp_list_tickets list of tickets, which allows to send them to another function to proper count sum price
    interface.wyswietnormalne(list, tmp_list_tickets)


def Restart(): #Restart program, new customer
    '''Restart program, new customer, called after user click zacznij od Nowa'''
    interface.widget_forget()
    temp = WrzuconeMonety.return_list()
    l =[(i.get_value()) for i in temp]
    [WrzuconeMonety.return_Nominal(i) for i in l]
    listanormalne, listaulgowe = config()
    interface.Start(listanormalne, listaulgowe)


def returnChange(Biletomat, reszta): #Function to return change
    '''Function responsible for returinng the change'''
    l2 = [] #temporary list to store all the coins which user put to machine
    o = [] #list to store value of the coins from l2
    listamonet = Biletomat.return_list()
    l = [(i.get_value()) for i in listamonet]
    l.sort(reverse=True)

    r = round(reszta, 2)
    if r == 0:

        return True, [0]

    for i in l:
        k = round(i, 2)
        r=round(r,2)
        if k <= r:
            r -= float(k)
            l2.append(i)
            if r == 0:
                for i in l2:
                    o.append(Biletomat.return_Nominal(i).get_value())
                return True, o
    else:
        return False, []


def Refresh_sum(value, coins_counter, sum_string, change,dictionary): 
    '''function to refresh sum after throw a coin into machine'''
    if not (isinstance(coins_counter.get(),int)) or (coins_counter.get() < 1): #validate if someone is trying to put negative or noninterger number of coins
        raise NiepoprawnaIloscMonetException('Niepoprawna ilosc monet')

    coins_thrown_in_counter = coins_counter.get()
    coins_counter.set(1) #set the coins counter to 1 after thrown some coins/bills

    for i in range(coins_thrown_in_counter):
        WrzuconeMonety.add_Coin_or_Bill(Coin_Bill(value)) #store the thrown coins

    sum_float = float(sum_string.get().split(" ")[0]) - coins_thrown_in_counter * value # calculate the sum

    global sum_test_purposes #variable for test purposes
    sum_test_purposes = sum_float

    sum_string.set('{:.2f}'.format(sum_float) + " zl") #display the sum for enduser
    if sum_float <= 0:
        interface.display_coins(sum_string, change, dictionary,"disabled")  # if sum <=0 then no more coins are allowed to be thrown in
        sum_string.set("0.00 zl")
        if sum_float < 0:
            sum_float = sum_float * -1
        change.set('{:.2f}'.format(sum_float) + " zl") #set the change value
        change_to_be_returned_bool, w = returnChange(Biletomat, sum_float) #calculate the change
        if w == [] and change_to_be_returned_bool == False:
            w = [(i.get_value()) for i in WrzuconeMonety.return_list()]

        finish(change_to_be_returned_bool, w,dictionary)
        interface.Summary_display(sum_string, change,"disabled")


def finish(change_to_be_returned_bool, text,dictionary):
    '''Finish function, which displays info if change has been returned and purcahsed tickets or if it was impossible it return all thrown coins/bills'''
    if change_to_be_returned_bool == True:
        t = "Wydano reszte:\n "
        [Biletomat.add_Coin_or_Bill(k) for k in WrzuconeMonety.return_list()]
    elif change_to_be_returned_bool == False:
        t = "Tylko odliczona kwota, zwrocono : \n"
    tmp2 = []
    for k in text:
        tmp2.append(str(float(k)) + " zl ")
    tmp = ' '.join(item for item in tmp2)
    change_info_text = StringVar()
    change_info_text.set(t + tmp)
    purchased_tickets_text = StringVar()

    d=copy.deepcopy(dictionary) #temproary dictionary to store the bilets which were selected to purchase
    for key, value in d.items():
        if value == 0:
            dictionary.pop(key)
            continue

    t3 ='\n'.join(str(value)+ "x"+key  for key,value in dictionary.items())
    purchased_tickets_text.set("Zakupione bilety:\n" +t3)
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
    '''Summary of purchased tickets'''
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
    tmp = 0
    for i in tmp_list:
        tmp = tmp + i
   
    tmp = tmp - float(tmp_sum)  # sum calculation

    tmp2 = '{:.2f}'.format(tmp) + " zl"
    global sum_test_purposes
    sum_test_purposes=tmp
    sum_string.set(tmp2)
    interface.display_coins(sum_string, change,ticket_name_price_dictionary)
    interface.Summary_display(sum_string, change)


tmp_list2 = []
tmp_list1 = []
random_generated_list_of_coins_bills = [random.choice(allowed_coins_bills) for x in
                                                                        range(100)]  # Randomowa list of nominals which are already stored in ticketing machine
Biletomat = Money_Storage('PLN', tmp_list1)
[Biletomat.add_Coin_or_Bill(Coin_Bill(i)) for i in random_generated_list_of_coins_bills]

WrzuconeMonety = Money_Storage('PLN', tmp_list2)
listanormalne, listaulgowe = config()


def main():
    '''Main function set window geometry, background, title and start the program'''
    interface.window.geometry("950x750")
    interface.window.configure(background="#231697")
    interface.window.title("Biletomat MPK")
    interface.Start(listanormalne, listaulgowe)  #Start the app

    interface.window.mainloop()


