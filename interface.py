# Import the required Libraries
from tkinter import *
import time
import os
import sys
from decimal import *
import copy
import random
import logic
window = Tk()
myfont = ("Rubik", 15)


def widget_forget():  # function to hide widgets
    for i in window.grid_slaves():
        i.grid_forget()



def wyswietlulgowe(list, tmp_list_tickets): #Display reduced tickets
    normalne = Button(window,
                      text="Bilety Normalne",
                      command=lambda: logic.Bilety_Normalne(tmp_list_tickets),
                      bg="#231697",
                      borderwidth=5,
                      relief="raised",
                      font=myfont,
                      fg="white",
                      activebackground='#3974BB',
                      ).grid(row=3, column=0, sticky="NSEW", padx=2, pady=20)
    platnosc = Button(window,
                      text="Platnosc",
                      command=lambda: logic.Summary(list, True),
                      bg="#231697",
                      borderwidth=5,
                      relief="raised",
                      font=myfont,
                      fg="white",
                      activebackground='#3974BB',
                      ).grid(row=3, column=1, sticky="NSEW", columnspan=3, padx=2, pady=20)




def wyswietnormalne(list, tmp_list_tickets): #Display normal tickets
    ulgowe = Button(window,
                    text="Bilety Ulgowe",
                    command=lambda: logic.Bilety_Ulgowe(tmp_list_tickets),
                    bg="#231697",
                    borderwidth=5,
                    relief="raised",
                    font=myfont,
                    fg="white",
                    activebackground='#3974BB',
                    ).grid(row=3, column=0, sticky="NSEW", padx=2, pady=20)
    Platnosc = Button(window,
                      text="Platnosc",
                      command=lambda: logic.Summary(list, False),
                      bg="#231697",
                      borderwidth=5,
                      relief="raised",
                      font=myfont,
                      fg="white",
                      activebackground='#3974BB',
                      ).grid(row=3, column=1, sticky="NSEW", columnspan=3, padx=2, pady=20)




def Start(listanormalne, listaulgowe): #Display buttons which allows end user to select which tickets he/she wants to choose
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
                                  command=lambda: logic.Bilety_Normalne(listanormalne),
                                  borderwidth=5,
                                  relief="raised",
                                  bg="#231697",
                                  font=myfont,
                                  fg="white",
                                  activebackground='#3974BB',
                                  ).grid(row=1, column=1, sticky="NSEW", padx=20, pady=35)
    button_halfprice_ticket = Button(window,
                                     text="Bilet Ulgowy",
                                     command=lambda: logic.Bilety_Ulgowe(listaulgowe),
                                     borderwidth=5,
                                     relief="raised",
                                     bg="#231697",
                                     font=myfont,
                                     fg="white",
                                     activebackground='#3974BB',
                                     ).grid(row=1, column=2, sticky="NSEW", padx=20, pady=35)





def display_coins(sum_string, change,dictionary,is_active="normal"): #Display coins
    coins_counter = IntVar()
    coins_counter.set(1)

    def onClick_addfun():
        coins_counter.set(coins_counter.get() + 1)

    def onClick_substract():
        if coins_counter.get() == 1:
            return
        coins_counter.set(coins_counter.get() - 1)

    i = 0
    for c in logic.allowed_coins_bills:  # Display coins/bills buttons
        if (i < 6):
            colnum = 3
            rownum = i + 1
        else:
            colnum = 5
            rownum = i - 5
        Button(window,
                text="Wrzuć " + str(c) + " zł",
                command=lambda c=c: logic.Refresh_sum(float(c), coins_counter, sum_string, change,dictionary),
                bg="#231697",
                borderwidth=5,
                relief="raised",
                font=myfont,
                fg="white",
                state=is_active,
                activebackground='#3974BB',
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
                          borderwidth=5,
                          bg="#231697",
                          font=myfont,
                          fg="white",
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


def Summary_display(sum_string, change,is_active="normal"):
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
                        command=lambda: Start(logic.listanormalne, logic.listaulgowe),
                        bg="#231697",
                        borderwidth=5,
                        relief="raised",
                        font=myfont,
                        fg="white",
                        state=is_active,
                        activebackground='#3974BB',
                        )
    add_ticket.grid(row=0, column=0, sticky="NSEW", padx=2, pady=20)
    add_ticket = Button(window,
                        text="Zacznij od nowa",
                        command=lambda: logic.Restart(),
                        bg="#231697",
                        borderwidth=5,
                        relief="raised",
                        font=myfont,
                        fg="white",
                        activebackground='#3974BB',
                        )
    add_ticket.grid(row=1, column=0, sticky="NSEW", padx=2, pady=20)


