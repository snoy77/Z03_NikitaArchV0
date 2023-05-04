

a = "hello".encode('utf-8')
print(a)
print(type(a))

b = " world".encode('utf-8')
c = a + b
print(c)
print(type(c))

new_byte = bytearray(0)
print(new_byte)

d = 0
for i in range(0, 52):
    new_byte.append(d)
    d = d + 1
print(type(new_byte[51]))
print(new_byte)

input("stop ============")
