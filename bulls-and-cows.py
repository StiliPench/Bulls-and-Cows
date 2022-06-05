import random

def diffDigits(number):
    number = str(number)
    for i in range(len(number)-1):
        for j in range(i+1,len(number)):
            if number[i]==number[j]:
                return False
    return True

def hasZero(number):
    number = str(number)
    for i in number:
        if i=="0":
            return True
    return False

def computerNum():
    number = None;
    while True:
        number = random.randint(1234, 9876)
        if diffDigits(number) and not(hasZero(number)):
            return number

def userInput():
    while True:
        try:
            number = int(input("Enter a number: "))
            if(hasZero(number) or not(diffDigits(number)) or number<1234 or number>9876):
                print("Incorrect input. Please enter a number which has 4 different digits excluding 0!")
                continue
            break
        except ValueError:
            print("Incorrect input. Please enter a number which has 4 different digits excluding 0!")
    return number
