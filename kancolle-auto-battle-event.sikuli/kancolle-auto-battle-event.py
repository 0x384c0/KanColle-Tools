from  kancolle_utils import *

def hinamatsuri_2020_e1_p4():
    popup("WARNING: AKASHI EQUPMENT, NELSON/NAGATO TOUCH")
    click_random("1584755580907.png")
    sleep(3)
    
    click_offset("1584750182160.png",10,10)
    click_offset("1584750279049.png",10,10)
    click_random("confirm_lbas.png")
    click_offset("1584750359020.png",10,10)
    click_offset("1584750373284.png",10,10)
    click_random("confirm_lbas.png")
    
    compass()
    compass()
    formation_combined_asw()
    accept_battle_results(True)
    next_node()
    
    compass()
    formation_combined_surface()
    accept_battle_results(True)
    next_node()
    
    compass()
    #skip repair
    formation_combined_aa()
    accept_battle_results(True)
    next_node()
    
    formation_combined_surface()
    accept_battle_results(True)
    next_node()
    
    compass()
    exit()

def hinamatsuri_2020_e1_p2():
    compass()
    formation_guard()
    accept_battle_results()
    next_node()
    
    compass()
    formation_line_abreast()
    accept_battle_results()
    next_node()
    
    compass()
    formation_diamond()
    accept_battle_results()
    next_node()

    formation_line_ahead()
    boss_preview()



def main():
    try:
        disable_auto_rethreat()
        hinamatsuri_2020_e1_p4()
    except Exception, e:
        print e
    finally:
        beep()
        
main()

# disable_auto_rethreat()
# compass()
# formation_combined_surface()
# formation_combined_aa()
# formation_combined_asw()
# formation_diamond()
# formation_guard()
# formation_line_ahead()
# formation_line_abreast():  # asw
# wait_for_select_node_dialog()
# accept_battle_results(True) # True if combined
# next_node()
# boss_preview()