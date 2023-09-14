def countCalories():
    input = open('input.txt', 'r')
    lines = input.readlines()
    
    
    sumCalories=0
    listCaloriesSums=[]
    
    for line in lines:
        
        if line.strip()=="":
            listCaloriesSums.apphend(sumCalories)
            sumCalories=0
            
        else:
            sumCalories += int(line)
            
    print(max(listCaloriesSums))
            