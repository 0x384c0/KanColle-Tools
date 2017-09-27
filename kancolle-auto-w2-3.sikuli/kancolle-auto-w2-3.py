from random import randrange, uniform

WAIT_TIMEOUT = 20
LONG_WAIT_TIMEOUT = 50
setAutoWaitTimeout(WAIT_TIMEOUT)

def sleep_random(min,max):
    time = uniform(min, max)
    LONG_DELAY_CHANCE = 0.05
    if time > max - (max - min) * LONG_DELAY_CHANCE:
        time = time * 2
    sleep(time)


def click_random(pic, out_of_area_click = False):
    sleep_random(0.2, 1.8)
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
        
        

def check_taiha():
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
    if not exists("menu_main_sortie.png",0):
        click_random("menu_side_home.png")

def select_w_3_2():
        
    click_random("menu_main_sortie.png")
    hover("chrome_refresh.png")
    click_random("sortie_combat.png")
    hover("chrome_refresh.png")
    wait("select_world.png")
    sleep_random(0.5,1.0)
    click_random(Pattern("ensei_area_03.png").similar(0.94))
    click_random("combat_panel_3-2.png")
    click("decision.png")
    hover("chrome_refresh.png")
    
def accept_battle_results():

    while True:
        # night battle
        if exists("is_night_battle.png"):
            click_random("combat_nb_retreat.png")
            break
            
        # battle results
        if exists("next.png"):
            break
        sleep_random(1,1.5)
            
    # wait for end 
    wait("next.png",FOREVER)
    click_random("next.png",out_of_area_click = True)
    sleep_random(1,1.5)
    click_random("next.png",out_of_area_click = True)
    waitVanish("friend_fleet_area.png")
    # new ship
    if exists("next_alt.png"):
        click_random("next_alt.png",out_of_area_click = True)
    sleep_random(0.5,1.0)

def begin_battle():
    check_taiha() # safety - is number one priority
    click_random("combat_start.png")

def compass():
    wait("compass.png",LONG_WAIT_TIMEOUT)
    click_random("compass.png")

def line_ahead():
    wait(Pattern("line_ahead.png").similar(0.97),LONG_WAIT_TIMEOUT)
    click_random(Pattern("line_ahead.png").similar(0.97))

def rethreat():
    hover("chrome_refresh.png")
    click_random("combat_retreat.png")

def resupply():
    wait("menu_main_resupply.png",LONG_WAIT_TIMEOUT)
    click_random("menu_main_resupply.png")
    wait("resupply_all.png")
    sleep(1)
    click_random("resupply_all.png")
    sleep(1)
    wait("resupply_not_available.png")
    sleep(1)
    


# main
while True:
    print "BEGIN LOOP"
    
    print "check_taiha"
    check_taiha()
    print "go_home"
    go_home()
    print "select_w"
    select_w_3_2()
    print "begin_battle"
    begin_battle()
    print "compass"
    compass()
    print "line_ahead"
    line_ahead()
    print "accept_battle_results"
    accept_battle_results()
    print "rethreat"
    rethreat()
    print "resupply"
    resupply()
    
    print "END LOOP"

















