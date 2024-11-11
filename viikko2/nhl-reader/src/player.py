class Player:
    def __init__(self, dict):
        self.name = dict['name']
    
    def __str__(self):
        return self.name
