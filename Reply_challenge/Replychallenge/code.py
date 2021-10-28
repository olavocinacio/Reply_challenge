'''
    Chalenge code
'''
# python3 main.py Inputs/input.in 2>/dev/null

import sys
import random

def stderrwriteflush(arg):
    '''
        Print to stderr
    '''
    sys.stderr.write(str(arg))
    sys.stderr.write("\n")

def distance(predio,output_antenna):
    '''
        Calculate the distance from antenna to building by manhatan
    '''
    distancia = (abs(int(predio[0])-int(output_antenna[0]))\
                 + abs(int(predio[1])-int(output_antenna[1])))
    return distancia

def building_score(building, antennas):
    '''
        Calculate the score for this building
    '''
    antennas_in_range_score = []
    for antenna in antennas:
        dist = distance (building, antenna)
        if int(antenna[2]) >= dist:
            score = int(building[3]) * int(antenna[3]) - dist\
                * int(building[2])
            antennas_in_range_score.append(score)

    if len(antennas_in_range_score) == 0:
        return 0
    return max(antennas_in_range_score)

def rewarding(building,antennas, reward):
    '''
        Create reward global
    '''
    final_score = 0
    for element in building:
        reward_step = int(building_score(element, antennas))
        final_score += reward_step
        if reward_step == 0:
            reward = 0
    return final_score + reward

def generate_coordinates(width, height, antennas):
    '''
        Generate coordinates random for the antennas
    '''
    last_coordinates = []
    for element in antennas:
        element.append(element[0])
        element.append(element[1])
        while True:
            element[0] = random.randint(0,width)
            element[1] = random.randint(0,height)
            if ([element[0], element[1]] in last_coordinates):
                pass
            else:
                last_coordinates.append([element[0], element[1]])
                break
    return antennas

def main_iterator(width, height, building, antennas, reward):
    '''
        iterator that manage dependences
    '''
    antennas = generate_coordinates(width, height, antennas)
    results = rewarding(building, antennas, reward)

    return results

def input_local():
    '''
        input from input file
    '''
    try:
        fin = open(sys.argv[1], "r")
        text = fin.read()
        fin.close()
        return text
    except FileNotFoundError:
        stderrwriteflush("Check the argument/file!")
        sys.exit()

def parse_input(textin):
    '''
        Parse input file
    '''
    arglist = [x.split(' ') for x in textin.split('\n')] # list of lists
    return arglist

def generation(arglist):
    '''
        central routine
    '''
    # First and second lines
    width = int(arglist[0][0])
    height = int(arglist[0][1])
    number_buildings = int(arglist[1][0])
    number_antennas = int(arglist[1][1])
    bonus = int(arglist[1][2])

    # Problem lines
    building = [arglist[i] for i in range(2,2+number_buildings)]
    antenna = [arglist[i] for i in
               range(2+number_buildings,2+number_buildings+number_antennas)]

    # Run main iterator
    final_result = main_iterator(width, height, building, antenna, bonus)
    return final_result

def main():
    '''
        Main routine
    '''
    # input & parse
    textin = input_local()
    arglist = parse_input(textin)

    # data structure generation
    final_result = generation(arglist)
    # Done
    # print(final_result)
    return final_result

if __name__ == "__main__":
    lst = []
    for i in range(1000):
        random.seed(i)
        val = main()
        lst.append(val)
    
    mx = max(lst)
    print(mx)
    ind = lst.index(mx)
    print(ind)