import random
import time
import os
import threading
from pygame import mixer

money = 0
days_played = 0
today_money = 0

currency = 0
currency_lose = 3 # days you can hold onto your k₹ (k₹ is special currency) only for display? idk yet
current_price = 0
currency_wallet = []

timer = 2

sick = False
scam = False

#limits
explore_limit = 3
total_explores = 0

total_customers = 0 #to limit number of customers. this is how many player has that day
customer_limit = 3
served = 0
failed = 0
reputation = 15

#upgrades
moneyUp_u1 = False
fallback_u3 = False
today_u4 = False
alarm_u5 = False
antiScam_u8 = True

# events
irs_encounter = False
icecream_broken = False
disaster = False

event_happened = True


#demo mode
demo = True

#upgrades/prices
upgrade1 = "More money per customer served"
price1 = 100

upgrade2 = "More explore actions per day (from 3 to 10)"
price2 = 250

upgrade3 = "Fall back money ($20, you can buy more once you use it)"
price3 = 700

upgrade4 = "Online ad (+10 reputation)"
price4 = 1500

upgrade5 = "Burgler alarm"
price5 = 5000

upgrade6 = "k₹ hold +2 (allows you to hold onto your k₹ for 5 days)"
price6 = 5000

upgrade7 = "More time time to complete task (2 sec -> 3 sec)"
price7 = 500

upgrade8 = "Scam protection (-20% Chance of getting a scam email)"
price8 = 2000

upgrade9 = ""
price9 = 0

owned_display = "[OWNED]"
owned_upgrades = []

#mail alert system
checked_today = False

claimed_d10 = False

def new_mail():
    input("[ALERT] 1 new message")


#System
username = os.getlogin().upper()
clear = os.system('cls')

#mail subjects
sub0 = "Welcome to Your New Store!"
sub1 = "Congratulations on Your First Day!"
sub6 = "Almost a Week Down – Stay Sharp!"
sub10 = "Congrats on your first week! Also… Potassium?"

#messages
message_d0 = (f"""
To: {username}
From: HANK
Subject: {sub0}

Hey there, Manager! 👋

Congratulations on taking over your very own store! I'm here to make sure you don't mess this up too badly. Let's get you started:

1. Your Goal:
Make money, serve customers, and grow your reputation.
Keep your balance above $0 — bankruptcy is a real bummer.

2. Your Actions:
Serve Tasks: Type customer orders exactly as they come in. Get it right before the timer runs out, and you earn cash + reputation. Mess it up, and they leave a bad review!
You can perform this action by typing "task"
Explore: Search your store for extra cash lying around. Limited per day, so use wisely.
You can perform this action by typing "explore"
Shop Upgrades: Spend money to improve your store! Some upgrades give more cash, extra explores, or even reputation boosts.
You can view the shop by typing "shop"

3. Daily Limits:
You can only serve a certain number of customers per day. Plan your actions strategically.
Explore is limited, so don't waste it.

4. Tracking Your Progress
Press [ENTER] anytime to see your current balance and days played.
Upgrades purchased are displayed after leaving the shop.

5. Quick Tips
Pay attention to the timer during tasks — it's ruthless.
Sometimes taking a risk can pay off big… or cost you everything.
Reputation matters! Happy customers = more opportunities.

To view the list of commands type "help"

That's it for now! Stay sharp, and remember: a well-managed store makes a happy manager. 😎

-HANK
              """)

message_d1 = (f"""
To: {username}
From: HANK
Subject: {sub1}

Hey there, Manager! 👋

You made it through your first day — not too shabby! I hope you didn't spill any coffee… at least not on the customers. 😏
Now that you've got the hang of serving, let's talk upgrades. 
Your first upgrade is:

“More Money Per Customer Served”
Every customer you serve now earns you extra cash automatically.
The more customers you serve in a day, the faster your balance grows.
This upgrade is permanent, so invest in it early to boost your profits!
To get your hands on this upgrade you can go into the shop and cough up 100 bucks.
Keep an eye on your balance and reputation — they're your lifelines. The better you do, the more opportunities open up, and the more upgrades you can buy.

Keep grinding, Manager! Tomorrow brings new challenges… and more ways to earn.

-HANK
              """)

message_d6 = (f"""
To: {username}
From: HANK
Subject: {sub6}

Hey Manager,

Wow — you’re almost a full week into running your store! Not bad at all. Keep it up! 👏
I wanted to drop a quick note about your second upgrade:

“More Explore Actions Per Day”
Normally, you’re limited in how many times you can search your store for extra cash each day.
This upgrade increases your daily explore limit, letting you find more hidden coins and tips.
More explores = more cash = more chances to invest in bigger upgrades.

Also, heads-up: every 7 days, something unexpected can happen. It might be taxes, a robbery, or some other event that affects your store’s money or reputation. I won’t spoil the details… but just be careful and save some cash for emergencies.
You’ve done well so far. Almost a week, almost a pro — just don’t get too cocky!
I'll see you on day 10 for some important news!

-HANK
              """)
message_d10 = (f"""
To: {username}
From: HANK
Subject: {sub10}

Hey there,

Well, look at you — over a week in business! Most new shop owners crash and burn by day three, but you’re still here, standing behind that counter like a pro. I’m impressed.
Now that you’ve proven you can keep the lights on, it’s time to start thinking about security and investment.


Let’s start with that third upgrade you might’ve seen in the shop — the fallback money.
Think of it as an emergency cushion. If you ever run your balance into the ground, that upgrade will automatically bail you out with $20, keeping you from losing everything. It’s a lifesaver — literally. 
You can even buy it again after it’s used up. Consider it your “break glass in case of bankruptcy” plan.

Business has been booming lately, huh? Word’s gotten around, and now the big leagues are startin’ to notice. 
You’ll start gettin’ emails from companies lookin’ to sponsor your shop, offerin’ deals and partnerships that could really boost your profits. 
But watch yourself — not all of ’em are the real deal. Some folks out there are just tryin’ to scam honest workers like you. If you’re not careful, you could end up losin’ more than you gain. 
I'm sure that their is an upgrade you can buy to help filter out the fakes, but even with that, you’ll still need to use your gut and figure out which messages are genuine and which ones smell fishy.

Now, about something new floating around town — Potassium (k₹).
It’s this new kind of digital currency people are calling “the future of finance.” It’s like the stock market, but with memes and caffeine. The value goes up and down faster than a customer’s mood when you mess up their latte. Some folks made a fortune, others… not so much.
You’ll be able to mess with it soon enough. Just remember: real money keeps your shop alive — Potassium’s more of a gamble.
You can visit the potassium market by typing "k"

Now, before you go diving headfirst into the Potassium craze, there’s a few things you should know. You can buy k₹ using your real money, and there’s no safety net like there is in the shop. If you spend everything 
chasing profits, you can go bankrupt — and the system won’t stop you. Each day, the value of Potassium 
shifts — sometimes it skyrockets, sometimes it tanks — so your goal is to buy low and sell high before the market turns on you. But here’s the kicker: you can only hold onto Potassium for three days before it 
expires and vanishes into thin air. There’s an upgrade later that extends that to five days, but until then, timing is everything. You can buy as much as you want, but be smart — one bad gamble, and you’ll be 
serving coffee out of a cardboard box.

Anyway, congrats again on making it this far. You’re doing better than most. Keep that momentum going — the real challenges start now. 
Below I've attached 5k₹ to help you get started, use it wisely!

Oh! Before I forget, the event that happened earlier, it's going to get alot harder as time goes on, so keep that in mind. Good luck on finishing your second week!

– HANK
              """)




#music
mixer.init()

def main_music():
    try:
        mixer.music.unpause()
    except:
        mixer.music.load(r"C:\Users\toadc\OneDrive\Music\Euphoria - Dyalla.mp3") #change later
        mixer.music.play(-1)
def shop_music():
    mixer.music.pause()         #https://stackoverflow.com/questions/20021457/playing-mp3-song-on-python
    pass
def minigame_music(): #for task
    mixer.music.pause()

#sounds
def day_end_sound():
    pass
def balance_sound():
    pass
def task_win_sound():
    pass
def task_lose_sound():
    pass
def money_lose_sound():
    pass
def money_gain_sound():
    pass



def update_currency():
    global currency_wallet, currency
    currency = sum(amount for amount, _ in currency_wallet)

def add_currency(add_amount):
    currency_wallet.append((int(add_amount), days_played))

def update_customerlim():
    global customer_limit, reputation

    if reputation < 0:
        reputation = 0

    div_rep = reputation / 5

    if div_rep.is_integer():
        customer_limit = div_rep
    elif div_rep <= 0:
        customer_limit = 1

def sick_days_check():
    global sick
    sick_num_check = random.randint(0, 1000)
    if sick_num_check > 950:
        sick = True
    else:
        sick = False

def scam_mail():
    global username
    scam_messages = [
        f"""
To: {username}
From: {review}@gmail.com
Subject:  Sponsorship offer

Hey!

This is Alan from {review}, my company was wondering if you would like to accept a sponsorship from us!
You've shown us your skills in store owning, and thought that if you were willing to accept our sponsorship
        """
    ]
    

print("Welcome to:")
def intro_page():
    print(r"""
░██████╗████████╗░█████╗░██████╗░███████╗  ████████╗██╗░░░██╗░█████╗░░█████╗░░█████╗░███╗░░██╗
██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██╔════╝  ╚══██╔══╝╚██╗░██╔╝██╔══██╗██╔══██╗██╔══██╗████╗░██║
╚█████╗░░░░██║░░░██║░░██║██████╔╝█████╗░░  ░░░██║░░░░╚████╔╝░██║░░╚═╝██║░░██║██║░░██║██╔██╗██║
░╚═══██╗░░░██║░░░██║░░██║██╔══██╗██╔══╝░░  ░░░██║░░░░░╚██╔╝░░██║░░██╗██║░░██║██║░░██║██║╚████║
██████╔╝░░░██║░░░╚█████╔╝██║░░██║███████╗  ░░░██║░░░░░░██║░░░╚█████╔╝╚█████╔╝╚█████╔╝██║░╚███║
╚═════╝░░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚══════╝  ░░░╚═╝░░░░░░╚═╝░░░░╚════╝░░╚════╝░░╚════╝░╚═╝░░╚══╝""")
    if demo:
        print("""
██████╗░███████╗███╗░░░███╗░█████╗░
██╔══██╗██╔════╝████╗░████║██╔══██╗
██║░░██║█████╗░░██╔████╔██║██║░░██║
██║░░██║██╔══╝░░██║╚██╔╝██║██║░░██║
██████╔╝███████╗██║░╚═╝░██║╚█████╔╝
╚═════╝░╚══════╝╚═╝░░░░░╚═╝░╚════╝░
              """)
    if not demo:
        print("")
    if days_played == 1 or days_played == 6 or days_played == 10 or scam:
        print("You have mail!")

intro_page()
print('To view your current balance press [ENTER]')
print('For help, type "help"')

if days_played == 0:
    print('\nTo get started type "mail"')


def balance():
    update_currency()
    print("------------------------------")
    print(f"Current Balance: ${money}")
    print(f"Days Played: {days_played}")
    if days_played >= 10:
        print(f"Potassium: {currency}k₹")
    print("------------------------------")

def help():
    print("""

█░█ █▀▀ █░░ █▀█
█▀█ ██▄ █▄▄ █▀▀
          """)
    print(f"""
List of commands:
    1. "help"
          opens this screen
    2. [ENTER]
          shows your balance and days played
    3. "explore"
          look around your store for money
    4. "task"
          serve a customer
    5. "mail"
          view your inbox
    6. "exit"
          closes your shop. make sure you save before doing this!
    7. "done"
          advances you to the next day. you can't go back, so make sure you have done everything you wanted to!
    8. "options"
          opens the configuration menu
    9. "shop"
          opens the shop where you can purchase upgrades and collectibles""")
    if days_played >= 10:
        print(f"""
    10. "k"
          opens the potassium market where you can buy and sell k₹. The price refreshes each day, 
          however, you can only hold on to shares for {currency_lose} days. 
          """)
def explore():
    print("You look around your store for spare change that customers may have left...")
    
    amounts = [0, 5, 1, 4, 9, 2, 1, 3, 5, 5, 5, 5, 5, 5, 7, 6, 8, 2, 2, 2, 2, 4, 3, 0, 0, 0, 0, 0]
    found_money = random.choice(amounts)
    time.sleep(2)
    if found_money == 0:
        print("You didn't find anything...")
    else:
        print(f"You found ${found_money}! Your current balance has been updated.")
        global money
        money += found_money
        global today_money
        today_money += found_money
        global total_explores
        total_explores += 1
    
#shop function
def shop():
    print("""
          
█▀ █░█ █▀█ █▀█
▄█ █▀█ █▄█ █▀▀
          """)
    print("Welcome to the shop! Here you can purchase upgrades for your store!\n")
    global today_u4
    #display logic
    if upgrade1 not in owned_upgrades:
        print(f"1. {upgrade1} - ${price1}")
    else:
        print(f"1. {owned_display}")
    if upgrade2 not in owned_upgrades:
        print(f"2. {upgrade2} - ${price2}")
    else:
        print(f"2. {owned_display}")
    if upgrade3 not in owned_upgrades:
        print(f"3. {upgrade3} - ${price3}")
    else:
        print(f"3. {owned_display}")
    if upgrade4 not in owned_upgrades and not today_u4:
        print(f"4. {upgrade4} - ${price4}")
    elif today_u4:
        print(f"4. {owned_display}")
    else:
        print(f"4. {owned_display}")
    if upgrade5 not in owned_upgrades:
        print(f"5. {upgrade5} - ${price5}")
    else:
        print(f"5. {owned_display}")
    if upgrade6 not in owned_upgrades and days_played >= 10:
        print(f"6. {upgrade6} - ${price6}")
    elif days_played < 10 and upgrade6 not in owned_upgrades:
        print("6. [LOCKED]")
    else:
        print(f"6. {owned_display}")
    if upgrade7 not in owned_upgrades:
        print(f"7. {upgrade7} - ${price7}")
    else:
        print(f"7. {owned_display}")
    if upgrade8 not in owned_upgrades and days_played >= 10:
        print(f"8. {upgrade8} - ${price8}")
    elif upgrade8 not in owned_upgrades and days_played < 10:
        print("8. [LOCKED]")
    else:
        print(f"8. {owned_display}")
    
    
    #purchase stuff
    shop_user = input("Enter the number of the item you want to buy: ")
    global money
    if shop_user == "1":
        if money >= price1 and upgrade1 not in owned_upgrades:
            money -= price1
            print(f"Purchased: {upgrade1}")
            owned_upgrades.append(upgrade1)
        elif upgrade1 in owned_upgrades:
            print("You already own this!")
        else:
            print("Insufficient funds")
    elif shop_user == "2":
        if money >= price2 and upgrade2 not in owned_upgrades: 
            money -= price2
            print(f"Purchased: {upgrade2}")
            owned_upgrades.append(upgrade2)
        elif upgrade2 in owned_upgrades:
            print("You already own this!")
        else:
            print("Insufficient funds")
    elif shop_user == "3":
        if money >= price3 and upgrade3 not in owned_upgrades:
            money -= price3
            print(f"Purchased: {upgrade3}")
            owned_upgrades.append(upgrade3)
        elif upgrade3 in owned_upgrades:
            print("You already own this!")
        else:
            print("Insufficient funds")
    elif shop_user == "4":
        if money >= price4 and upgrade4 not in owned_upgrades and not today_u4:
            money -= price4
            print(f"Purchased: {upgrade4}")
            owned_upgrades.append(upgrade4)
            today_u4 = True
        elif upgrade4 in owned_upgrades:
            print("You already own this!")
        elif today_u4:
            print("You may not purchase this upgrade again today.")
        else:
            print("Insufficient funds")
    elif shop_user == "5":
        if money >= price5 and upgrade5 not in owned_upgrades: 
            money -= price5
            print(f"Purchased: {upgrade5}")
            owned_upgrades.append(upgrade5)
        elif upgrade5 in owned_upgrades:
            print("You already own this!")
        else:
            print("Insufficient funds")
    elif shop_user == "6":
        if money >= price6 and upgrade6 not in owned_upgrades and days_played >= 10: 
            money -= price6
            print(f"Purchased: {upgrade6}")
            owned_upgrades.append(upgrade6)
        elif upgrade6 in owned_upgrades and days_played >= 10:
            print("You already own this!")
        elif upgrade6 not in owned_upgrades and days_played < 10:
            print("This item is currently locked, come back later and it might be unlocked")
        else:
            print("Insufficient funds")
    elif shop_user == "7":
        if money >= price7 and upgrade7 not in owned_upgrades: 
            money -= price7
            print(f"Purchased: {upgrade7}")
            owned_upgrades.append(upgrade7)
        elif upgrade7 in owned_upgrades:
            print("You already own this!")
        else:
            print("Insufficient funds")
    elif shop_user == "8":
        if money >= price8 and upgrade8 not in owned_upgrades and days_played >= 10:
            money -= price8
            print(f"Puchased: {upgrade8}")
            owned_upgrades.append(upgrade8)
        elif upgrade8 in owned_upgrades and days_played >= 10:
            print("You already own this!")
        elif upgrade8 not in owned_upgrades and days_played < 10:
            print("This item is currently locked, come back later and it might be unlocked")
        else:
            print("Insufficient funds")
        
    print(f"Owned Upgrades: {', '.join(owned_upgrades) if owned_upgrades else 'None'}")
    print("----------")


#day end summary
def day_end():
    print("""
          
█▀ █░█ █▀▄▀█ █▀▄▀█ ▄▀█ █▀█ █▄█
▄█ █▄█ █░▀░█ █░▀░█ █▀█ █▀▄ ░█░
          """)
    global days_played, current_price, past_price, currency_wallet, event_happened, sick
    update_currency()
    print("\n"
        f"Today's Revenue: ${today_money}\n"
        f"Current Balance: ${money}")
    if days_played >= 10:
        print(f"Potassium: {currency}k₹")
    if total_customers > 0:
        print(f"Customers Served: {served}/{total_customers}\n"
        f"Customers Lost: {failed}/{total_customers}\n")
    if not demo:
        print(f"Customer Limit: {customer_limit}")
        print(f"Reputation: {reputation}")
    print(f"Times Explored: {total_explores}/{explore_limit}")
    print("Preparing for next shift.", end= "\r")
    
    days_played += 1
    event_test = days_played / 7
    
    past_price = current_price
    current_price = random.randint(199, 999)
    currency_wallet = [(amount, day_bought) for amount, day_bought in currency_wallet if days_played - day_bought < currency_lose]
    

    time.sleep(1)
    print("Preparing for next shift..", end="\r")
    time.sleep(1)
    print("Preparing for next shift...", end="\r")
    time.sleep(1)
    print("Preparing for next shift....", end="\r")
    time.sleep(1)
    print("Preparing for next shift.....", end="\r")
    time.sleep(1)
    os.system('cls')

    update_customerlim()

    intro_page()

    if event_test.is_integer():
        event_happened = False
        events()
    
        
            
        
    

    
def events():
    print("""

█▀▀ █░█ █▀▀ █▄░█ ▀█▀
██▄ ▀▄▀ ██▄ █░▀█ ░█░
        """)
    e1 = "A burglar broke into your shop last night"
    e2 = "Your neighbor has informed you that the IRS is coming around collecting taxes"
    e3 = "A news channel desides to interview you"
    e4 = "You wake up to find the the ice cream machine is broken!"
    e5 = "A natural disaster has struck your town."

    global event_loss, event_happened, icecream_broken, irs_encounter
    if days_played >= 14:
        event_loss = random.randint(50, 400)
    else:
        event_loss = random.randint(25, 100)


    #e1 protection
    global alarm_u5, irs_encounter, money, reputation
    chosen_event = random.choice([e1, e2, e3, e4, e5])
    if chosen_event == e1 and alarm_u5:
        print(e1)
        print("Thankfully they were caught before you could \nlose anything thanks to your top of the line alarm system!")
        event_happened = True
    elif chosen_event == e1 and not alarm_u5:
        print(e1)
        print(f"They got away with ${event_loss}")
        money -= event_loss
        print(f"You balance has been updated")
        event_happened = True

    if chosen_event == e2:
        print(e2)
        irs_encounter = True
        
    if chosen_event == e3:
        print(e3)
        print("Free positive publicity!")
        reputation += 10
        event_happened = True

    if chosen_event == e4:
        print(e4)
        print("You'll get less customer revenue today.")
        icecream_broken = True
        event_happened = True

    if chosen_event == e5:
        print(e5)
        print("You don't risk coming into work today.")
        event_happened = True
        day_end()
        



# for the irs encounter task
def IRS_task():
    print("""
          
▀█▀ ▄▀█ █▀ █▄▀
░█░ █▀█ ▄█ █░█
          """)
    global money, event_loss, irs_encounter, event_happened
    print("Serve the customers by typing their order correctly before the time runs out!" \
    "\nIf you  fail to complete the order in time you lose the customer, and potential revenue. \nYou will also have the possiblility of getting less customers per day.\n\n")
    time.sleep(3)
    print("[2 seconds starting in 3]", end="\r")
    time.sleep(1)
    print("[2 seconds starting in 2]", end="\r")
    time.sleep(1)
    print("[2 seconds starting in 1]", end="\r")
    time.sleep(1)
    print("[GO]                         ")

    print("You notice that this isn't a normal customer... It's a member of the IRS!")
    print("They force you to do your taxes... Your balance has been updated.")
    money -= event_loss
    time.sleep(0.5)
    irs_encounter = False
    event_happened = True
    print(f"Current balance: ${money}")
    
    


# normal task logic
def task():
    print("""
          
▀█▀ ▄▀█ █▀ █▄▀
░█░ █▀█ ▄█ █░█
          """)
    
    print("Serve the customers by typing their order correctly before the time runs out!" \
    "\nIf you  fail to complete the order in time you lose the customer, and potential revenue. \nYou will also have the possiblility of getting less customers per day.\n\n")
    time.sleep(3)
    print("[2 seconds starting in 3]", end="\r")
    time.sleep(1)
    print("[2 seconds starting in 2]", end="\r")
    time.sleep(1)
    print("[2 seconds starting in 1]", end="\r")
    time.sleep(1)
    print("[GO]                          ")

    drink = ["Coffee", "Tea", "Juice", "Soda", "Water", "Milk", "Lemonade", "Smoothie", "Hot Chocolate"]
    flavor = ["Vanilla", "Chocolate", "Strawberry", "Mint", "Caramel", "Hazelnut", "Cinnamon", "Pumpkin Spice", "Banana", "Cherry", "Peach", "Buttery", "Spinach", "Watermelon"]
    size = ["Small", "Medium", "Large", "Extra Large"]
    order_drink = random.choice(drink)
    order_flavor = random.choice(flavor)
    order_size = random.choice(size)

    food = ["Muffin", "Bagel", "Sandwich", "Salad", "Cookie", "Brownie", "Croissant", "Wrap", "Cupcake", "Pizza", "Hamburger", "Hotdog", "Cheeseburger", "Donut"]
    order_food = random.choice(food)

    quip = random.choice(["Make it snappy!", "Hurry up, I'm in a rush!", "I don't have all day!", "Can you make it extra special?", "Surprise me!", "I hope you're good at this!", "Don't mess this up!", "I need this ASAP!", "This had better be good!", "I'm counting on you!", "I WANT TO SPEAK TO YOUR MANAGER. oh, your the manager? I'm sueing.", "I forgot what else."])
    global moneyUp_u1
    
    if not moneyUp_u1 and not icecream_broken:
        order_payment = random.randint(15, 35)
    elif moneyUp_u1 and not icecream_broken:
        order_payment = random.randint(35, 100)
    elif icecream_broken:
        if moneyUp_u1:
            order_payment = random.randint(15, 35)
        else:
            order_payment = random.randint(7, 17)

    global review, money, timer
    review = random.choice(["Yelp", "Google Maps", "Twitter", "Facebook", "Instagram"])

    custom_order = f"I'll have a {order_size} {order_flavor} {order_drink} and a {order_food}. {quip}"
    print(f'"{custom_order}"\n\n')

    
    
    timer_rundown = True
    

    def timer_countdown():
        global timer
        while timer_rundown and timer > 0:
            time.sleep(1)
            timer -= 1

    threading.Thread(target = timer_countdown, daemon=True).start()


    size_input = input("What size drink do they want? ").lower().strip()
    flavor_input = input("What flavor drink do they want? ").lower().strip()
    drink_input = input("What drink do they want? ").lower().strip()
    food_input = input("What food do they want? ").lower().strip()
    



    #check order/payment

    if drink_input == order_drink.lower() and flavor_input == order_flavor.lower() and size_input == order_size.lower() and food_input == order_food.lower():
        timer_rundown = False
        timer = 15
        print("", f"[ORDER COMPLETE] You earned ${order_payment}.")
        money += order_payment
        global today_money
        today_money += order_payment
        global served
        served += 1
        global reputation
        reputation += 1
        global total_customers
        total_customers += 1

    elif timer == 0:
        timer_rundown = False
        timer = 15
        print("", f"[OUT OF TIME] The customer leaves you a bad review on {review}.")
        global failed
        failed += 1
        reputation -= 1
        total_customers += 1
    else:
        timer_rundown = False
        timer = 15
        print("", f"[ORDER FAILED] The customer leaves you a bad review on {review}.")

        failed += 1
        total_customers += 1
        reputation -= 1
        
def mail():
    global username
    print("""
          
█▀▄▀█ ▄▀█ █ █░░
█░▀░█ █▀█ █ █▄▄
          """)
    global checked_today, message_d1, message_d0, currency, claimed_d10
    if days_played == 0:
        print(message_d0)
        checked_today = True
    elif days_played == 1:
        print(message_d1)
        checked_today = True
    elif days_played == 6:
        print(message_d6)
        checked_today = True
    elif days_played == 10:
        print(message_d10)
        if not checked_today:
            input("[EMAIL ATTACHMENT]")
            print("[ACCEPTED] You got 5 k₹!")
            add_currency(5)
        
        checked_today = True
        claimed_d10 = True
    elif days_played >=2 and days_played < 6:
        print(f"""
1. {sub0}
2. {sub1}
              """)
        select_mail = input("Which message would you like to read?").strip()
        if select_mail == "1":
            print(message_d0)
        elif select_mail == "2":
            print(message_d1)
    elif days_played >= 7 and days_played < 10:
                print(f"""
1. {sub0}
2. {sub1}
3. {sub6}
              """)
                select_mail = input("Which message would you like to read?").strip()
                if select_mail == "1":
                    print(message_d0)
                elif select_mail == "2":
                    print(message_d1)
                elif select_mail == "3":
                    print(message_d6)
                elif select_mail == "4":
                    print(message_d10)
    elif days_played > 10:
        print(f"""
1. {sub0}
2. {sub1}
3. {sub6}
4. {sub10}
              """)
        select_mail = input("Which message would you like to read?").strip()
        if select_mail == "1":
            print(message_d0)
        elif select_mail == "2":
            print(message_d1)
        elif select_mail == "3":
            print(message_d6)
        elif select_mail == "4":
            print(message_d10)
            if not claimed_d10:
                input("[EMAIL ATTACHMENT]")
                print("[ACCEPTED] You got 5 k₹!")
                add_currency(5)
                claimed_d10 = True
                

def market():
    print("""

█▀█ █▀█ ▀█▀ ▄▀█ █▀ █▀ █ █░█ █▀▄▀█
█▀▀ █▄█ ░█░ █▀█ ▄█ ▄█ █ █▄█ █░▀░█
          """)
    global current_price, currency, past_price, money, currency_wallet

    update_currency()
    if current_price > past_price:
        print("""
                     /
                    /  
                   /    
    /\          /\/      
   /  \    _ _ /          
  /    \  /                
 /      \/                   
/
[PRICE UP]""")
    elif current_price < past_price:
        print("""
\                         
 \                        
  \                       
   \/\ 
      \_ _     /\ 
           \  /  \ 
            \/    \ 
                   \ 
[PRICE DOWN]""")
    elif current_price == past_price:
        print("""

---------------------

              """)
    else:
        print("""
[DISPLAY ERROR]
              """)
    print(f"""
1. Buy k₹ for ${current_price}
2. Sell k₹ for ${current_price}
          """)
    k_input = input("What would you like to do? ")

    if k_input == "1":
        print(f"\nYour balance: ${money}")
        k_buy_input = input("How many would you like to buy? ")
        try:
            if int(k_buy_input) <= 0:
                print("Invalid, please use a number greater than zero.")
            else:
                sub_money_k = int(k_buy_input) * current_price
                money -= sub_money_k
                currency_wallet.append((int(k_buy_input), days_played))

                currency = sum(amount for amount, _ in currency_wallet)

                print("Balance updated")
        except ValueError:
            print(f"{k_buy_input} is not a valid number. Please try again.")
    elif k_input == "2":                                                                # sell
        if currency <= 0:
            print("You don't have anything to sell!")
        else:
            print(f"\nYour potassium: {currency}k₹")
            k_sell_input = input("How many would you like to sell? ")
            try:
                if int(k_sell_input) > currency:
                    print("You don't have enough for that!")
                else:
                    money += int(k_sell_input) * current_price

                    remaining = int(k_sell_input)
                    new_wallet = []
                    for amount, day_bought in currency_wallet:
                        if remaining >= amount:
                            remaining -= amount
                        else:
                            new_wallet.append((amount - remaining, day_bought))
                            remaining = 0
                    currency_wallet[:] = new_wallet
                    currency = sum(amount for amount, _ in currency_wallet)
                    print("Balance updated")
            except ValueError:
                print(f"{k_sell_input} is not a valid number. Please try again.")

def sleep():
    os.system('cls')
    print("""
          
█▀ █░░ █▀▀ █▀▀ █▀█
▄█ █▄▄ ██▄ ██▄ █▀▀
          """)
    global dream_happen
    dream_happen = random.choice([True, False])
    
def dream():
    possible_dreams = [
        "1"
        "2"
        "3"
        "4"
        "5"
        "6"
        "7"
        "8"
        "9"
        "10"
    ]
    dream_weights = [18.2, 16.4, 14.5, 12.7, 10.9, 9.1, 7.3, 5.5, 3.6, 1.8]
    chosen_dream = random.choice(possible_dreams, weights=dream_weights, k=1)
    print(chosen_dream)
    
    
    





HANK = "Helpful, Ai, Not, Killer"
#end
def exit_game():
    print("Closing shop, please wait...")
    time.sleep(1)
    exit()

while True and not sick:
    user = input(">").lower().strip()
    if user == "":
        balance()
    elif user == "exit":
        exit_game()
    elif user == "help":
        help()
    elif user == "explore":
        if total_explores >= explore_limit:
            print("You already searched the whole store. There is nothing else to find today.")
        else:
            explore()
    elif user == "shop":
        shop()
    elif user == "77432" and not demo:                                       #dev code, take out later.
        print("---Developer Code Active---")
        add_money_input = input("Enter amount to add: ")
        try:
            money += int(add_money_input)
            print(f"Added ${add_money_input} to balance.")
        except ValueError:
            print("Invalid amount.")
    elif user == "77433" and not demo:
        print("---Developer Code Active---")
        set_day_input = input("Enter the day you would like to advance too: ")
        try:
            days_played = int(set_day_input)
            print(f"Current day: {days_played}")
        except ValueError:
            print("Invalid amount.")
    elif user == "fail task":
        reputation -= 1
    elif user == "win task":
        reputation += 1
    elif user == "done" and event_happened:
        day_end()
        today_money = 0
        served = 0
        failed = 0
        games_played = 0
        total_explores = 0
        total_customers = 0
        today_u4 = False
        checked_today = False
        
    elif user == "done" and not event_happened:
        print("Nope! Not getting out of it that easily!")
    elif user == "done" and event_happened:
        day_end()

    elif user == "task":
        if total_customers >= customer_limit:
            print("There aren't any more customers to serve today.")
        elif irs_encounter:
            IRS_task()
            event_happened = True
        else:
            task()
    elif user == "k" and days_played >= 10:
        market()
    elif user == "mail":
        if days_played == 0 and not checked_today:
            new_mail()
        elif days_played ==1 and not checked_today:
            new_mail()
        elif days_played == 6 and not checked_today:
            new_mail()
        elif days_played == 10 and not checked_today:
            new_mail()
        elif scam:
            new_mail()
        
        mail()
        
    
    #make upgrades do somthing
    if upgrade4 in owned_upgrades:
        owned_upgrades.remove(upgrade4)
        reputation += 10

    if upgrade3 in owned_upgrades:
        fallback_u3 = True
    elif fallback_u3 not in owned_upgrades:
        fallback_u3 = False

    if upgrade5 in owned_upgrades:
        alarm_u5 = True
    
    if upgrade2 in owned_upgrades:
        explore_limit = 10
    
    if upgrade6 in owned_upgrades:
        currency_lose = 5
    
    if upgrade1 in owned_upgrades:
        moneyUp_u1 = True

    if upgrade7 in owned_upgrades:
        timer = 3

    if upgrade8 in owned_upgrades:
        antiScam_u8 = True
    
    
        
      

    if money < 0 and not fallback_u3:
        time.sleep(3)
        print("\n\nYour buisness is bankrupt.\n" \
        "\nYou sold all of your earthly posessions and now live on the streets." \
        "\nYour the topic of conversation at the dinner table of your family, they use you as an example for your younger siblings." \
        "\nAs you walk down the street, you come across your old shop, now owned by a wealthy entrepreneur." \
        "\nThey are now selling really nice items that you could have never afforded, even if you sold your kidneys on the blackmarket.\n\n")
        time.sleep(10)
        input("[ENTER] to quit")
        exit()
    elif money < 0 and fallback_u3:
        money = 20
        print(f"\n\nYou spent all of your money, but thankfuly you purchased an upgrade from the shop that saved you from bankruptcy!\nYour ballance is now ${money}\n")
        owned_upgrades.remove(upgrade3)

while True and sick:
    user = input("[SICK DAY]>").lower().strip()
    if user == "":
        balance()
    elif user == "help":
        print("""
Things to do when your sick:

1. You can still trade k₹ from your personal laptop
2. You can visit the doctor to cure your sickness
3. You can still check your inbox
4. You can type "sleep" to advance to the next day, but your not garenteed to be cured by then.
5. You can still check your balance
              """)
    elif user == "sleep":
        sleep()

"""
add game saving (money, postasium wallet, day's played)
add events 5/-- 
make upgrades do somthing 7/9
finish making upgrades 9/10 (bot that monitors email and has chance of catching scammers)
music
more emails
options menu (delete save data, achivements, ect.)
scam emails/sponsorship (one sponsor at a time) (scams oviouse) (more reputation, more likely)
acheivments
finish making dreams
cure sickness

plumbing explode
eletrical stop
"""