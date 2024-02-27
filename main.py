import time
import json
import os
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
    os.system("cls")
    print("░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░\n"
          "░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░\n"
          "░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░\n"
          "░▒▓███████▓▒░░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░\n"
          "░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░\n"
          "░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░\n"
          "░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░")

    login_attempts = 0
    jsonData = load_credentials()

    #Eseguire se login_attempts e minore o uguale a 3
    while login_attempts <= 3:
        inpt = int(input("1. Login     2. Register > "))
        time.sleep(0.75)

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
            passwrd = getpass("Enter your new bank password here > ")

            new_credentials = {"Name": name, "Password": passwrd}
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
            #Fine del ciclo WHILE
            break
        
        #Se l'input dell'utente e diverso da 1 o 2, allora abortiamo
        else:
            time.sleep(0.75)
            os.system("cls")
            print("Invalid Number! Please try again...")
            os.abort()

main()
