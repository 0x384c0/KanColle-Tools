from  kancolle_utils import *

# main
def main_loop():
    while True:
        show_kancolle_page()
        refresh_home()
        accept_expeditions()
        send_fleet_to_expedition(2,"2")
        send_fleet_to_expedition(3,"38")
        send_fleet_to_expedition(4,"A2")
        hide_kancolle_page()
        sleep_random(60 * 30,60 * 45)

while True:
    try:
        main_loop()
    except FindFailed, e:
        recover(e)