import random
import string
from rich import print

char = " " + string.punctuation + string.digits + string.ascii_letters
char = list(char)
code = string.ascii_letters + " " + string.punctuation + string.digits
code = list(code)

# Banner
print(r'''
[bold magenta]   ____    _                    _                          [/bold magenta] [bold green]  _______                          [/bold green]
[bold magenta]  / ___|  | |__     __ _       | |    ___    _          _  [/bold magenta] [bold green] |__   __|                         [/bold green]         
[bold magenta] | |      |  _ \   / _  |   ___| |   / _ \  \  \      /  / [/bold magenta] [bold green]    | |    ___   _      _    _     [/bold green]     
[bold magenta] | |___   | | | | | (_| |  /  _  |  | (_) |  \  \ /\ /  /  [/bold magenta] [bold green]    | |   / _ \ \  \  /  /  | |    [/bold green]      
[bold magenta]  \____ \ |_| |_|  \__ _| | ( _| |   \___/    \   ..   /   [/bold magenta] [bold green]    | |  |  __/  \  \/  /   | __|  [/bold green]      
[bold magenta]       | |                 \ ____|             \_/  \_/    [/bold magenta] [bold green]    |_|   \___|  /  /\  \   | |    [/bold green]          
[bold magenta]   ____| |                                                 [/bold magenta] [bold green]                /__/  \__\  \__|   [/bold green]         
[bold magenta]  |_____/                                                  [/bold magenta]           
      ''')

print("[bold yellow]       Welcome to ShadowText, here you can ENCRYPT or DECRYPT your plain text[/bold yellow]")

abc = input("\n\033[92mENCRYPT or DECRYPT ? (e/d): \033[0m").lower()

# Encrypt
if abc == "e":
    normal = input("\n\033[92mEnter your Message here to Encrypt=> \033[0m")
    morce = ""

    for letter in normal:
        index = char.index(letter)
        morce += code[index]

    print(f"\nYour message is : {normal}")
    print(f"Encrypted Message is : {morce}")
    input("\n\033[1mPress Enter To Exit !!\033[0m")

# Decrypt
elif abc == "d":
    morce = input("\n\033[92mEnter Encrypted Message here=> ")
    normal = ""

    for letter in morce:
        index = code.index(letter)
        normal += char[index]

    print(f"\nYour Encrypted Message is : {morce}")
    print(f"\nDecrypted Message is : {normal}")
    input("\n\n\033[1mPress Enter To Exit !!\033[0m")

else:
    print("\n\nPlease enter only [ e or d ]")
