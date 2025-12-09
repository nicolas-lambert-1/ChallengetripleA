import psutil
from datetime import datetime
import time 
import platform
import socket
import sys
import pandas as pd
import os
from pathlib import Path


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
 global uptime_formatted
 global currenttime
 machine_name=socket.gethostname()
 print(f"Nom de la machine: {machine_name}")
 machine_system=platform.system()
 vers=sys
 print(f"Système d'exploitation: {machine_system, vers.version_info}")
 psutil.boot_time()
 boot_time=psutil.boot_time() 
 uptime_seconds = time.time() - boot_time
 currenttime=datetime.now()

 hrs = int(uptime_seconds // 3600)
 mins = int((uptime_seconds % 3600) // 60)
 secs = int(uptime_seconds % 60)
 uptime_formatted = f"{hrs:02d}:{mins:02d}:{secs:02d}"
  
 connected_users=len(psutil.users())
 print(f"Nombres d'utilisateurs connectés: {connected_users}")
 ip_adress=socket.gethostbyname(machine_name)
 print(f"Adresse IP: {ip_adress}")

def processes():
   global proces
   global process_1, process_2, process_3
   
   listproces = []
   
   for proces in psutil.process_iter():
      proces.cpu_percent()
   for proces in psutil.process_iter(attrs=["name", "pid", "username", "cpu_percent"]):
      listproces.append(proces.info)
      
   listproces = sorted(listproces, key=lambda p: p["cpu_percent"], reverse=True)
   
   if len(listproces) > 0:
      process_1 = f'{listproces[0]["name"]} ({listproces[0]["cpu_percent"]:.1f}% CPU)'
   else:
      process_1 = ""

   if len(listproces) > 1:
      process_2 = f'{listproces[1]["name"]} ({listproces[1]["cpu_percent"]:.1f}% CPU)'
   else:
      process_2 = ""

   if len(listproces) > 2:
      process_3 = f'{listproces[2]["name"]} ({listproces[2]["cpu_percent"]:.1f}% CPU)'
   else:
      process_3 = ""
   
   print(process_1)
   print(process_2)
   print(process_3)


def processes_ram():
   global proces_ram
   global process_ram_1, process_ram_2, process_ram_3
   
   listprocesram = []
   
   for proces_ram in psutil.process_iter():
      proces_ram.memory_percent()
   for proces_ram in psutil.process_iter(attrs=["name", "pid", "username", "memory_percent"]):
      listprocesram.append(proces_ram.info)
   
   listprocesram = sorted(listprocesram, key=lambda p: p["memory_percent"], reverse=True)
   
   if len(listprocesram) > 0:
      process_ram_1 = f'{listprocesram[0]["name"]} ({listprocesram[0]["memory_percent"]:.1f}% RAM)'
   else:
      process_ram_1 = ""

   if len(listprocesram) > 1:
      process_ram_2 = f'{listprocesram[1]["name"]} ({listprocesram[1]["memory_percent"]:.1f}% RAM)'
   else:
      process_ram_2 = ""

   if len(listprocesram) > 2:
      process_ram_3 = f'{listprocesram[2]["name"]} ({listprocesram[2]["memory_percent"]:.1f}% RAM)'
   else:
      process_ram_3 = ""
   

   print(process_ram_1)
   print(process_ram_2)
   print(process_ram_3)


def get_connected_users():
    output = os.popen("who").read().strip()
    if output == "":
        return 1 
    return len(output.split("\n"))



def file_analysis():
    directory= Path("/home/nico/Documents")
    for item in directory.iterdir():
        if item.is_file():
            print("Fichier :", item.name, "Taille :", item.stat().st_size, "octets")
        elif item.is_dir():
            print("Dossier :", item.name)
    
    file_extension = {
    
    "txt":0,
    "jpg":0,
    "py":0,
    "pdf":0,
    }
   
    

    for item in directory.iterdir():
     if item.is_file():
       ext=item.suffix[1:]
       if ext in file_extension:
        file_extension[ext]+=1


while True:
    cpu_infos()
    memory_infos()
    systems_infos()
    processes()
    processes_ram()
    file_analysis()
    users_number = print(get_connected_users())
    time.sleep(3)
    
    html = open("template.html").read()
    html = html.replace("{{ core }}", str(core))
    html = html.replace("{{ ram_used }}", str(ram_usedformat))
    html = html.replace("{{ memory }}", str(ram_totalformat))
    html = html.replace("{{ ram_active }}", str(rampourcentformat))
    html = html.replace("{{ name_machine }}", (machine_name))
    html = html.replace("{{ name_os }}", (machine_system))
    html = html.replace("{{ systeme_uptime }}", str(uptime_formatted))
    html = html.replace("{{ systeme_user_count }}", str(users_number))
    html = html.replace("{{ network_ip }}", str(ip_adress))
    html = html.replace("{{ process_1 }}", str(process_1))
    html = html.replace("{{ process_2 }}", str(process_2))
    html = html.replace("{{ process_3 }}", str(process_3))
    html = html.replace("{{ ram_1 }}", str(process_ram_1))
    html = html.replace("{{ ram_2 }}", str(process_ram_2))
    html = html.replace("{{ ram_3 }}", str(process_ram_3))
    html = html.replace("{{ generated_timestamp }}", str(currenttime))
    with open("index.html", "w") as fp:
       fp.write(html)




