import requests
#########################################
print('''
:::        ::::::::::: :::    ::: :::::::::: 
:+:            :+:     :+:   :+:  :+:        
+:+            +:+     +:+  +:+   +:+        
+#+            +#+     +#++:++    +#++:++#   
+#+            +#+     +#+  +#+   +#+        
#+#            #+#     #+#   #+#  #+#        
########## ########### ###    ### ########## 
''') 
print("WELCOME TO BOT LIKES: \n")
uidd = int(input("Enter uid for send 100 likes  In one day: \n"))
keyy = "c4-kj00llkaj"
url = f"https://mahmoud-aheqh0b3csgagdf4.eastus-01.azurewebsites.net/likes?uid={uidd}&key={keyy}"
response = requests.get(url)
status = response.status_code
if status == 200:
    data = response.text
    print(data)
else:
    print(f"Error with server!: {status}")  