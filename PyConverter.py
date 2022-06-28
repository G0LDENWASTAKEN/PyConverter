#imports
import time
import random
from random import randint

time.sleep(1)
print('''
██████╗░██╗░░░██╗████████╗██╗░░██╗░█████╗░███╗░░██╗
██╔══██╗╚██╗░██╔╝╚══██╔══╝██║░░██║██╔══██╗████╗░██║
██████╔╝░╚████╔╝░░░░██║░░░███████║██║░░██║██╔██╗██║
██╔═══╝░░░╚██╔╝░░░░░██║░░░██╔══██║██║░░██║██║╚████║
██║░░░░░░░░██║░░░░░░██║░░░██║░░██║╚█████╔╝██║░╚███║
╚═╝░░░░░░░░╚═╝░░░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚══╝

░█████╗░░█████╗░███╗░░██╗██╗░░░██╗███████╗██████╗░████████╗███████╗██████╗░
██╔══██╗██╔══██╗████╗░██║██║░░░██║██╔════╝██╔══██╗╚══██╔══╝██╔════╝██╔══██╗
██║░░╚═╝██║░░██║██╔██╗██║╚██╗░██╔╝█████╗░░██████╔╝░░░██║░░░█████╗░░██████╔╝
██║░░██╗██║░░██║██║╚████║░╚████╔╝░██╔══╝░░██╔══██╗░░░██║░░░██╔══╝░░██╔══██╗
╚█████╔╝╚█████╔╝██║░╚███║░░╚██╔╝░░███████╗██║░░██║░░░██║░░░███████╗██║░░██║
░╚════╝░░╚════╝░╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝
''')

time.sleep(1)
print("Here is a list of things you can convert:")
time.sleep(0.5)


#defines different conversions so user can choose
answer1 = print("1. Bianary to Decimal")
answer2 = print("2. Decimal to Bianary")
answer3 = print("3. Decimal to Hexadecimal")
answer4 = print("4. Hexadecimal to Decimal")
answer5 = print("5. Binary to Hexadecimal")
answer6 = print("6. Hexadecimal to Binary")

time.sleep(0.5)
print()
print()
question = input("Enter the number corresponding to the conversion you would like: ")


if question == ("1"):
    b_num = list(input("Input a binary number: "))
    value = 0
    time.sleep(0.5)
    print()
    print("Calculating...")
    print()
    time.sleep(random.randint(1, 5,))
    for i in range(len(b_num)):
            digit = b_num.pop()
            if digit == '1':
                    value = value + pow(2, i)
    print("The decimal value of the number is: ", value)
    
    time.sleep(1)
    print()
    print("Program will now exit")
    print(".")
    time.sleep(0.25)
    print(".")
    time.sleep(0.4)
    print(".")
    time.sleep(0.7)
    print(".")
    time.sleep(3)
    exit()




if question == ("2"):
    #get input and initialize variables
    decimal = int(input("Enter a decimal number: "))
    binary = 0
    ctr = 0
    temp = decimal  #copy input decimal

    #find binary value using while loop
    while(temp > 0):
        binary = ((temp%2)*(10**ctr)) + binary
        temp = int(temp/2)
        ctr += 1
        time.sleep(0.5)
    print()
    print("Calculating...")
    print()
    time.sleep(random.randint(1, 5,))
    #output the result       
    print("Binary of {x} is: {y}".format(x=decimal,y=binary))

    time.sleep(1)
    print()
    print("Program will now exit")
    print(".")
    time.sleep(0.25)
    print(".")
    time.sleep(0.4)
    print(".")
    time.sleep(0.7)
    print(".")
    time.sleep(3)
    exit()

if question == ("3"):
    
    conversion_table = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A' , 'B', 'C', 'D', 'E', 'F']

    decimal = int(input("Enter your decimal number: "))
    hexadecimal = ''

    while(decimal>0):
        remainder = decimal%16
        hexadecimal = conversion_table[remainder]+ hexadecimal
        decimal = decimal//16
    time.sleep(0.5)
    print()
    print("Calculating...")
    print()
    time.sleep(random.randint(1, 5,))
    print("The Hexadecimal of", decimal, "is:",hexadecimal)
    
    time.sleep(1)
    print()
    print("Program will now exit")
    print(".")
    time.sleep(0.25)
    print(".")
    time.sleep(0.4)
    print(".")
    time.sleep(0.7)
    print(".")
    time.sleep(3)
    exit()



if question == ("4"):
    # Creating the Dictionary  
    dictionary_hexa_to_decimal = {'0': 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9, 'A' : 10 , 'B' : 11, 'C' : 12, 'D' : 13, 'E' : 14, 'F' : 15}  
    hexadecimal_string = input("Please enter the hexadecimal value: ").strip().upper()  
    decimal = 0  
  
    length = len(hexadecimal_string) -1  
   
    for digit in hexadecimal_string:  
        decimal += dictionary_hexa_to_decimal[digit]*16**length  
        length -= 1  
    time.sleep(0.5)
    print()
    print("Calculating...")
    print()
    time.sleep(random.randint(1, 5,))
    print ("The converted hexadecimal to decimal is: ", decimal)
    
    time.sleep(1)
    print()
    print("Program will now exit")
    print(".")
    time.sleep(0.25)
    print(".")
    time.sleep(0.4)
    print(".")
    time.sleep(0.7)
    print(".")
    time.sleep(3)
    exit()


if question == ("5"):
    binary_string = input('Input your Binary code: ')

    decimal_representation = int(binary_string, 2)
    hexadecimal_string = hex(decimal_representation)
    time.sleep(0.5)
    print()
    print("Calculating...")
    print()
    time.sleep(random.randint(1, 5,))
    print("Your converted Bianary to Hexadecimal is: ", hexadecimal_string)

    time.sleep(1)
    print()
    print("Program will now exit")
    print(".")
    time.sleep(0.25)
    print(".")
    time.sleep(0.4)
    print(".")
    time.sleep(0.7)
    print(".")
    time.sleep(3)
    exit()


if question == ("6"):
    print()
    time.sleep(1)
    print("This part of the project has not finished yet! Please try again later!")
    time.sleep(5)
    exit()

else:
    print()
    time.sleep(1)
    print("Invalid number!")
    time.sleep(1)
    exit()
