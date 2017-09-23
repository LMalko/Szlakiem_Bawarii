
# mod_npc - custom mod, contains npc / quest data
# function npc_settings(name = None, loc = None, lvl = None, gen = None)
# load specified or random oponent to main

import random

# custom modules:
import mod_hero
import mod_items

# NPC class:


class Npc:

    def __init__(self, name, location_list):
        self.name = name
        self.location_list = location_list
        # dict with items, reward for finish quest
        self.inventory_dict = {}
        # contain NPC statments (just small talk)
        self.speach_list = []
        # if true - it's a shop keeper with buy/sell option (not used yet)
        self.shop = None
        # stores quest items forming quest condition:
        # if hero has that items, quest condition fulfilled
        self.quest_items = {}
        # contain NPC quest statments
        self.npc_quest_list = []
        # XP reward for finish quest
        self.xp_reward = 0
        # quest name related to NPC
        self.quest_name = ""
        # quest condition (it's password / ticket):
        # if hero has it in his list, means, that condition is fulfilled
        self.quest_condition = ""
        # stores extra reward for finish quest
        # (f.ex. portal (teleport) to next map)
        self.quest_special_reward = ""
        # contains items, that can be gift to hero
        self.treasure_dict = {}
        # contains statments, that can be delivered to hero
        # (if they ar not on hero speach_blocked_list)
        self.speach_list = []


def npc_settings(name=None, loc=None, gen=None):
    '''
    Stores NPC data base. 
    Creates NPC and export to MAIN using specific arguments:
    name = imports by name, for expample: if name = "wilk",
    function exports object WOLF
    or
    if name (in function arguments) is not specified,
    enemy is generated by filters:
        location (loc, ex. loc = 2 - second map level),
        enemy level (lvl = 1,2,3...),
        genre (gen, ex. gen = "animal": it will choose between enemies
        with genre = "animal")
        then export to main
    '''

    # REGULAR NPC (not quest)
    # randomly used in calendar function (rumors, short statements)

    #   wieśniak (name, location_list, inventory_dict, speach_list)
    villager = Npc("wieśniak", [1])
    villager.speach_list = [
        "Jak się masz?", "Dużo roboty", "Stara mnie pogoniła",
        "Ide po cebule", "bry, bry",
        "słyszałem o niedźwiedziu, który kradnie rzeczy",
        "uważaj na wilki i gobliny",
        "podobno leśniczego okradli"
        ]
    villager.map_symbol = "V"

    villager1 = Npc("garbaty wieśniak", [1])
    villager.speach_list = [
        "Cieżkie życie!", "Dużo roboty", "Stara mnie pogoniła",
        "słyszałem o niedźwiedziu, który kradnie rzeczy",
        "uważaj na wilki i gobliny",
        "podobno leśniczego okradli"
        ]

    mushrooman = Npc("grzybiarz", [1])
    mushrooman.speach_list = [
        "Grzybów mało w tym roku", "Znów robaczywe",
        "Patrz, jaki borowik!",
        "Poszedłbym głębiej w las, ale dużo niedźwiedzi",
        "Słyszałem, że leśniczy potrzebuje pomocy",
        "podobne gdzieś tu jest bestia, która gada",
        "strasznie tu czasem", "uważaj na wilki",
        "dużo tu szczurołaków",
        "podobno dziewczynka w czerwonym kapturze ma problem z babcią"
        ]

    hans = Npc("Hans z wioski", [1])
    hans.speach_list = [
        "w sąsiedniej krainie moja wioska potrzebuje pomocy",
        "Słyszałem, że leśniczy potrzebuje pomocy",
        "ponoć jest tu obóz niesłusznie rozbitych",
        "podobne gdzieś tu jest bestia, która gada",
        "strasznie tu czasem", "uważaj na wilki",
        "dużo tu szczurołaków"
        ]

    gretchel = Npc("Gretchel", [1])
    gretchel.speach_list = [
        "ładna jestem, co nie? Nie?! Twoja strata!",
        "<tupie nóżką>", "<puszcza oko>",
        "słyszałam o leśniczym, który potrzebuje pomocy..",
        "podobno dziewczynka w kapturze ma problem z babcią",
        "dużo tu szczurołaków"
        ]
    
    wrongly_smashed = Npc("Niesłusznie rozbity", [1])
    wrongly_smashed.speach_list = [
        "Serwus, chodź do naszego obozu, mamy dobry miodzik",
        "Lecę, mamy dziś spotkanie! ",
        "Lepiej nam się ostatnio wiedzie! "
        ]

    villager2 = Npc("wieśniak ze Szwarzwaldu", [2])
    villager.speach_list = [
        "Uważaj, niebezpiecznie tu!", "Przed nocą trzeba mi w dom..",
        "Stara mnie pogoniła", "Dużo tu grzybów i trolli..", "bry, bry",
        "Oblib.. nie wiem o nim.., ale kręcił się jakiś karzeł..",
        "uważaj na trolle!",
        "Moja wioska potrzebuje pomocy.."
        ]

    villager21 = Npc("wieśniaczka ze Szwarzwaldu", [2])
    villager.speach_list = [
        "Uważaj, niebezpiecznie tu!", "Przed nocą trzeba mi w dom..",
        "Żyto zgniło, bieda straszna..", "Dużo tu grzybów i trolli..",
        "bry, bry",
        "Oblib.. nie wim.., ale kręcił się jakiś karzeł..",
        "Troll!! a, nie, to tylko drzewo.. ",
        "Okradli naszą wioskę", "Uważaj na rabusiów",
        "Moja wioska potrzebuje pomocy.."
        ]

    villager3 = Npc("wieśniak Hans", [2])
    villager.speach_list = [
        "Jak się masz?", "Dużo roboty",
        "Stara mnie pogoniła", "Ide po cebule", "bry, bry",
        "Oblib... tak, poszedł do Dymiącej góry..",
        "uważaj na wilki i gobliny",
        "Przejścia do Dymiącej góry pilnuje straszny Troll Silnoręki!"
        ]

    villager4 = Npc("mieszkaniec przysiółka", [2, 3])
    villager.speach_list = [
        "Oblib? Widziałek go wczoraj, idź do Strażnika bramy w Dymiącej Górze",
        "Mamy problem z rabusiami",
        "Skurczybyki dają się we znaki",
        "Podobno Strażnik bramy pomoże temu, kto pokona skurczybyka.."
        ]

    warrior = Npc("wojownik", [1, 2, 3])
    warrior.speach_list = [
        "Ruch to zdrowie!", "Oblib? Był tu.. wstrętny karzeł..",
        "Dość bitew widziałem, spotkać by kobitę, ożenić się.."
        ]

    mountainman = Npc("Góral", [2, 3])
    mountainman.speach_list = [
        "Oblib.. coś słyszałem..", "Wiało tu wczoraj... ",
        "Uważaj na olbrzymy!",
        "Piękne i straszne nasze góry!", "bry, bry",
        "Oblib... tak, poszedł do Dymiącej góry..",
        "uważaj na wilki i gobliny",
        "Podobno Oblib zginął, idź do Pustelnika - on wiele wie.."
        ]

    joulderadom = Npc("Joul z Radomia", [3])
    mountainman.speach_list = [
        "Będąc w Bawarii, skosztuj kiełbasę!",
        "To mydło jest z pobiskiego zajazdu (czka)",
        "Miło Cię poznać..",
        "Dobry miodzik mam, nikomu nie dam..",
        "Przed wyruszeniem w drogę należy zebrać drużynę..",
        "Hej, hoo!"
        ]

    oblibghost = Npc("Jakiś głos, czy to duch?", [3, 4])
    oblibghost.speach_list = [
        "Byłem karłem, dziś niczym...",
        "Podstępny Czarownik zniknął mnie...", "Uuuuuuu...",
        "Na co mi to było.."
        ]

    oldtroll = Npc("Stary Troll wegetarianin", [3, 4])
    oldtroll.speach_list = [
        "Ha, ho! Ja ci nic nie robić, nie mieć zebów!",
        "Jeść jagody, jeść borówki, nie pić wódki! ",
        "Oblib, gdzie on? Nie wiedzieć, ale coś słyszeć.."
        ]

    oldhunter = Npc("Stary Łowca", [3, 4])
    oldtroll.speach_list = [
        "Widziałeś Starego Trolla? Od rana go szukam..",
        "Oblib ponoć zaginął..", "Bry, bry!", "Bywaj!",
        "Zimno kości łamie"
        ]

    # npc_regular_list contains list with not quest npc
    # to generate and export to main:
    npc_regular_list = [   
        villager, mushrooman, hans, gretchel, wrongly_smashed, villager1,
        villager2, villager3, mountainman, joulderadom,
        villager4, oblibghost, oldtroll, oldhunter, warrior
        ]

    # QUEST NPC - not randomly generated:

    # Czerowny Kapturek
    redhood = Npc("Czerwony Kapturek", [1])
    redhood.speach_list = ["O, witaj! Co u Ciebie?", "Miło Cię widzieć!"]
    redhood.xp_reward = 50
    redhood.quest_name = "Ratuj Babcię"
    redhood.quest_list = [
        "Możesz mi pomóc? Babcię porwał wilk.\
        \nOdszukaj go, zwróć Starowinkę, to będę Ci dozgonnie wdzięczna!",
        "Ojejku, jejku, Babcia uratowana, Zły Wilk pokonany! Dziękuję Ci!"
        ]
    
    redhood.quest_condition = "Babcia uratowana"
    redhood.inventory_dict = {"diament": 1, "wilcza skóra": -1}

    # Leśniczy
    forester = Npc("Leśniczy", [1])
    forester.speach_list = [
        "O, witaj!", "Miło Cię widzieć", "Co u Ciebie?", "Dużo mam pracy..",
        "Ładny ten las, prawda?"
        ]
    forester.xp_reward = 100
    forester.quest_name = "Narzędzia pomiarowe"
    forester.quest_items = {"liczydło": -1, "lina pomiarowa": -1}
    forester.quest_list = [
        "Słyszałem o Tobie - może mi pomożesz...\
        \nZłodziejski Miś ukradł mi narzędzia pomiarowe,\
         \nnie mogę wykonać swojej pracy.\
         \nJeśli mi pomożesz, pokażę Ci drogę do następnej krainy..",
        "Udało Ci się! Brawo, bardzo Ci dziękuję. Czas na Twoją nagrodę!"
        ]
    
    forester.quest_condition = "Zdobyto narzędzia pomiarowe"
    forester.inventory_dict = {"diament": 1}  # hero reward
    forester.quest_special_reward = ["portal 2"]

    # obóz Nieszłusznie rozbitych
    wrongly_smashed_camp = Npc
    wrongly_smashed_camp = Npc("Obóz niesłusznie rozbitych", [1])
    wrongly_smashed_camp.speach_list = [
        "No czołem, czołem!", "Co tam u Ciebie?", "Dobry miodzik mamy, co nie?"
        ]
    wrongly_smashed_camp.xp_reward = 5
    wrongly_smashed_camp.quest_name = "Otrzymałem miodzik!"
    wrongly_smashed_camp.quest_condition = ""
    wrongly_smashed_camp.inventory_dict = {"miodzik": 1}
    wrongly_smashed_camp.quest_list = [
        "Hihi, pewnie chcesz naszego miodzika? A proszę bardzo!\
        \nTakie to nasze zadanie dla Ciebie: weź miodzik, ha! ",
        "Bywaj zdrów!"
    ]

    # Zły wilk (QUEST in lvl 1) - quest czerwonego kapturka
    bad_wolf = Npc("Zły Wilk", [1])
    bad_wolf.speach_list = [u"wrrr.."]
    bad_wolf.quest_name = "Zły Wilk zabity!"
    bad_wolf.xp_reward = 30
    bad_wolf.quest_condition = "Babcia uratowana"
    bad_wolf.quest_list = [
        "wrrrrr",
        "(ślini się)"]

    # Złodziejski miś
    thievish_bear_quest = Npc("Złodziejski Miś", [1])
    thievish_bear_quest.speach_list = [
        "Ten gupi myśliwy Cię przysłał?", "Nie drażnij mnie!",
        "(mruczy)", "Co tam masz, miodzik?!"
        ]
    thievish_bear_quest.xp_reward = 50
    thievish_bear_quest.quest_name = "Złodziejski Miś"
    thievish_bear_quest.quest_condition = "Zdobyto miodzik"
    thievish_bear_quest.quest_items = {"miodzik": -1}
    thievish_bear_quest.inventory_dict = {"liczydło": 1, "lina pomiarowa": 1}
    thievish_bear_quest.quest_list = [
        "Przynieś mi miodzika, to pogadamy.\
        \nWróć z pustymi rękami, to Cię zjem!",
        "Udało Ci się, masz Miodzik! Proszę, oto rzeczy Leśniczego,\
        \nno idź do niego i nie zawracaj mi głowy więcej.."
        ]
        
    # Herszt bandytów (QUEST in lvl 1)
    ringleader = Npc("Herszt bandytów", [2])
    ringleader.quest_name = "Herszt bandytów zabity!"
    ringleader.xp_reward = 50
    ringleader.quest_condition = "Zdobyto zabytkowy obraz"
    ringleader.quest_info = (
        "O, jaki dziwny obraz.\
        \nWydaje mi się, że to coś ważnego, coś o nim mówiono.."
        )

    # ringleader.quest_list = ["", ""]

    # Sołtys
    mayor = Npc("Sołtys", [2])
    mayor.speach_list = [
        "No, bywaj tu!", "Cieszysz oczy!",
        "Co u Ciebie?", "Witaj w naszej wiosce",
        "Uważaj, to niebezpieczna okolica",
        "Oblib, chyba tu był, poszedł do Dymiącej Góry.."
        ]
    mayor.xp_reward = 180
    mayor.quest_name = "Zabytkowy obraz"
    mayor.quest_items = {"zabytkowy obraz": -1}
    mayor.quest_list = [
        "Ratuj proszę! Herszt łotrzyków okradł nas, w tym zabytkowy obraz,\
        \nktóry wiele dla nas znaczy..\
        \nOdzyskaj go, to damy rubiny - przekupisz nimi Trolla Silnorękiego.",
        "Udało Ci się! Dziękuję! Wspaniale. Doprawdy nie wiem, jak Ci dziękować..\
        \nA tak, oto Twoja nagroda!\
         \nIdź, daj to Trollowi, to Cię przepuści.. "
        ]
    mayor.quest_condition = "Zdobyto zabytkowy obraz"
    mayor.inventory_dict = {"rubin": 3}

    # Troll Silnoręki
    troll_strong_hand = Npc("Troll Silnoręki", [2])
    troll_strong_hand.speach_list = [
        "Chcieć na druga strona dziury? Dać rubiny", "<sapie>",
        "Śmierć tu znaleźć.."
        ]
    troll_strong_hand.xp_reward = 300
    troll_strong_hand.quest_name = "Rubiny dla trolla"
    troll_strong_hand.quest_condition = "Zdobyto rubiny"
    troll_strong_hand.quest_items = {"rubin": -3}
    troll_strong_hand.quest_list = [
        "Dać mi trzy rubiny, ja cie puścić.\
        \nWrócić bez nich - zginąć marnie, zginąć marnie, tak... ",
        "Mieć rubiny?! Ty przejść, ja cie nie zabić teraz.. "]
    troll_strong_hand.quest_special_reward = ["portal 3"]

    # Strażnik portalu
    portal_keeper = Npc("Strażnik portalu", [3])
    portal_keeper.speach_list = [
        "To niebezpieczna kraina, uważaj na siebie! ",
        "Co słychać? ", "Oblib, oblib... no nie wiem.. ",
        "Pilnuję portalu.. ",
        "Mam nadzieję, że skończą się problemy ze skurczybykami.. "
        ]
    portal_keeper.xp_reward = 400
    portal_keeper.quest_name = "pierścień skurczybyka"
    portal_keeper.quest_items = {"pierścień skurczybyka": -1}
    portal_keeper.quest_list = [
        "Czarownik? Tak, jego siedziba jest za portalem. Chcesz przejść?\
        \nPomóż mi ze skurczybykami - nie dają nam spokoju!\
        \nPrzynieś pierścień skurczybyka, to Cię przepuszczę..",
        "Już pogoniłeś szubrawca? Nie doceniałem Cię.\
        \nOwtwieram portal - przejdź proszę!\
         \nUważaj jeno na podstępnego czarownika! Masz też coś na drogę.. " 
        ]
    portal_keeper.quest_condition = "Zdobyto pierścień skurczybyka"
    portal_keeper.inventory_dict = {"placek śliwkowy": 2}
    portal_keeper.quest_special_reward = ["portal 4"]

    # Pustelnik - przełęcz rozpaczy
    hermit = Npc("Pustelnik", [3])
    hermit.speach_list = [
        "Witaj w mojej pustelni..", "Oblib.. tak, posłuchaj...",
        "Od wieku żyję tu w samotni..",
        "Uważaj, to straszna kraina..",
        "Idź do Strażnika portalu, porozmawiaj z nim.. "]
    hermit.xp_reward = 10
    hermit.quest_name = "Oblib.."
    hermit.quest_condition = ""
    hermit.inventory_dict = {"sztabka srebra": 1}
    hermit.quest_list = [
        "Tak, karzeł Oblib.. Niestety zginął. Obrączka? Zabił go czarownik,\
        \nale to potężna i straszna kreatura..\
         \nIdź do Strażnika portalu, on zna drogę..",
        "I jak, byłeś u Strażnika portalu?.. "
        ]

    # npc_quest_list contains list
    # with QUEST npc to generate and export to main:
    npc_quest_list = [
        redhood, bad_wolf, forester, wrongly_smashed_camp,
        thievish_bear_quest, mayor, ringleader,
        troll_strong_hand, portal_keeper, hermit
        ]
    
    # npc_all_list contains list of all NPC
    npc_all_list = (
        npc_regular_list + npc_quest_list
        )

    # if NPC name was specified, it will export NPC by given name:
    npc_exported_to_main = ''
    if name:
        for element in npc_all_list:
            if element.name == name:
                npc_exported_to_main = element

        return npc_exported_to_main

    # if enemy name wasn't specified, it will export random enemy
    # (random using optional filters - level, location, genre):
    else:
        npc_random_list = []
        # temporary helper list
        tmp_lvl = 0  # helps in loop below:
        for element in npc_regular_list:
            if (loc in element.location_list or loc is None):
                npc_random_list.append(element)
        
        # export random npc to main function:
        npc_rnd_exported_to_main = random.choice(npc_random_list)
        
        return npc_rnd_exported_to_main
