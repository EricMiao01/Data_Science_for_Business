# -*- coding: utf-8 -*-
"""
W1Q2 解方程式根
"""
# ax^2 + bx + c = 0
a = int(input("Type a: "))
b = int(input("Type b: "))
c = int(input("Type c: "))

#判別式: >0兩實根; =0重根; <0無實根
discriminant = (b ** 2) - (4 * a * c)

if discriminant >= 0:
    x1 = ((-b) + (discriminant ** 0.5)) / (2 * a)
    x2 = ((-b) - (discriminant ** 0.5)) / (2 * a)
    print("The solution of the equation is: ({}, {})".format(int(x1), int(x2)))
else:
    print("Thie equation hasn't real roots")