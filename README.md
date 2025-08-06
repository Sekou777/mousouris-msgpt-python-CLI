#  MSGPT-Python-CLI

MSGPT-Python-CLI est un outil en ligne de commande permettant aux utilisateurs d'envoyer des **prompts spécialisés** pour interagir avec un shell intelligent.  
Chaque utilisateur dispose de **5 prompts maximum par jour**.

---

##  Fonctionnalités

-  Enregistrement et authentification utilisateur
-  Envoi de prompts structurés avec différentes options
-  Gestion des sessions (connexion / déconnexion)
-  Options disponibles : `scan`, `enum`, `footprint`

---

##  Installation
- Clonez ce dépôt.

- Le fichier requirements.txt contient les détails sur les dépendances à installer et la version minimale à utiliser :
  - `requests>=2.32.4`  
  - `rich>=14.0.0` 
  
Commande: pip install -r requirements.txt (nom du fichier) pour installer automatiquement les dependances

---

##  Configuration du PATH
  export PATH="/media/sf_formation_MOUSSOURIS/Moussourisgpt-backend/mousourisgpt-PythonCli:$PATH" 
/media/sf_formation_MOUSSOURIS/Moussourisgpt-backend/mousourisgpt-PythonCli: répresente emplacement de mon repertoire

Rechargez votre shell :

## Pour ZSH 
    source ~/.zshrc
    
## Pour BASH 
    source ~/.bashrc

##  Mode d'utilisation

## Créer un compte 
    msgpt register

## Se connecter 
    msgpt login

## Se déconnecter :
    msgpt logout

 Envoyer un prompt :

**msgpt run -o "option" -p "prompt"**

### Options possibles:

scan : pour analyser un réseau

enum : pour faire de l’énumération

footprint : pour  recueillir des données précieuses sur l'infrastructure, les technologies utilisées.

### Exemples d'utilisation

 1. Scanner un réseau :
    msgpt run -o "scan" -p "scanne le réseau 192.168.1.0"

3. Enumération de ports :
    msgpt run "enum" "énumère les ports ouverts sur l’hôte 10.0.0.5"

4. Profiling système :
    msgpt run "footprint" "récupère les informations système de la machine cible"











