import json

class QuestManager:
    def __init__(self, path_to_file):
        self.all_quests = {}
        self.completed_quests = []
        self.load_quests(path_to_file)

    def load_quests(self, path):
        try:
            with open (path, 'r') as file:
                self.all_quests = json.load(file)
            print("[QuestManager]: Successfuly loaded quests file!") #DEBUG
        except Exception as e:
            print(f"[QuestManager]: Can't load quests file: {e}") #DEBUG

    def get_quest(self, quest_id):
        return self.all_quests[str(quest_id)]
    
    def quest_completed(self, quest_id):
        self.is_completed = True
        # self.completed_quests.append(quest_id)
        print(f"[QuestManager]: Completed quest: {quest_id}") #DEBUG
    
    def is_quest_completed(self, quest_id):
        if quest_id in self.completed_quests:
            return True
        
    def accept_quest(self, quest_id):
        print(f"[QuestManager]: Accepted quest: {self.all_quests[str(quest_id)]['id'], self.all_quests[str(quest_id)]['description']}")
