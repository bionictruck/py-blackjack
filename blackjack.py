import random
import time
from decimal import Decimal

dealer = []
player = []
wallet = Decimal('100.00')
wager = 0

### Heart = u"\u2665")
### Spade = u"\u2660"
### Club = u"\u2663"
### Diamond = u"\u2666"

def bet():
    global wallet
    global wager
    if wallet <= 0:
        print("You're out of money! See you next time!")
        quit()
    else:
        print("You have $" + str(wallet) + " to play with.")
        wager = int(input("how much would you like to bet? $"))
        if wager > wallet:
            print("You don't have enough money! Enter a bet less than $" + str(wallet))
            bet()
        elif wager < 5:
            print("The table minimum is $5. Please bet more than $5")
            bet()
        else:
            play()

def play():
    global wallet
    global wager
    dealer.clear()
    player.clear()
    dealer.append(random.randrange(2, 12))
    dealer.append(random.randrange(2, 12))
    player.append(random.randrange(2, 12))
    player.append(random.randrange(2, 12))
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
        choice = input("Would you like to (H)it, (S)tand or (D)ouble Down? ")
        if choice.lower() == "h" or  choice.lower() == "hit":
            hit()
        elif choice.lower() == "s" or choice.lower() == "stand":
            print("You have chosen to stand.")
            time.sleep(1)
            computer()
        elif choice.lower() == "d" or choice.lower() == "double down":
            wager += wager
            player.append(random.randrange(2, 12))
            print("You doubled down, increasing your bet to $" + str(wager) + " and have a total of " + str(sum(player)))
            computer()

def hit():
    global wallet
    global wager
    print("You have chosen to hit.")
    time.sleep(1)
    player.append(random.randrange(2, 12))
    print("You have a total of " + str(sum(player)))
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

def computer():
    global wallet
    global wager
    print("The dealer has a total of " + str(sum(dealer)))
    time.sleep(2)
    if sum(dealer) < 17:
        print("The dealer takes a hit")
        dealer.append(random.randrange(2, 12))
        if sum(dealer) < 17:
            computer()
        elif sum(dealer) > 17 and sum(dealer) <= 21:
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

bet()