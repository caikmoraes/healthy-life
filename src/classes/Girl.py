from classes.Character import Character
import glob

class Girl(Character):
    def __init__(self, name):
        self.walkingUp = glob.glob('images/girl/girl_up*.png')
        self.walkingLeft = glob.glob('images/girl/girl_left*.png')
        self.walkingDown = glob.glob('images/girl/girl_down*.png')
        self.walkingRight = glob.glob('images/girl/girl_right*.png')
        super(Girl, self).__init__(name, self.walkingUp, self.walkingLeft, self.walkingDown, self.walkingRight)