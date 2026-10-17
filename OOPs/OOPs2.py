class spotify_playlist:
    def __init__(self,name,genre):
        self.name=name
        self.genre=genre
        self.songs=[]
        print("playlist has been created!")
    def add_songs(self,songs):
        self.songs.append(songs)
        print("song has been added")
    def display(self):
        print("playlist is",self.name)
        print("playlist genre is",self.genre)
        print("playlist songs are",self.songs)
ob=spotify_playlist("shahmirs spotify","pop")
ob.add_songs("BABY SHARK")
while True:
    print("\n1 add songs")
    print("\n2 display songs")
    print("\n3 delete playlist")
    choice=input("enter your option")
    if choice=="1":
        songs=input("enter your song name")
        ob.add_songs(songs)
    elif choice=="2":
        ob.display(songs)
    elif choice=="3":
        del ob
        break
    else:
        print("invalid choice")
        
