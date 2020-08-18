data = [100,24,255]
buffer = bytes(data)
print(buffer)
f = open("Future Learn\Programming 103\August2020\\binary.txt", "bw")
f.write(buffer)
f.close()


f = open("Future Learn\Programming 103\August2020\\binary.txt", "br")
binary = f.read()
print(binary)
data = list(binary)
print(data)
f.close()
