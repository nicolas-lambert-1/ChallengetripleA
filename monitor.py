import psutil
import datetime
import time 
import platform
import socket
import sys
from pathlib import Path
import pandas as pd


def cpu_infos():
 global core
 core=psutil.cpu_count(())
 print(f"Nombre de coeurs: {core}")
 frequency=psutil.cpu_freq(())
 print("Fréquence du CPU: ", frequency.current)
 cpu_usage= psutil.cpu_percent(interval=1)
 print(f"Pourcentage d'utilisation du CPU: {cpu_usage}%")

def memory_infos():
 global ram
 global ram_usedformat
 global ram_totalformat
 global rampourcentformat
 ram=psutil.virtual_memory()
 
 ram_used1=ram.used/(1024**3)
 ram_usedformat= f"{ram_used1:.2f}"
 
 ram_total1=ram.total/(1024**3)
 ram_totalformat= f"{ram_total1:.2f}"
 
 rampourcent=ram.active/ram.total*100
 rampourcentformat= f"{rampourcent:.2f}"
 
 print(f"RAM utilisée en Gb: {ram_usedformat} GB")
 print("RAM totale: ", ram_total1, "GB")
 print("Pourcentage d'utilisation de la RAM: ", rampourcent, "GB")

def systems_infos():
 global machine_name
 global machine_system
 global boot_time
 global connected_users
 global ip_adress
 machine_name=socket.gethostname()
 print(f"Nom de la machine: {machine_name}")
 machine_system=platform.system()
 vers=sys
 print(f"Système d'exploitation: {machine_system, vers.version_info}")
 psutil.boot_time()
 boot_time=datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%H:%M-%S")
 print(f"Heure de démarrage du système: {boot_time}")
 
 
 
 connected_users=psutil.users()
 print(f"Nombres d'utilisateurs connectés: {connected_users}")
 ip_adress=socket.gethostbyname(machine_name)
 print(f"Adresse IP: {ip_adress}")

def processes():
   global proces
   global proces_ram
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
  
 numeration={}
 
 for item in directory.iterdir():
     if item.is_file():
        extens=item.suffix
        numeration[extens]=numeration.get(extens, 0) +1
     
     elif item.is_dir():
        print("Dossier :", item.name)
     
 for extens, total in numeration.items():
        print(f"Il y'a {total} fichiers {extens}")
 
 file_extension = {}
 
 for item in directory.iterdir():
     if item.is_file():
        ext=item.suffix[1:]
        if ext:
           file_extension[ext]=file_extension.get(ext, 0) +1
           
 total=sum(file_extension.values())

 for ext, count in file_extension.items():
        percent=(count/total)*100
        print(f"{count} fichiers .{ext}, {percent:.2f}% du total")
 print(f"Il y a {total} fichier au total")
    


    




while True:
    cpu_infos()
    memory_infos()
    systems_infos()
    processes()
    file_analysis()
    time.sleep(3)
    
    html = open("template.html").read()
    html = html.replace("{{ core }}", str(core))
    html = html.replace("{{ ram_used }}", str(ram_usedformat))
    html = html.replace("{{ memory }}", str(ram_totalformat))
    html = html.replace("{{ ram_active }}", str(rampourcentformat))
    html = html.replace("{{ name_machine }}", (machine_name))
    html = html.replace("{{ name_os }}", (machine_system))
    html = html.replace("{{ systeme_uptime }}", str(boot_time))
    html = html.replace("{{ systeme_user_count }}", str(connected_users))
    html = html.replace("{{ network_ip }}", str(ip_adress))
    html = html.replace("{{  }}", str(proces))
    html = html.replace("{{  }}", str(proces_ram))
    html = html.replace("{{ generated_timestamp }}", str())
    with open("index.html", "w") as fp:
       fp.write(html)




