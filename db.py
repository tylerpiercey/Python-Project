def read_balance():
    balance = 0
    try:
        with open("money.txt", "r") as file:
            balance = file.read()
            balance = float(balance)
    except FileNotFoundError:
        print("Could not find balance file!.")
    return balance

def write_balance(balance):
    with open("money.txt", "w") as file:
        file.write(str(balance))





