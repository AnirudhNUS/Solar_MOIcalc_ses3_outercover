import math

# class definitions

class intervals:         # given inputs about the body
    mbody = 0
    dcom = 0
    moipanels = [0,0,0]
    moibody = [0,0,0]
    mpa = 5    


class outvals:
    MOI = [0,0,0]
    powmass = 6
    powvol = 3


# calculating intermediate values

def get_inter_vals(bodyobj, calcobj):

    varint = intervals()
    varint.mbody = round(bodyobj.mass - calcobj.mtot ,2)
    varint.dcom = round((calcobj.mtot*bodyobj.L)/bodyobj.mass ,2)
    area = calcobj.lenopen[0]*calcobj.widopen[0] + calcobj.lenopen[1]*calcobj.widopen[1] - calcobj.widopen[0]*calcobj.widopen[1]
    # note that this area is in mm^2
    varint.mpa = round(calcobj.mtot/area,2)  # kg/mm^2
    
    # Initialize separate lists for moipanels and moibody
    varint.moipanels = [0.0, 0.0, 0.0]
    varint.moibody = [0.0, 0.0, 0.0]            
    # this allows for moi arrays[] to be re-initialized each time such that they store new values 
    # instead of storing only the last value for every output

    # MOI panels
    areamoi = calcobj.widopen[0]*math.pow(calcobj.lenopen[0],3) + (calcobj.lenopen[1]-calcobj.widopen[0])*math.pow(calcobj.widopen[1],3)
    # this is in m^4
    varint.moipanels[0] = round( (varint.mpa*areamoi)/12 ,3)    # kg m^2
    areamoi = calcobj.widopen[1]*math.pow(calcobj.lenopen[1],3) + (calcobj.lenopen[0]-calcobj.widopen[1])*math.pow(calcobj.widopen[0],3)
    varint.moipanels[1] = round( (varint.mpa*areamoi)/12 ,3)    
    # kg m^2
    varint.moipanels[2] = round( varint.moipanels[0] + varint.moipanels[1] ,3)
    # MOI body
    varint.moibody[0] = round((varint.mbody*(math.pow(bodyobj.H,2)))/(12*math.pow(10,6)) ,4)
    varint.moibody[1] = round((varint.mbody*(math.pow(bodyobj.W,2)))/(12*math.pow(10,6)) ,4)  # divide by 10^6 to get MOI in kg m^2 instead of mm^2
    varint.moibody[2] = round(varint.moibody[0] + varint.moibody[1] ,4)

    return varint


# calculating output values
def get_outvals(bodyobj, calcobj, intobj):
    varout = outvals()
    varout.powmass = round(calcobj.ptot/calcobj.mtot ,3)
    varout.powvol = round((calcobj.ptot/calcobj.vtot)*math.pow(10,6) ,3)   # Get power per unit volume in m^3 instead of cm^3

    # Initialize separate list for MOI
    varout.MOI = [0.0, 0.0, 0.0]           
    # this allows for moi array[] to be re-initialized each time such that they store new values 
    # instead of storing only the last value for every output

    tempMOIsum = [0,0,0]
    for j in range(3):
        tempMOIsum[j] = intobj.moipanels[j] + intobj.moibody[j]
    
    parallel_add = (calcobj.mtot*math.pow((bodyobj.L - intobj.dcom),2) + intobj.mbody*math.pow(intobj.dcom,2))/(math.pow(10,6))   
    # divide by 10^6 to go from mm^2 to m^2
    print("\n Parallel addition is: ", parallel_add)
    print("Temp MOI is: ", tempMOIsum)
    print("moipanels is: ", intobj.moipanels)
    print("moibody is: ", intobj.moibody)

    varout.MOI[0] = round( tempMOIsum[0] + parallel_add ,3)
    varout.MOI[1] = round( tempMOIsum[1] + parallel_add  ,3)
    varout.MOI[2] = round( tempMOIsum[2] ,3)

    return varout