from python_practice.tonglao.python_tonglao import TongLao

class XuZhu(TongLao):
    def __init__(self,hp,power):
        self.read()
    def read(self):
        print("罪过罪过")
    def see_people(self,name):
        self.read()
    def fight_zms(self,hp_enemy, power_enemy):
        self.read()

p1 = XuZhu(500,30)
p1.see_people("丁春秋")
p1.fight_zms(4000,800)
p1.read()