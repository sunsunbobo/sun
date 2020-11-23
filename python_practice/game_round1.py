"""
回合制游戏
hp代表血量，power代表攻击力，每个角色都有hp和power
hp的初始值为1000，power的初始值为200
"""

def fight():
    my_hp = 1000
    my_power = 200
    your_hp =1000
    your_power = 199

    my_finial_hp = my_hp - your_power
    your_finial_hp = your_hp - my_power

    if my_finial_hp > your_finial_hp:
        print("I win!")
    elif your_finial_hp > my_finial_hp:
        print("You win!")
    else:
        print("Ping!")

fight()