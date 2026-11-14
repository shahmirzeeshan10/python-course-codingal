import os
with open("science notes.txt","r") as f:
    print(f.read())
with open("math notes.txt","r") as f:
    for line in f:
        words=line.split()
        print(len(words),"words")
content=""
with open("science notes.txt","r") as f:
    content+= f.read()
with open("math notes.txt","r") as f:
    content+="\n"+f.read()
if os.path.exists("all notes.txt"):
    print("file already exists")
with open("all notes.txt","w") as f:
    f.write(content)
print("notes have been successfully merged")
if os.path.exists("all notes.txt"):
    os.remove("all notes.txt")
print("file has been deleted bye bye")