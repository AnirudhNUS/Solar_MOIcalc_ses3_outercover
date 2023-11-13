
import matplotlib.pyplot as plt 

def write_inter(interobj):
    
    out_dat = open("intermediate values.txt",'w')
    out_dat.write("mbody \t dcom \t moipanels[0 \t 1 \t 2] \t moibody[0 \t 1 \t 2] \n")
    
    for i in range(7):
        out_dat.write(str(interobj[i].mbody) + '\t')
        out_dat.write(str(interobj[i].dcom) + "\t\t")

        out_dat.write(str(interobj[i].moipanels[0]) + '\t')
        out_dat.write(str(interobj[i].moipanels[1]) + '\t')
        out_dat.write(str(interobj[i].moipanels[2]) + "\t\t")

        out_dat.write(str(interobj[i].moibody[0]) + '\t')
        out_dat.write(str(interobj[i].moibody[1]) + '\t')
        out_dat.write(str(interobj[i].moibody[2]) + '\n')
        
    out_dat.close()     # close the file after done reading
    

def write_out(outobj, craft):
    
    out_dat = open("output values.txt",'w')
    out_dat.write("U \t powmass \t powvol \t MOI[0 \t 1 \t 2] \n")
    
    for i in range(7):
        out_dat.write(str(craft[i].U) + '\t')
        out_dat.write(str(outobj[i].powmass) + '\t')
        out_dat.write(str(outobj[i].powvol) + "\t\t")

        out_dat.write(str(outobj[i].MOI[0]) + '\t')
        out_dat.write(str(outobj[i].MOI[1]) + '\t')
        out_dat.write(str(outobj[i].MOI[2]) + '\n')
        
    out_dat.close()     # close the file after done reading
    return 

def make_graphs():
    SizeU = []
    PM = []
    PV = []
    moiz = []        # typically MOIz is a good proxy for the max moi 
    # only moix for 16U is higher than moiz. otherwise always moiz is highest 

    inp_dat = open("output values.txt",'r')
    line = inp_dat.readline() # truncate the first row
    i = 0
    for line in inp_dat:
        row = line.split('\t')      # get row as an array
        SizeU.append(int(row[0]))         # size of craft in U
        PM.append(float(row[1]))          # power per unit mass
        PV.append(float(row[2]))       # power per unit volume
        moiz.append(float(row[6]))     # its 6 instead of 5 due to the extra \t

        print("For iteration: ", i)
        print("Craft Size in U: ", SizeU[i])
        print("Power per unit mass (W/kg): ", PM[i])
        print("Power per unit volume (W/m^3): ", PV[i])
        print("Craft MOI in z direction: ", moiz[i])
        i = i+1
    
    plt.xlabel('Craft Size in U', fontsize = 10) 
    plt.ylabel('Power per unit mass (W/kg)', fontsize = 10) 
    plt.title('Power per unit mass for outer cover panels', fontsize = 16) 
    # plt.legend() 
    plt.yticks(PM) 
    plt.plot(SizeU, PM, marker = 'o', c = 'g')
    plt.show() 

    plt.xlabel('Craft Size in U', fontsize = 10) 
    plt.ylabel('Power per unit volume (W/m^3)', fontsize = 10) 
    plt.title('Power per unit volume for outer cover panels', fontsize = 16) 
    # plt.legend() 
    plt.yticks(PV) 
    plt.plot(SizeU, PV, marker = 'o', c = 'g')
    plt.show() 
    
    plt.xlabel('Craft Size in U', fontsize = 10) 
    plt.ylabel('Max MOI (moi z axis) (kg m^2)', fontsize = 10) 
    plt.title('MOI for outer cover panels', fontsize = 16) 
    # plt.legend() 
    plt.yticks(moiz) 
    plt.plot(SizeU, moiz, marker = 'o', c = 'g')
    plt.show() 