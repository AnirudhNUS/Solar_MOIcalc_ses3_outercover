import outer_cover_calc
import reader_outer
import writer_outer

# inputing the variables 

craft = reader_outer.read_craft_inp()

'''
for i in range(7):
    print("For iteration: ", i)
    print("craft U, L, W, H, mass is: " + str(craft[i].U) + " " + str(craft[i].L) + " " + str(craft[i].W) + " " + str(craft[i].H) + " " + str(craft[i].mass))
'''

varinps = []

for i in range(7):
    name = "outer cover outputs/output vals " + str(craft[i].U) + "U.txt"
    print("The file name is ",name)
    obj = reader_outer.calcedinps()   # need to declare obj every time to avoid retroactive overwrite
    obj = reader_outer.read_outs(name)
    varinps.append(obj)

    '''
    print("Calculated inputs for iteration: " + str(i) + " where U is: " + str(craft[i].U))
    print("ptot vtot mtot " + str(varinps[i].ptot) + " " + str(varinps[i].vtot) + " " + str(varinps[i].mtot))
    print("lenopen [0,1] " + str(varinps[i].lenopen[0]) + " " + str(varinps[i].lenopen[1]))
    print("widopen [0,1] " + str(varinps[i].widopen[0]) + " " + str(varinps[i].widopen[1]))
    '''
    # calculating intermediate values

intvars = []

for i in range(7):
    intobj = outer_cover_calc.get_inter_vals(craft[i],varinps[i])
    intvars.append(intobj)
    
    print("Calculated intermediate values for iteration: " + str(i) + " where U is: " + str(craft[i].U))
    print("mbody dcom " + str(intvars[i].mbody) + " " + str(intvars[i].dcom))
    print("moipanels [0,1,2] ", intvars[i].moipanels)
    print("moibody [0,1,2] ", intvars[i].moibody)
    
writer_outer.write_inter(intvars)

# calculating outer values

outvars = []

outobj = outer_cover_calc.outvals()
outobj.MOI = [0.0 , 0.0 , 0.0]
outobj.powmass = 0.0
outobj.powvol = 0.0

outvars.append(outobj)   # for 1U since it doesn't fit, everything is set to 0

for j in range(6):        # starting from 2U
    i = j+1
    outobj = outer_cover_calc.get_outvals(craft[i],varinps[i],intvars[i])
    outvars.append(outobj)
    
for i in range(7):      # separate loop to print everything
    print("Output values for iteration: " + str(i) + " where U is: " + str(craft[i].U))
    print("MOI[0,1,2]: " + str(outvars[i].MOI))
    print("powmass, powvol " + str(outvars[i].powmass) + " " + str(outvars[i].powvol))

writer_outer.write_out(outvars, craft)

writer_outer.make_graphs()

