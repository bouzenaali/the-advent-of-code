def isWining(numbers):
    
    WINING, MY_NUMS = numbers.split('|')
    WINING = WINING.split()
    WINING = WINING[2:]


    MY_NUMS = MY_NUMS.split()


    my_wining = ''
    for number in MY_NUMS:
        if (number in WINING) and (number != ''):
            my_wining += f"{number} "

    return my_wining


def tryIsWining():
    total_score = 0
    with open("Day4/input.txt", "r") as file:
        for line in file:
            winings = isWining(line)
            current_score = score(winings)
            total_score += current_score            
        
    
    return total_score
            

def score(wins):
    win_nums = wins.split()
    if win_nums == []:
        return 0

    points = 1
    for i in range(1, len(win_nums)):
        points *= 2

    return points    

if __name__ == "__main__":
    score = tryIsWining()
    print(f"My SCORE is: {score}")
