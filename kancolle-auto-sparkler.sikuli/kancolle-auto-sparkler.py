from random import randrange, uniform

WAIT_TIMEOUT = 10
FLEET_NUMBER = 1
setAutoWaitTimeout(WAIT_TIMEOUT)

def sleep_random(min,max):
    time = uniform(min, max)
    LONG_DELAY_CHANCE = 0.1
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

def accept_battle_results():
    print("wait for battle finish")

    while True:
        # night battle
        if exists("1499960148905.png"):
            click_random("1499957281501.png")
            break
            
        # battle results
        if exists("1499956703868.png"):
            break
        sleep_random(1,1.5)
            
    print("battle finished")
    # wait for end 
    wait("1499956703868.png",FOREVER)
    click_random("1499956703868.png",out_of_area_click = True)
    sleep_random(1,1.5)
    click_random("1499956703868.png",out_of_area_click = True)
    waitVanish("1502635171297.png")
    # new ship
    if exists("1499956814235.png"):
        click_random("1499956814235.png",out_of_area_click = True)
    sleep_random(0.5,1.0)




# main
if not exists("1499956402975.png",0):
    print("going to home")
    click_random("menu_side_home.png")
   
print("Beginning")   
click_random("1499956402975.png")
hover("1499957259515.png")
click_random("1499956459323.png")
hover("1499957259515.png")
wait("1502723824704.png")
sleep_random(0.5,1.0)

click_random(Pattern("1502634102077.png").similar(0.95))
click("1499956562272.png")
hover("1499957259515.png")

if FLEET_NUMBER == 2:
    click_random("fleet_2.png")
if FLEET_NUMBER == 3:
    click_random("fleet_3.png")
if FLEET_NUMBER == 4:
    click_random("fleet_4.png")
   
click_random("1499956601222.png")

accept_battle_results()
    
click_random("1499956999900.png")
wait("1499957036043.png",FOREVER)
click_random("1499957036043.png")
hover("1499957259515.png")
accept_battle_results()
















