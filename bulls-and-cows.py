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
                print("Incorrect input. Please enter a number which has 4 different digits and excludes 0!")
                continue
            break
        except ValueError:
            print("Incorrect input. Please enter a number which has 4 different digits and excludes 0!")
    return number

def countBullsAndCows(userNum, compNum):
    userNum = str(userNum)
    compNum = str(compNum)
    numBulls=0
    numCows=0
    for i in range(4):
        if userNum[i] == compNum[i]:
            numBulls+=1
    for i in range(4):
        for j in range(4):
            if userNum[i]==compNum[j]:
                numCows+=1
    numCows -= numBulls
    print("There are {} Bull(s) and {} Cow(s) in your number.\n".format(numBulls, numCows))

def play():
    print("Hey!\nThis is the game Bulls and Cows!\n")
    compNum = computerNum()
    rounds = 0
    while True:
        rounds+=1
        print("Round {:n}. ".format(rounds), end=" ")
        userNum = userInput()
        if userNum==compNum:
            break
        countBullsAndCows(userNum, compNum)
    print("\nCongrats!!!\nYou guessed the number correctly in {:n} attempts.".format(rounds))

play()