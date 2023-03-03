#with open('binarysample.dat', 'wb') as f:
#    f.write(b'012345');

with open('binarysample.dat', 'rb') as f:
    data = f.read(6)
    print(data)
