import requests
import os

file = "downloaded.txt"
file_exists = os.path.exists(file)
if file_exists == False:
    print("File does not exist.\nWriting file")
    url = "https://raw.githubusercontent.com/Mherstik/Automation-grp1/main/Grouplist-singleline.txt"
    resp1 = requests.get(url).content.decode()
    #resp = requests.get(url)
    #resp = resp.content.decode()
    #print(resp1)

    with open(file, "w") as f:
        f.write(resp1)
        #f.close()
else:
    print("File",file,"exists.\nNot writing")



# 
# with open('Grouplist-singleline.txt','r') as fp:
#     newline = fp.read()
# 
# print(newline)
# 
# print(type(newline))
# print(len(newline))