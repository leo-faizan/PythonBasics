import numpy as nm
import matplotlib.pyplot as mt

x = nm.arange(0, 4*nm.pi, 0.1)
y = nm.sin(x)

a = nm.arange(0, 4*nm.pi, 0.1)
b = nm.cos(a)

mt.plot(x, y)
mt.plot(a, b)

mt.title("SINE VS COSINE")

mt.show()

