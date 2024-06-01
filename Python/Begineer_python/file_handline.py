# f = open('E:\Python\CCA_Pipeline_Course\CodeCGAcademy\Python\Begineer_python/text.txt', 'r') 
# print(type(f))
# print(f.closed)
# print(f.read())
# f.close()
# print(f.closed)

# f = open('E:\Python\CCA_Pipeline_Course\CodeCGAcademy\Python\Begineer_python/text.txt', 'a')

# f.write('\n trying again')
# f.close()

# with open('E:\Python\CCA_Pipeline_Course\CodeCGAcademy\Python\Begineer_python/text.txt') as f:
#     print(f.read())
# print(f.closed)
# with open('E:\Python\CCA_Pipeline_Course\CodeCGAcademy\Python\Begineer_python/text.txt','w') as fw:
#     fw.write('new file! \n')
#     fw.write('This is second line! \n')
#     fw.write('This is Third line!')

# with open('E:\Python\CCA_Pipeline_Course\CodeCGAcademy\Python\Begineer_python/text.txt', 'r') as f:
#     print(f.read(5))
#     print(f.read(10))
#     print(f.tell())
#     f.seek(0)
#     print(f.tell())
#     print(f.read(5))
#     print(f.readlines())

with open('E:\Python\CCA_Pipeline_Course\CodeCGAcademy\Python\Begineer_python/Python Basics - Day2.jpg', 'rb') as f:
    data = f.read()
    print(data)
    with open('E:\Python\CCA_Pipeline_Course\CodeCGAcademy\Python\Begineer_python/new - Day2.jpg', 'wb') as d:
        d.write(data)


# handling bianary



