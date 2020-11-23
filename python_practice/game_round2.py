"""
回合制游戏
hp代表血量，power代表攻击力，每个角色都有hp和power
hp的初始值为1000，power的初始值为200
打斗多个回合，谁的hp先为0 谁就输了
"""

def fight():
    my_hp = 1000
    my_power = 203
    your_hp =1000
    your_power = 201

    round_num = 0
    while my_hp > 0 and your_hp > 0:
        round_num = round_num + 1
        print(round_num)
        your_hp = your_hp - my_power
        if your_hp <= 0:
            print("I win!")
            print(f'Your hp is {your_hp}')
            print(f'my hp is {my_hp}')
            break
        my_hp = my_hp - your_power
        if my_hp <= 0:
            print("You win!")
            print(f'Your hp is {your_hp}')
            print(f'my hp is {my_hp}')
            break

fight()