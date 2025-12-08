import psutil
import datetime
import time



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
 print("Pourcentage d'utilisation de la RAM: ", ram.active/(1024**3),"GB")

def systems_infos():
 machine_name=psutil.users()
 print(f"Nom de la machine: {machine_name}")
 boot_hour=psutil.boot_time()
 print(f"Heure de démarrage du système: {boot_hour}")

while True:
    cpu_infos()
    memory_infos()
    systems_infos()
    time.sleep(3)



