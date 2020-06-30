
import sqlite3
conn = sqlite3.connect(r"C:\Users\charles.sharpe\OneDrive - Global Graphics PLC\Documents\1_CS\Random\Future Learn\Programming 103\SQL_LITE_1\computer_cards.db")




result = conn.execute("SELECT * FROM computer")
print(result)

computers = result.fetchall()

for computer in computers:
    name = computer[0:]
    print(name)


conn.close()


