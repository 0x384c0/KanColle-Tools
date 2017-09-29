from  kancolle_utils import *

FLEET_NUMBER = 1

def check_fleet_for_sparkling():
    if not exists(Pattern("three_ships_fleet.png").exact()):
        print "ERROR: wrong fleet"
        exit(1)

# main
check_taiha()
go_home()
accept_expeditions()
select_w_1_1()
select_fleet(FLEET_NUMBER)
check_fleet_for_sparkling()
begin_battle()
accept_battle_results()
check_taiha()
next_node()
compass()
accept_battle_results()