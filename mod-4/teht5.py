user = 'python'
password = 'rules'
guesses = 0
while guesses < 5:
    user_guess = input("Käyttäjänimi: ")
    pass_guess = input("Salasana: ")
    if (user_guess != user or pass_guess != password):
        print("Pääsy evätty")
        guesses += 1
    else:
        print("Tervetuloa")
        break
