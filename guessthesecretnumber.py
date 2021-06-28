secret = 9

print("░█████╗░░█████╗░░██████╗██╗███╗░░██╗░█████╗░")
print("██╔══██╗██╔══██╗██╔════╝██║████╗░██║██╔══██╗")
print("██║░░╚═╝███████║╚█████╗░██║██╔██╗██║██║░░██║")
print("██║░░██╗██╔══██║░╚═══██╗██║██║╚████║██║░░██║")
print("╚█████╔╝██║░░██║██████╔╝██║██║░╚███║╚█████╔╝")
print("░╚════╝░╚═╝░░╚═╝╚═════╝░╚═╝╚═╝░░╚══╝░╚════╝░")
print("")
print("Let's play a game called 'guess the secret number'...")
print("")
print("I have a number in mind. It's an integer between 0 and 10. Can you guess what it is?")
guess = int(input("Pick a number : "))
if secret == guess:
    print("Congratulations! You guessed correctly.")
else :
    print("Awwww, you guessed wrong.")
