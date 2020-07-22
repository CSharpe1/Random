import sqlite3
from random import randint
conn = sqlite3.connect(r"C:\Users\charles.sharpe\OneDrive - Global Graphics PLC\Documents\1_CS\Random\Future Learn\Programming 103\SQL_LITE_1\computer_cards.db")

def read_all_cards():
    result = conn.execute("SELECT * FROM computer")
    return result.fetchall()

def pick_card():
    cards = read_all_cards()
    random_card = cards[randint(0, len(cards) - 1)]
    return random_card

  



card = pick_card()
print(card)



########################
player = input("Are you player (1) or (2) >")
choosing_player = "1"

for round in range(5):
    
    input("Press enter to pick a card when both players are ready >")

    card = pick_card()
    card_text = "{}, cores={}, speed={}GHz, RAM={}MB, cost={}$".format(card[0], card[1], card[2], card[3], card[4])
    print(card_text)

    print("Player " + choosing_player + " picks.")

    winner = input("Did you win? (Y)es, (N)o, (D)raw >").lower()
    if winner == "y":
            choosing_player = player
    elif winner == "n":
        choosing_player = "2" if player == "1" else "1"

conn.close()
