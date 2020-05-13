from  kancolle_utils import *

FLEET_NUMBER = 1

def check_fleet_for_sparkling():
    #return
    sleep(1)
    if not exists(Pattern("three_ships_fleet.png").exact()):
        print "ERROR: wrong fleet"
        exit(1)
        

try:
    #popup("WARNING: CHECK EQUPMENT BEFORE SORTIE")
    # main
    go_home()
    accept_expeditions()
    select_w_1_1()
    select_fleet(FLEET_NUMBER)
    check_fleet_for_sparkling()
    begin_battle()
    #formation_line_ahead()
    accept_battle_results()
    next_node()
    compass()
    #formation_line_ahead()
    accept_battle_results()
except Exception, e:
    print e
finally:
    beep()