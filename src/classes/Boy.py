from classes.Character import Character
import glob

class Boy(Character):
    def __init__(self, name):
        self.walkingUp = glob.glob('images/boy/boy_up*.png')
        self.walkingLeft = glob.glob('images/boy/boy_left*.png')
        self.walkingDown = glob.glob('images/boy/boy_down*.png')
        self.walkingRight = glob.glob('images/boy/boy_right*.png')
        super(Boy, self).__init__(name, self.walkingUp, self.walkingLeft, self.walkingDown, self.walkingRight)