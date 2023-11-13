import csv

# class definitions

class bodyinps:         # given inputs about the body
    U = 1
    L = 100
    W = 100
    H = 100
    mass = 2

class calcedinps:     # calculated inputs from ses 2
    ptot = 109.2
    mtot = 12.7
    vtot = 15.5
    lenopen = []
    widopen = []

# inputing functions

def read_craft_inp():
    craft = []
    inp_dat = open("craft inputs.txt",'r')
    line = inp_dat.readline() # truncate the first row
    # i = 0
    for line in inp_dat:
        # row = next(tsv_reader) # get the values from each row
        row = line.split("\t")      # get row as an array
        var = bodyinps()            # declare variable inside the loop so it is refreshed every time
        var.U = int(row[0])          # size of craft in U
        var.L = float(row[1])          # length of craft
        var.W = float(row[2])       # width of craft
        var.H = float(row[3])     # height of craft
        var.mass = float(row[4])     # mass of craft
        craft.append(var)
        '''
        print("For iteration: ", i)
        print("craft U is: ", craft[i].U)
        print("craft L is: ", craft[i].L)
        print("craft W is: ", craft[i].W)
        print("craft H is: ", craft[i].H)
        print("craft mass is: ", craft[i].mass)
        '''
        # i = i+1
        
    inp_dat.close()     # close the file after done reading
        
    return craft

##################################################

def read_outs(name):

    obj = calcedinps()    # declare variable here

    obj.lenopen = []
    obj.widopen = []    # declare arrays again to avoid duplicate values

    inp_dat = open(name,'r')
    line = inp_dat.readline() # truncate the first row for number of cells

    line = inp_dat.readline() # get next line
    row = line.split(":")
    obj.ptot = float(row[0])

    line = inp_dat.readline() # get next line
    row = line.split(":")
    obj.vtot = float(row[0])

    line = inp_dat.readline() # get next line
    row = line.split(":")
    obj.mtot = float(row[0])
    
    line = inp_dat.readline() # get next line
    row = line.split(":")
    obj.lenopen.append(float(row[0]))
    obj.lenopen.append(float(row[1]))
        
    line = inp_dat.readline() # get next line
    row = line.split(":")
    obj.widopen.append(float(row[0]))
    obj.widopen.append(float(row[1]))

    return obj