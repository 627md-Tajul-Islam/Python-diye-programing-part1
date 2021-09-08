S = "Hello"
B = len(S)
print(B)

S = "Hello"
B = len(S)
print(B)

s = " "
b = len(s)
print(b)  #space in string means 1

s = ""
b = len(s)
print(b) # no space means 0

s = "Dimik's"
print(s)

s = 'Tajul\'s'
print(s) #another way

con = "Tajul Islam"
print(con[0])
print(con[1])
print(con[2])
print(con[3])
print(con[4])
print(con[5])
print(con[6])
print(con[7])
print(con[8])
print(con[9])
print(con[10])

for c in con:
    print(c) # loop

c = ['a','b','c']
print(c)
print(c[1])

desh = "Afghan" + "istan"
print(desh)

x = "10" + "0"
print(x)

con = "Bangladesh"
a = con.find("a")
print(a) #  it will return output in the o,1 format
b = con.find("t") # cause its not in the string
print(b)

country = "North korea"
new = country.replace("North", "South") # replaced
print(new)

text = "hello"
text = text.replace("hello","Hello")
print(text)

text = "hello"
text = text.replace("hello","Hello man") # new
print(text)

text = " this is a space"
text = text.lstrip()
print(text) # full strip
