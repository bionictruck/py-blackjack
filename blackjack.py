import os
import random
import time
from decimal import Decimal

dealer = []
player = []
wallet = Decimal('100.00')
wager = 0

### Heart = u"\u2665"
### Spade = u"\u2660"
### Club = u"\u2663"
### Diamond = u"\u2666"

def bet():
    global wallet
    global wager
    os.system('clear')
    if wallet <= 0:
        print("You're out of money! See you next time!")
        quit()
    else:
        print("You have $" + str(wallet) + " to play with.")
        try:
            wager = Decimal(input("Place a bet between $5 and $" + str(wallet) + " $"))
        except Exception:
            print("Invalid entry. Please enter a bet between $5 and $" + str(wallet))
            time.sleep(2)
            bet()
        if wager < 5:
            print("You bet must be at least $5.")
            time.sleep(2)
            bet()
        elif wager > wallet:
            print("You don't have enough money! Enter a bet less than $" + str(wallet))
            time.sleep(2)
            bet()
        else:
            play()

def play():
    global wallet
    global wager
    os.system('clear')
    dealer.clear()
    player.clear()
    dealer.append(random.randrange(1, 11))
    dealer.append(random.randrange(1, 11))
    if dealer[0] == 1 and dealer[1] == 1:
        dealer[0] = 11
        dealer[1] = 1
    elif dealer[0] == 1:
        dealer[0] = 11
    elif dealer[1] == 1:
        dealer[1] = 11
    player.append(random.randrange(1, 11))
    player.append(random.randrange(1, 11))
    print("The dealer's upcard is " + str(dealer[0]))
    print("You have a total of " + str(sum(player)))
    if sum(dealer) == 21:
        print("The dealer has 21. BLACKJACK! Better luck next time.")
        wallet -= Decimal(wager)
        playagain()
    elif sum(player) == 21:
        print("You have 21. BLACKJACK!")
        wallet += Decimal((wager * 3 / 2))
        playagain()
    else:
        decision()

def decision():
    global wallet
    global wager
    choice = input("Would you like to (H)it, (S)tand or (D)ouble Down? ")
    if choice.lower() == "h" or  choice.lower() == "hit":
        hit()
    elif choice.lower() == "s" or choice.lower() == "stand":
        print("You have chosen to stand with " + str(sum(player)) + ".")
        time.sleep(1)
        computer()
    elif choice.lower() == "d" or choice.lower() == "double down":
        wager += wager
        player.append(random.randrange(1, 11))
        if player[-1] == 1:
            if (sum(player) + 10) <= 21:
                player[-1] = 11
                print("You doubled down, increasing your bet to $" + str(wager) + ".")
                print("You recieve an Ace and have a total of " + str(sum(player)) + ".")
                time.sleep(1)
                computer()
            else:
                player[-1] = 1
                print("You doubled down, increasing your bet to $" + str(wager) + ".")
                print("You receive an Ace and have a total of "  + str(sum(player)) + ".")
                time.sleep(1)
                computer()
        else:
            if sum(player) < 21:
                print("You doubled down, increasing your bet to $" + str(wager) + ".")
                print("You receive " + str(player[-1]) + " and have a total of " + str(sum(player)) + ".")
                time.sleep(1)
                computer()
            else:
                print("You receive " + str(player[-1]) + " and have a total of " + str(sum(player)) + ".")
                print("Sorry, you are over 21 and have busted.")
                wallet -= wager
                time.sleep(1)
                playagain()                                            

def hit():
    global wallet
    global wager
    print("You have chosen to hit.")
    time.sleep(1)
    player.append(random.randrange(1, 11))
    if player[-1] == 1:
        aces()
    print("You receive a " + str(player[-1]) + " and have a total of " + str(sum(player)))
    if sum(player) <= 21:
        print("The dealer's upcard is " + str(dealer[0]))
        choice = input("Would you like to (H)it or (S)tand? ")
        if choice.lower() == "h" or choice.lower() == "hit":
            hit()
        elif choice.lower() == "s" or choice.lower() == "stand":
            print("You have chosen to stand")
            computer()
    else:
        print("Sorry, you are over 21 and have busted.")
        wallet -= wager
        playagain()

def aces():
    ace = input("You recieved an Ace. Would you like the Ace to be a 1 or 11? Type O or E. ")
    if ace.lower() == "one" or ace.lower() == "o":
        print("You have a total of " + str(sum(player)))
        decision()
    elif ace.lower() == "eleven" or ace.lower() == "e":
        player[-1] = 11
        print("You have a total of " + str(sum(player)))
        decision()
    else:
        print("Invalid entry. Please use O or E.")
        time.sleep(1)
        aces()    

def computer():
    global wallet
    global wager
    print("The dealer has a total of " + str(sum(dealer)))
    time.sleep(2)
    if sum(dealer) < 17:
        dealer.append(random.randrange(1, 11))
        if dealer[-1] == 1:
            print("The dealer takes a hit and receives an Ace.")
            if (sum(dealer) + 10) <= 21:
                dealer[-1] = 11
                ("The dealer now has " + str(sum(dealer)))
                computer()
            else:
                ("The dealer now has " + str(sum(dealer)))
                computer()
        else:
            print("The dealer takes a hit receives a " + str(dealer[-1]))
            time.sleep(1)
            if sum(dealer) < 17:
                computer()
            elif sum(dealer) >= 17 and sum(dealer) <= 21:
                print("The dealer stands with " + str(sum(dealer)))
                time.sleep(1)
                result()
            else:
                print("The dealer has busted! You win!")
                wallet += wager
                playagain()
    elif sum(dealer) >= 17:
        print("The dealer stands with " + str(sum(dealer)))
        time.sleep(1)
        result()

def result():
    global wallet
    global wager
    print("The dealer has " + str(sum(dealer)))
    print("You have " + str(sum(player)))
    if sum(dealer) > sum(player):
        print("The dealer has won. Better luck next time.")
        wallet -= wager
        playagain()
    elif sum(dealer) < sum(player):
        print("You have won!")
        wallet += wager
        print("You now have $" + str(wallet))
        playagain()
    else:
        print("This hand is a push.")
        playagain()

def playagain():
    global wallet
    global wager
    replay = input("Would you like to play again? Y/N ")
    if replay.lower() == 'y' or replay.lower() == 'yes':
        bet()
    else:
        print("You finished with $" + str(wallet))
        print("See you next time!")
        quit()

bet()