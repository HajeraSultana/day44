import random

my2DList = []

def ran():
    number = random.randint(1,90)
    return number

num = []
for i in range(8):
    num.append(ran())

my2DList = [[num[0], num[1], num[2]],[num[3], "BINGO", num[4]], [num[5], num[6], num[7]]]

def prettyprint():
    for row in my2DList:
        for values in row:
            print(f"{values:^10}", end=" | ")
        print()



print ("David's Nan's Bingo Card Generator")
print()
prettyprint()
exces = 0
while True:
    print()
    userGuess = int(input("What number was called? "))

    for row in range(3):
        for values in range(3):
            if my2DList [row][values] == userGuess:
                my2DList [row][values] = "X" 
                exces +=1
                
    if exces == 8:
        print("You have won!")
        break
    prettyprint()   



