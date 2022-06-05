def diffDigits(number):
    number = str(number)
    for i in range(len(number)-1):
        for j in range(i+1,len(number)):
            if number[i]==number[j]:
                return False
    return True