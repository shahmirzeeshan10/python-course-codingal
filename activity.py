folder=open("grocery-list.txt","r")
n=int(input("how many charecters do you want to preview"))
print(folder.read(n))
folder.close()
folder=open("grocery-list.txt","r")
line=folder.readlines()
folder.close()
print("total lines in the folder are ",len(line))
for i in line:
    print(i.strip())
word=input("skip lines which start with:")
for i in line:
    if i.startswith(word):
        print("skip this line",i.strip())
    else:
        print("keep these lines", i.strip())
folder=open("old lines.txt","w")
for i in range(0,len(line),2):
    folder.write(line[i])
folder.close()
print("old lines are saved")

 
              
    
