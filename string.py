name=input("enter your name:")
string=f"{name}"
new_string=string[0:3]
print(new_string)
print(string[:5])#print(string[:5]) is same as print(string[0:5])
print(string[1:])#print(string[1:]) is same as print(string[1:len])
print(string[1::2])# same as [1:len] with 2 skip value
print(len(string))
print(string.endswith("an"))
print(string.startswith("Sa"))
print(string.capitalize())
print(string.lower())
print(string.upper())
a= "he is a good boy\nnot a bad boy."
b= "he is a good boy\nnot a bad \"boy\"."
c="Escape sequence is \\n"
print(a)
print(b)
print(c)
print(string[::-1])# reverse of a string
print(a[::-1])
