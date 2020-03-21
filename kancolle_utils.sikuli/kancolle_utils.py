from random import randrange, uniform
from sikuli import *
from org.sikuli.script import *
from time import sleep
import inspect
import datetime
import traceback
from java.applet.Applet import newAudioClip
from java import io

# SETTINGS
WAIT_TIMEOUT = 20
LONG_WAIT_TIMEOUT = 60 * 3
MAX_MINUTES_SINCE_LAST_CRASH = 5
MAX_CRASH_COUNT = 5
setAutoWaitTimeout(WAIT_TIMEOUT)

# BASICS
def beep():
    url = io.File("C:\Windows\Media\Windows Exclamation.wav").toURL()
    audio = newAudioClip(url)
    audio.play()

def sleep_random(min,max):
    sleep(uniform(min, max))
    
def click_offset(pic,w_offset,h_offset):
    print str(inspect.getframeinfo(inspect.currentframe()).function) + " " + str(pic)
    sleep_random(0.2, 1)
    pattern = Pattern(pic).targetOffset(randrange(-w_offset, w_offset),randrange(-h_offset, h_offset))
    click(pattern)

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
    images = {
            "chrome_kancolle_page_icon":Pattern("chrome_kancolle_page_icon.png").similar(0.80),
            "opera_kancolle_page_icon":Pattern("opera_kancolle_page_icon.png").similar(0.85)
            }
    if exists(images["chrome_kancolle_page_icon"]):
        click(images["chrome_kancolle_page_icon"])
    sleep(2)

def hide_kancolle_page():
    print inspect.getframeinfo(inspect.currentframe()).function
    images = {
            "chrome_empty":"chrome_empty_tab_header.png",
            "chrome_new":"chrome_new_tab_button.png",
            "opera_empty":"opera_empty_tab_header.png",
            "opera_new":"opera_new_tab_button.png"
            }
    if exists(images["chrome_empty"]):
        click(images["chrome_empty"])
    else:
        click(images["chrome_new"])



def recover(e):
    check_crash_frequency(e)
    

last_crash_date = datetime.datetime(2000,01,01)
crash_count = 0
def check_crash_frequency(e):
    global last_crash_date
    global crash_count
    minutes_since_last_crash = (datetime.datetime.now() - last_crash_date).total_seconds() / 60
    print "\n*** WARNING: CRASH ***" 
    print "minutes_since_last_crash: " + str(minutes_since_last_crash)
    print "crash_count: " + str(crash_count)
    traceback.print_exc()
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
    sleep(1)
    is_exp = exists(Pattern("sortie_top_combat.png").similar(0.95),1)
    worlds = worlds_exp if is_exp else worlds_sortie
    return worlds[world_number]

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
    if exists(Pattern("expedition_finish.png").similar(0.65),0.5):
    	return
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
    
def sortie_to_world():
    print inspect.getframeinfo(inspect.currentframe()).function
    wait_and_click("decision.png")
    remove_cursor()

def select_event_world():
    print inspect.getframeinfo(inspect.currentframe()).function
    click_random("event_world.png.png")

def sortie_to_event_world():
    print inspect.getframeinfo(inspect.currentframe()).function
    wait_and_click("event_chalkboard.png")
    sleep(1)
    wait_and_click("event_chalkboard.png")
    sortie_to_world()


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
    sortie_to_world()

def select_w_1_5():
    print inspect.getframeinfo(inspect.currentframe()).function
    select_sortie_combat()
    click_random("combat_panel_1-extra.png")
    remove_cursor()
    click_random("combat_panel_1-5.png")
    
    sortie_to_world()

def select_w_2_2():
    print inspect.getframeinfo(inspect.currentframe()).function
    select_sortie_combat()
    click_random(get_pattern_for_world(2))
    click_random(Pattern("combat_panel_2-2.png.png").similar(0.90))
    
    sortie_to_world()

def select_w_3_3():
    print inspect.getframeinfo(inspect.currentframe()).function
    select_sortie_combat()
    click_random(get_pattern_for_world(3))
    click_random("combat_panel_3-3.png")
    
    sortie_to_world()


def begin_battle():
    print inspect.getframeinfo(inspect.currentframe()).function
    if is_taiha():
        print "ERROR: taiha"
        exit(1)# safety first
    click_random("combat_start.png")

def accept_battle_results(combined_fleet=False):
    print inspect.getframeinfo(inspect.currentframe()).function
    while True:
        # skip night battle
        if exists("is_night_battle.png",0.3):
            click_random("combat_nb_retreat.png")
            break
            
        # battle results
        if exists("next.png",0.3):
            break
        sleep_random(0.5,1.0)
        # wait for end

    wait("next.png",WAIT_TIMEOUT)
    sleep(5)
    click_random("next.png",out_of_area_click = True)
    sleep_random(4,5)
    wait("next.png")
    wait("friend_fleet_area.png")
    isTaiha = is_taiha()
    click_random("next.png",out_of_area_click = True)

    if combined_fleet:
        sleep(1)
        wait("next.png",WAIT_TIMEOUT)
        wait("friend_fleet_area.png")
        isTaiha = isTaiha or is_taiha()
        click_random("next.png",out_of_area_click = True)

    waitVanish("friend_fleet_area.png")

    # new ship
    sleep(1)
    if exists("next_alt.png",6):
        sleep(0.5)
        click_random("next_alt.png",out_of_area_click = True)
    sleep_random(0.5,1.0)
    rethreat_if_taiha(isTaiha)
        
def accept_empty_node():
     click_random("next_alt.png",out_of_area_click = True)

def is_taiha():
    print inspect.getframeinfo(inspect.currentframe()).function
    return exists(Pattern("kc3_fleet_critical_state.png").similar(0.80),0.5) or exists("dmg_critical.png",2)


auto_rethreat = True

def disable_auto_rethreat():
    global auto_rethreat
    auto_rethreat = False

def rethreat_if_taiha(is_taiha):
    global auto_rethreat
    if is_taiha:
        if auto_rethreat:
            rethreat()
        print "ERROR: taiha, "
        exit(1)

# map navigation
def wait_for_select_node_dialog():
    remove_cursor()
    wait("select_node_dialog.png",LONG_WAIT_TIMEOUT)
    sleep(1)

def compass():
    print inspect.getframeinfo(inspect.currentframe()).function
    sleep(1)
    if exists("compass.png",WAIT_TIMEOUT):
        click_random("compass.png")

def formation_line_ahead(): # surface
    print inspect.getframeinfo(inspect.currentframe()).function
    wait_and_click(Pattern("line_ahead.png").similar(0.97))

def formation_line_abreast():  # asw
    print inspect.getframeinfo(inspect.currentframe()).function
    wait_and_click(Pattern("line_abreast.png").similar(0.95))

def formation_guard(): # preboss surface
    print inspect.getframeinfo(inspect.currentframe()).function
    wait_and_click(Pattern("formation_guard.png").similar(0.95))

def formation_diamond(): #aa
    print inspect.getframeinfo(inspect.currentframe()).function
    wait_and_click(Pattern("formation_diamond.png").similar(0.97))

def formation_combined_asw(): # asw
    print inspect.getframeinfo(inspect.currentframe()).function
    wait_and_click(Pattern("formation_combined_asw.png").similar(0.97)) 

def formation_combined_surface(): #surface
    print inspect.getframeinfo(inspect.currentframe()).function
    wait_and_click("formation_combined_surface.png")

def formation_combined_aa(): # anti air
    print inspect.getframeinfo(inspect.currentframe()).function
    wait_and_click(Pattern("1560898740258.png").similar(0.97))

def boss_preview(): # boss preview
     click_random(Pattern("boss_preview.png").similar(0.95))
    

def next_node():
    click_random("combat_nextnode.png")

def rethreat():
    print inspect.getframeinfo(inspect.currentframe()).function
    remove_cursor()
    click_random("combat_retreat.png")

def accept_expeditions():
    print inspect.getframeinfo(inspect.currentframe()).function
    wait("menu_main_sortie.png",LONG_WAIT_TIMEOUT)
    sleep(1)
    print "Will look for returned expeditions"
    while exists("expedition_finish.png",1):
        print "--CAWD-- INFO: Fleet was returned. Welcome home, my darlings"
        click_random("expedition_finish.png")
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
def send_fleet_to_expedition(fleet_number,expedition_name):
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
            "2"      : Pattern("ensei_name_02.png").similar(0.90),
            "3"      : Pattern("ensei_name_03.png").similar(0.90),
            "4"      : Pattern("ensei_name_04.png").similar(0.90),
            "5"      : Pattern("ensei_name_05.png").similar(0.90),
            "6"      : Pattern("ensei_name_06.png").similar(0.90),
            "A2"     : Pattern("ensei_name_a2.png").similar(0.90),
            "11"     : Pattern("ensei_name_11.png").similar(0.90),
            "B1"     : Pattern("1578031143800.png").similar(0.89),
            "20"     : Pattern("ensei_name_20.png").similar(0.90),
            "21"     : Pattern("ensei_name_21.png").similar(0.90),
            "38"     : Pattern("ensei_name_38.png").similar(0.95)
            }

    expedition_scroll_down_counts = {
            "A2"     : 2,
            "B1"     : 1
            }
    
    expedition_world = {
            "2"      : get_pattern_for_world(1),
            "3"      : get_pattern_for_world(1),
            "4"      : get_pattern_for_world(1),
            "5"      : get_pattern_for_world(1),
            "6"      : get_pattern_for_world(1),
            "A2"     : get_pattern_for_world(1),
            "11"     : get_pattern_for_world(2),
            "B1"     : get_pattern_for_world(2),
            "20"     : get_pattern_for_world(3),
            "21"     : get_pattern_for_world(3),
            "38"     : get_pattern_for_world(6)
            }
    # select world
    if exists(expedition_world[expedition_name],1):
        click_random(expedition_world[expedition_name])
        sleep(1)

    # scroll down if needed
    expedition_scroll_down_count = expedition_scroll_down_counts.get(expedition_name,0)
    for i in range(expedition_scroll_down_count):
        sleep(0.5)
        click_random("exp_scroll_down.png")
        sleep(0.5)

    # select expedition
    expedition = expeditions[expedition_name]
    if not exists(expedition):
        expedition = expedition.similar(0.75)
    click_random(expedition)

    #send fleet
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
