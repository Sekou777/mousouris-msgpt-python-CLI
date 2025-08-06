import requests
from rich import print
from .config import *
from getpass import getpass
import os

def register():
    print(" [bold cyan]\n  --- Création de compte --- [/]")
    fullname = input("Nom complet: ")
    pseudo = input("pseudo:")
    email = input("Email: ")
    password = getpass("Mot de passe: ")

    try:
        response = requests.post(f"{API_BASE}/auth/inscription", json={
            "fullname": fullname,
            "pseudo": pseudo,
            "email": email,
            "password": password,
        })
        if response.status_code == 201:
            print("[bold green]Compte créé avec succès.Vous pouvez maintenant vous connecter.[/]")
        else:
            print("[bold red]Erreur lors de la création du compte.[/]",response.json().get('message','Erreur inconnue'))
    except Exception as e:
        print(f"Une erreur est survenue: {e}")

def login():
    print(" [bold cyan]\n  --- Connexion --- [/]")
    email = input("email:")
    password = getpass("Mot de passe: ")
    try:
        response = requests.post(f"{API_BASE}/auth/connexion", json={
            "email": email,
            "password": password,
            })
        if response.status_code == 200:
            token =response.json()['token']
            saveToken(token)
            print("[bold green]Vous êtes connecté avec succès.[/]")
        else:
            print("[bold red]Erreur lors de la connexion.[/]",response.json().get('message','Erreur inconnue'))
    except Exception as e:
        print(f"Une erreur est survenue: {e}")

def logout():
    if os.path.exists(TOKEN_FILE):
        os.remove(TOKEN_FILE)
        print("[bold green]Déconnexion réussie.[/]")
    else:
        print("[bold red]Vous n'êtes pas connecté.[/]")


def saveToken(token):
    with open(TOKEN_FILE, 'w') as f:
        f.write(token)

def loadToken():
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, 'r') as f:
            return f.read().strip()
