import psutil
import datetime
import time 
import platform
import socket
import sys
import os
from pathlib import Path


def cpu_infos():
 core=psutil.cpu_count(())
 print(f"Nombre de coeurs: {core}")
 frequency=psutil.cpu_freq(())
 print("Fréquence du CPU: ", frequency.current)
 cpu_usage= psutil.cpu_percent(interval=1)
 print(f"Pourcentage d'utilisation du CPU: {cpu_usage}%")



def memory_infos():
 ram=psutil.virtual_memory()
 print("RAM utilisée en Gb: ", ram.used/(1024**3),"GB")
 print("RAM totale: ", ram.total/(1024**3),"GB")
 print("Pourcentage d'utilisation de la RAM: ", ram.active/ram.total*100, "%")

def systems_infos():
 machine_name=socket.gethostname()
 print(f"Nom de la machine: {machine_name}")
 machine_system=platform.system()
 vers=sys
 print(f"Système d'exploitation: {machine_system, vers.version_info}")
 psutil.boot_time()
 boot_time=datetime.datetime.fromtimestamp(psutil.boot_time())
 boot_time=datetime.datetime.fromtimestamp(psutil.boot_time())
 print("Heure de démarrage du système: ", boot_time.strftime("%Hh%Mm-%Ss"))
 up_time=datetime.datetime.now() - boot_time
 print(f"Temps écoulé depuis démarrage: {up_time} h")
 

 connected_users=psutil.users()
 print(f"Nombres d'utilisateurs connectés: {connected_users}")
 ip_adress=socket.gethostbyname(machine_name)
 print(f"Adresse IP: {ip_adress}")

def processes():
 for proces in psutil.process_iter():
  proces.cpu_percent()
 for proces in psutil.process_iter(attrs=["name", "pid", "username", "cpu_percent"]):
  print(proces.info)

 for proces_ram in psutil.process_iter():
    proces_ram.memory_percent()
 for proces_ram in psutil.process_iter(attrs=["name", "pid", "username", "memory_percent"]):
  print(proces_ram.info)

def file_analysis():
 
 directory= Path("/home/mahira/Documents")
 
 for item in directory.iterdir():
     if item.is_file():
        print("Fichier :", item.name, "Taille :", item.stat().st_size, "octets")
     elif item.is_dir():
        print("Dossier :", item.name)
 
 file_extension = {}
 
 for item in directory.iterdir():
     if item.is_file():
        ext=item.suffix[1:]
        file_extension[ext]=file_extension.get(ext, 0)

 total=sum(file_extension.values())
 if total==0:
    print("Aucun fichier dans ce dossier")
 else:
    for ext, count in file_extension.items():
     percent=(count/total)*100
     print(f"{ext}: {count} fichiers, {percent:.2f}% du total")
    


    


        
            
while True:
    cpu_infos()
    memory_infos()
    systems_infos()
    processes()
    file_analysis()
    time.sleep(3)



