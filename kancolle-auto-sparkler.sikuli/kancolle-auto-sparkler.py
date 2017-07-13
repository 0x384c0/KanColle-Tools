WAIT_TIMEOUT = 10
setAutoWaitTimeout(WAIT_TIMEOUT)
def accept_battle_results():
    print("wait for battle finish")

    while True:
        # night battle
        if exists("1499960148905.png"):
            click("1499957281501.png")
            break
            
        # battle results
        if exists("1499956703868.png"):
            break
        sleep(1)
            
    print("battle finished")
    # wait for end 
    wait("1499956703868.png",FOREVER)
    click("1499956703868.png")
    sleep(1)
    click("1499956703868.png")
    # new ship
    if exists("1499956814235.png"):
        click("1499956814235.png")
    

click("1499956402975.png")
hover("1499957259515.png")
click("1499956459323.png")
hover("1499957259515.png")

click(Pattern("1499966616577.png").similar(0.90))
click("1499956562272.png")
hover("1499957259515.png")
click("1499956601222.png")

accept_battle_results()
    
click("1499956999900.png")
click("1499957036043.png")
hover("1499957259515.png")
accept_battle_results()
















