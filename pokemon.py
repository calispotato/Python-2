"""Pokemon Class/Interface"""

class Pokemon():
    level = 1
    xp = 0
    hight = 0
    weight = 0
    speed = 0
    hp = 0
    attack = 0
    special_attack = 0
    defense = 0
    special_defence = 0
    type1 = ""
    type2 = ""
    usable_moves = []
    moves = []

    def choose_move(self,move):
        if move in usable_moves:
            self.move = move

    def attack(self,target):
        """Resolve each attack exactly as done in game"""
        A = target.level
        B = self.attack
        if self.move.is_special:
            B = self.special_attack
            D = self.special_defense
        C = self.move.power
        X = 1
        if self.move.type in [self.type1,self.type2]:
            X = 1.5
        #TODO resolve Y
        # ((2A/5+2)*B*C)/D)/50)*X)*Y/10)*Z)/255
        
class Charizard(Pokemon):
    level = 36
    hight = 1.70
    weight = 90.5
    speed = 100
    hp = 78
    attack = 87
    special.attack = 
    defense =
    special =
