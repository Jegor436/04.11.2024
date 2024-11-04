# Piedzīvojums Spoku Mājā
import random

# Inicializē mainīgos
inventory = []
player_alive = True

# Definē funkciju, kas sāk spēli un vada ciklu, kamēr spēlētājs ir dzīvs
def start_game():
    while player_alive:
        entrance()

def entrance():
    print("Tu atrodies spoku mājas ieejā. Vai vēlies iet 'iekšā' vai bēgt 'prom'?")
    choice = ""
    while choice not in ["iekšā", "prom"]:
        choice = input(">>> ").lower()
        if choice == "iekšā":
            foyer()
        elif choice == "prom":
            print("Tu izbēdzi droši. Spēle beigusies!")
            end_game()
        else:
            print("Nepareiza izvēle. Mēģini vēlreiz.")

def foyer():
    print("Tu ieej foajē. Ir tumšs, bet redzi durvis uz 'virtuvi', 'dzīvojamo istabu', 'pagrabu'un 'veļas istabu'.")
    choice = ""
    while choice not in ["virtuve", "dzīvojamā istaba"]:
        choice = input(">>> ").lower()
        if choice == "virtuve":
            kitchen()
        elif choice == "dzīvojamā istaba":
            living_room()
        elif choice == "pagrabs":
            basement()
        elif choice == "veļas istaba":
            laundry()
        else:
            print("Nepareiza izvēle. Mēģini vēlreiz.")

def kitchen():
    print("Tu esi virtuvē. Tā ir biedējoša, un tu atrod ieročus. Vai tu to 'ņem' vai atstāj 'aizvērtu'?")
    choice = ""
    while choice not in ["ņem", "aizvērtu"]:
        choice = input(">>> ").lower()
        if choice == "ņem":
            inventory.append("nazis")
            print("Tu paņēmi nazi.")
        print("Pēkšņi parādās spoks! Vai tu vēlies 'cīnīties' vai 'bēgt'?")
        action = input(">>> ").lower()
        if action == "cīnīties":
            if "nazis" in inventory:
                print("Tu uzvarēji spoku ar nazi! Tu atgriezies foajē.")
                foyer()
            if "panna" in inventory:
                print("Tu uzvarēji spoku ar pannu! Tu atgriezies foajē.")
                foyer()
            if "bise" in inventory:
                print("Tu uzvarēji spoku ar bisi! Tu atgriezies foajē.")
                foyer()
            else:
                print("Tev nav ar ko aizstāvēties. Spēle beigusies.")
                end_game() 
            
        elif action == "bēgt":
            print("Tu aizbēdzi atpakaļ uz foajē.")
            foyer()
        else:
            print("Nepareiza izvēle.")

def living_room():
    print("Dzīvojamā istaba ir putekļaina un tajā ir dīvains spogulis. Vai tu vēlies 'skatīties' spogulī vai iet 'atpakaļ'?")
    choice = ""
    while choice not in ["skatīties", "atpakaļ"]:
        choice = input(">>> ").lower()
        if choice == "skatīties":
            print("Spogulis ir nolādēts! Tu pārvērties par spoku. Spēle beigusies.")
            end_game()
        elif choice == "atpakaļ":
            foyer()
        else:
            print("Nepareiza izvēle.")

def basement():
    print("Tu atrodi durvis uz pagrabu. Tās ir aizslēgtas. Ja tev būtu atslēga un kods, tu varētu tās 'atvērt' ar atslēgu vai 'ievadiet kodu'.")
    choice = ""
    while choice != "atvērt":
        choice = input(">>> ").lower()
        if choice == "atvērt":
            if "atslēga" in inventory:
                print("Tu atvēri slēdzeni, bet tev vajag arī 'ievadiet kodu'!")
            else:
                print("Durvis ir aizslēgtas. Tev nepieciešama atslēga.")
                basement()
        elif choice == "ievadiet kodu":
            if "kods" in inventory:
                print("ievadiet pareizu kodu")
                number = int(input("Ievadiet kodu"))
                if number == "5090":
                    print("Pareizi!")
                else: 
                    print("Nepareizi!")
            else:
                 print("Durvis ir aizslēgtas. Tev nepieciešams kods.")
                 basement()        
        else:
            print("Nepareiza izvēle.")
            foyer()

def laundry():
    print("Veļas istabā jāatrod kods durvīm pagrabā. Vai tu vēlies 'meklēt' kodu vai iet 'atpakaļ'?")
    choice = ""
    while choice not in ["meklēt", "atpakaļ"] :
        choice = input(">>> ").lower()
        if choice == "meklēt":
                print("Tu atradīsi kodu '5090' un ej atpakaļ uz durvīm!")
                number = "5090"
                basement()
        elif choice == "atpakaļ":
                foyer()       
        else:
            print("Nepareiza izvēle.")
                       

def end_game():
    global player_alive
    player_alive = False
    print("Paldies, ka spēlēji Piedzīvojums Spoku Mājā!")

# Sāk spēli
print("Sveicināts Piedzīvojums Spoku Mājā!")
start_game()
