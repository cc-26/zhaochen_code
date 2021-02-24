
list_c = [1,2,3,4,5,6]
list_z = ['a','b','a',2,'f','y']
''''#反转列表中的元素
list.reverse(list_c)
print(list_c)
#统计'a'元素在列表中出现的个数
print(list_z.count('a'))
# 在列表末尾增加一个新元素
list_z.append('X')
print(list_z)
#查看某个元素第一次出现的索引位置
print(list_z.index(2))
#删除列表中指定位置的元素
print(list_c.pop())
print(list_c)
'''
# cc = list_c[:]
# list_c.append('C')
# print(list_c)
# print(cc)
cc2 = list_z.copy()
list_z.append('A')
print(list_z)
print(cc2)



