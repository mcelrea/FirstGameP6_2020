x = 5
y = 6
z = 10

def doThis():
    global x
    global y
    global z
    x += y
    if (x > z):
        z -= y

def doThisAlso():
    global x
    global y
    global z
    z += 1
    x = x / z

doThis()
doThisAlso()
print str(x) + ", " + str(y) + ", " + str(z)