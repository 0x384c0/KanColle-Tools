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
    hover("chrome_refresh.png")

def select_sortie_combat():
    wait_and_click("menu_main_sortie.png")
    hover("chrome_refresh.png")
    click_random("sortie_combat.png")
    hover("chrome_refresh.png")
    wait("select_world.png")
    sleep_random(0.5,1.0)
    

def select_w_1_1():
    print inspect.getframeinfo(inspect.currentframe()).function
    select_sortie_combat()
    click_random("combat_panel_1-1.png")
    wait_and_click("decision.png")
    hover("chrome_refresh.png")
    

def select_w_3_2():
    print inspect.getframeinfo(inspect.currentframe()).function
    select_sortie_combat()
    click_random("ensei_area_03.png")
    click_random("combat_panel_3-2.png")
    wait_and_click("decision.png")
    hover("chrome_refresh.png")


def select_fleet(FLEET_NUMBER):
    print inspect.getframeinfo(inspect.currentframe()).function
    if FLEET_NUMBER == 2:
        click_random("fleet_2.png")
    if FLEET_NUMBER == 3:
        click_random("fleet_3.png")
    if FLEET_NUMBER == 4:
        click_random("fleet_4.png")

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
    if exists("next_alt.png",3):
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
    hover("chrome_refresh.png")
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