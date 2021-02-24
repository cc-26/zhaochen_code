

def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)


print(fact(5))


# return self 返回一个实例
class A:
    def __init__(self):
        self.c = 0

    def count(self):
        self.c+=1
        print(self.c)
        return self

a = A()
a.count().count().count()

#工厂函数
#嵌套作用域
X = 99

def f1():
    X = 88
    def f2():
        print(X)
    #内层函数需要在外层函数里调用，否则仅是定义函数
    f2()
f1()

class Person:
    def __init__(self,):
        self.name = None
        self.gender = None

    def getName(self):
        return self.name

    def getGender(self):
        return self.gender

#Person子类
class Male(Person):
    def __init__(self, name):
        print (f"Hello Mr.{name}")
#Person子类
class Female(Person):
    def __init__(self, name):
        print (f"Hello Miss.{name}" )

#工厂类
class Factory:
    def getPerson(self, name, gender):
        if gender == 'M':
            return Male(name)
        if gender == 'F':
            return Female(name)


if __name__ == '__main__':
    factory = Factory()
    person = factory.getPerson("lulu", "F")
    person_cc = Person()
    print(person_cc.getGender())
    print(factory)


#链式调用
class Person:
    def name(self, name):
        self.name = name
        return self

    def age(self, age):
        self.age = age
        return self

    def show(self):
        # print ("My name is", self.name, "and I am", self.age, "years old.")
        print (f"My name is{self.name}and I am{self.age}years old")   #直接用的类中self.name,self.age

p = Person()
p.name("Li Lei").age(15).show()



'''
*arg会把多出来的位置参数转化为tuple
**kwarg会把关键字参数转化为dict
'''
#定义一个带有*arg参数的函数
def sum(*arg):
    res = 0
    for e in arg:
        res += e
    return res

print(sum(1, 2, 3, 4))
print(sum(1, 1))

#定义一个带有**kwward参数的函数
def dictc(**kwargs):
    return kwargs

mydict = dictc(system="系统", China="中国", link="联接") #调用dictc函数，并传入一个dict
x = input("请输入单词：")
if x in mydict.keys():
    print("中文意思：", mydict[x])
else:
    print("抱歉，没找到。")
