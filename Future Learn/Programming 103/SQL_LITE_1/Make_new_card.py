import sqlite3
conn = sqlite3.connect(r"C:\Users\charles.sharpe\OneDrive - Global Graphics PLC\Documents\1_CS\Random\Future Learn\Programming 103\SQL_LITE_1\computer_cards.db")


def create(name, cores, cpu_speed, ram):
    insert_sql = "INSERT INTO computer(name, cores, cpu_speed, ram) VALUES ('{}', {}, {}, {})".format(name, cores, cpu_speed, ram)

    conn.execute(insert_sql)

    conn.commit()



print("Enter the details:")

name = input("Name > ")
cores = input("Cores > ")

cpu_speed = input("Cpu_speed > ")
ram = input("Ram > ")

create(name, cores, cpu_speed, ram)

conn.close()
