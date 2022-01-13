import unittest
import logic
from tkinter import *
import random


class TestTicketingSystem(unittest.TestCase):   
   #def test_no_change(self):
   #    tmp_list2 = []
   #    tmp_list1 = []
   #    coins_counter = IntVar()
   #    coins_counter.set(1)
   #    change = StringVar()
   #    change.set("0.00 zl")
   #    sum = StringVar()
   #    Biletomat = logic.Money_Storage('PLN', tmp_list1)
   #    WrzuconeMonety = logic.Money_Storage('PLN', tmp_list2)
   #    Test_2_zlote=logic.Coin_Bill(2)
   #    #Test_1_zlote=logic.Coin_Bill(1)    
   #    WrzuconeMonety.add_Coin_or_Bill(Test_2_zlote)
   #   # WrzuconeMonety.add_Coin_or_Bill(Test_1_zlote)
   #    listanormalne, listaulgowe = logic.config()
   #    #logic.Start(listanormalne, listaulgowe)
   #    a,b,c,d,e,f = listaulgowe
   #    a.ticket_counter.set(1)
   #    ticket_price = a.ticket_counter.get()* logic.price_20_minutes/2
   #    sum.set(str(ticket_price)+" zl")
   #    logic.Bilety_Ulgowe(listaulgowe)
   #    ticket_name_price_dictionary ={}
   #    for i in listaulgowe:
   #        ticket_name_price_dictionary[i.get_name()] = i.ticket_counter.get()
   #    a,b,c,d,e,f = listaulgowe
   #    flag, w =logic.returnChange(Biletomat, 0)
   #    print("w")
   #    print(w)
   #    logic.Summary(listaulgowe, True)  
   #    print("printuje a")
   #    print(ticket_price)
   #    logic.Refresh_sum(2,coins_counter,sum,change,ticket_name_price_dictionary)
   #    k=[]
   #    lista_tmp=WrzuconeMonety.return_list()
   #    total =0
   #    for l in lista_tmp:
   #        k.append(l.get_value())
   #    for ele in range(0, len(k)):
   #        total = total + k[ele]  
   #    t1=ticket_price-float(total)
   #    #self.assertEqual(t1,w[0])
   #    self.assertFalse(w[0])

   #def test_expected_change(self):
   #    tmp_list2 = []
   #    tmp_list1 = []
   #    random_generated_list_of_coins_bills = [random.choice(logic.allowed_coins_bills) for x in
   #                                                                    range(100)]  # Randomowa lista nominalow znajdujacych sie w biletomacie
   #    Biletomat = logic.Money_Storage('PLN', tmp_list1)
   #    for i in random_generated_list_of_coins_bills:
   #         Biletomat.add_Coin_or_Bill(logic.Coin_Bill(i))
   #    print(Biletomat.Sum())
   #    coins_counter = IntVar()
   #    coins_counter.set(1)
   #    change = StringVar()
   #    change.set("0.00 zl")
   #    sum = StringVar()
   #    #Biletomat = logic.Money_Storage('PLN', tmp_list1)
   #    WrzuconeMonety = logic.Money_Storage('PLN', tmp_list2)
   #    Test_5_zlote=logic.Coin_Bill(5)
   #    #Test_1_zlote=logic.Coin_Bill(1)

   #    WrzuconeMonety.add_Coin_or_Bill(Test_5_zlote)
   #   # WrzuconeMonety.add_Coin_or_Bill(Test_1_zlote)
   #    listanormalne, listaulgowe = logic.config()
   #    #logic.Start(listanormalne, listaulgowe)
   #    a,b,c,d,e,f = listaulgowe
   #    a.ticket_counter.set(1)
   #    ticket_price = a.ticket_counter.get()* logic.price_20_minutes/2
   #    sum.set(str(ticket_price)+" zl")
   #    logic.Bilety_Ulgowe(listaulgowe)
   #    ticket_name_price_dictionary ={}
   #    for i in listaulgowe:
   #        ticket_name_price_dictionary[i.get_name()] = i.ticket_counter.get()
   #    a,b,c,d,e,f = listaulgowe
   #    flag, w =logic.returnChange(Biletomat, 3)
   #    print("w")
   #    print(w)
   #    logic.Summary(listaulgowe, True)  
   #    print("printuje a")
   #    print(ticket_price)
   #    logic.Refresh_sum(5,coins_counter,sum,change,ticket_name_price_dictionary)
   #   # k=[]
   #   # lista_tmp=WrzuconeMonety.return_list()
   #    total =0
   #    #for l in lista_tmp:
   #    #    k.append(l.get_value())
   #    for ele in range(0, len(w)):
   #        total = total + w[ele]
   #    print("printujeW")
   #    print(w)

   #    t1=float(total) -ticket_price 
   #    #self.assertNotEqual(0,float(total))
   #    self.assertTrue(w)
   #def test_expected_return_monety(self):
   #    tmp_list2 = []
   #    tmp_list1 = []
   #    random_generated_list_of_coins_bills = [random.choice(logic.allowed_coins_bills) for x in
   #                                                                    range(0)]  # Randomowa lista nominalow znajdujacych sie w biletomacie
   #    Biletomat = logic.Money_Storage('PLN', tmp_list1)
   #    for i in random_generated_list_of_coins_bills:
   #         Biletomat.add_Coin_or_Bill(logic.Coin_Bill(i))
   #    print("Sumabieltomatu")
   #    print(Biletomat.Sum())
   #    coins_counter = IntVar()
   #    coins_counter.set(1)
   #    change = StringVar()
   #    change.set("0.00 zl")
   #    sum = StringVar()
   #    #Biletomat = logic.Money_Storage('PLN', tmp_list1)
   #    WrzuconeMonety = logic.Money_Storage('PLN', tmp_list2)
   #    Test_5_zlote=logic.Coin_Bill(5)
   #    #Test_1_zlote=logic.Coin_Bill(1)

   #    WrzuconeMonety.add_Coin_or_Bill(Test_5_zlote)
   #   # WrzuconeMonety.add_Coin_or_Bill(Test_1_zlote)
   #    listanormalne, listaulgowe = logic.config()
   #    #logic.Start(listanormalne, listaulgowe)
   #    a,b,c,d,e,f = listaulgowe
   #    a.ticket_counter.set(1)
   #    ticket_price = a.ticket_counter.get()* logic.price_20_minutes/2
   #    sum.set(str(ticket_price)+" zl")
   #    logic.Bilety_Ulgowe(listaulgowe)
   #    ticket_name_price_dictionary ={}
   #    for i in listaulgowe:
   #        ticket_name_price_dictionary[i.get_name()] = i.ticket_counter.get()
   #    a,b,c,d,e,f = listaulgowe
   #    change_to_be_returned_bool, w =logic.returnChange(Biletomat, 3)
   #    if w == [] and change_to_be_returned_bool == False:
   #        l = WrzuconeMonety.return_list()
   #        for i in l:
   #            w.append(i.get_value())
   #    print(w)
   #    logic.finish(change_to_be_returned_bool, w,{})
   #    self.assertEqual(w[0],Test_5_zlote.get_value())
    #def test_no_change_gr(self):
    # tmp_list2 = []
    # tmp_list1 = []
    # coins_counter = IntVar()
    # coins_counter.set(1)
    # change = StringVar()
    # change.set("0.00 zl")
    # sum = StringVar()
    # Biletomat = logic.Money_Storage('PLN', tmp_list1)
    # WrzuconeMonety = logic.Money_Storage('PLN', tmp_list2)
    # for i in range (200):
    #      WrzuconeMonety.add_Coin_or_Bill(logic.Coin_Bill(0.01))
    # #Test_2_zlote=logic.Coin_Bill(2)
    # #Test_1_zlote=logic.Coin_Bill(1)    
    ## WrzuconeMonety.add_Coin_or_Bill(Test_2_zlote)
    ## WrzuconeMonety.add_Coin_or_Bill(Test_1_zlote)
    # listanormalne, listaulgowe = logic.config()
    # #logic.Start(listanormalne, listaulgowe)
    # a,b,c,d,e,f = listaulgowe
    # a.ticket_counter.set(1)
    # ticket_price = a.ticket_counter.get()* logic.price_20_minutes/2
    # sum.set(str(ticket_price)+" zl")
    # logic.Bilety_Ulgowe(listaulgowe)
    # ticket_name_price_dictionary ={}
    # for i in listaulgowe:
    #     ticket_name_price_dictionary[i.get_name()] = i.ticket_counter.get()
    # a,b,c,d,e,f = listaulgowe
    # flag, w =logic.returnChange(Biletomat, 0)
    # print("w")
    # print(w)
    # logic.Summary(listaulgowe, True)  
    # print("printuje a")
    # print(ticket_price)
    # logic.Refresh_sum(2,coins_counter,sum,change,ticket_name_price_dictionary)
    # k=[]
    # lista_tmp=WrzuconeMonety.return_list()
    # total =0
    # for l in lista_tmp:
    #     k.append(l.get_value())
    # for ele in range(0, len(k)):
    #     total = total + k[ele]  
    # t1=ticket_price-float(total)
    # self.assertEqual(t1,w[0])
    # self.assertFalse(w[0])


    def test_two_tickets(self):
         tmp_list2 = []
         tmp_list1 = []
         coins_counter = IntVar()
         coins_counter.set(1)
         change = StringVar()
         change.set("0.00 zl")
         sum = StringVar()
         Biletomat = logic.Money_Storage('PLN', tmp_list1)
         WrzuconeMonety = logic.Money_Storage('PLN', tmp_list2)

         WrzuconeMonety.add_Coin_or_Bill(logic.Coin_Bill(1))  
         listanormalne, listaulgowe = logic.config()
         #logic.Start(listanormalne, listaulgowe)
         a,b,c,d,e,f = listaulgowe
         a.ticket_counter.set(1)
         b.ticket_counter.set(1)
         ticket_price = a.ticket_counter.get()* logic.price_20_minutes/2 + b.ticket_counter.get()*logic.price_40_minutes/2
         sum.set(str(ticket_price)+" zl")
         logic.Bilety_Ulgowe(listaulgowe)
         ticket_name_price_dictionary ={}
         for i in listaulgowe:
             ticket_name_price_dictionary[i.get_name()] = i.ticket_counter.get()
         a,b,c,d,e,f = listaulgowe
         flag, w =logic.returnChange(Biletomat, 0)
         print("w")
         print(w)
         logic.Summary(listaulgowe, True)  
         print("printuje a")
         print(ticket_price)
         logic.Refresh_sum(2,coins_counter,sum,change,ticket_name_price_dictionary)
         k=[]
         lista_tmp=WrzuconeMonety.return_list()
         print("PRINTUJE C")
         print(logic.sum_test_purposes)
         total =0
         for l in lista_tmp:
             k.append(l.get_value())
         print(k)
         for ele in range(0, len(k)):
             total = total + k[ele]  
         t1=ticket_price-float(total)
         self.assertEqual(logic.sum_test_purposes,ticket_price)
    