#!/bin/usr/python3
import requests,bs4


def super_lotto():
    lotto_list=[]

    page = requests.get('http://www.calottery.com/play/draw-games/superlotto-plus')
    page.raise_for_status()
    soup=bs4.BeautifulSoup(page.text,"lxml")

    for ultag in soup.find_all('ul', {'class': 'winning_number_sm'}):
        for litag in ultag.find_all('li'):
            lotto_list.append(litag.text)
    lotto_list = [int(i) for i in lotto_list]
    return lotto_list
   # print(lotto_list)


def mega_millions():
    lotto_list=[]

    page=requests.get('https://www.calottery.com/play/draw-games/mega-millions')
    page.raise_for_status()
    soup=bs4.BeautifulSoup(page.text,"lxml")

    for ultag in soup.find_all('ul', {'class': 'winning_number_sm'}):
        for litag in ultag.find_all('li'):
            lotto_list.append(litag.text)
    lotto_list = [int(i) for i in lotto_list]
    return lotto_list


def power_ball():
    lotto_list=[]

    page=requests.get('https://www.calottery.com/play/draw-games/powerball')
    page.raise_for_status()
    soup=bs4.BeautifulSoup(page.text,"lxml")

    for ultag in soup.find_all('ul', {'class': 'winning_number_sm'}):
        for litag in ultag.find_all('li'):
            lotto_list.append(litag.text)
    lotto_list = [int(i) for i in lotto_list]
    print(lotto_list)
    return lotto_list


def menu():
    print("\nWelcome to Lotto Checker!\n")
    print("1: Check Super Lotto")
    print("2: Check Mega Millions")
    print("3: Check PowerBall")
    print("4: Quit\n")
    return input("Choose a Selection\n")


def main():

    choice ="0"

    while choice is not "4":
        choice =menu()
        if choice =="1":
            lotto =super_lotto()
            if  not lotto:
                print("Results are not available yet try again later")
                continue
        elif choice == "2":
            lotto=mega_millions()
            if  not lotto:
                print("Results are not available yet try again later")
                continue
        elif choice == "3":
            lotto=power_ball()
            if  not lotto:
                print("Results are not available yet try again later")
                continue
        elif choice == "4":
            quit()
        else:
            print("You have entered an invalid selection try again\n")
            choice=menu()
        counter =0
        mega =0

        #print(lotto)
        print ("\nThe Lotto Numbers are " + str(lotto)[1:-1] )
        user = [0,0,0,0,0,0]


        def  no_duplicates(user,num):
            for x in range(0,6):

                if(user[x] == num):

                    return True


        for x in range(0,6):
            num_lotto="Lotto Number: "+str(x+1)+"\n"
            while True:
                try:
                    num =int(input(num_lotto))
                    break
                except ValueError:
                    print("Invalid number try again\n")


            while no_duplicates(user,num) is True:
                print(" You have already entered that number! please try again\n" )
                while True:
                    try:
                        num =int(input(num_lotto))
                        break
                    except ValueError:
                        print("Invalid number try again\n")


            user[x]=num


        for x in range(0,5):

                for y in range(0,5):
                    if lotto[x] == user[y]:
                        print(" You have a match! it was " + str(user[y]) + "\n")
                        y+=1
                        counter += 1
        if lotto[-1] == user[-1]:
            mega =1



        print("The lotto numbers are:\n")
        print (lotto)
        print("Your numbers are:")
        print(user)
        print("you had " + str(counter) + "  matches\n")
        if mega ==1:
            print("You had matched the mega!\n")


main()
