import random2
s = 0
b = 3
x = 0
l = 0
c = 20
Coins = 0
u = 100
while l == 0:
    x = 0
    print "Choose Game Mode:\nPress:\n1 - Easy Mode\n2 - Normal Mode\n3 - Difficult Mode\n4 - Super Difficult Mode\n5 - Impossibe Mode\n6 - Custom Mode"
    m = int(raw_input("Choose Mode: "))
    print(chr(27) + "[2J")
    if m == 1:
        u = 50
    elif m == 2:
        u = 100
    elif m == 3:
        u = 150
    elif m == 4:
        u = 200
    elif m == 5:
        u = 1000000000000
    elif m == 6:
        ctm = int(raw_input("Choose a Number, in the random range 1 until: "))
        u = ctm
    else:
        print "Im don't understand, your game mode is Normal Mode"
        u = 100
    if Coins > c or Coins == c:
        yon = int(raw_input("Do You Want To Buy More Trials With Your Coins?\nPress:\n1 - Yes\n2 - No\nChoose: "))
        print(chr(27) + "[2J")
        if yon == 1:
            print "You have ", Coins, " coins"
            print "One more trial cost: ", c, " coins, do you want to buy?\nPress:\n1 - buy\n2 - cancel"
            yon2 = int(raw_input("Choose: "))
            if yon2 == 1:
                if Coins > c or Coins == c:
                    Coins = Coins - c
                    b = b + 1
                elif Coins < c:
                    print "You don't have enoghf coins"
                else:
                    s = s + 1
            elif yon2 == 2:
                s = s + 1
            else:
                s = s + 1
    Ran = random2.randint(1, u)
    print "You have ", b, " trials, if you'll be right you'll get ", u / 10, "more coins.\nGood luck!"
    while x < b:
        print(chr(27) + "[2J")
        print "Trial: ", x + 1
        print "Coins: ", Coins
        Num = int(raw_input("Pick a number between 1 and %s : " % (u)))
        if Num == Ran:
            print "Wow! You Are Right!\nHow did you know that?"
            Coins = Coins + u / 10
            print "Now you have ", Coins, "coins!"
            x = 4
        elif Num > Ran:
            print " Your Number is bigger than the random number"
            x = x + 1
        elif Num < Ran:
            print " Your Number is smaller than the random number"
            x = x + 1
    if Num == Ran:
        print "You win!"
        print(chr(27) + "[2J")
    elif Num != Ran:
        print "You Lose...\nthe Number is: ", Ran
        print "Coins: ", Coins
