import sqlite3
import matplotlib.pyplot as plt

running = True
lis = []

conn = sqlite3.connect("budget.db")

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    type TEXT,
    category TEXT,
    amount REAL,
    description TEXT
    );
''')

conn.commit()

while running:
    print("Choose 1 to insert income.")
    print("Choose 2 to insert expenses.")
    print("Choose 3 to display budget.")
    print("Choose 4 to display analysis charts.")
    print("Choose 5 to exit.")

    choice = int(input("Enter Your Choice: "))
    if choice == 1:
        date = input("Enter income date: ")
        type = "income"
        category = input("Enter income category: ")
        amount = float(input("Enter the amount: "))
        description = input("Enter the description: \n")

        cursor.execute('''
            INSERT INTO transactions (date, type, category, amount, description)
            VALUES (?,?,?,?,?)
        ''', (date, type, category, amount, description))

        conn.commit()
        print("Income added successfully")
    
    elif choice == 2:
        date = input("Enter expense date: ")
        type = "expense"
        category = input("Enter category: ")
        amount = float(input("Enter the amount: "))
        description = input("Enter the description: \n")

        cursor.execute('''
            INSERT INTO transactions (date, type, category, amount, description)
            VALUES (?,?,?,?,?)
        ''', (date, type, category, amount, description))

        conn.commit()
        print("Expenses added successfully")

    elif choice == 3:
        cursor.execute('''
            SELECT SUM(amount) FROM transactions
            WHERE type = "income"
        ''')
        inc = cursor.fetchone()[0]
        if inc is None:
            inc = 0
        
        cursor.execute('''
        SELECT SUM(amount) FROM transactions
        WHERE type = "expense"
        ''')
        exp = cursor.fetchone()[0]
        if exp is None:
            exp = 0
        
        remaining = inc - exp

        lis.append(inc)
        lis.append(exp)
        lis.append(remaining)

        print("\n===== SUMMARY =====")
        print("Total Income  :", inc)
        print("Total Expense :", exp)
        print("Remaining     :", remaining)


    elif choice == 4:
        print("Charts")
        plt.title("Pie Chart")
        labels = ["Total Income", "Total Expenses", "Total Budget"]
        plt.pie(lis, labels= labels, autopct="%1.1f%%")
        plt.show()


    elif choice == 5:
        print("Complete.")
        running = False




    