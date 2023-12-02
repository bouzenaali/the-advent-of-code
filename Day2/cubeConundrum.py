def cubeConundrum(game_input):

    games = game_input.split('; ')
    for game in games:
        red_count = 12
        green_count = 13
        blue_count = 14
        cubes = game.split(', ')
        for cube in cubes:
            count, color = cube.split(' ')
            count = int(count)

            if color == 'red':
                red_count -= count
            elif color == 'green':
                green_count -= count
            elif color == 'blue':
                blue_count -= count

        if red_count < 0 or blue_count < 0 or green_count < 0 :
            return False

    return True


game = '1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue'

is_possible = cubeConundrum(game)
if is_possible:
    print("the game is possible")
else:
    print("the game is not possible")



def tryCubeConundrum():
    i = 0
    j = 0
    with open('Day2/games.txt', 'r') as file:
        for line in file:
            is_possible = cubeConundrum(line)
            if is_possible:
                print("the game is possible")
                i = i+1
            else:
                print("the game is not possible")
                j = j+1

    print("games possible : ",i, " games impossible : ", j)
tryCubeConundrum()
