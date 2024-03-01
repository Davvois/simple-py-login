import time, json, os
from getpass import getpass

jsonFile = "D:\\Coding\\Python\\Bank\\credentials.json"

#Funzione per caricare le credenziali
def load_credentials():
    #Nel caso il file fosse vuoto, si inizializza il file
    try:
        with open(jsonFile, "r") as file1:
            jsonData = json.load(file1)
    except:
        jsonData = []

    return jsonData

#Funzione per salvare le credenziali
def save_credentials(credentials):
    with open(jsonFile, "w") as files1:
        json.dump(credentials, files1, indent=4)

def main():
    logged_in = False
    os.system("cls")

    login_attempts = 0

    #Eseguire se login_attempts e minore o uguale a 3
    while login_attempts <= 3:
        print("░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░\n"
        "░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░\n"
        "░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░\n"
        "░▒▓███████▓▒░░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░\n"
        "░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░\n"
        "░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░\n"
        "░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░")

        inpt = int(input("1. Login     2. Register > "))
        time.sleep(0.75)

        jsonData = load_credentials()
        
        #Controllare se l'input dell'utente è "login"
        if inpt == 1:
            os.system("cls")

            name = input("Please enter your bank's name > ")
            time.sleep(0.75)

            #La funzione any() restituirà True se una delle due funzioni iteranti e vera
            #se facciamo print(entry), verranno outputati tutti i dati del file jsonData
            #con entry["Name"] andiamo a selezionare la sezione "Name" nel file json
            if any(entry["Name"] == name for entry in jsonData):
                passwrd = getpass("\nPlease enter your bank's password > ")
                time.sleep(0.75)

                #Stesso discorso per la password
                if any(entry["Name"] == name and entry["Password"] == passwrd for entry in jsonData):
                    os.system("cls")
                    print("Successfully logged in!")

                    logged_in = True
                    time.sleep(1)
                    #Il ciclo WHILE viene interrotto, la password e l'username sono corretti
                    break
                
                #Se il nome, o la password non esiste, allora aggiungiamo 1 a login_attempts e ricominciamo il ciclo
                else:
                    os.system("cls")
                    print("Invalid password! Try again")
                    login_attempts += 1
                    time.sleep(0.75)
                    os.system("cls")

            else:
                os.system("cls")
                print("Invalid username! Try again")
                login_attempts += 1
                time.sleep(0.75)
                os.system("cls")

            #Se login_attempts = 3, abortiamo
            if login_attempts == 3:
                print("Maximum login attempts reached! Please try later...")
                time.sleep(1)
                os.abort()

        #Controlliamo che l'input dell'utente sia "Register"
        elif inpt == 2:
            os.system("cls")
            dots = "..."

            name = input("Enter your new bank name here > ")

            if len(name) <= 3:
                print("Name must be 4 letters or more!")

            passwrd = getpass("Enter your new bank password here > ")

            new_credentials = {"Name": name, "Password": passwrd, "Coins": 0.0}
            #Appendiamo le credenziali messe dall'utente nell'array jsonData e salviamo le credenziali con la funzione save_credentials()
            jsonData.append(new_credentials)
            save_credentials(jsonData)

            time.sleep(0.75)
            os.system("cls")
            print("Please wait", end="")

            for c in dots:
                print(c, end="")
                time.sleep(0.75)

            time.sleep(0.5)
            os.system("cls")
            print("Successfully created new account!")
            logged_in = True
            time.sleep(1)
            #Fine del ciclo WHILE
            break
        
        #Se l'input dell'utente e diverso da 1 o 2, allora abortiamo
        else:
            time.sleep(0.75)
            os.system("cls")
            print("Invalid Number! Please try again...")
            os.abort()
    
    #Se la bool logged_in = Vera, allora eseguiamo la funzione whenLogged()
    if logged_in == True:
        whenLogged()
        return

#Funzione che viene eseguita nel caso l'utente sia loggato
def whenLogged():
    public_coins = 500.0
    #Loadiamo le credenziali grazie alla funzione load_credentials()
    jsonData = load_credentials()

    while True:
        os.system("cls")
        print("░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░\n"
        "░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░\n"
        "░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░\n"
        "░▒▓███████▓▒░░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░\n"
        "░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░\n"
        "░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░\n"
        "░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░\n")

        print("What would you like to do?")
        inpt2 = int(input("1. Deposit Coins         2. Withdraw Coins > "))

        #Prendiamo tutti i dati del file json
        for entry in jsonData:
            name = entry["Name"]
            passwrd = entry["Password"]
            coins = entry["Coins"]

        #Controlliamo che l'utente abbia scelto "Deposit Coins"
        if inpt2 == 1:
            os.system("cls")
            public_coins_deposit = float(input("Amount of money to deposit (Your money: " + str(public_coins) + ") > "))  

            #Controlliamo che l'importo da depositare inserito dall'utente sia minore dei soldi totali         
            if public_coins_deposit > public_coins:
                print("You can't afford to deposit all that money!")
                time.sleep(1)

            else:
                public_coins -= public_coins_deposit

                old_credentials = {"Name" : name, "Password" : passwrd, "Coins" : coins}

                coins += public_coins_deposit
                new_credentials = {"Name": name, "Password": passwrd, "Coins": coins}

                jsonData.remove(old_credentials)
                jsonData.append(new_credentials)
                save_credentials(jsonData)

                print("Successfully deposited money!")
                time.sleep(1)
            
        elif inpt2 == 2:
            os.system("cls")
            public_coins_withdraw = float(input("Amount of money to withdraw (Your money: " + str(coins) + ") > ")) 

            #Controlliamo che l'importo da prendere inserito dall'utente sia minore dei soldi totali         
            if public_coins_withdraw > coins:
                print("You can't afford to withdraw all that money!")
                time.sleep(1)

            else:
                public_coins += public_coins_withdraw

                old_credentials = {"Name" : name, "Password" : passwrd, "Coins" : coins}

                
                coins -= public_coins_withdraw
                new_credentials = {"Name": name, "Password": passwrd, "Coins": coins}

                jsonData.remove(old_credentials)
                jsonData.append(new_credentials)
                save_credentials(jsonData)

                print("Successfully withdrawn money!")
                time.sleep(1)
            
if __name__ == "__main__":
    main()
