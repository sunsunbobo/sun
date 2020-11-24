"""
回合制游戏
hp代表血量，power代表攻击力，每个角色都有hp和power
hp的初始值为1000，power的初始值为200
打斗多个回合，谁的hp先为0 谁就输了
"""
import yaml
class Game:
    def __init__(self):
        data = yaml.safe_load(open("game.yaml"))
        print(data)
        self.my_hp = data['me']['hp']
        print(self.my_hp)
        self.my_power = data['me']['power']
        self.your_hp = data['you']['hp']
        self.your_power = data['you']['power']
    def fight(self):
        round_num = 0
        while self.my_hp > 0 and self.your_hp > 0:
            round_num = round_num + 1
            print(round_num)
            self.your_hp = self.your_hp - self.my_power
            if self.your_hp <= 0:
                print("I win!")
                print(f'Your hp is {self.your_hp}')
                print(f'my hp is {self.my_hp}')
                break
            self.my_hp = self.my_hp - self.your_power
            if self.my_hp <= 0:
                print("You win!")
                print(f'Your hp is {self.your_hp}')
                print(f'my hp is {self.my_hp}')
                break

game = Game()
# print(game.my_hp)
# print(game.your_hp)
game.fight()
# fight()