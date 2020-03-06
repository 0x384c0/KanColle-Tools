from  kancolle_utils import *

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

try:
    # e1 p2
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
    
except Exception, e:
    print e
finally:
    beep()