
fo = open('C:/Users/LENOVO/Desktop/CodeSpeedyProject/hello.txt', 'r')
for x in fo.read():
    y = x.upper()
    fo1 = open('C:/Users/LENOVO/Desktop/CodeSpeedyProject/hello.txt', 'a')
    fo1.write(y)