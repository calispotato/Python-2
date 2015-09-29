"""A battle engine API (and storyeng plugin) for Pokemon-like battles"""

class SkilMon():
    uid = 0
    name = ""
    description = ""
    defense = 0
    attack = 0
    exp = 0
    happiness = 0
    hp = 0
    sp_attack = 0
    sp_defense = 0
    speed = 0
    total = 0
    evolves_at = 0
    spiecies = ""
    catch_rate = 0
    hight = 0
    width = 0
    mf_ratio = 0
    abilities = []
    moves = []
    types = []

class Move():
    uid = 0
    name = ""
    description = ""
    category = ""
    learn_type = ""
    power = 0
    acuracy = 0
    pp = 0
    learned_at = ""

class Abillity():
    uid = 0
    name = ""
    description = ""
    decription = ""

class Type():
    uid = 0
    name = ""
    description = ""

class Controller():
    
    def handle_battle(team1, team2):
        #TODO apply stats changes
        A = target
        B = self.attack
