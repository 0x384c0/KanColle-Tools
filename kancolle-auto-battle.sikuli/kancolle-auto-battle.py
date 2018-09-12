from  kancolle_utils import *

world = "e1"

def generic_battle():# TODO: make it working
    begin_battle()
    for i in range(3):
        compass()
        formation_line_ahead()
        accept_battle_results()
        next_node()

def preboss_formation():
    return formation_guard() #formation_line_ahead()
    
    

#1CL 4DD
if world == "e1": 
    begin_battle()
    
    compass()
    formation_guard()
    accept_battle_results()
    next_node()
    
    compass()
    formation_guard()
    accept_battle_results()
    next_node()
    
    formation_line_abreast()
    boss_preview()
    accept_battle_results()

# bm3 3CL 3DD
# CL - falgship
if world == "w14": 
    generic_battle()

# 2CL BBV CVL
if world == "w15": 
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

#bw2 4BB 2CV
if world == "w21": 
    begin_battle()
    
    preboss_formation()
    accept_battle_results()
    next_node()
    compass()# check if compass
    compass()
    
    formation_line_ahead()
    accept_battle_results()
    next_node()
    compass()
    
    formation_line_ahead()
    accept_battle_results()

# bw7 FBB CVB 2CLT 2DD
# need radars
if world == "w33": 
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