import requests
from rich import print
from .config import *
from .auth import *
import subprocess 

def sendPrompt(option: str="Scan", prompt: str=None):
    token=loadToken()

    if not token:
        print("[bold red]Erreur:Veuillez vous connecter au préalable !![/]")
        exit()
    headers = {"Authorization":f"Bearer {token}"}
    try:
        response = requests.post(f"{API_BASE}/openai/chat",json={
            "option": option,
            "prompt": prompt
            }, headers=headers)
        if response.status_code == 200:
            limiteRep=response.json()["limite"]
            dataCode=response.json()["data"]
            print(f"\n[bold green] {limiteRep}[/]")
            print("\n[bold green]Réponse à executer:[/]",dataCode)
            subprocess.run(dataCode,shell=True)
        else:
            print("[bold red]Erreur: Erreur de requête !![/]",response.text)        

    except Exception as e:
        print(f"[red]Erreur: {e}[/red]")