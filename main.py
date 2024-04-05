# Import of tk
import os
import tkinter
import tkinter as tk
from tkinter import *
import winsound
import sys

# Increase recursion limit (example: 5000)
sys.setrecursionlimit(5000)
window = tkinter.Tk()
window.geometry("1920x1080")
window.title("Mining Incremental")
window.update()

# Definition of Pictures
bgmine = PhotoImage(file="mine.png")
bgupgradexp = PhotoImage(file="upgradexp.png")
bgupgrademoney = PhotoImage(file="upgrademoney.png")
bgcollapse = PhotoImage(file="collapse.png")
moneypic = PhotoImage(file="money.png")
xppng = PhotoImage(file="xp.png")
tpng = PhotoImage(file="tpoint.png")
bgupgradetier = PhotoImage(file="upgradetier.png")
progress = PhotoImage(file="Progressbar.png")
progress0 = PhotoImage(file="Progressbar%/Progressbar0%.png")
progress1 = PhotoImage(file="Progressbar%/Progressbar5%.png")
progress2 = PhotoImage(file="Progressbar%/Progressbar10%.png")
progress3 = PhotoImage(file="Progressbar%/Progressbar15%.png")
progress4 = PhotoImage(file="Progressbar%/Progressbar20%.png")
progress5 = PhotoImage(file="Progressbar%/Progressbar25%.png")
progress6 = PhotoImage(file="Progressbar%/Progressbar30%.png")
progress7 = PhotoImage(file="Progressbar%/Progressbar35%.png")
progress8 = PhotoImage(file="Progressbar%/Progressbar40%.png")
progress9 = PhotoImage(file="Progressbar%/Progressbar45%.png")
progress10 = PhotoImage(file="Progressbar%/Progressbar50%.png")
progress11 = PhotoImage(file="Progressbar%/Progressbar55%.png")
progress12 = PhotoImage(file="Progressbar%/Progressbar60%.png")
progress13 = PhotoImage(file="Progressbar%/Progressbar65%.png")
progress14 = PhotoImage(file="Progressbar%/Progressbar70%.png")
progress15 = PhotoImage(file="Progressbar%/Progressbar75%.png")
progress16 = PhotoImage(file="Progressbar%/Progressbar80%.png")
progress17 = PhotoImage(file="Progressbar%/Progressbar85%.png")
progress18 = PhotoImage(file="Progressbar%/Progressbar90%.png")
progress19 = PhotoImage(file="Progressbar%/Progressbar95%.png")
progress20 = PhotoImage(file="Progressbar%/Progressbar100%.png")
progress1t = PhotoImage(file="Progressbar%/ProgressbarT5%.png")
progress2t = PhotoImage(file="Progressbar%/ProgressbarT10%.png")
progress3t = PhotoImage(file="Progressbar%/ProgressbarT15%.png")
progress4t = PhotoImage(file="Progressbar%/ProgressbarT20%.png")
progress5t = PhotoImage(file="Progressbar%/ProgressbarT25%.png")
progress6t = PhotoImage(file="Progressbar%/ProgressbarT30%.png")
progress7t = PhotoImage(file="Progressbar%/ProgressbarT35%.png")
progress8t = PhotoImage(file="Progressbar%/ProgressbarT40%.png")
progress9t = PhotoImage(file="Progressbar%/ProgressbarT45%.png")
progress10t = PhotoImage(file="Progressbar%/ProgressbarT50%.png")
progress11t = PhotoImage(file="Progressbar%/ProgressbarT55%.png")
progress12t = PhotoImage(file="Progressbar%/ProgressbarT60%.png")
progress13t = PhotoImage(file="Progressbar%/ProgressbarT65%.png")
progress14t = PhotoImage(file="Progressbar%/ProgressbarT70%.png")
progress15t = PhotoImage(file="Progressbar%/ProgressbarT75%.png")
progress16t = PhotoImage(file="Progressbar%/ProgressbarT80%.png")
progress17t = PhotoImage(file="Progressbar%/ProgressbarT85%.png")
progress18t = PhotoImage(file="Progressbar%/ProgressbarT90%.png")
progress19t = PhotoImage(file="Progressbar%/ProgressbarT95%.png")
progress20t = PhotoImage(file="Progressbar%/ProgressbarT100%.png")
# Definition of Ores


upgradecolor = "red"
upgradexpcolor = "red"
tiercolor = "red"
musiclength = 145
musicplaying = 0
# XP BAR


# Save File


# Logo and save
window.iconphoto(False, (tk.PhotoImage(file="LogoProgramu.png")))

if not os.path.exists("C:/MiningIncremental"):
    # Create the folder if it doesn't exist
    os.makedirs("C:/MiningIncremental")
if os.path.exists("C:/MiningIncremental/savedata.txt"):
    with open("C:/MiningIncremental/savedata.txt", "r") as file:
        money = int(file.readline())
        upgraded = int(file.readline())
        level = int(file.readline())
        xp = int(file.readline())
        xprequire = int(file.readline())
        xpupgrade = int(file.readline())
        boulders = float(file.readline())
        xpmoneyrequire = float(file.readline())
        upgradecost = float(file.readline())
        tier = int(file.readline())
        tierpoint = float(file.readline())
        tierreqire = float(file.readline())
        upgradedtiergather = float(file.readline())
        upgradetiergathercost = float(file.readline())
else:
    money = 0
    upgraded = 1
    upgradecost = 15 * upgraded * (3 * upgraded)
    level = 1
    xp = 0
    xprequire = 100
    xpupgrade = 1
    xpmoneyrequire = xpupgrade * 20 * (5 * xpupgrade)
    boulders = 0
    tierpoint = 0
    tier = 1
    tierreqire = 1000
    upgradedtiergather = 1
    upgradetiergathercost = 1



# Music

# Definition of Events
# Mine
def mine():
    global money
    global upgradecost
    global upgradecolor
    global xp
    global level
    global xprequire
    global xpupgrade
    global xpmoneyrequire
    global upgradexpcolor
    global tier
    global tierreqire
    global tierpoint
    global tiercolor
    global tieramount
    global tierprogress
    global fillbarxp
    global xpper
    global xpper2
    global fillbart
    global tper
    global tper2
    global upgradedtiergather
    tierpoint = tierpoint + (1 * upgradedtiergather)
    money = money + (1 * upgraded * (tier * 3 - 2))
    xp = xp + (1 * xpupgrade) * (tier * 2 - 1)
    if upgradecost <= money:
        upgradecolor = "green"
    else:
        upgradecolor = "red"
    if xprequire <= xp:
        level = level + 1
        xp = 0
        xprequire = xprequire * 2
    if xpmoneyrequire <= money:
        upgradexpcolor = "green"
    else:
        upgradexpcolor = "red"
    if tierreqire <= tierpoint:
        tier = tier + 1
        tierreqire = tierreqire * 10
        tierpoint = 0
    xpper = xprequire / 100
    xpper2 = xp / xpper
    tper = tierreqire / 100
    tper2 = tierpoint / tper
    if tper2 <= 2.5:
        fillbart = progress0
    elif tper2 <= 7.5:
        fillbart = progress1t
    elif tper2 <= 12.5:
        fillbart = progress2t
    elif tper2 <= 17.5:
        fillbart = progress3t
    elif tper2 <= 22.5:
        fillbart = progress4t
    elif tper2 <= 27.5:
        fillbart = progress5t
    elif tper2 <= 32.5:
        fillbart = progress6t
    elif tper2 <= 37.5:
        fillbart = progress7t
    elif tper2 <= 42.5:
        fillbart = progress8t
    elif tper2 <= 47.5:
        fillbart = progress9t
    elif tper2 <= 52.5:
        fillbart = progress10t
    elif tper2 <= 57.5:
        fillbart = progress11t
    elif tper2 <= 62.5:
        fillbart = progress12t
    elif tper2 <= 67.5:
        fillbart = progress13t
    elif tper2 <= 72.5:
        fillbart = progress14t
    elif tper2 <= 77.5:
        fillbart = progress15t
    elif tper2 <= 82.5:
        fillbart = progress16t
    elif tper2 <= 87.5:
        fillbart = progress17t
    elif tper2 <= 92.5:
        fillbart = progress18t
    elif tper2 <= 97.5:
        fillbart = progress19t
    else:
        fillbart = progress20t

    if xpper2 <= 2.5:
        fillbarxp = progress0
    elif xpper2 <= 7.5:
        fillbarxp = progress1
    elif xpper2 <= 12.5:
        fillbarxp = progress2
    elif xpper2 <= 17.5:
        fillbarxp = progress3
    elif xpper2 <= 22.5:
        fillbarxp = progress4
    elif xpper2 <= 27.5:
        fillbarxp = progress5
    elif xpper2 <= 32.5:
        fillbarxp = progress6
    elif xpper2 <= 37.5:
        fillbarxp = progress7
    elif xpper2 <= 42.5:
        fillbarxp = progress8
    elif xpper2 <= 47.5:
        fillbarxp = progress9
    elif xpper2 <= 52.5:
        fillbarxp = progress10
    elif xpper2 <= 57.5:
        fillbarxp = progress11
    elif xpper2 <= 62.5:
        fillbarxp = progress12
    elif xpper2 <= 67.5:
        fillbarxp = progress13
    elif xpper2 <= 72.5:
        fillbarxp = progress14
    elif xpper2 <= 77.5:
        fillbarxp = progress15
    elif xpper2 <= 82.5:
        fillbarxp = progress16
    elif xpper2 <= 87.5:
        fillbarxp = progress17
    elif xpper2 <= 92.5:
        fillbarxp = progress18
    elif xpper2 <= 97.5:
        fillbarxp = progress19
    else:
        fillbarxp = progress20
    fillbarxplabel.config(image=fillbarxp, bg="white")
    fillbartlabel.config(image=fillbart, bg="white")
    MoneyCounter.config(text=str(money))
    UpgradeCounter.config(text="Level " + ": " + str(upgraded))
    UpgradecostCounter.config(text="Price " + ": " + str(upgradecost))
    LevelCounter.config(text=level)
    LevelprogressCounter.config(text=str(xp) + "/" + str(xprequire))
    tierprogress.config(text="Tier Progress :" + " " + str(tierpoint) + "/" + str(tierreqire))
    upgrademoney.config(
        text="Upgrade Money Gain",
        width=180,
        height=120,
        image=bgupgrademoney,
        bg=upgradecolor,
        fg="black",
        command=upgradegainmoney
    )
    UpgradeXpCounter.config(text="Level " + ": " + str(xpupgrade))
    round(xpmoneyrequire, 1)
    UpgradeXpCostCounter.config(text="Price " + ": " + str(xpmoneyrequire))
    UpgradeButton.config(
        text="Upgrade XP Gain",
        width=180,
        height=120,
        image=bgupgradexp,
        bg=upgradexpcolor,
        fg="black",
        command=upgradexpgain)
    tieramount.config(text=str(tier))
    tierprogress.config(text=str(int(tierpoint)) + "/" + str(int(tierreqire)))


# Close window
def Closed():
    global money
    global upgraded
    global level
    global upgradecolor
    global xp
    global xprequire
    global xpupgrade
    global upgradexpcolor
    global boulders
    global xpmoneyrequire
    global file
    global upgradecost
    with open("C:/MiningIncremental/savedata.txt", "w") as file:
        file.write(str(money))
        file.write("\n")
        file.write(str(upgraded))
        file.write("\n")
        file.write(str(level))
        file.write("\n")
        file.write(str(xp))
        file.write("\n")
        file.write(str(xprequire))
        file.write("\n")
        file.write(str(xpupgrade))
        file.write("\n")
        file.write(str(boulders))
        file.write("\n")
        file.write(str(xpmoneyrequire))
        file.write("\n")
        file.write(str(upgradecost))
        file.write("\n")
        file.write(str(tier))
        file.write("\n")
        file.write(str(tierpoint))
        file.write("\n")
        file.write(str(tierreqire))
        file.write("\n")
        file.write(str(upgradedtiergather))
        file.write("\n")
        file.write(str(upgradetiergathercost))
        file.write("\n")

window.protocol("WM_DELETE_WINDOW", Closed())


# MONEY UPGRADE
def upgradegainmoney():
    global money
    global upgradecost
    global upgraded
    global upgradecolor
    global upgradexpcolor
    upgradecost = 15 * upgraded * (2 * upgraded)
    if upgradecost <= money:
        money = money - upgradecost
        upgraded = upgraded + 1
        upgradecost = 15 * upgraded * (2 * upgraded)
    if upgradecost <= money:
        upgradecolor = "green"
    else:
        upgradecolor = "red"
    if xpmoneyrequire <= money:
        upgradexpcolor = "green"
    else:
        upgradexpcolor = "red"
    MoneyCounter.config(text=str(money))
    UpgradeCounter.config(text="Level " + ": " + str(upgraded))
    UpgradecostCounter.config(text="Price " + ": " + str(upgradecost))
    upgrademoney.config(
        text="Upgrade Money Gain",
        width=180,
        height=120,
        image=bgupgrademoney,
        bg=upgradecolor,
        fg="black",
        command=upgradegainmoney
    )
    UpgradeButton.config(
        text="Upgrade XP Gain",
        width=180,
        height=120,
        image=bgupgradexp,
        bg=upgradexpcolor,
        fg="black",
        command=upgradexpgain
    )


# xp money
def upgradexpgain():
    global money
    global xp
    global xpupgrade
    global xpmoneyrequire
    global upgradecolor
    global upgradexpcolor
    xpmoneyrequire = xpupgrade * 20 * (3 * xpupgrade)
    round(xpmoneyrequire, 1)
    if xpmoneyrequire <= money:
        money = money - xpmoneyrequire
        xpupgrade = xpupgrade + 1
        xpmoneyrequire = xpupgrade * 20 * (3 * xpupgrade)
        round(xpmoneyrequire, 1)
    if xpmoneyrequire <= money:
        upgradexpcolor = "green"
    else:
        upgradexpcolor = "red"
    if upgradecost <= money:
        upgradecolor = "green"
    else:
        upgradecolor = "red"
    MoneyCounter.config(text=str(money))
    UpgradeXpCounter.config(text="Level " + ": " + str(xpupgrade))
    round(xpmoneyrequire, 1)
    UpgradeXpCostCounter.config(text="Price " + ": " + str(xpmoneyrequire))
    UpgradeButton.config(
        text="Upgrade XP Gain",
        width=180,
        height=120,
        image=bgupgradexp,
        bg=upgradexpcolor,
        fg="black",
        command=upgradexpgain
    )
    upgrademoney.config(
        text="Upgrade Money Gain",
        width=180,
        height=120,
        image=bgupgrademoney,
        bg=upgradecolor,
        fg="black",
        command=upgradegainmoney
    )


# Reset layer 1 - Collapse


def collapse():
    global money
    global level
    global xprequire
    global xpupgrade
    global upgraded
    global upgradecolor
    global upgradexpcolor
    global xpmoneyrequire
    global upgradecost
    global xp
    global boulders
    global tiercolor
    global upgradetiergathercost
    if 30 <= level:
        money = 0
        upgraded = 1
        xpupgrade = 1
        xp = 0
        boulders = boulders + (level - 29) * 2.5
        xprequire = 100
        level = 1
    if xpmoneyrequire <= money:
        upgradexpcolor = "green"
    else:
        upgradexpcolor = "red"
    if upgradecost <= money:
        upgradecolor = "green"
    else:
        upgradecolor = "red"
    UpgradeCounter.config(text="Level : " + str(upgraded))
    UpgradecostCounter.config(text="Price " + ": " + str(upgradecost))
    LevelCounter.config(text=level)
    LevelprogressCounter.config(text=str(xp) + "/" + str(xprequire))
    MoneyCounter.config(text=str(money))
    UpgradeXpCounter.config(text="Level " + ": " + str(xpupgrade))

    round(xpmoneyrequire, 1)
    UpgradeXpCostCounter.config(text="Price " + ": " + str(xpmoneyrequire))
    UpgradeButton.config(
        text="Upgrade XP Gain",
        width=180,
        height=120,
        image=bgupgradexp,
        bg=upgradexpcolor,
        fg="black",
        command=upgradexpgain
    )
    upgrademoney.config(
        text="Upgrade Money Gain",
        width=180,
        height=120,
        image=bgupgrademoney,
        bg=upgradecolor,
        fg="black",
        command=upgradegainmoney
    )
    boulderamount.config(text="Boulders :" + " " + str(boulders))
    if upgradetiergathercost <= boulders:
        tiercolor = "green"
    else:
        tiercolor = "red"
    UpgradetierButton.config(
        text="Upgrade Tier",
        width=180,
        height=120,
        image=bgupgradetier,
        bg=tiercolor,
        fg="black",
    )

# Upgrade Tier Gathering
def UpgradeTierGatherCollapse():
    global boulders
    global upgradedtiergather
    global upgradetiergathercost
    global tiercolor
    if upgradetiergathercost <= boulders:
        upgradedtiergather = upgradedtiergather + 1
        boulders = boulders - upgradetiergathercost
        upgradetiergathercost = upgradedtiergather * 2
        pricetier.config(text="Price :" + " " + str(int(upgradetiergathercost)))
        if upgradetiergathercost <= boulders:
            tiercolor = "green"
        else:
            tiercolor = "red"
        UpgradetierButton.config(
        text="Upgrade Tier",
        width=180,
        height=120,
        image=bgupgradetier,
        bg=tiercolor,
        fg="black",
        command=UpgradeTierGatherCollapse,
        )
        boulderamount.config(text="Boulders :" + " " + str(boulders))
        UpgradeCounterTier.config(text="Level :" + " " + str(int(upgradedtiergather - 1)))
def resetdata():
    global money
    global xp
    global boulders
    global upgraded
    global xpmoneyrequire
    global tier
    global tierpoint
    global upgradedtiergather
    global upgradetiergathercost
    global tierreqire
    global upgradecost
    global level
    global xprequire
    money = 0
    upgraded = 1
    upgradecost = 15 * upgraded * (3 * upgraded)
    level = 1
    xp = 0
    xprequire = 100
    xpupgrade = 1
    xpmoneyrequire = xpupgrade * 20 * (5 * xpupgrade)
    boulders = 0
    tierpoint = 0
    tier = 1
    tierreqire = 1000
    upgradedtiergather = 1
    upgradetiergathercost = 1


while True:
    # variables used in realtime
    global UpgradecostCounter
    global xpper
    global xpper2
    global tper
    global tper2
    if musicplaying == 0:
        winsound.PlaySound('Backgroundsound.wav', winsound.SND_LOOP | winsound.SND_ASYNC | winsound.SND_NOWAIT)
        musicplaying = 1
    xpper = xprequire / 100
    xpper2 = xp / xpper
    tper = tierreqire / 100
    tper2 = tierpoint / tper
    if tper2 <= 2.5:
        fillbart = progress0
    elif tper2 <= 7.5:
        fillbart = progress1t
    elif tper2 <= 12.5:
        fillbart = progress2t
    elif tper2 <= 17.5:
        fillbart = progress3t
    elif tper2 <= 22.5:
        fillbart = progress4t
    elif tper2 <= 27.5:
        fillbart = progress5t
    elif tper2 <= 32.5:
        fillbart = progress6t
    elif tper2 <= 37.5:
        fillbart = progress7t
    elif tper2 <= 42.5:
        fillbart = progress8t
    elif tper2 <= 47.5:
        fillbart = progress9t
    elif tper2 <= 52.5:
        fillbart = progress10t
    elif tper2 <= 57.5:
        fillbart = progress11t
    elif tper2 <= 62.5:
        fillbart = progress12t
    elif tper2 <= 67.5:
        fillbart = progress13t
    elif tper2 <= 72.5:
        fillbart = progress14t
    elif tper2 <= 77.5:
        fillbart = progress15t
    elif tper2 <= 82.5:
        fillbart = progress16t
    elif tper2 <= 87.5:
        fillbart = progress17t
    elif tper2 <= 92.5:
        fillbart = progress18t
    elif tper2 <= 97.5:
        fillbart = progress19t
    else:
        fillbart = progress20t

    if xpper2 <= 2.5:
        fillbarxp = progress0
    elif xpper2 <= 7.5:
        fillbarxp = progress1
    elif xpper2 <= 12.5:
        fillbarxp = progress2
    elif xpper2 <= 17.5:
        fillbarxp = progress3
    elif xpper2 <= 22.5:
        fillbarxp = progress4
    elif xpper2 <= 27.5:
        fillbarxp = progress5
    elif xpper2 <= 32.5:
        fillbarxp = progress6
    elif xpper2 <= 37.5:
        fillbarxp = progress7
    elif xpper2 <= 42.5:
        fillbarxp = progress8
    elif xpper2 <= 47.5:
        fillbarxp = progress9
    elif xpper2 <= 52.5:
        fillbarxp = progress10
    elif xpper2 <= 57.5:
        fillbarxp = progress11
    elif xpper2 <= 62.5:
        fillbarxp = progress12
    elif xpper2 <= 67.5:
        fillbarxp = progress13
    elif xpper2 <= 72.5:
        fillbarxp = progress14
    elif xpper2 <= 77.5:
        fillbarxp = progress15
    elif xpper2 <= 82.5:
        fillbarxp = progress16
    elif xpper2 <= 87.5:
        fillbarxp = progress17
    elif xpper2 <= 92.5:
        fillbarxp = progress18
    elif xpper2 <= 97.5:
        fillbarxp = progress19
    else:
        fillbarxp = progress20
    fillbarxplabel = tk.Label(image=fillbarxp, bg="white")
    fillbarxplabel.config(image=fillbarxp, bg="white")
    fillbartlabel = tk.Label(image=fillbart, bg="white")
    fillbartlabel.config(image=fillbart, bg="white")
    upgradecost = 15 * upgraded * (3 * upgraded)
    xpmoneyrequire = xpupgrade * 20 * (5 * xpupgrade)
    round(xpmoneyrequire, 1)
    if upgradecost <= money:
        upgradecolor = "green"
    else:
        upgradecolor = "red"
    if upgradetiergathercost <= boulders:
        tiercolor = "green"
    else:
        tiercolor = "red"
    # definition of buttons and labels
    MoneyCounter = tk.Label(font=('Arial', 50), text=str(money))
    LevelCounter = tk.Label(font=("Arial", 35), text=level)
    LevelprogressCounter = tk.Label(font=("Arial", 15), text=str(xp) + "/" + str(xprequire))
    UpgradeCounter = tk.Label(text="Level : " + str(upgraded))
    UpgradecostCounter = tk.Label(text="Price : " + str(upgradecost))
    button = tk.Button(
        text="Mine",
        width=360,
        height=120,
        bg="grey",
        image=bgmine,
        fg="white",
        command=mine
    )
    upgrademoney = tk.Button(
        text="Upgrade Money Gain",
        width=180,
        height=120,
        image=bgupgrademoney,
        bg=upgradecolor,
        fg="black",
        command=upgradegainmoney
    )
    UpgradeXpCounter = tk.Label(text="Level " + ": " + str(xpupgrade))
    round(xpmoneyrequire, 1)
    UpgradeXpCostCounter = tk.Label(text="Price " + ": " + str(xpmoneyrequire))
    UpgradeButton = tk.Button(
        text="Upgrade XP Gain",
        width=180,
        height=120,
        image=bgupgradexp,
        bg=upgradexpcolor,
        fg="black",
        command=upgradexpgain
    )
    CollapseButton = tk.Button(
        text="Collapse",
        width=180,
        height=120,
        image=bgcollapse,
        bg="orange",
        fg="black",
        command=collapse
    )
    UpgradetierButton = tk.Button(
        text="Upgrade Tier",
        width=180,
        height=120,
        image=bgupgradetier,
        bg=tiercolor,
        fg="black",
        command=UpgradeTierGatherCollapse,
    )
    ResetButton = tk.Button(
        text="Reset Data?",
        width=10,
        height=2,
        fg="black",
        command=resetdata,
    )

    LevelRequirementCollapse = tk.Label(text="Requires Level 30")
    boulderamount = tk.Label(text="Boulders :" + " " + str(boulders))
    UpgradeCounterTier = tk.Label(text="Level :" + " " + str(int(upgradedtiergather - 1)))
    pricetier = tk.Label(text="Price :" + " " + str(int(upgradetiergathercost)))
    tieramount = tk.Label(font=("Arial", 35), text=str(tier))
    tierprogress = tk.Label(font=("Arial", 15), text=str(int(tierpoint)) + "/" + str(int(tierreqire)))
    splitbasic = tk.Label(
        text="------------------------------------------------------------------------------------------------------------------------------------------Basic------------------------------------------------------------------------------------------------------------------------------------------")
    splitcollapse = tk.Label(
        text="---------------------------------------------------------------------------------------------------------------------------Collapse------------------------------------------------------------------------------------------------------------------------------------------")
    window.iconphoto(False, (tk.PhotoImage(file="LogoProgramu.png")))
    moneyicon = tk.Label(image=moneypic)
    progressbar = tk.Label(image=progress)
    progressbar2 = tk.Label(image=progress)
    xpicon = tk.Label(image=xppng)
    ticon = tk.Label(image=tpng)
    # displaying buttons and text
    MoneyCounter.place(x=120, y=45)
    moneyicon.place(x=0, y=30)
    fillbarxplabel.place(x=1000, y=0)
    LevelCounter.place(x=900, y=0)
    LevelprogressCounter.place(x=1090, y=17)
    fillbartlabel.place(x=1000, y=71)
    tieramount.place(x=900, y=71)
    tierprogress.place(x=1085, y=88)
    xpicon.place(x=830, y=3)
    ticon.place(x=830, y=74)
    boulderamount.place(x=70, y=370)
    splitbasic.place(x=0, y=140)
    button.place(x=10, y=160)
    upgrademoney.place(x=420, y=160)
    UpgradeCounter.place(x=490, y=285)
    UpgradecostCounter.place(x=488, y=305)
    UpgradeButton.place(x=650, y=160)
    UpgradeXpCounter.place(x=715, y=285)
    UpgradeXpCostCounter.place(x=710, y=305)
    CollapseButton.place(x=10, y=400)
    LevelRequirementCollapse.place(x=55, y=530)
    splitcollapse.place(x=50, y=325)
    UpgradeCounterTier.place(x=325, y=530)
    pricetier.place(x=325, y=550)
    UpgradetierButton.place(x=260, y=400)
    ResetButton.place(x=1400, y=50)
    window.mainloop()
    window.protocol("WM_DELETE_WINDOW", Closed())
