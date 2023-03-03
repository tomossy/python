#with open('filesample.txt', 'r') as f:
#    data = f.readline()
#    print(data)

#with open('filesample.txt', 'w') as f:
#    f.write('test\nあいうえ\n1234\n') 

#with open('filesample.txt', 'r') as f:
#    data = f.readline()
#    line = data.strip()

with open('filesample.txt', 'r') as f:
    for line in f:
        print(line.strip())
