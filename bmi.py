#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print("A Program to canlculate BMI of an individual")
name = input("Enter your name: ")
weight = float(input("Enter your weight in pounds: "))
height = float(input("Enter your height in inches: "))

def BMI(weight, height):
    bmi = weight / (height ** 2) * 703

    if (bmi < 16):
        return 'severely underweight', bmi
    elif (bmi >= 16 and bmi < 18.5):
        return 'underweight', bmi
    elif (bmi >= 18.5 and bmi < 25):
        return 'healthy', bmi
    elif (bmi >= 25 and bmi < 30):
        return 'overweight', bmi
    elif (bmi >= 30):
        return 'obese', bmi

quote, bmi = BMI(weight, height)
print('your bmi is: {} and your are: {}'.format(bmi, quote)) 


# In[ ]:




