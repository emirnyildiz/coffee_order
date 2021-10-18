#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 23:41:00 2021

@author: seymayilmaz
"""

spider = ' ||  || ' + '\n' + ' \\\\()// ' + '\n' + '//(__)\\\\' + '\n' + '||    ||'

espresso_s = 8.75
espresso_d = 9.75
latte_s = 11.50
latte_m = 13.25
latte_l = 14.75
mocha_s = 13.50
mocha_m = 15.50
mocha_l = 18.75

print("What would you like to drink?")
while True:    
    coffee_name = input("Coffee Name:")    
    if coffee_name == "espresso" or coffee_name == "Espresso":        
        print("These are the size options: single or double.")
        coffee_size = input("Coffee size:")       
        if coffee_size == "single":                   
            print("Price: {} TL".format(round(espresso_s,2)))           
            price = espresso_s              
        elif coffee_size == "double":            
            print("Price: {} TL".format(round(espresso_d,2)))            
            price = espresso_d            
        else:            
            print("İnvalid value")            
            break        
        print("""The payment method options are:
    1)cash
    2)credit card
    3)debit card""")        
        payment_method = int(input("Please enter your payment method:"))        
        if payment_method == 1:
            price = price*0.95            
            print("That will be {} TL in total. Thank you.".format(round(price,2)))        
        elif payment_method == 2 or payment_method == 3:           
            print("That will be {} TL in total. Thank you.".format(price))            
        else:
            print("invalid option ")
    elif coffee_name == "Latte" or coffee_name == "latte":        
        print("""These are the size options: S M L
Please write in capital letters.""")        
        coffee_size = input("Coffee size:")    
        if coffee_size == "S":
            print("Price: {} TL".format(round(latte_s,2)))            
            price = latte_s        
        elif coffee_size == "M":            
            print("Price: {} TL".format(round(latte_m,2)))            
            price = latte_m        
        elif coffee_size == "L":            
            print("Price: {} TL".format(round(latte_l,2)))            
            price = latte_l            
        else:            
            print("İnvalid value")            
            break        
        print("""The payment method options are:
    1)cash
    2)credit card
    3)debit card""")        
        payment_method = int(input("Please enter your payment method:"))        
        if payment_method == 1:
            price = price*0.95            
            print("That will be {} TL in total. Thank you.".format(round(price,2)))        
        elif payment_method == 2 or payment_method == 3:          
            print("That will be {} TL in total. Thank you.".format(price))           
        else:
            print("invalid option ")        
    elif coffee_name == "Mocha" or coffee_name == "mocha":        
        print("""These are the size options: S M L
Please write in capital letters.""")
        coffee_size = input("Coffee size:")        
        if coffee_size == "S":
            print("Price: {} TL".format(round(mocha_s,2)))        
            price = mocha_s       
        elif coffee_size == "M":            
            print("Price: {} TL".format(round(mocha_m,2)))            
            price = mocha_m       
        elif coffee_size == "L":            
            print("Price: {} TL".format(round(mocha_l,2)))           
            price = mocha_l           
        else:            
            print("İnvalid value")            
            break       
        print("""The payment method options are:
    1)cash
    2)credit card
    3)debit card""")        
        payment_method = int(input("Please enter your payment method:"))        
        if payment_method == 1:
            price = price*0.95            
            print("That will be {} TL in total. Thank you.".format(round(price,2)))        
        elif payment_method == 2 or payment_method == 3:           
            print("That will be {} TL in total. Thank you.".format(price))            
        else:
            print("invalid option ")   
    elif coffee_name == "q":        
        print("System closed.")
        break   
    else:       
        print("Sorry, this drink is not available.")    
    print(spider)
        
        
    
