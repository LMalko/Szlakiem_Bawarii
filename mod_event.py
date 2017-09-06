﻿# mod event contains event functions
#!/usr/bin/python3

import time, random, os, math
import mod_hero, mod_enemy, mod_items, mod_display, mod_npc



def priority_test(enemy = None, hero = None):
    '''
    who's attacker, who's defender
    '''
    mod_display.clear_screen()
    mod_display.display_enemy_vs_hero(enemy = enemy, hero = hero, attacker = None)
    # zwinność, percepcja i inteligencja have influence on this test:
    hero_test_stats = (int(hero.attrib_dict["zwinność"])+int(hero.attrib_dict["percepcja"])+
    int(hero.attrib_dict["inteligencja"]))
    enem_test_stats = (int(enemy.attrib_dict["zwinność"])+int(enemy.attrib_dict["percepcja"])+int(enemy.attrib_dict["inteligencja"]))
    print("Kto uzyskał inicjatywę? (test inicjatywy)\n")
    while True:
        test_var1 = hero_test_stats + enem_test_stats
        test_var2 = random.randint(1,test_var1)      
        print('\r\r'+hero.name+":", hero_test_stats)
        print('\r\r'+enemy.name+":", test_var2)
        if hero_test_stats > test_var2:
            print("\nRezultat:", end=''), mod_display.dot_loop()
            print("\n\natakuje",hero.name+'!')
            attacker = hero
            break
          
        elif hero_test_stats < test_var2:
            print("\nRezultat:", end=''), mod_display.dot_loop()
            print("\n\natakuje",enemy.name+'!')
            attacker = enemy
            break

    mod_display.pause()
    mod_display.clear_screen()

    return attacker


def win_fight(enemy = None, hero = None):
    print("Zwycięstwo,", enemy.name, "został pokonany! Sława i doświadczenie są Twoje, ...a może jeszcze jakiś łup bitewny?")
    if len(enemy.treasure_dict) > 0: # check if there are some treasures in enemy inventory
        mod_display.dot_loop()
        time.sleep(1)
        print("\nTak!\n")
        add_remove_items_dict = enemy.treasure_dict
        mod_display.display_looted_items(add_remove_items_dict) # display treasures from enemy inventory
        mod_hero.inventory_update(hero, add_remove_items_dict)

    mod_display.clear_screen()
    print("Może coś jeszcze?", end=''), mod_display.dot_loop()
    mod_display.pause()
    # and some random generated items:
    mod_items.treasure_generator(maxloops = enemy.maxdrop, maxitem_lvl = enemy.maxdrop_lvl, item_gen = None, hero = hero)
    mod_display.display_hero_chart(hero=hero)
    mod_display.pause()
    return hero

def rip(enemy = None, hero = None):
    print("Po heroicznej walce świat zapłakał,", enemy.name, "zabił bohatera o imieniu", hero.name+". RIP,", hero.name+"!")
    mod_display.display_hero_chart(hero = hero)
    mod_display.pause()
    mod_display.clear_screen()
    mod_display.game_over(hero = hero)

def counterattack(enemy = None, hero = None, attacker = None, attack = None):
    '''
    part of the fight mechanic (part of fight function) 
    '''
    mod_display.display_enemy_vs_hero(enemy = enemy, hero = hero, attacker = attacker)
    #attacker = priority_test(enemy = enemy, hero = hero) 
    # define attacker and defender:
    if attacker == hero: defender = enemy
    elif attacker == enemy: defender = hero

    print("\nkontratak!", end='')
    mod_display.dot_loop()
    counterattack_result = 0
    print('\n'+defender.name, " kontratakuje: rzuca",str(defender.attrib_dict[str(defender.combat_attribute)]),"razy kością K4:")
    damage = random.randint(defender.dmg_list[0], defender.dmg_list[1])
    for i in range(int(defender.attrib_dict[str(defender.combat_attribute)])):
        counterattack_var = random.randint(1,4)
        print((str(counterattack_var)),"      ", sep='', end='', flush=True), time.sleep(0.3)
        counterattack_result += counterattack_var
    print("\n\nRezultat:", end=''), mod_display.dot_loop()
    print('\n\n'+defender.name+':',counterattack_result,'+',defender.attack,"(atak):", counterattack_result+defender.attack)
    print(attacker.name+':', attack), time.sleep(0.3)
    if attack < counterattack_result+defender.attack:
        attacker.actualLife -= damage
        print(defender.name, "zadał obrażenia:", attacker.name, "stracił", damage, "pkt. życia")
        time.sleep(0.3)
        if defender == hero:
            hero.actualExp += damage
            print(hero.name+", zdobyto doświadczenie:", damage)
            
            return hero.actualExp


        if defender.actualLife < 0:
            defender.actualLife = 0
            combat_end = 1
            return combat_end


    else:
        print('\n'+attacker.name, "obronił się!")
        attacker_change = 1
        return attacker_change
            
            

def fight(enemy = None, hero = None, attacker = None):
    '''
    fight mechanic = hit
    '''

    # define attacker and defender:
    if attacker == hero: defender = enemy
    elif attacker == enemy: defender = hero 

    attacker_change = 0

    attack_result = 0
    defend_result = 0
    print(attacker.name, "atakuje: rzuca",attacker.attrib_dict[str(attacker.combat_attribute)],"razy kością K4:")
    for i in range(int(attacker.attrib_dict[str(attacker.combat_attribute)])):
        attack_var = random.randint(1,4)
        print((str(attack_var)),"      ", sep='', end='', flush=True), time.sleep(0.3)
        attack_result += attack_var
    time.sleep(0.3)
    print('\n'+defender.name, "broni się: rzuca",str(defender.attrib_dict["zwinność"]),"razy kością K4:")
    for i in range(int(defender.attrib_dict["zwinność"])):
        defend_var = random.randint(1,4)
        print((str(attack_var)),"      ", sep='', end='', flush=True), time.sleep(0.3)
        defend_result += defend_var
        
    print("\n\nRezultat:", end=''), mod_display.dot_loop()
    print('\n\n'+attacker.name+':',attack_result,'+',attacker.attack,"(atak):", attack_result+attacker.attack)
    print(defender.name+':',defend_result,'+',defender.defend,"(obrona):", defend_result+defender.defend)
    if attack_result+attacker.attack <= defend_result+defender.defend:
        print('\n'+defender.name, "obronił się!")
        mod_display.pause()
        attacker_change = 1
        #attacker = priority_test(enemy = enemy, hero = hero)
        #if float(defend_result+defender.defend) > (float(attack_result+attacker.attack)*1.2):
        attack = int(attack_result+attacker.attack)
        counterattack(enemy = enemy, hero = hero, attacker = attacker, attack = attack)
        return attacker_change

    else:
        damage = random.randint(attacker.dmg_list[0], attacker.dmg_list[1])
        print('\n'+attacker.name, "zadał obrażenia:", defender.name, "stracił", damage, "pkt. życia")
        time.sleep(0.3)
        defender.actualLife -= damage
        if attacker == hero:
            hero.actualExp += damage
            print(hero.name+", zdobyto doświadczenie:", damage)
        if defender.actualLife < 0:
            defender.actualLife = 0
            combat_end = 1
            time.sleep(0.3)
            return combat_end

def event_fight_spec_enemy(enemy = None, hero = None):
    '''
    event == fight with random enemy
    '''
    # random generate enemy (using filters):
    enemy = mod_enemy.enemy_settings(name = enemy, loc = None, lvl = None, gen = None)
    enemy.attack = mod_enemy.attack_points_calc(enemy = enemy)
    enemy.defend = mod_enemy.defend_points_calc(enemy = enemy)
    mod_enemy.combat_attribute_default(enemy = enemy)
    enemy.combat_attribute = mod_enemy.combat_attribute_default(enemy = enemy)
    # update hero attrinute:
    mod_hero.combat_attribute_default(hero = hero)
    mod_hero.attack_points_calc(hero)
    mod_hero.defend_points_calc(hero)
    print("\n\nZaraz, zaraz... Coś się dzieje!\n"), time.sleep(.3)
    print("Szykuj się do walki. Twój przeciwnik to", end=''), mod_display.dot_loop()
    
    print(' ',enemy.name.upper()+'!','\n')
    mod_display.pause()
    mod_display.clear_screen()
    # pętla walki:
    combat_end = 0
    while combat_end == 0 and hero.actualLife > 0 and enemy.actualLife > 0:
        # initiative test:
        attacker = priority_test(enemy = enemy, hero = hero)
        # define attacker and defender:
        if attacker == hero: defender = enemy
        elif attacker == enemy: defender = hero  
        attacker_change = 0 # if 1 = loop is break and we repeat initiative test
        while True:
            mod_display.display_enemy_vs_hero(enemy = enemy, hero = hero, attacker = attacker)
            attacker_change = fight(enemy = enemy, hero = hero, attacker = attacker)
            mod_display.pause()
            mod_display.clear_screen()
            if hero.actualLife < 1:
                rip(enemy = enemy, hero = hero)
                combat_end = 1
                break
            elif enemy.actualLife < 1:
                enemy.actualLife = 0
                hero.quest_condition_list.append(enemy.quest_condition)
                if enemy.quest_info: print(enemy.quest_info)
                win_fight(enemy = enemy, hero = hero)
                combat_end = 1
                break
            elif attacker_change == 1:
                break



def event_fight(enemy = None, hero = None):
    '''
    event == fight with random enemy
    '''
    # random generate enemy (using filters):
    enemy = mod_enemy.enemy_settings(name = None, loc = hero.location, lvl = None, gen = None)
    enemy.attack = mod_enemy.attack_points_calc(enemy = enemy)
    enemy.defend = mod_enemy.defend_points_calc(enemy = enemy)
    mod_enemy.combat_attribute_default(enemy = enemy)
    enemy.combat_attribute = mod_enemy.combat_attribute_default(enemy = enemy)
    # update hero attrinute:
    mod_hero.combat_attribute_default(hero = hero)
    mod_hero.attack_points_calc(hero)
    mod_hero.defend_points_calc(hero)
    print("\n\nZaraz, zaraz... Coś się dzieje!\n"), time.sleep(.3)
    print("Twój przeciwnik to", end=''), mod_display.dot_loop()
    
    print(' ',enemy.name.upper()+'!','\n')
    mod_display.pause()
    mod_display.clear_screen()
    # pętla walki:
    combat_end = 0
    while combat_end == 0 and hero.actualLife > 0 and enemy.actualLife > 0:
        # initiative test:
        attacker = priority_test(enemy = enemy, hero = hero)
        # define attacker and defender:
        if attacker == hero: defender = enemy
        elif attacker == enemy: defender = hero  
        attacker_change = 0 # if 1 = loop is break and we repeat initiative test
        while True:
            mod_display.display_enemy_vs_hero(enemy = enemy, hero = hero, attacker = attacker)
            attacker_change = fight(enemy = enemy, hero = hero, attacker = attacker)
            mod_display.pause()
            mod_display.clear_screen()
            if hero.actualLife < 1:
                rip(enemy = enemy, hero = hero)
                combat_end = 1
                break
            elif enemy.actualLife < 1:
                win_fight(enemy = enemy, hero = hero)
                combat_end = 1
                break
            elif attacker_change == 1:
                break
    
    return hero


def event_quest(npc = None, hero = None):
    '''
    event == quest adventure
    '''

    npc = mod_npc.npc_settings(name = npc, loc = None, gen = None)
    mod_hero.quest(hero = hero, npc = npc)
    mod_display.display_event_quest(hero = hero, npc = npc)

        

    return hero


def event_npc(npc = None, hero = None):
    '''
    event == meet specified (by name) NPC
    '''
    # summon npc by name:
    npc = mod_npc.npc_settingsnpc_settings(name = npc.name, loc = None, gen = None)



def event_random_npc(hero = None):
    '''
    event == meet random (from hero location) NPC
    '''
    # random generate npc (using filters):
    try:
        npc = mod_npc.npc_settings(name = None, loc = hero.location, gen = None)
        mod_display.display_NPC_random_speach(npc = npc)
        
    except:
        pass



def event_choose(hero = None, location = None):
    '''
    Depends on the event refers to specific event function
    '''
    ### tymczasowo mamy tylko walkę i zabawę z przedmiotami ;)
    p = 1
    while p < 3:
        mod_display.display_hero_chart(hero = hero)
        event = input("Jeśli chcesz walki, napisz: walka lub  po prostu naciśnij 'enter', żeby polosować itemy do ekwipunku ")
        if event == "walka":
            mod_display.display_varied_info()    
            # załóżmy, że wylosowany został event z przeciwnikiem:
            event_fight(enemy = None, hero = hero)
            
        else:
            print("No to pogenerujemy przemioty dla zabawy...")
            # mamy mało itemów, więc filtry wyłączyłem
            mod_items.treasure_generator(maxloops = 20, maxitem_lvl = None, item_gen = None, hero = hero)
        p += 1
    
    
    return hero.inventory_dict

def quest_event_smashed_camp(hero = None):
    '''
    smashed camp quest
    '''

    npc = mod_npc.npc_settings(name = "Obóz niesłusznie rozbitych", loc = None, gen = None)
    if npc.quest_condition not in hero.quest_condition_list:
        hero.quest_condition_list.append(npc.quest_condition)

    event_quest(npc = "Obóz niesłusznie rozbitych", hero = hero)


    return hero


def quest_event_thievish_bear(hero = None):
    '''
    bad quest thievish_bear_quest
    '''

    npc = mod_npc.npc_settings(name = "Złodziejski Miś", loc = None, gen = None)
    if npc.quest_list[0] in hero.quest_blocked_list:
        if npc.quest_condition not in hero.quest_condition_list:      
            event_fight_spec_enemy(enemy = "Złodziejski Miś", hero = hero)

    else:
        event_quest(npc = "Złodziejski Miś", hero = hero)
        mod_display.pause()
        if "liczydło" in hero.inventory_dict.keys():
            #if npc.quest_condition not in hero.quest_condition_list:
            hero.quest_condition_list.append("Zdobyto narzędzia pomiarowe")

            


    return hero


def event_well_of_life(hero = None):
    '''
    full life regeneration
    '''

    print("\n\nZa cenę 50 sztuk złota w pełni Cię uleczę.. ")
    if hero.gold >= 50:
        
        while True:
            player_choice = input("Jeśli chcesz skorzystać, wpisz 't', jeśli nie, wpisz 'n' i zatwierdź <enter> -->")
            
            try: 
                if player_choice == 't' or player_choice == 'n':
                    if player_choice == 't':
                        print("Uzupełniono życie!")
                        hero.actualLife = hero.maxLife
                        hero.gold -= 50
                        mod_display.pause()
                    elif player_choice == 'n':
                        print("Bywaj zatem!")
                        mod_display.pause()
                    break
                        


            except:
                continue

    else:
        print("Niestety brakuje Ci złota")
        mod_display.pause()

    return hero

