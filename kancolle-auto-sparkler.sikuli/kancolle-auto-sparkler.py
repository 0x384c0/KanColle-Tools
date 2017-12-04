from  kancolle_utils import *

FLEET_NUMBER = 2

def check_fleet_for_sparkling():
    if not exists(Pattern("three_ships_fleet.png").exact()):
        print "ERROR: wrong fleet"
        exit(1)

# main
go_home()
accept_expeditions()
select_w_1_1()
select_fleet(FLEET_NUMBER)
check_fleet_for_sparkling()
begin_battle()
accept_battle_results()
next_node()
compass()
accept_battle_results()