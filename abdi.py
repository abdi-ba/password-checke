import string
import time

RED = "\033[91m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
CYAN = "\033[96m"
WHITE = "\033[97m"
BOLD = "\033[1m"
DIM = "\033[2m"
RESET = "\033[0m"

def banner():
    print(CYAN + BOLD)
    print("  ╔══════════════════════════════════════════════╗")
    print("  ║        🔐  PASSWORD STRENGTH CHECKER         ║")
    print("  ║         Cybersecurity Toolkit v1.0           ║")
    print("  ╚══════════════════════════════════════════════╝")
    print(RESET)

def divider():
    print(DIM + CYAN + "  ──────────────────────────────────────────────" + RESET)

def check_password(password):
    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False

    for char in password:
        if char.isupper():
            has_upper = True
        if char.islower():
            has_lower = True
        if char.isdigit():
            has_digit = True
        if char in string.punctuation:
            has_symbol = True

    length = len(password)
    score = 0

    if length >= 8:
        score += 1
    if length >= 12:
        score += 1
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_symbol:
        score += 1

    return score, length, has_upper, has_lower, has_digit, has_symbol

def show_results(password):
    score, length, has_upper, has_lower, has_digit, has_symbol = check_password(password)

    print()
    divider()
    print(WHITE + BOLD + "  📊  ANALYSIS REPORT" + RESET)
    divider()

    def status(condition, label):
        if condition:
            print(GREEN + "  ✔  " + label + RESET)
        else:
            print(RED + "  ✘  " + label + RESET)

    status(length >= 8, f"Length: {length} characters (min. 8 required)")
    status(has_upper, "Contains uppercase letters (A-Z)")
    status(has_lower, "Contains lowercase letters (a-z)")
    status(has_digit, "Contains numbers (0-9)")
    status(has_symbol, "Contains special symbols (!@#$...)")

    print()
    divider()
    print(WHITE + BOLD + "  🏁  VERDICT" + RESET)
    divider()

    if score <= 2:
        print(RED + BOLD + "  ⚠   Strength : WEAK" + RESET)
        print(RED + "  ▓░░░░░░░░░  10%" + RESET)
    elif score <= 4:
        print(YELLOW + BOLD + "  ⚡  Strength : MEDIUM" + RESET)
        print(YELLOW + "  ▓▓▓▓▓▓░░░░  60%" + RESET)
    else:
        print(GREEN + BOLD + "  🛡   Strength : STRONG" + RESET)
        print(GREEN + "  ▓▓▓▓▓▓▓▓▓▓  100%" + RESET)

    print()

    if score <= 4:
        divider()
        print(CYAN + BOLD + "  💡  SUGGESTIONS" + RESET)
        divider()
        if length < 8:
            print(YELLOW + "  →  Make your password at least 8 characters long" + RESET)
        if length < 12:
            print(YELLOW + "  →  Use 12+ characters for better security" + RESET)
        if not has_upper:
            print(YELLOW + "  →  Add uppercase letters like A, B, C" + RESET)
        if not has_lower:
            print(YELLOW + "  →  Add lowercase letters like a, b, c" + RESET)
        if not has_digit:
            print(YELLOW + "  →  Mix in some numbers like 1, 2, 3" + RESET)
        if not has_symbol:
            print(YELLOW + "  →  Use symbols like @, #, !, $ for strength" + RESET)
        print()

    divider()

import string
import time

# ... (Keep all your color variables RED, YELLOW, etc.)
# ... (Keep all your functions divider, check_password, show_results, banner)

def main():
    banner()
    print("\033[2m  Analyze your passwords locally. Nothing is stored.\033[0m\n")
    while True:
        print("\033[97m  Enter a password to check\033[0m")
        print("\033[2m  (type 'quit' to exit)\033[0m\n")
        password = input("\033[96m  🔑  Password: \033[0m")
        if password.lower() == "quit":
            print("\n\033[96m\033[1m  Goodbye! Stay safe online. 🔐\033[0m\n")
            break
        if password == "":
            print("\033[91m\n  ⚠  Please enter a password.\n\033[0m")
            continue
        print("\033[2m\n  Analyzing...\033[0m")
        time.sleep(0.6)
        show_results(password)
        print("\033[97m  Check another password? \033[2m(press Enter to continue)\033[0m")
        input()

# THIS IS THE PERFECT SOLUTION: 
# It prevents the installer from getting stuck in the 'while' loop.
if __name__ == "__main__":
    main()
