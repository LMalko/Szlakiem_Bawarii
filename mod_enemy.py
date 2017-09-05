
# mod_enemy - custom mod, contains enemy data
# function enemy_settings(name = None, loc = None, lvl = None, gen = None) load specified or random oponent to main

import random

################################ Hero's enemies class:
class Enemy:
   def __init__(self, name, actualLife, level, act_armour, genre, location, attrib_dict, treasure_dict, specials_list, speach_list, dmg_list):
        self.name = name
        self.actualLife = actualLife
        self.level = level
        self.act_armour = act_armour # armour points - buffs enemy defend
        self.genre = genre
        self.location = location
        self.attrib_dict = attrib_dict
        self.treasure_dict = treasure_dict
        self.specials_list = specials_list
        self.speach_list = speach_list
        self.dmg_list = dmg_list
        self.attack = 0 # initial attack points
        self.defend = 0 # initial defend points
        self.courage = 0 # initial courage points  TODO

        # maxdrop determines what is max item drop from monster
        #...(f.ex. 3 = hero may recieve max 3 items (pieces) from dead monster )
        # default = 0 
        self.maxdrop = 0


        # maxdrop_lvl determines what is max item level that could be drop from dead monster
        # default = enemy.level+1
        self.maxdrop_lvl = self.level+1


        # enemy combat_attribute:
        # determines what enemy attribute is used in combat tests, it set by function:
        # combat_attribute_default(enemy = None) int his mod
        self.combat_attribute = None

 
        # ww. "location" przyjmuje wartość elementów listy (element = lvl mapy)
        # ...w ten sposób decydujemy, czy dany przeciwnik może się pojawić w danyn lvlu
def enemy_settings(name = None, loc = None, lvl = None, gen = None):
    '''
    Stores enemies data base. 
    Creates enemy and export to MAIN using specific arguments:
    name = imports by name, for expample: if name = "wilk", function exports object WOLF
    or
    if name (in function arguments) is not specified, enemy is generated by filters:
        location (loc, ex. loc = 2 - second map level),
        enemy level (lvl = 1,2,3...),
        genre (gen, ex. gen = "animal": it will choose between enemies with genre = "animal")
        then export to main 
    '''

    attrib_dict = {} # pusty słownik dla atrybutów przeciwników
    treasure_dict = {} # pusty słownik z miejscem na przedmioty u przeciwników (można to wykorzystać m.in. do "losowania łupu")
    specials_list = [] # pusty słownik z miejscem na cechy specjalne (możemy je wyświetlać w trakcie walki) - domyślnie pusta
    speach_list = [] # zawiera kwestie wypowiadane przez przeciwnika w czasie walki (możemy je losować :) ) - domyślnie pusta
    dmg_list = [] # contains min and max dmg ([min, max])
    # data in (...) are enemy:
    # name, life, level, xp4hero, genre, location (list), attrib_dict, treasure_dict, specials_list, speach_list

    #   Wilk
    wolf = Enemy(u"wilk",6, 1, 0, "animal", [1,2,3], attrib_dict, treasure_dict, specials_list, speach_list, [1,3])
    wolf.attrib_dict = {u"siła":1, "zwinność":2, "percepcja":3, "inteligencja":1, "siła woli":1}
    wolf.speach_list = [u"wrrrr", "auuuuuuuuuuuuu!"]
    wolf.specials_list = [u"szybki skubaniec!"]
    wolf.treasure_dict = {u"wilcza skóra":1}
    wolf.maxdrop = 0

    #   Szczurołak
    ratman = Enemy(u"szczurołak",3, 1, 0, "animal", [1,2], attrib_dict, treasure_dict, specials_list, speach_list, [1,2])
    ratman.attrib_dict = {u"siła":1, "zwinność":2, "percepcja":1, "inteligencja":1, "siła woli":1}
    ratman.speach_list = [u"wrrrr", "(sapie)"]
    ratman.specials_list = [u"dość szybki jest!"]
    ratman.maxdrop = 0

    # Goblin
    goblin = Enemy(u"goblin",10, 1, 1, "beast", [1,2,3], attrib_dict, treasure_dict, specials_list, speach_list, [1,4])
    goblin.attrib_dict = {u"siła":1, "zwinność":2, "percepcja":2, "inteligencja":1, "siła woli":1}
    goblin.speach_list = [u"Ja ubić ludzia!", "Ty trup!"]
    goblin.treasure_dict = {u"popsuta ryba":1}
    goblin.maxdrop = 2

     # Skurczybyk
    skurczybyk = Enemy(u"skurczybyk",13, 2, 1, "human", [1,2], attrib_dict, treasure_dict, specials_list, speach_list, [2,5])
    skurczybyk.attrib_dict = {u"siła":2, "zwinność":2, "percepcja":2, "inteligencja":1, "siła woli":1}
    skurczybyk.speach_list = [u"Ah, co tam masz w sakiewce?", "Złoto albo śmierć!"]
    skurczybyk.treasure_dict = {u"jantar":random.randint(1,3), "pierścień skurczybyka":1, "nóż":1} # ring for optional quest
    skurczybyk.speach_list = [u"Co tam masz w sakiewce?", "Złoto albo śmierć!", "Kto zadziera ze skurczybykiem, ten frajer!"]
    skurczybyk.specials_list = [u"Straszna menda", "Lepkie ręce"]
    skurczybyk.maxdrop = 2



    #   Miś
    bear = Enemy(u"niedźwiedź",30, 2, 2, "animal", [1,2,3], attrib_dict, treasure_dict, specials_list, speach_list, [3,7])
    bear.attrib_dict = {u"siła":4, "zwinność":1, "percepcja":2, "inteligencja":1, "siła woli":1}
    bear.speach_list = [u"Mrrrrr!", "Wrrrrrr!", "Rgh!"]


    #   Ogr (strong opponent)
    ogr = Enemy(u"ogr", 65, 3, 2, "beast", [2, 3, 4], attrib_dict, treasure_dict, specials_list, speach_list, [5,10])
    ogr.attrib_dict = {u"siła":4,"zwinność":1, "percepcja":1, "inteligencja":1, "siła woli":1}
    ogr.treasure_dict = {u"złoto":random.randint(1,20)} # placki???
    ogr.speach_list = [u"Czo to...", "yyyy...", "ja stracha ty..", "Wont mi stomd!", "<czka>"]
    ogr.specials_list = [u"Okrótna siła", "Głupi jak but", "Niezdara", "Zgniata czaszki"]
    ogr.maxdrop = 4

    #   Troll (strong opponent)
    troll = Enemy(u"troll", 75, 3, 4, "beast", [2, 3, 4], attrib_dict, treasure_dict, specials_list, speach_list, [2,12])
    troll.attrib_dict = {u"siła":5, "zwinność":1, "percepcja":1, "inteligencja":1, "siła woli":2}
    troll.treasure_dict = {u"złoto":random.randint(1,100), "rubiny":random.randint(0,12)}
    troll.speach_list = [u"U mnie głód! Ty smakowite!", "Ty grube!", "Ty ładne i smaczne!", "Argh!", "(warczy)"]
    troll.specials_list = [u"Kamienna skóra", "Niezdara", "Okrótna siła"]
    troll.maxdrop = 4

    #   Olbrzym górski
    mountain_giant = Enemy(u"olbrzym górski", 99, 4, 5, "beast", [3, 4], attrib_dict, treasure_dict, specials_list, speach_list, [7,15])
    mountain_giant.attrib_dict = {u"siła":6, "zwinność":1, "percepcja":1, "inteligencja":1, "siła woli":2}
    mountain_giant.treasure_dict = {u"złoto":random.randint(1,100), "diamenty":random.randint(1,3), "olbrzymia maczuga": 1}
    mountain_giant.speach_list = [u"Ty chcieć mi odebrać błyszczące?!", "Twój czerep nada się na ząb!", "(straszny ryk)", "Gnieść, łupić!"]
    mountain_giant.specials_list = [u"Olbrzymia wytrzymałość", "Okrótna siła"]
    mountain_giant.maxdrop = 5



    #################################### quest/special enemies: - special monsters has Capitalic in names (Zły Miś, Głupi Jaś) 

    #   Zły miś (QUEST in lvl 1)
    bear_special_quest = Enemy("Zły Miś",30, 2, 2, "animal, special" , [2], attrib_dict, treasure_dict, specials_list, speach_list, [1,4])
    bear_special_quest.attrib_dict = {"siła":4, "zwinność":1, "percepcja":1, "inteligencja":2, "siła woli":2}
    bear_special_quest.treasure_dict = {"liczydło":1, "lina pomiarowa":1}
    bear_special_quest.speach_list = [u"Ten gupi myśliwy Cię przysłał? Figa, niczego Ci nie dam!"]
    bear_special_quest.specials_list = [u"Ten miś mówi!", "Na szyi ma linę, a pod ogonem liczydło"]


############## list with all enemies - we use this in functions below:
    # na razie potrzeba ręcznie dopisywać każdego przeciwnika, ale to raczej nie problem
    # mogę po każdym przeciwniku robić list.append, ale nie ma tego tak dużo, żeby kompa obciążać ;)
    enemies_all_list = [wolf, ratman, goblin, skurczybyk, bear, bear_special_quest, ogr, troll, mountain_giant]


    # if enemy name was specified, it will export enemy by given name:
    enemy_exported_to_main = ''
    if name != None:
        
        for element in enemies_all_list:
            if element.name == name:
                enemy_exported_to_main = element

        return enemy_exported_to_main


    # if enemy name wasn't specified, it will export random enemy (random using optional filters - level, location, genre):
    else:
        enemy_random_list = []
         # temporary helper list
        tmp_lvl = 0 # helps in loop below:
        for element in enemies_all_list:
            if (loc in element.location or loc == None) and (lvl == element.level or lvl == None) and (gen == element.genre or gen == None):
                enemy_random_list.append(element)
        

        # export random enemy to main function:
        enemy_rnd_exported_to_main = enemy_random_list[random.randint(0, len(enemy_random_list)-1)]
        
        return enemy_rnd_exported_to_main
        # loc = None, lvl = None, gen = None


    #   # name, life, level, attrib_dict, treasure_dict, genre, xp4hero, specials, speach, location
    #wolf = Enemy("wilk",10, 1, attrib_dict,treasure_dict,"animal",5,None,"Wrrrrr!",


def attack_points_calc(enemy = None):
    ''' calculates enemy attack ability '''
    enemy.attack = 2*enemy.attrib_dict["siła"]+2*enemy.attrib_dict["zwinność"]+enemy.attrib_dict["inteligencja"]
    
    return enemy.attack


def defend_points_calc(enemy = None):
    ''' calculates enemy defend ability '''
    enemy.defend = 3*enemy.attrib_dict["zwinność"]+enemy.attrib_dict["siła"]+enemy.attrib_dict["inteligencja"]+enemy.act_armour
    
    return enemy.defend


def combat_attribute_default(enemy = None):
    '''set default value of combat_attribute'''
    if enemy.attrib_dict["siła"] >= enemy.attrib_dict["zwinność"]:
        enemy.combat_attribute = "siła"
        return enemy.combat_attribute
    else:
        enemy.combat_attribute = "zwinność"
        return enemy.combat_attribute

def enemy_info(enemy = None):    
    '''display shot info about enemy (imported from enemy specials_list and speach_list)'''
    if len(enemy.speach_list) > 0:
        print(enemy.name,"do Ciebie:",'"'+"\x1b[6;30;44m"+enemy.speach_list[random.randint(0, len(enemy.speach_list)-1)]+ "\x1b[0m"+'"'+'\n')
    if len(enemy.specials_list) > 0:
        print(enemy.name,"ma właściwość:",enemy.specials_list[random.randint(0, len(enemy.specials_list)-1)])



