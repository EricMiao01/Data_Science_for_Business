# -*- coding: utf-8 -*-
"""
W1Q1：BMI計算機
"""

height = float(input("Type your height(cm): "))
weight = float(input("Type your weight(kg): "))

bmi = int(weight / ((height / 100) ** 2))
print("Your BMI is:", bmi)