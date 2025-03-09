import math

def getWeight():
    weight=float(input("Please Enter your weight in pounds :   "))
    return weight


def getHeight():
    inputheight=input("please Enter your height in feet and inches(ex: 5'8\"):   ")
    splitinput=inputheight.split("'")
    feet=float(splitinput[0])
    inches=float(splitinput[1].strip('"'))
    height=(feet*12)+inches
    return height

def calculateBMI(weight,height):
    meters=height*0.0254
    kilogram=weight*0.453592
    bmi=kilogram/(meters*meters)
    return bmi

def classify_bmi(bmi):
    
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"
if __name__ =="__main__":
    print("\n!....Welcome to my BMI calculator....!\n")
    weight=getWeight()
    height=getHeight()
    bmi=calculateBMI(weight,height)
    print(f"your final BMI is:{round(bmi,2)}")
    print(classify_bmi(bmi))
