
class TongLao:
    def __init__(self,hp,power):
        self.hp = hp
        self.power = power
    def see_people(self,name):
        if name == "XYZ":
            print("师弟！！！！")
        elif name == "李秋水":
            print("呸，贱人")
        elif name == "丁春秋":
            print("叛徒！我杀了你")

    def fight_zms(self,hp_enemy, power_enemy):
        self.power = self.power*10
        self.hp = self.hp/2
        self.hp = self.hp - power_enemy
        hp_enemy = hp_enemy - self.power
        if self.hp > hp_enemy:
            print("我赢了！")
        elif self.hp < hp_enemy:
            print("你赢了！")
        else:
            print("打平手！")

p = TongLao(300,50)
p.see_people("丁春秋")
p.fight_zms(4000,800)
