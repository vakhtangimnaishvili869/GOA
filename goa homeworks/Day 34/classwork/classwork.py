#1)
def count_positives_sum_negatives(arr):
    List1 = []
    List2 =[]
    
    if arr == []:
        return []
    
    for i in arr:
        if i > 0:
            List1.append(i)
        elif i < 0:
            List2.append(i)
    return [len(List1), sum(List2)]
#2)
def dna_to_rna(dna):
    return dna.replace("T","U")
#3)
def zero_fuel(distance_to_pump, mpg, fuel_left):
    if fuel_left < distance_to_pump / mpg:
        return False
    else:
        return True
#4)
def bmi(weight, height):
    bmi = weight / height**2
    if bmi <= 18.5:
        return "Underweight"
    elif bmi <= 25.0:
        return "Normal"
    elif bmi <= 30.0:
        return "Overweight"
    elif bmi > 30:
        return "Obese"
#5)
def minimum(arr):
    return min(arr)

def maximum(arr):
    return max(arr)