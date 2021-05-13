class Level():
    def __init__(self):
        self.fat_timer = 0
        self.health_timer = 0
    
    def next_level(self):
        self.fat_timer -= 50
        self.health_timer += 200
