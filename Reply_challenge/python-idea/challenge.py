#!/usr/bin/env python3
# awk '!/^ *#/ && NF' challenge.py (use this to strip # comments)
# system
import sys
# application
import networkx as nx         # graph
import more_itertools as mi   # iterators and permutations
import combi                  # combinatorics
# application
def stderrwriteflush(arg):
    sys.stderr.write(str(arg))
    sys.stderr.write("\n")
# def randomfunctiontodowhatisrequired:
# generic flow
def input():
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
    # first line
    #params = arglist[0]
    # problem lines
    ''' use some functional witchcraft or iterator '''
    # last line
    #params2 = arglist[-1]
    ## structure gen
    ''' we will generate a graph or permutation str here, probably'''
    return "[datastr]"

def processing(datastr):
    ''' apply algos here, such as nx.shortest_path with the given metrics '''
    return "[outlist]"

def parse_output(outlist):
    ''' generate textout here '''
    return "[textout]"

def output(textout):
    stringout = sys.argv[1]
    stringout = stringout.replace("input","output")
    stringout = stringout.replace(".in",".out")
    stderrwriteflush(stringout)
    fout = open(stringout, "w")
    fout.write(textout)
    fout.close()
    return

def main():
    # input & parse
    textin = input()
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