class QuestRoom:
    def __init__(self,name:str,level:int,players_limit:int):
        self.name=name
        self.level=level
        self.players_limit=players_limit
        self.players=[]
        self.status="waiting"
        self.events_log=[]

    def start(self):
        if len(self.players) == 0:
            return "Room is empty"
        else:
            self.status="active"
            self.events_log.append("Quest started")
            return f"Quest {self.name} started with {len(self.players)} players!"

    def add_player(self,player):
        if player in self.players:
            return f"player {player} exists"
        else:
            if self.is_full():
                return "room is full"
            else:
                self.players.append(player)
                self.events_log.append(f"Player {player} joined")
                return f"Player {player} is add"

    def remove_player(self,player):
        if player in self.players:
            self.players.remove(player)
            self.events_log.append(f"Player {player} left")
            return f"player {player} has been removed"
        else:
            return "Player not found!"

    def is_full(self):
        return self.players_limit==len(self.players)

    def reset_room(self):
        self.players=[]
        self.status="finished"
        self.events_log.append("Room reset")
        return "Room reset!"

    def players_list(self):
        if len(self.players) == 0: 
            return "No players in the room"
        else:
            return self.players
        
    def __str__(self):
        return f"QuestRoom: {self.name} | Difficulty: {self.level} | Players: {len(self.players)}/{self.players_limit}"
    def show_log(self):
        if len(self.events_log)==0:
            return "No events yet"
        else:
            return self.events_log



room = QuestRoom("Піратський острів", 3, 4)

print(room)  
room.add_player("Олег")
room.add_player("Даша")
print(room.start())
print(room)

