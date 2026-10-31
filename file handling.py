folder=open("grocery-list.txt","w")
folder.write("cookies\nstrawberries\nchocolate")
folder.close()
print("my grocery list is complete")

folder=open("grocery-list.txt","r")
print(folder.read())
folder.close()

folder=open("grocery-list.txt","r")
shahmir=folder.readlines()
print("total items in your grocery list",len(shahmir))
folder.close()
folder=open("grocery-list.txt","a")
folder.write("\nmilk\npopcorn")
print("your items have been added")
folder.close()
folder=open("grocery-list.txt","r")
folder.read()
print("this is your updated grocery list")
folder.close()




