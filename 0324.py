#
# t = ('a', 'b', 'c', 1, 2, 3)
#
# print(t[5])
# print(t[-1])
# print(t[1:4])
# print('b' in t)
#
# tt = ([1,2,3],[4,5,6])
# tt[1][2] = 99
# print(tt)


# l = 776351721
# is_prime = True
# for i in range(2,l):
#     if(l % i ) == 0:
#         is_prime = False
#         break
# if is_prime :
#     print("{0}是质数".format(l))
# else :
#     print("{0}不是质数".format(l))


# ls = []
# count = 0
# for i in range(1,5):
#     for j in range(1,5):
#         if i != j:
#             ii = str(i)
#             jj = str(j)
#             ij = ii+jj
#             ls.append(int(ij))
#             count+=1
# print(ls,count)


# l1 = ['a', 'b', 'c']
# t1 = ('d', 'e', 'f')
# s1 = 'abc123'
# s2 = 'abc,123'
# r1 = range(1,3)
# l2 = list(l1)
# print(l2)
# print(list(s1))
# print(s2.split(","))
# print(list(r1))
#
# print(tuple(l1))
# print(tuple(s1))
# print(tuple(s2.split(',')))
# print(tuple(r1))
#
# print(str(l1))
# print("".join(l1))




#
# college1 = {"哲学", '经济学', '法学', '教育学'}
# print(college1)
#
# college2 = set(['经济学', "哲学", '历史学', '文学', '金融学'])
# print(college2)
#
# college3 = set("中华人民共和国")
# print(college3)
#
# c3 = college1.intersection(college2)
# print(c3)
#
# c4 = college1.union(college2)
# print(c4)
#
# c5 = college1.difference(college2)
# print(c5)
#
# c6= college2.difference(college1)
# print(c6)
#
# c7 = college1.symmetric_difference(college2)
# print(c7)

# s1 = {4,5,6,7}
# s2 = {1,2,3,4,5,6,7,8,9}
# print(s1.issubset(s2))
# print(s2.issuperset(s1))
#
# s3 = {99}
# print(s3.isdisjoint((s2)))


#
# college1 = {"哲学", '经济学', '法学', '教育学'}
# college1.add("计算机学")
# print(college1)
# college1.d

# college1 = {"哲学", '经济学', '法学', '教育学'}
# print(college1)
#
# college2 = set(['经济学', "哲学", '历史学', '文学', '金融学'])
# print(college2)
#
# college3 = set("中华人民共和国")
# print(college3)
#
# c3 = college1&college2
# print(c3)

#
# college1 = {"哲学", '经济学', '法学', '教育学'}
# college1 = frozenset(college1)
# print(college1)
# college1.pop()


#生成式
# list1 = []
# for i in range(10,20):
#     list1.append(i * 10)
# print(list1)
#
# list2 = [i * 10 for i in range(10,20)]
# print(list2)
#
# list3 = [i * 10 for i in range(10,20) if i % 2 == 0]
# print(list3)
#
# set1 = {i*j for i in range(1,4) for j in range(1,4) if i==j}
# print(set1)

# l =['春天','夏天','秋天','冬天']
# s = {'season'+str(i+1):l[i] for i in range(0,len(l))}
# print(s)


# t1 = (1,2,3)
# t2 = (4,5,6)
# t3 = t1 + t2
# print(t3)






# li1 = [1,2,3]
# li2 = li1.copy()
# li3 = li1
# print('源：',id(li1))
# print('copy():',id(li1) == id(li2))
# print('=：',id(li1) == id(li3))

# print("花费了{:0,.2f}".format(1024.6868))

# print(6.0 == int('6'))
# print(type(6.0) == type(6))

# print(6.0 == 6)


#形参解包，实参普通 元祖套列表 , 引用
#形参解包，实参解包 元祖
#形参普通，实参普通 列表 ， 引用
li1 = 0
def fun1(per):
    print(per)
    per = 9
    print(per)



fun1(li1)
print(li1)
