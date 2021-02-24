


class c_car():
    def __init__(self,xiandai,dazhong):
        self.xiandai = xiandai
        self.dazhong = dazhong




#数据封装
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

    def get_name(self): #定义获取私有变量的方法
        return self.__name

    def get_score(self,score): #定义修改__score私有变量的方法，可避免传入无效参数
        if 0 <= score <=100:
            self.__score = score
            print(self.__score)
        else:
            raise ValueError('bad score')


lulu = Student('lulu',90)
# print(lulu.__name)
print(lulu.get_grade())
print(lulu.get_name())
print(lulu.get_score(40))
