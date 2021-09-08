import turtle

name = turtle.textinput("name", "What is your name?")
name = name.lower()
if name.startswith("Md"):
    print("Assalamualaikum, May Allah Bless You")
elif name.startswith("Sree"):
    print("Get in hell")
else:
    name = name.capitalize()