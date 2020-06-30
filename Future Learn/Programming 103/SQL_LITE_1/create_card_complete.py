import sqlite3
conn = sqlite3.connect("computer_cards.db")

def create(name, cores, cpu_speed, ram, cost):
    insert_sql = "INSERT INTO computer(name, cores, cpu_speed, ram, cost) VALUES ('{}', {}, {}, {}, {})".format(name, cores, cpu_speed, ram, cost)

    conn.execute(insert_sql)

    conn.commit()

print("Enter the details:")

name = input("Name >")
cores = input("Cores >")
cpu_speed = input("CPU speed (GHz) >")
ram = input("RAM (MB) >")
cost = input("Power usage ($) >")

create(name, cores, cpu_speed, ram, cost)

conn.close()