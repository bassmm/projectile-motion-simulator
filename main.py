# s = ut + 0.5at^2
# -4.905t^2 +ut - s = 0
# (u + math.sqrt(math.pow(u,2) - 4*4.905*s)) / (2*-4.905) 
import math

u = 100
angle = 45
s_vert = []
s_hori = []

s_y = 0
t = 0
while s_y >= 0:
    s_y = int(t*u*math.sin(angle) - 4.905*math.pow(t,2))
    s_x = int(t*u*math.cos(angle))
    s_vert.append(s_y)
    s_hori.append(s_x)
    t += 1
    if s_y < 0:
        s_vert.pop()
print(s_vert)
print(s_hori)

