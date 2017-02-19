def BMI(height, weight):
    bmi = float((weight * 703) / height**2)
    
    if bmi < 18.5:
        print("You're underweight")
    elif bmi < 25:
        print("You're healthy.")
    else: #if bmi >= 25:
        print("You're overweight")
        
