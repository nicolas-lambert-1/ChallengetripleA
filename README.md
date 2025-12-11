# 💻 Challenge Triple A - Dashboard de Monitoring

## Sommaire

 - [Description du projet](#description-du-projet)
 - [Prérequis](#prérequis)
 - [Installation](#installation-et-commandes)
 - [Commandes pour installer les dépendances](#commandes-pour-installer-les-dépendances)
 - [Utilisation](#utilisation)
 - [Fonctionnalités](#fonctionnalités)
 - [Screenshot](#screenshot)
 - [Difficultés rencontrées](#difficultés-rencontrées)
 - [Améliorations possibles](#améliorations-possibles)
 - [Auteurs](#auteurs)






## Description du projet

Ce projet a été réalisé dans le cadre du *Challenge Triple A* :  
Administration, Algorithmique et Affichage.  
L’objectif est de créer un **outil de monitoring en temps réel** pour une machine Linux.  


Le script `monitor.py` récupère des informations système grâce au module `psutil` puis génère une page HTML (`index.html`) à partir d’un template (`template.html`).  
Le dashboard affiche en continu :

- Les informations CPU  
- La mémoire utilisée  
- Le système et l’uptime  
- Le réseau  
- Les processus les plus gourmands  
- Une analyse automatique d’un dossier avec statistiques de fichiers  

L’interface est rafraîchie automatiquement et permet de visualiser l’état de la machine de manière simple.




## Prérequis

- Ubuntu 22.04 minimum  
- Python 3.x  
- Modules Python :
  - `psutil`
  - `pandas`
  - `pathlib`
  - `socket`, `platform`, `sys`, etc. (inclus dans Python)
- Un template HTML et CSS
- Une VM

---


## Installation et Commandes

```bash
  git clone https://github.com/nicolas-lambert-1/ChallengetripleA
  cd ChallengetripleA
```


## Commandes pour installer les dépendances
![Dépendances](https://github.com/nicolas-lambert-1/ChallengetripleA/blob/Image/Modules.png)
## Utilisation

📍 Comment lancer le script
python3 monitor.py

```bash
python3 monitor.py
```
📍Le script :
  - Exécute les fonctions de récupération système
  - Met à jour le HTML toutes les 3 secondes
  - Écrit un fichier index.html contenant :
    - `CPU`
    - `RAM`
    - `System infos`
    - `Processus CPU/RAM`
    - `Types de fichiers du dossier analysé`




---


📍 Ouvrir index.html dans le navigateur

Tape simplement :

```bash
python -m webbrowser index.html
```
dans un navigateur (Firefox, Chrome…).

## Fonctionnalités

🔥 CPU

- Nombre de cœurs
- Fréquence actuelle
- % d’utilisation du CPU
- Top 3 des processus qui consomment le plus de CPU

🧠 Mémoire

- RAM totale
- RAM utilisée en GB
- Pourcentage de RAM active

🖥️ Système

- Nom de la machine
- Système d'exploitation
- Heure actuelle
- Uptime
- Nombre d’utilisateurs connectés
- Adresse IP locale

📁 Analyse de fichiers

- Analyse du dossier choisi avec :

   - `Comptage des fichiers .txt, .py, .pdf, .jpg`
   - `Total de fichiers rencontrés`
   - ` Pourcentage de chaque type de fichier`

🧵 Processus (RAM)

- Top 3 des processus utilisant le plus de RAM




## Screenshot

![meta](https://github.com/nicolas-lambert-1/ChallengetripleA/blob/Image/Biblio_w3.png)
![dashboard](https://github.com/nicolas-lambert-1/ChallengetripleA/blob/Image/Dashboard.png)



## Difficultés rencontrées

- Nicolas à corrompu ma branche python
- Difficultés de compatiblité avec MacOs 
- Formater l'affichage str des variables
- Triage(top 3) des processus 
- Gestion du templating HTML (remplacement automatique des valeurs)
- Jauge Java

## Améliorations possibles

- Ajouter la charge système (load average 1/5/15)
- Afficher l’utilisation de chaque cœur CPU individuellement
- Scanner les sous-dossiers de manière récursive
- Afficher l’espace disque utilisé
- Un CSS plus poussé





## Auteurs

- [@nicolas-lambert-1](https://github.com/nicolas-lambert-1)
- [@mahira-manico](https://github.com/mahira-manico)
- [@marion-ory](https://github.com/marion-ory)


