Description du projet

def userslist():
   global connected_users
   connected_users=[]
   with open("/etc/passwd/") as f :
      
   for u in psutil.users():
      connected_users.append(u.name)
   print("Utilisateurs connectés:", connected_users)
   return connected_users