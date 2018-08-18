from  kancolle_utils import *

FLEET_NUMBER = 1

def check_fleet_for_sparkling():
    sleep(1)
    if not exists(Pattern("three_ships_fleet.png").exact()):
        print "ERROR: wrong fleet"
        exit(1)
        

# main
while True:
    check_taiha_on_KC3()
    go_home()
    select_w_1_1()
    select_fleet(FLEET_NUMBER)
    begin_battle()
    formation_line_ahead()
    accept_battle_results()
    next_node()
    compass()
    formation_line_ahead()
    accept_battle_results()
    accept_expeditions()
    resupply()