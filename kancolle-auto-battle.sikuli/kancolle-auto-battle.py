from  kancolle_utils import *

world = "w25"

def generic_battle():# TODO: make it working
    begin_battle()
    for i in range(3):
        compass()
        formation_line_ahead()
        accept_battle_results()
        next_node()

def preboss_formation():
    return formation_line_ahead() #formation_guard()

def wait_for_select_node_dialog():
    remove_cursor()
    wait("select_node_dialog.png",LONG_WAIT_TIMEOUT)
    sleep(1)


def formation_diamond():
    print inspect.getframeinfo(inspect.currentframe()).function
    wait_and_click(Pattern("formation_diamond.png").similar(0.97))


def formation_combined_aa():
    print inspect.getframeinfo(inspect.currentframe()).function
    wait_and_click(Pattern("1560898740258.png").similar(0.97))


if world == "e4":
    compass()
    formation_combined_asw()
    accept_battle_results(True)
    next_node()
    
    compass()
    formation_combined_surface()
    accept_battle_results(True)
    next_node()
    
    compass()
    formation_combined_aa()
    accept_battle_results(True)
    next_node()
    
    compass()
    formation_combined_surface()
    accept_battle_results(True)
    next_node()
    
    compass()
    formation_combined_surface()
    boss_preview()

# bm3 3CL 3DD
# CL - falgship
if world == "w14": 
    generic_battle()

# 2CL BBV CVL
if world == "w15": 
    go_home()
    accept_expeditions()
    select_w_1_5()
    begin_battle()

    formation_line_abreast()
    accept_battle_results()
    next_node()
    
    formation_line_abreast()
    accept_battle_results()
    next_node()
    
    compass()
    formation_line_abreast()
    accept_battle_results()
    next_node()
    
    compass()
    compass()
    formation_line_abreast()
    accept_battle_results()

#bw2 2CV 4BB 
if world == "w21": 
    begin_battle()
    
    preboss_formation()
    accept_battle_results()
    next_node()
    compass()# check if compass
    compass()
    
    preboss_formation()
    accept_battle_results()
    next_node()
    compass()
    
    preboss_formation()
    accept_battle_results()


#transports 2CLT 3CV(B) 1FBB
if world == "w22":
    go_home()
    accept_expeditions()
    select_w_2_2()
    begin_battle()
    
    compass()
    formation_line_ahead()
    accept_battle_results()
    next_node()
    
    accept_empty_node()
    
    accept_expeditions()
    resupply()


# CL CV CVL 3DD los >= 34
if world == "w25": 
    begin_battle()
    
    compass()
    formation_line_ahead()
    accept_battle_results()
    next_node()
    
    compass()
    formation_line_ahead()
    accept_battle_results()
    next_node()

    compass()
    compass()
    formation_line_ahead()
    #TODO: night battle
    

# bw7 2DD CVB 2CLT FBB
# need radars
if world == "w33":
    go_home()
    accept_expeditions()
    select_w_3_3()
    begin_battle()
    
    preboss_formation()
    accept_battle_results()
    next_node()

    compass()
    compass()
    preboss_formation()
    accept_battle_results()
    next_node()
    
    compass()
    formation_line_ahead()
    #TODO: night battle

# bw7 3DD CAV 2CL
# need radars
# costs buckets
if world == "w34":
    begin_battle()
    
    compass()
    preboss_formations()
    accept_battle_results()
    next_node()

    compass()
    compass()
    formation_line_ahead()
    #TODO: night battle
    
# bw6 bm6 2CV 1CVL 1CL 2DD
if world == "w42":
    generic_battle()