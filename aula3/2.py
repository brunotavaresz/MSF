import numpy as np
import matplotlib.pyplot as plt
import sympy

t0 = 0
tf = 4
dt = 0.1
N = int((tf-t0/dt)) + 1
t= np.linspace(t0, tf,N)

y,t,vt,g = sympy.symbols("y, t, vt, g")

y = (vt**2/g) *sympy.log(sympy.cosh(g*t/vt))
v = sympy.diff(y, t)
a = sympy.diff(v,t)


y = y.subs([(g, 9.8), (vt, 6.8)])
v = v.subs([(g, 9.8), (vt, 6.8)])
a = a.subs([(g, 9.8), (vt, 6.8)])

print("a= ", a)

v_plot= sympy.lambdify(t, v, "numpy")
a_plot = sympy.lambdify(t, a, "numpy")

ts = np.linspace(0, 4, 100)
plt.plot(ts, v_plot(ts), "-")
plt.xlabel("t")
plt.ylabel("v(t)")
plt.show()

ts = np.linspace(0, 4, 100)
plt.plot(ts, a_plot(ts), "-")
plt.xlabel("t")
plt.ylabel("a(t)")
plt.show()

acheck =sympy.symbols("acheck")
acheck = g - g * np.abs(v)*v / vt**2
print("a expected = ", acheck)
acheck = acheck.subs([(g, 9.8), (vt, 6.8)])
acheck_plot = sympy.lambdify(t, acheck, "numpy")

plt.plot(ts, a_plot(ts), "r-")
plt.plot(ts, acheck_plot(ts), "k--")
plt.xlabel("t")
plt.ylabel("a(t)")
plt.show()

#..................................................................................


tfinal = sympy.nsolve(y - 20,t,0)
yfinal = y.subs(t, tfinal)

print(tfinal, yfinal)
y_plot= sympy.lambdify(t,y,"numpy")

y2, v2, a2,v2_0, y2_0 = sympy.symbols("y, v, a, v0, y0")
a2= g
v2 = sympy.integrate(a2,t) + v2_0
y2 = sympy.integrate(v2, t) + y2_0
y2 = y2.subs([(g, 9.8), (v2_0, 0), (y2_0, 0)])

tfinal2 = sympy.nsolve(y2 - 20, t, 0)
yfinal2 = y.subs(t, tfinal2)
print(tfinal, yfinal)
y_plot2 = sympy.lambdify(t, y2, "numpy")


plt.plot(ts, y_plot(ts), "b--", label="com atrito")
plt.plot(tfinal, 20, "bo")
plt.plot(ts, y_plot2(ts), "r--", label="sem atrito")
plt.plot(tfinal2, 20, "ro")
plt.legend()
plt.show()
