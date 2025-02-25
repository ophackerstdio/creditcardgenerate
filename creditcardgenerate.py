import random
import pyfiglet
import time
import sys
from termcolor import colored
from colorama import init

# Initialize colorama for Windows support
init()

def type_effect(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def logo():
    return colored(pyfiglet.figlet_format("OP HACKER"), "green")

def generate_fake_card():
    brands = ["VISA", "MasterCard", "American Express", "Discover"]
    banks = ["Bank of Nowhere", "Test Financial C.U.", "Sample Bank Ltd."]
    names = ["John Doe", "Jane Smith", "Alex Johnson", "Chris Walker"]
    
    debit_cards = [f"{random.randint(4000000000000000, 4999999999999999)}" for _ in range(200)]
    
    card_number = random.choice(debit_cards)
    cvv = str(random.randint(100, 999))
    expiry_month = str(random.randint(1, 12)).zfill(2)
    expiry_year = str(random.randint(2025, 2030))
    pin = str(random.randint(1000, 9999))
    money_range = f"${random.randint(100, 500)}"
    
    card_info = colored(f"""
    ╔══════════════════════════════════╗
    ║ [-] Brand     : {random.choice(brands)}
    ║ [-] Card No   : {card_number}
    ║ [-] Bank      : {random.choice(banks)}
    ║ [-] Name      : {random.choice(names)}
    ║ [-] Address   : 123 Fake Street, Imaginary City
    ║ [-] Country   : Wonderland
    ║ [-] Money     : {money_range}
    ║ [-] CVV       : {cvv}
    ║ [-] Expiry    : {expiry_month}/{expiry_year}
    ║ [-] Pin       : {pin}
    ╚══════════════════════════════════╝
    """, "cyan")
    
    return card_info

def about():
    return colored("""
    Follow me on:
    YouTube: https://www.youtube.com/@ophackerstdio
    Instagram: https://www.instagram.com/ophackerstdio
    """, "red")

def main():
    print(logo())
    watermark = colored("\n[-]Powered by OP HACKER STDIO\n[-]Made by OP Haseeb\n", "green")
    type_effect(watermark, 0.02)
    
    print(colored("\nSelect an option:", "yellow"))
    print(colored("1 - Single Card Generate", "blue"))
    print(colored("2 - Multi Cards Generate (2-4)", "blue"))
    print(colored("3 - About", "blue"))
    
    choice = input(colored("\nEnter your choice: ", "magenta"))
    
    if choice == "1":
        print(generate_fake_card())
    elif choice == "2":
        while True:
            try:
                num_cards = int(input(colored("\nHow many cards do you want to generate? (2-4): ", "magenta")))
                if 2 <= num_cards <= 4:
                    break
                else:
                    print(colored("Invalid input! Please enter a number between 2 and 4.", "red"))
            except ValueError:
                print(colored("Invalid input! Please enter a numeric value.", "red"))
                
        for _ in range(num_cards):
            print(generate_fake_card())
    elif choice == "3":
        print(about())
    else:
        print(colored("Invalid choice! Please restart the program and select a valid option.", "red"))

if __name__ == "__main__":
    main()
