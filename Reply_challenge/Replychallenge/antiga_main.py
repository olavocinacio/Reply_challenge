# python3 main.py Inputs/input.in 2>/dev/null

import sys
import random

from datetime import datetime

milliseconds_since_epoch = datetime.now().timestamp() * 1000

random.seed(milliseconds_since_epoch)

def stderrwriteflush(arg):
    sys.stderr.write(str(arg))
    sys.stderr.write("\n")

def distance(predio,output_antenna):
	distancia = (abs(int(predio[0])-int(output_antenna[0])) + abs(int(predio[1])-int(output_antenna[1])))
	return distancia

def building_score(building, antennas, buildings):
  antennas_in_range_score = []
  for antenna in antennas:
    dist = distance (building, antenna)
    if int(antenna[2]) >= dist:
      score = int(building[3]) * int(antenna[3]) - dist * int(building[2])
      antennas_in_range_score.append(score)  
  if len(antennas_in_range_score) == 0:
    return [0, None]
  return [max(antennas_in_range_score), antennas[max(antennas_in_range_score[buildings.index(building)])]]

def rewarding(building, antennas, reward):
  final_score = 0
  used_antennas = []
  for element in building:
    [reward_step, antenna_index] = building_score(element, antennas, building)
    print(reward_step)
    final_score += reward_step
    if(reward_step == 0):
      reward = 0
    used_antennas.append(antenna_index)
  return (final_score + reward)

def generate_coordinates(Width, Height, antennas):

  last_coordinates = []
  for element in antennas:
    element.append(element[0])
    element.append(element[1])
    while True: 
      element[0] = random.randint(0,Width)
      element[1] = random.randint(0,Height)
      if ([element[0], element[1]] in last_coordinates):
        pass
      else:
        last_coordinates.append([element[0], element[1]])
        break;
  #print(antennas)
  return antennas

def main_iterator(Width, Height, building, antennas, reward):
  antennas = generate_coordinates(Width, Height, antennas)
  [results , antennas] = rewarding(building, antennas, reward)
  print(results)
  print(antennas)
  return "aaaa" #outlist ###### retornar lista

# generic flow
def input_local():
  try:
    fin = open(sys.argv[1], "r")
    text = fin.read()
    fin.close()
    return text
  except:
    stderrwriteflush("Check the argument/file!")
    sys.exit()

def parse_input(textin): 
  arglist = [x.split(' ') for x in textin.split('\n')] # list of lists
  return arglist

def generation(arglist):
  # first and second lines
  Width = int(arglist[0][0])
  Height = int(arglist[0][1])
  Number_buildings = int(arglist[1][0])
  Number_antennas = int(arglist[1][1])
  Bonus = int(arglist[1][2])
  # problem lines
  building = [arglist[i] for i in range(2,2+Number_buildings)]
  antenna = [arglist[i] for i in range(2+Number_buildings,2+Number_buildings+Number_antennas)]
  outlist = main_iterator(Width, Height, building, antenna, Bonus)



  return "[datastr]"

def parse_output(outlist):
  #textlist[0][0] =  # Número de antenas alocadas
  #texlist[1+i] = i xi yi # Vetori de antenas alocadas por identidade
  #textout = ''
  #for line in antenna: # antenna aqui são as alocadas
  #    for element in line:
  #        textout += str(element)
  #        textout += ' '
  #    textout += '\n'
  #textout = ''.join(map(str,M))
  #print(textout)
  return "[textout]"

def output(textout):
  stringout = sys.argv[1]
  stringout = stringout.replace("Input","Output")
  stringout = stringout.replace(".in",".out")
  stderrwriteflush(stringout)
  fout = open(stringout, "w")
  fout.write(textout)
  fout.close()
  return

def main():
  # input & parse
  textin = input_local()
  stderrwriteflush(textin)
  arglist = parse_input(textin)
  stderrwriteflush(arglist)
  # data structure generation
  datastr = generation(arglist)
  stderrwriteflush(datastr)
  # parse & output
  textout = parse_output(datastr)
  stderrwriteflush(textout)
  output(textout)
  print("done!")

if __name__ == "__main__":
  main()


################################################################ ZONA DE DESENVOLVIMENTO ###################################################################################



# Modelo com algorítmo genético padrão: minimizar uma função custo (ou função erro)
# import numpy as np
# from geneticalgorithm import geneticalgorithm as ga
# def geneticAlgorithm():
  
#   varbound=np.array([[0,10]]*3)
#   model=ga(function='''AQUI VAI A FUNÇÃO CUSTO PESSOAL''',dimension=3,variable_type='int',variable_boundaries=varbound)
#   model.run()








