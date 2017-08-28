﻿# mod_varied_info - custom mod, contains list of short messages to random display in main:

import random


def display_varied_info():
    '''
    function with a list of short messages (mainly to increse playability). It random generates message to display from list:
    '''
    info_to_display_list = [
    "Zapowiada się piękny dzień", "Zbiera się na burzę", "Noc była chłodna, ale poranek słoneczny i ciepły",
    "Mam przeczycie, że coś się dziś zdarzy",



    "Porada: sklep na mapce oznaczony jest literką 'S'", "Porada: symbol '?' oznacza zagadkowe zdarzenie - kto wie, co to może być?"

    ]


    info_to_display = info_to_display_list[random.randint(0, len(info_to_display_list)-1)]

    return print(info_to_display)