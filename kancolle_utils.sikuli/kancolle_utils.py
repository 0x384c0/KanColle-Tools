from random import randrange, uniform
from sikuli import *
from org.sikuli.script import *
from time import sleep
import inspect

# SETTINGS
WAIT_TIMEOUT = 20
LONG_WAIT_TIMEOUT = 50
setAutoWaitTimeout(WAIT_TIMEOUT)

# BASICS
def sleep_random(min,max):
    sleep(uniform(min, max))

def click_random(pic, out_of_area_click = False):
    sleep_random(0.2, 1)
    match = find(pic)
    h = match.getH()
    w = match.getW()
    h_offset = randrange(-(h/2), h/2)
    w_offset = randrange(-(w/2), w/2)
    if out_of_area_click:
        h_offset = h_offset - randrange(0, 200)
        w_offset = h_offset - randrange(0, 200)
    
    pattern = Pattern(pic).targetOffset(w_offset,h_offset)
    click(pattern)

def wait_and_click(pic):
    wait(pic,LONG_WAIT_TIMEOUT)
    sleep(0.5)
    click_random(pic)

def remove_cursor():
    hover(Location(0,0))
    
def show_kancolle_page():
    if exists(Pattern("chrome_kancolle_page_icon.png").similar(0.90)):
        click(Pattern("chrome_kancolle_page_icon.png").similar(0.90))
    sleep(2)

def hide_kancolle_page():
    if exists("chrome_empty_tab_header.png"):
        click("chrome_empty_tab_header.png")
    else:
        click("chrome_new_tab_button.png")

# GAME ACTIONS

def check_taiha():
    print inspect.getframeinfo(inspect.currentframe()).function
    if exists(Pattern("kc3_fleet_taiha.png").similar(0.95),0.5):
        print "ERROR: taiha"
        exit(1)                                                                                                                            
    if exists("kc3_fleet_critical_state.png",0.5):
        print "ERROR: critical"
        exit(1)

    # check is kc3 working
    wait("kc3_1st_fleet_selected.png")
    click("kc3_combined_button.png")
    click("kc3_1st_fleet_button.png")
    print "ships are OK"

def go_home():
    print inspect.getframeinfo(inspect.currentframe()).function
    if not exists("menu_main_sortie.png",0):
        click_random("menu_side_home.png")
    remove_cursor()


def refresh_home():
    sleep(2)
    remove_cursor()
    if exists("menu_main_sortie.png"):
        click_random("menu_main_sortie.png")
        wait("sortie_combat.png",60 * 3)
        sleep(2)
    go_home()

def select_sortie_combat():
    wait_and_click("menu_main_sortie.png")
    remove_cursor()
    click_random("sortie_combat.png")
    remove_cursor()
    wait("select_world.png")
    sleep_random(0.5,1.0)
    



def select_fleet(FLEET_NUMBER):
    print inspect.getframeinfo(inspect.currentframe()).function
    if FLEET_NUMBER == 2:
        if not exists("fleet_2s.png"):
            click_random("fleet_2.png")
    if FLEET_NUMBER == 3:
        click_random("fleet_3.png")
    if FLEET_NUMBER == 4:
        click_random("fleet_4.png")

def select_w_1_1():
    print inspect.getframeinfo(inspect.currentframe()).function
    select_sortie_combat()
    click_random("combat_panel_1-1.png")
    wait_and_click("decision.png")
    remove_cursor()
    

def select_w_3_2():
    print inspect.getframeinfo(inspect.currentframe()).function
    select_sortie_combat()
    click_random("ensei_area_03.png")
    click_random("combat_panel_3-2.png")
    wait_and_click("decision.png")
    remove_cursor()



def begin_battle():
    print inspect.getframeinfo(inspect.currentframe()).function
    check_taiha() # safety - is number one priority
    click_random("combat_start.png")

def accept_battle_results():
    print inspect.getframeinfo(inspect.currentframe()).function
    while True:
        # night battle
        if exists("is_night_battle.png",3):
            click_random("combat_nb_retreat.png")
            break
            
        # battle results
        if exists("next.png",3):
            break
        sleep_random(1,1.5)
            
    # wait for end 
    wait("next.png",FOREVER)
    sleep(0.5)
    click_random("next.png",out_of_area_click = True)
    sleep_random(1,1.5)
    click_random("next.png",out_of_area_click = True)
    waitVanish("friend_fleet_area.png")
    # new ship
    sleep(1)
    if exists("next_alt.png",6):
        sleep(0.5)
        click_random("next_alt.png",out_of_area_click = True)
    sleep_random(0.5,1.0)


def compass():
    print inspect.getframeinfo(inspect.currentframe()).function
    wait_and_click("compass.png")

def line_ahead():
    print inspect.getframeinfo(inspect.currentframe()).function
    wait_and_click(Pattern("line_ahead.png").similar(0.97))


def next_node():
    click_random("combat_nextnode.png")

def rethreat():
    print inspect.getframeinfo(inspect.currentframe()).function
    remove_cursor()
    click_random("combat_retreat.png")

def accept_expeditions():
    print inspect.getframeinfo(inspect.currentframe()).function
    wait("menu_main_sortie.png",180)
    sleep(2)
    while exists("expedition_finish.png",0.3):
        print "--CAWD-- INFO: Fleet was returned. Welcome home, my darlings"
        click_random("expedition_finish.png")
        wait("next.png",20)
        sleep(3)
        click_random("next.png",out_of_area_click = True)
        sleep(3)
        click_random("next.png",out_of_area_click = True)
        wait("menu_main_sortie.png",180)
        sleep(1.5)
        

def resupply():
    print inspect.getframeinfo(inspect.currentframe()).function
    wait_and_click("menu_main_resupply.png")
    wait_and_click(Pattern("resupply_all.png").similar(0.95))
    sleep(1)
    wait("resupply_not_available.png")
    sleep(1)

#EXPED
def send_fleet_to_expedition(fleet_number,expedition_number):
    if not exists("sortie_top_combat.png"):
        # go to exp screen
        wait_and_click("menu_main_sortie.png")
        remove_cursor()
        click_random("sortie_expedition.png")
        remove_cursor()
        wait("sortie_top_combat.png")
        sleep(1)
    # on exp screen
    expeditions = {
            2      : Pattern("ensei_name_02.png").similar(0.95),
            6      : Pattern("ensei_name_06.png").similar(0.95),
            21     : Pattern("ensei_name_21.png").similar(0.95),
            38     : Pattern("ensei_name_38.png").similar(0.95)
            }
    expedition_world = {
            2      : Pattern("ensei_area_01.png").similar(0.95),
            6      : Pattern("ensei_area_01.png").similar(0.95),
            21     : Pattern("ensei_area_03.png").similar(0.95),
            38     : Pattern("ensei_area_05.png").similar(0.95)
            }

    if exists(expedition_world[expedition_number]):
        click_random(expedition_world[expedition_number])
        sleep(1)
    click_random(expeditions[expedition_number])
    if exists(Pattern("decision.png").similar(0.95)):
        click_random("decision.png")
        select_fleet(fleet_number)
        remove_cursor()
        sleep(1)
        # resupply
        if exists("temporary_resupply.png"):
            click_random("temporary_resupply.png")
            sleep(2)
            wait("fleet_stats.png")
            
        # send exp
        wait_and_click(Pattern("ensei_start.png").similar(0.95))
        wait("exp_started.png")
    sleep(1)
  
