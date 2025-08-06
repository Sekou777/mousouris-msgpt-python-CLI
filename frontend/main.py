from .utils import menu
from .auth import *
from .api import *
import argparse

def cli_mode():
    parser = argparse.ArgumentParser(prog="msrgpt", description="MSRGPT CLI")

    subparsers = parser.add_subparsers(dest="command", required=True)

    # login command
    subparsers.add_parser("login", help="Connexion à MsrGPT")

    # logout command
    subparsers.add_parser("logout", help="Déconnexion de MsrGPT")

    # register command
    subparsers.add_parser("register", help="Créer un compte")

    # run command avec des arguments propres
    run_parser = subparsers.add_parser("run", help="Exécuter un prompt")
    run_parser.add_argument("-o", "--option", required=True, help="Option permettant de specifier le resultat")
    run_parser.add_argument("-p", "--prompt", required=True, help="Prompt à envoyer")

    args = parser.parse_args()

    if args.command == "login":
        login()
    elif args.command == "logout":
        logout()
    elif args.command == "register":
        register()
    elif args.command == "run":
        if args.option in ["Scan", "Footprint", "Enum"]:
            sendPrompt(args.option, args.prompt)
        else:
            print("Option non prise en charge")
            return False

    return True
   
    

def main():

    if cli_mode():
        return

    while True:
        menu()

        choice= input("choix du numero: ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            option=input("Option: ")
            prompt=input("Prompt---> ")
            sendPrompt(option,prompt)
        elif choice == "4":
            logout()
        elif choice =="5":
            print("Bye bye")
            exit()
        else:
            print("Choix incorrecte, veuillez reesayer !") 
    

if __name__ == "__main__":
    main()
