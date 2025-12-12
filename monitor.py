import psutil
from datetime import datetime
import time 
import platform
import socket
import sys
import os
from pathlib import Path


def cpu_infos():
 global core
 global frequency
 global cpu_usage
 core=psutil.cpu_count(())
 print(f"Nombre de coeurs: {core}")
 frequency=psutil.cpu_freq(())
 print("Fréquence du CPU: ", frequency.max)
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
 global ip_adress
 global uptime_formatted
 global currenttimeformated
 global version_fuse
 machine_name=socket.gethostname()
 print(f"Nom de la machine: {machine_name}")
 machine_system=platform.system()
 vers=platform.version()
 version_part = vers.split()[:2]
 version_fuse = " ".join(version_part)
 print(f"Système d'exploitation: {machine_system, vers}")
 psutil.boot_time()
 boot_time=psutil.boot_time() 
 uptime_seconds = time.time() - boot_time
 currenttimeformated=datetime.now().strftime("%H:%M:%S")
 
 hrs = int(uptime_seconds // 3600)
 mins = int((uptime_seconds % 3600) // 60)
 secs = int(uptime_seconds % 60)
 uptime_formatted = f"{hrs:02d}:{mins:02d}:{secs:02d}"
  
 connected_users=psutil.users()
 print(f"Nombres d'utilisateurs connectés: {connected_users}")
 ip_adress=socket.gethostbyname(machine_name)
 print(f"Adresse IP: {ip_adress}")


def userslist():
   with open("/etc/passwd") as f:
      return [line.split(":")[0] for line in f
              if int(line.split(":")[2]) >=1000 and line.split(":")[0] != "nobody"]
   usernames_str = ", ".join(usernames)
   return usernames_str

   



def processes():
   global proces
   global process_1, process_2, process_3
   global process_1_percent, process_2_percent, process_3_percent
   listproces = []
   
   for proces in psutil.process_iter():
      proces.cpu_percent()
   for proces in psutil.process_iter(attrs=["name", "pid", "username", "cpu_percent"]):
      listproces.append(proces.info)
      
   listproces = sorted(listproces, key=lambda p: p["cpu_percent"], reverse=True)
   
   if len(listproces) > 0:
      process_1 = f'{listproces[0]["name"]} ({listproces[0]["cpu_percent"]:.1f}% CPU)'
      process_1_percent = listproces[0]["cpu_percent"]
   else:
      process_1 = ""

   if len(listproces) > 1:
      process_2 = f'{listproces[1]["name"]} ({listproces[1]["cpu_percent"]:.1f}% CPU)'
      process_2_percent = listproces[1]["cpu_percent"]
   else:
      process_2 = ""

   if len(listproces) > 2:
      process_3 = f'{listproces[2]["name"]} ({listproces[2]["cpu_percent"]:.1f}% CPU)'
      process_3_percent = listproces[2]["cpu_percent"]
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


def file_analysis():
    directory = Path("/home/nico/Documents/B1/Challenge/TripleA/v2")
  
    numeration = {}

    for item in directory.iterdir():
      if item.is_file():
         extens=item.suffix
         numeration[extens]=numeration.get(extens, 0) +1
      
      elif item.is_dir():
         print("Dossier :", item.name)
         
    results = ""

    total = sum(numeration.values())
    for ext, count in numeration.items():
        percent = (count / total) * 100
        results += f"{count} fichiers {ext}, {percent:.2f}% du total.</br>"
    results += f"Il y a {total} fichier au total."
    return results



while True:
    cpu_infos()
    userslist()
    memory_infos()
    systems_infos()
    processes()
    processes_ram()
    file_analysis_results = file_analysis()
    usernames_str=userslist()
    username_list=", ".join(usernames_str)
    time.sleep(0)
    
    html = open("template.html").read()
    html = html.replace("{{ core }}", str(core))
    html = html.replace("{{ core_frequency }}", str(frequency.current))
    html = html.replace("{{ ram_used }}", str(ram_usedformat))
    html = html.replace("{{ memory }}", str(ram_totalformat))
    html = html.replace("{{ ram_active }}", str(rampourcentformat))
    html = html.replace("{{ name_machine }}", (machine_name))
    html = html.replace("{{ name_os }}", (machine_system))
    html = html.replace("{{ systeme_uptime }}", str(uptime_formatted))
    html = html.replace("{{ systeme_user_count }}", str(username_list))
    html = html.replace("{{ network_ip }}", str(ip_adress))
    html = html.replace("{{ process_1 }}", str(process_1))
    html = html.replace("{{ process_2 }}", str(process_2))
    html = html.replace("{{ process_3 }}", str(process_3))
    html = html.replace("{{ ram_1 }}", str(process_ram_1))
    html = html.replace("{{ ram_2 }}", str(process_ram_2))
    html = html.replace("{{ ram_3 }}", str(process_ram_3))
    html = html.replace("{{ generated_timestamp }}", str(currenttimeformated))
    html = html.replace("{{ files_stats }}", file_analysis_results)
    html = html.replace("{{ cpu_usage }}", str(cpu_usage))
    html = html.replace("{{ process_percent_1 }}", str(process_1_percent))
    html = html.replace("{{ process_percent_2 }}", str(process_2_percent))
    html = html.replace("{{ process_percent_3 }}", str(process_3_percent))
    html = html.replace("{{ version }}", str(version_fuse))

    with open("index.html", "w") as fp:
       fp.write(html)




