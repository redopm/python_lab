#!/usr/lib/python3

import matplotlib.pyplot as plt
import mpld3
import jinja2


x=[2,4,7,10,17,28,37,45,59,70]
y=[0,9,1,30,27,48,6,55,79,90]

plt.xlabel("time")
plt.ylabel("velocity")
plt.bar(x,y,label="people")
plt.plot(x,y,label="color")
plt.scatter(x,y,label="word count ")
plt.grid(c="r")
plt.show()
