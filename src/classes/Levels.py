class Level():
    def __init__(self, is_health):
        self.is_health = is_health
        self.timer = 0
    
    def set_timer(self):
        if self.is_health:
            self.timer += 100
        else:
            self.timer -= 200
