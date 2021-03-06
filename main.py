# python3 main.py Inputs/input.in 2>/dev/null

import sys
import math; # uso da função sqrt

def stderrwriteflush(arg):
    sys.stderr.write(str(arg))
    sys.stderr.write("\n")



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
    print(building)
    print(antenna)
    ## structure gen
    ''' we will generate a graph or permutation str here, probably'''
    return "[datastr]"

def processing(datastr):
    ''' apply algos here, such as nx.shortest_path with the given metrics '''
    return "[outlist]"

def parse_output(outlist):
    #textlist[0][0] =  # Número de antenas alocadas
    #texlist[1+i] = i xi yi # Vetor i de antenas alocadas por identidade
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
    # algorithm application
    outlist = processing(datastr)
    stderrwriteflush(outlist)
    # parse & output
    textout = parse_output(outlist)
    stderrwriteflush(textout)
    output(textout)
    print("done!")

if __name__ == "__main__":
    main()


################################################################ ZONA DE PRODUÇÃO ###################################################################################
def scoring(predios,antennas,antennas_output): # antennas - lista do input; antenas_output - output gerado com as posições
	score = 0;
	for predio in predios:
		for antena in antennas_output:
			score += ((predio[3]*antennas[antena[1]])-(predio[2]*distance(predio,antena)));
	score += reward(predios,1000); # alterar o prêmio dinamicamente
	return score;

def distance(predio,output_antenna): # predio - construção específica; output_antena - antena mais próxima
	distancia = (abs(predio[0]-output_antenna[0]) + abs(predio[1]-output_antenna[1]));
  	#round(math.sqrt((predio[0]-output_antena[1])^2+(predio[1]-output_antena[2])^2));
	return distancia;

def reward(predios, premio):
	for predio in predios:
		if(): # Se o prédio não estiver conectado
			reward = 0;
			break;
		else:
			reward = premio;
	return reward;