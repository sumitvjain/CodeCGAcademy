# a = 10
# def greet():
#     # global a
#     # a = 20
#     b = 50
#     print(a+b)    

# greet()
# print(a)

# func = (lambda c,d : c * d)
# print(func(6,6))

# f = lambda x,y : x if x > y else y
# print(f(200, 205))

# lst = [(50,100,(4,5),(10,20))]
# # print(lst)
# # print(lst.sort())
# def k(x):
#     return x[1]
# lst.sort(key=k)
# print(lst)

# def count():
#     c = []
#     for i in range(0,10):
#         c.append(i)
     
#     return c
# c = count()
# d = [1,2,3,4,5,6,7,8,9,0]
# f = open('E:\Python\Code_CG_Academy/test.txt', mode = 'a') 
# f.writelines(f'\ncounting in  append mode -------- {c}')
# f.close()
# print(f)
# f = open('E:\Python\Code_CG_Academy/test.txt', 'r') 
# data = f.readline()
# data1 = f.readline()
# data2 = f.readline()
# data3 = f.readline()
# data4 = f.readline()
# f.close()
# print('data : ',data)
# print('data1 : ',data1)
# print('data2 : ',data2)
# print('data3 : ',data2)
# print('data4 : ',data2)
# print(f.tell())
# data = f.read(5)
# print(data)
# print(f.tell())
# f.seek(3)
# print(f.tell())
# result = f.read()
# print('result : ',result)
# f.close()

# f = lambda x,y,z: print(f'this is labmda function : {x*y+z}')
# f(10,5,12)

# with open('E:\Python\Code_CG_Academy/Python Basics - Day2.png', 'rb') as wb:
#     data = wb.read()
#     # print(f'this is data : {data}')
#     with open('E:\Python\Code_CG_Academy/new.txt', 'wb') as w:
#         w.write(data)
#         print('crated binary file ')

# print(dir(__builtins__))
# sample = ['mum', 'pune', 'hyd', 'delhi','kolkata', 'gujrat', 'rajasthan', 'chennai', 'bgl', 'lucknow']
# for i in sample:
#     if len(i) < 5:
#         print(i)