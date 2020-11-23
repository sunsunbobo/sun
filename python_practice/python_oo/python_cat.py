##定义类，首字母需要大写
class Cat:
    #毛色，橘色，四条腿，
    #会吃，会叫，会睡
    ##属性
    color = "orange"
    leg = 4

    ##方法，在类的方法中，是使用def关键字定义
    ##def定义的 在类外叫做函数function，在类内叫做method
    def eat(self):
        print("Cat can eat!")
    def cry(self):
        print("Cat can cry!")
    def sleep(self):
        print("Cat can sleep!")

cat = Cat()
print(cat.color)
cat.eat()