from random import randrange, uniform
from sikuli import *
from org.sikuli.script import *
from time import sleep
import inspect
import datetime

# SETTINGS
WAIT_TIMEOUT = 20
LONG_WAIT_TIMEOUT = 60 * 3
MAX_MINUTES_SINCE_LAST_CRASH = 5
MAX_CRASH_COUNT = 5
setAutoWaitTimeout(WAIT_TIMEOUT)

# BASICS
def sleep_random(min,max):
    sleep(uniform(min, max))

def click_random(pic, out_of_area_click = False):
    print str(inspect.getframeinfo(inspect.currentframe()).function) + " " + str(pic)
    sleep_random(0.2, 1)
    match = find(pic)
    h = match.getH()
    w = match.getW()
    h_offset = randrange(-(h/2), h/2)
    w_offset = randrange(-(w/2), w/2)
    if out_of_area_click:
        h_offset = h_offset - randrange(0, 200)
        w_offset = h_offset - randrange(0, 200)
        
    if isinstance(pic,Pattern):
        curr_h_offset = pic.getTargetOffset().getX()
        curr_w_offset = pic.getTargetOffset().getY()
        pattern = pic.targetOffset(curr_h_offset + w_offset,curr_w_offset + h_offset)
    else:
        pattern = Pattern(pic).targetOffset(w_offset,h_offset)
    click(pattern)

def wait_and_click(pic):
    wait(pic,LONG_WAIT_TIMEOUT)
    sleep(0.5)
    click_random(pic)

def remove_cursor():
    hover(Location(0,0))
    
def show_kancolle_page():
    print inspect.getframeinfo(inspect.currentframe()).function
    if exists(Pattern("chrome_kancolle_page_icon.png").similar(0.80)):
        click(Pattern("chrome_kancolle_page_icon.png").similar(0.80))
    sleep(2)

def hide_kancolle_page():
    print inspect.getframeinfo(inspect.currentframe()).function
    if exists("chrome_empty_tab_header.png"):
        click("chrome_empty_tab_header.png")
    else:
        click("chrome_new_tab_button.png")



def recover(e):
    check_crash_frequency(e)
    remove_cursor()
    click(Pattern("chrome_to_window_mode.png").similar(0.80))
    sleep(1)
    remove_cursor()
    click(Pattern("chrome_to_fullscreen_mode.png").similar(0.80))
    

last_crash_date = datetime.datetime(2000,01,01)
crash_count = 0
def check_crash_frequency(e):
    global last_crash_date
    global crash_count
    minutes_since_last_crash = (datetime.datetime.now() - last_crash_date).total_seconds() / 60
    print "\n*** WARNING: CRASH ***" 
    print "minutes_since_last_crash: " + str(minutes_since_last_crash)
    print "crash_count: " + str(crash_count)
    print e
    print "**********************\n"
    if (minutes_since_last_crash < MAX_MINUTES_SINCE_LAST_CRASH):
        if (crash_count > MAX_CRASH_COUNT):
            exit()
        crash_count += 1
    last_crash_date = datetime.datetime.now()

def get_pattern_for_world(world_number):
    worlds_sortie = {
            1:"ensei_area_01_sortie.png",
            2:"ensei_area_02_sortie.png",
            3:"ensei_area_03_sortie.png",
            4:Pattern("ensei_area_04_sortie.png").similar(0.80),
            5:Pattern("ensei_area_05_sortie.png").similar(0.85),
            6:Pattern("ensei_area_06_sortie.png").similar(0.90)
            }
    worlds_exp = {
            1:"ensei_area_01_exp.png",
            2:"ensei_area_02_exp.png",
            3:"ensei_area_03_exp.png",
            4:Pattern("ensei_area_04_exp.png").similar(0.80),
            5:Pattern("ensei_area_05_exp.png").similar(0.85),
            6:Pattern("ensei_area_06_exp.png").similar(0.90)
            }
    is_exp = exists("sortie_top_combat.png",1)
    worlds = worlds_exp if is_exp else worlds_sortie
    return worlds[world_number]
    # TODO: remove if needed
    # print inspect.getframeinfo(inspect.currentframe()).function + " " + str(world_number)
    # SPACE_BETWEEN_WORLD_BUTTONS = 61
    # print str((world_number - 1) * SPACE_BETWEEN_WORLD_BUTTONS)
    # pattern = Pattern("ensei_area_01_sortie.png").targetOffset((world_number - 1) * SPACE_BETWEEN_WORLD_BUTTONS, 0)
    # return pattern

# GAME ACTIONS

def check_taiha_on_KC3():
    print inspect.getframeinfo(inspect.currentframe()).function
    if exists(Pattern("kc3_fleet_taiha.png").similar(0.95),0.5):
        print "ERROR: taiha"
        exit(1)                                                                                                                            
    if exists(Pattern("kc3_fleet_critical_state.png").similar(0.95),0.5):
        print "ERROR: critical"
        exit(1)

    # check is kc3 working
    wait("kc3_1st_fleet_selected.png")
    click("kc3_combined_button.png")
    click("kc3_1st_fleet_button.png")
    print "ships are OK"

def go_home():
    print inspect.getframeinfo(inspect.currentframe()).function
    
    if not exists("menu_main_sortie.png",0.5) and not exists("next.png",0.5):
        click_random("menu_side_home.png")
    # accept exp
    while exists("next.png",1):
        click_random("next.png",out_of_area_click = True)
        sleep_random(4,5)
    
    remove_cursor()
    sleep(1)
    wait("menu_main_sortie.png",LONG_WAIT_TIMEOUT)
    sleep(1)


def refresh_home():
    print inspect.getframeinfo(inspect.currentframe()).function
    sleep(2)
    remove_cursor()
    if exists("menu_main_sortie.png"):
        click_random("menu_main_sortie.png")
        wait("sortie_combat.png",LONG_WAIT_TIMEOUT)
        sleep(2)
    go_home()

def select_sortie_combat():
    print inspect.getframeinfo(inspect.currentframe()).function
    wait_and_click("menu_main_sortie.png")
    remove_cursor()
    click_random("sortie_combat.png")
    remove_cursor()
    wait("select_world.png",WAIT_TIMEOUT)
    sleep_random(0.5,1.0)
    



def select_fleet(FLEET_NUMBER):
    print inspect.getframeinfo(inspect.currentframe()).function
    if FLEET_NUMBER == 2:
        if not exists(Pattern("fleet_2s.png").similar(0.90),1):
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
    click_random(get_pattern_for_world(3))
    
    exit()
    click_random("combat_panel_3-2.png") #TODO: update
    wait_and_click("decision.png")
    remove_cursor()



def begin_battle():
    print inspect.getframeinfo(inspect.currentframe()).function
    if is_taiha():
        print "ERROR: taiha"
        exit(1)# safety first
    click_random("combat_start.png")

def accept_battle_results():
    print inspect.getframeinfo(inspect.currentframe()).function
    while True:
        # skip night battle
        if exists("is_night_battle.png",3):
            click_random("combat_nb_retreat.png")
            break
            
        # battle results
        if exists("next.png",3):
            break
        sleep_random(1,1.5)
            
    # wait for end 
    wait("next.png",FOREVER)
    sleep(5)
    click_random("next.png",out_of_area_click = True)
    sleep_random(4,5)
    wait("next.png")
    isTaiha = is_taiha()
    click_random("next.png",out_of_area_click = True)
    waitVanish("friend_fleet_area.png")
    # new ship
    sleep(1)
    if exists("next_alt.png",6):
        sleep(0.5)
        click_random("next_alt.png",out_of_area_click = True)
    sleep_random(0.5,1.0)
    rethreat_if_taiha(isTaiha)
        

def is_taiha():
    print inspect.getframeinfo(inspect.currentframe()).function
    return exists("kc3_fleet_critical_state.png",0.5) or exists("dmg_critical.png",5)

def rethreat_if_taiha(is_taiha):
    if is_taiha:
        rethreat()
        print "ERROR: taiha, "
        exit(1)# safety first 

def compass():
    print inspect.getframeinfo(inspect.currentframe()).function
    wait_and_click("compass.png")

def formation_line_ahead():
    print inspect.getframeinfo(inspect.currentframe()).function
    wait_and_click(Pattern("line_ahead.png").similar(0.97))

def formation_guard():
    print inspect.getframeinfo(inspect.currentframe()).function
    exit()
    wait_and_click(Pattern("formation_guard.png").similar(0.85))# TODO: update


def next_node():
    click_random("combat_nextnode.png")

def rethreat():
    print inspect.getframeinfo(inspect.currentframe()).function
    remove_cursor()
    click_random("combat_retreat.png")

def accept_expeditions():
    print inspect.getframeinfo(inspect.currentframe()).function
    wait("menu_main_sortie.png",LONG_WAIT_TIMEOUT)
    sleep(3)
    print "Will look for returned expeditions"
    while exists(Pattern("expedition_finish.png").similar(0.65),0.5):
        print "--CAWD-- INFO: Fleet was returned. Welcome home, my darlings"
        click_random(Pattern("expedition_finish.png").similar(0.65))
        wait("next.png",WAIT_TIMEOUT)
        sleep(5)
        click_random("next.png",out_of_area_click = True)
        sleep(5)
        click_random("next.png",out_of_area_click = True)
        wait("menu_main_sortie.png",LONG_WAIT_TIMEOUT)
        sleep(1.5)
    print "Finished accepting expeditions"
        

def resupply():
    print inspect.getframeinfo(inspect.currentframe()).function
    wait_and_click("menu_main_resupply.png")
    wait_and_click(Pattern("resupply_all.png").similar(0.95))
    sleep(1)
    wait("resupply_not_available.png",WAIT_TIMEOUT)
    sleep(1)

#EXPED
def send_fleet_to_expedition(fleet_number,expedition_number):
    if not exists("sortie_top_combat.png"):
        # go to exp screen
        wait_and_click("menu_main_sortie.png")
        remove_cursor()
        click_random("sortie_expedition.png")
        remove_cursor()
        wait("sortie_top_combat.png",WAIT_TIMEOUT)
        sleep(1)
    # on exp screen
    expeditions = {
            2      : Pattern("ensei_name_02.png").similar(0.90),
            4      : Pattern("ensei_name_04.png").similar(0.90),
            5      : Pattern("ensei_name_05.png").similar(0.90),
            6      : Pattern("ensei_name_06.png").similar(0.90),
            11     : Pattern("ensei_name_11.png").similar(0.90),
            21     : Pattern("ensei_name_21.png").similar(0.90),
            38     : Pattern("ensei_name_38.png").similar(0.95)
            }
    expedition_world = {
            2      : get_pattern_for_world(1),
            4      : get_pattern_for_world(1),
            5      : get_pattern_for_world(1),
            6      : get_pattern_for_world(1),
            11     : get_pattern_for_world(2),
            21     : get_pattern_for_world(3),
            38     : get_pattern_for_world(6)
            }

    if exists(expedition_world[expedition_number]):
        click_random(expedition_world[expedition_number])
        sleep(1)
    click_random(expeditions[expedition_number])
    if exists("decision.png"):
        click_random("decision.png")
        select_fleet(fleet_number)
        remove_cursor()
        sleep(1)
        # resupply
        if exists("temporary_resupply.png"):
            sleep(2)
            click_random("temporary_resupply.png")
            sleep(2)
            wait(Pattern("fleet_stats.png").similar(0.60),WAIT_TIMEOUT)
            
        # send exp
        wait_and_click("ensei_start.png")
        wait("exp_started.png",WAIT_TIMEOUT)
    sleep(5)
