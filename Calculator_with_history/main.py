HISTORY_FILE = "history.txt"

def show_history():
    file = open(HISTORY_FILE, "r")
    lines = file.readlines()
    
    if len(lines) == 0:
        print("No history found!")
    else:
        for line in reversed(lines):
            print(line.strip())
    
    file.close()

def clear_history():
    open(HISTORY_FILE, "w").close()
    print("History cleared")

def save_to_history(equation, result):
    file = open(HISTORY_FILE, "a")
    file.write(f"{equation} = {result}\n")
    file.close()

def calculate(user_input):
    # 👇 Fix for 8+8, 4-1 etc
    user_input = user_input.replace("+", " + ")\
                           .replace("-", " - ")\
                           .replace("*", " * ")\
                           .replace("/", " / ")

    parts = user_input.split()

    if len(parts) != 3:
        print("Invalid input! use format: number operator number (e.g. 8 + 8)")
        return

    num1 = float(parts[0])
    op = parts[1]
    num2 = float(parts[2])

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            print("Cannot divide by zero")
            return
        result = num1 / num2
    else:
        print("Invalid operator. Use only + - * /")
        return

    if int(result) == result:
        result = int(result)

    print("Result:", result)
    save_to_history(user_input.strip(), result)

def main():
    print("--- SIMPLE CALCULATOR (type history, clear or exit) ---")
    
    while True:
        user_input = input("Enter calculation (+ - * /) or command(type history, clear or exit): ").strip().lower()

        if user_input == 'exit':
            print("Goodbye")
            break
        elif user_input == 'history':
            show_history()
        elif user_input == 'clear':
            clear_history()
        else:
            calculate(user_input)

main()