counter =0
lotto =[2, 23, 41, 53, 63, 11]
print ("The Lotto Numbers are " + str(lotto)[1:-1])
user = [0,0,0,0,0,0]


def  no_duplicates(user,num):
    for x in range(0,6):

      if(user[x] == num):

          return True


for x in range(0,6):
    while True:
        try:
            num =int(input("Lotto Number: \n"))
            break
        except ValueError:
            print("Invalid number try again\n")


    while no_duplicates(user,num) is True:
        print(" You have already entered that number! please try again" )
        while True:
            try:
                num =int(input("Lotto Number: \n"))
                break
            except ValueError:
                print("Invalid number try again\n")


    user[x]=num


for x in range(0,6):

        for y in range(0,6):
            if lotto[x] == user[y]:
                print(" You have a match! it was " + str(user[y]) )
                y+=1
                counter += 1

print("The lotto numbers are:")
print (lotto)
print("Your numbers are:")
print(user)
print("you had " + str(counter) + "  matches")
