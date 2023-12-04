def calcCalibration(string):
    for char in string:
        if char.isdigit():
            i = char
            break
    
    for char in string[::-1]:
        if char.isdigit():
            i += char
            break
    
    return i




def tryCalcCalibration():
    i = 0
    sum = 0
    with open('Day1/input.txt') as file:
        for line in file:
            caliber = calcCalibration(line)
            i = i+1
            print(f"the calibration of line {i} is : {caliber}")
            sum += int(caliber)
                
        print(f"the sum of the calibers is : {sum}")
    return

tryCalcCalibration()