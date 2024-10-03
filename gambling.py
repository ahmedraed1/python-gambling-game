import random


MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3


symbols_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winnings_lines = []
    for line in range(lines):
        symbol = columns[0][line] 
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings = values[symbol] * bet
            winnings_lines.append(line + 1)
            
            
    return winnings, winnings_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbol = all_symbols[:]
        for _ in range(rows):
            value = random.choice(all_symbols)
            current_symbol.remove(value)
            column.append(value)
        columns.append(column)

    return columns
        
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i , column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()
        

def deposit():
    """
    Prompts user to enter a valid amount to deposit.
    """
    while True:
        try:
            amount = int(input("Enter amount to be deposited: $"))
            if amount > 0:
                break
            else:
                print("Please enter a valid amount.")

        except ValueError:
            print("Invalid input. Please enter a number.")

    return amount

def get_number_of_lines():
    """
    Prompts user to enter the number of lines to bet on.
    """
    while True:
        try:
            lines = int(input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? "))
            if lines >= 1 and lines <= MAX_LINES:
                break
            else:
                print("Please enter a valid number of lines.")

        except ValueError:
            print("Invalid input. Please enter a number.")

    return lines


def get_bet():
    """
    Prompts user to enter the bet amount.
    """
    while True:
        try:
            bet = int(input("Enter the bet amount ($" + str(MIN_BET) + "-" + str(MAX_BET) + ")? $"))
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print("Please enter a valid bet amount.")

        except ValueError:
            print("Invalid input. Please enter a number.")

    return bet

def spin(balance):
    """
    Main game function.
    """
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print("You do not have enough to bet that amount, your current balance is: $" + str(balance))
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to ${total_bet}.")
    
    slots = get_slot_machine_spin(ROWS, COLS, symbols_count)
    print_slot_machine(slots)
    winnings , winnings_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on : ", *winnings_lines)
    return winnings - total_bet

def main():
    """
    Main function.
    """
    balance = deposit()
    while True:
        print(f"Current balance is: ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)
   
main()