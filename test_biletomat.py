import unittest
import logic
from tkinter import *
import random


class TestTicketingSystem(unittest.TestCase):
    def test_no_change(self):
       tmp_list2 = []
       tmp_list1 = []
       coins_counter = IntVar()
       coins_counter.set(1)
       change = StringVar()
       change.set("0.00 zl")
       sum = StringVar()
       Biletomat = logic.Money_Storage('PLN', tmp_list1)
       WrzuconeMonety = logic.Money_Storage('PLN', tmp_list2)
       Test_2_zlote=logic.Coin_Bill(2)
       WrzuconeMonety.add_Coin_or_Bill(Test_2_zlote)
       listanormalne, listaulgowe = logic.config()
       a,b,c,d,e,f = listaulgowe
       a.ticket_counter.set(1)
       ticket_price = a.ticket_counter.get()* logic.price_20_minutes/2
       sum.set(str(ticket_price)+" zl")
       ticket_name_price_dictionary ={}
       flag, w =logic.returnChange(Biletomat, 0)
       logic.Refresh_sum(2,coins_counter,sum,change,ticket_name_price_dictionary)
       k=[]
       lista_tmp=WrzuconeMonety.return_list()
       total =0
       for l in lista_tmp:
           k.append(l.get_value())
       for ele in range(0, len(k)):
           total = total + k[ele]  
       t1=ticket_price-float(total)
       self.assertEqual(t1,logic.sum_test_purposes)

    def test_expected_change(self):
         tmp_list2 = []
         tmp_list1 = []
         random_generated_list_of_coins_bills = [random.choice(logic.allowed_coins_bills) for x in
                                                                         range(100)]  # Randomowa lista nominalow znajdujacych sie w biletomacie
         Biletomat = logic.Money_Storage('PLN', tmp_list1)
         for i in random_generated_list_of_coins_bills:
              Biletomat.add_Coin_or_Bill(logic.Coin_Bill(i))
         coins_counter = IntVar()
         coins_counter.set(1)
         change = StringVar()
         change.set("0.00 zl")
         sum = StringVar()
         WrzuconeMonety = logic.Money_Storage('PLN', tmp_list2)
         Test_5_zlote=logic.Coin_Bill(5)
         WrzuconeMonety.add_Coin_or_Bill(Test_5_zlote)
         listanormalne, listaulgowe = logic.config()
         a,b,c,d,e,f = listaulgowe
         a.ticket_counter.set(1)
         ticket_price = a.ticket_counter.get()* logic.price_20_minutes/2
         sum.set(str(ticket_price)+" zl")
         #logic.Bilety_Ulgowe(listaulgowe)
         ticket_name_price_dictionary ={}
         for i in listaulgowe:
             ticket_name_price_dictionary[i.get_name()] = i.ticket_counter.get()
         flag, w =logic.returnChange(Biletomat, 3)

         self.assertTrue(w)

    def test_expected_return_monety(self):
       tmp_list2 = []
       tmp_list1 = []
       random_generated_list_of_coins_bills = [random.choice(logic.allowed_coins_bills) for x in
                                                                       range(0)]  # Randomowa lista nominalow znajdujacych sie w biletomacie
       Biletomat = logic.Money_Storage('PLN', tmp_list1)
       for i in random_generated_list_of_coins_bills:
            Biletomat.add_Coin_or_Bill(logic.Coin_Bill(i))
       coins_counter = IntVar()
       coins_counter.set(1)
       WrzuconeMonety = logic.Money_Storage('PLN', tmp_list2)
       Test_5_zlote=logic.Coin_Bill(5)
       WrzuconeMonety.add_Coin_or_Bill(Test_5_zlote)
       listanormalne, listaulgowe = logic.config()
       a,b,c,d,e,f = listaulgowe
       a.ticket_counter.set(1)
       ticket_price = a.ticket_counter.get()* logic.price_20_minutes/2
       logic.Bilety_Ulgowe(listaulgowe)
       ticket_name_price_dictionary ={}
       for i in listaulgowe:
           ticket_name_price_dictionary[i.get_name()] = i.ticket_counter.get()
       change_to_be_returned_bool, w =logic.returnChange(Biletomat, 3)
       if w == [] and change_to_be_returned_bool == False:
           l = WrzuconeMonety.return_list()
           for i in l:
               w.append(i.get_value())
       logic.finish(change_to_be_returned_bool, w,{})
       self.assertEqual(w[0],Test_5_zlote.get_value())

    def test_no_change_gr(self):
         tmp_list2 = []
         tmp_list1 = []
         coins_counter = IntVar()
         coins_counter.set(1)
         change = StringVar()
         change.set("0.00 zl")
         sum = StringVar()
         Biletomat = logic.Money_Storage('PLN', tmp_list1)
         WrzuconeMonety = logic.Money_Storage('PLN', tmp_list2)
         for i in range (200):
              WrzuconeMonety.add_Coin_or_Bill(logic.Coin_Bill(0.01))
         listanormalne, listaulgowe = logic.config()
         a,b,c,d,e,f = listaulgowe
         a.ticket_counter.set(1)
         ticket_price = a.ticket_counter.get()* logic.price_20_minutes/2
         sum.set(str(ticket_price)+" zl")
         logic.Bilety_Ulgowe(listaulgowe)
         ticket_name_price_dictionary ={}
         k=[]
         lista_tmp=WrzuconeMonety.return_list()
         total =0
         for l in lista_tmp:
             k.append(l.get_value())
         for ele in range(0, len(k)):
             total = total + k[ele]  
         t1=ticket_price-float(total)
         self.assertEqual(t1,logic.sum_test_purposes)

    def test_two_tickets(self):
        tmp_list1 = []
        tmp_list2 = []
        change = StringVar()
        change.set("0.00 zl")
        sum = StringVar()
        Biletomat = logic.Money_Storage('PLN', tmp_list1)
        WrzuconeMonety = logic.Money_Storage('PLN', tmp_list2) 
        WrzuconeMonety.add_Coin_or_Bill(logic.Coin_Bill(5))  
        listanormalne, listaulgowe = logic.config()
        a,b,c,d,e,f = listaulgowe
        a.ticket_counter.set(1)
        b.ticket_counter.set(1)
        ticket_price = a.ticket_counter.get()* logic.price_20_minutes/2 + b.ticket_counter.get()*logic.price_40_minutes/2 -2
        sum.set(str(ticket_price)+" zl")
        logic.Summary(listaulgowe, True)  
        k=[]
        lista_tmp=WrzuconeMonety.return_list()
        total =0
        for l in lista_tmp:
            k.append(l.get_value())
        for ele in range(0, len(k)):
            total = total + k[ele]
        t1=ticket_price-float(total)
        self.assertEqual(logic.sum_test_purposes ,ticket_price)


    def test_6(self):
          tmp_list2 = []
          tmp_list1 = []
          coins_counter = IntVar()
          coins_counter.set(1)
          change = StringVar()
          change.set("0.00 zl")
          sum = StringVar()
          Biletomat = logic.Money_Storage('PLN', tmp_list1)
          WrzuconeMonety = logic.Money_Storage('PLN', tmp_list2)

          WrzuconeMonety.add_Coin_or_Bill(logic.Coin_Bill(2))  
          listanormalne, listaulgowe = logic.config()
          a,b,c,d,e,f = listaulgowe
          a.ticket_counter.set(1)
          ticket_price = a.ticket_counter.get()* logic.price_20_minutes/2 #+ b.ticket_counter.get()*logic.price_40_minutes/2
          sum.set(str(ticket_price)+" zl")
          logic.Bilety_Ulgowe(listaulgowe)
          ticket_name_price_dictionary ={}
          for i in listaulgowe:
              ticket_name_price_dictionary[i.get_name()] = i.ticket_counter.get()
          a,b,c,d,e,f = listaulgowe
          flag, w =logic.returnChange(Biletomat, 0)
          logic.Summary(listaulgowe, True)  
          WrzuconeMonety.add_Coin_or_Bill(logic.Coin_Bill(5))
          b.ticket_counter.set(1)
          ticket_price = a.ticket_counter.get()* logic.price_20_minutes/2 + b.ticket_counter.get()*logic.price_40_minutes/2
          logic.Summary(listaulgowe, True)
          k=[]
          lista_tmp=WrzuconeMonety.return_list()
          total =0
          for l in lista_tmp:
              k.append(l.get_value())
          for ele in range(0, len(k)):
              total = total + k[ele]  
          t1=ticket_price-float(total)
          self.assertEqual(logic.sum_test_purposes,ticket_price)  
    def test_7(self):
        tmp_list2 = []
        tmp_list1 = []
        coins_counter = IntVar()
        coins_counter.set(-1.5)
        change = StringVar()
        change.set("0.00 zl")
        sum = StringVar()
        Biletomat = logic.Money_Storage('PLN', tmp_list1)
        WrzuconeMonety = logic.Money_Storage('PLN', tmp_list2)

        WrzuconeMonety.add_Coin_or_Bill(logic.Coin_Bill(2))  
        listanormalne, listaulgowe = logic.config()
        a,b,c,d,e,f = listaulgowe
        a.ticket_counter.set(1)
        ticket_price = a.ticket_counter.get()* logic.price_20_minutes/2 #+ b.ticket_counter.get()*logic.price_40_minutes/2
        sum.set(str(ticket_price)+" zl")

        self.assertRaises(logic.NiepoprawnaIloscMonetException, logic.Refresh_sum,2,coins_counter,sum,change,{})        