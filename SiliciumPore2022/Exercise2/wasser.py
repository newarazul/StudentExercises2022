import math
import csv




#Funtion to read the xyz file and store the atomic positions in atoms[] and store the coordinates
#in xyz_coordinates[]. 
def read_xyz_file(filename, look_for_charge=False):
    """
    """

    #Initializing the arrays to store the coordinates and element symbols 
    atomic_symbols = []
    xyz_coordinates = []
    atoms = []
    charge = 0
    title = ""
    isN=False
    count=0
    

    with open(filename, "r") as file:
        for line_number, line in enumerate(file):
            if line_number == 0:
                num_atoms = int(line)
            elif line_number == 1:
                title = line
                if "charge=" in line:
                    charge = int(line.split("=")[1])
            else:
                atomic_symbol, x, y, z = line.split()
                x=float(x)-7.16
                y=float(y)-7.16
                z=float(z)-7.16
                if z < -7.16:
                    z=z+14.32
                if (math.sqrt((x*x)+(y*y)) < Radius hier angeben!!! and atomic_symbol=="O") or isN==True:
                    isN=True
                    with open("new.xyz", "a") as outfile:
                        outfile.writelines([atomic_symbol,"\t",str(x),"\t",str(y),"\t",str(z),"\n"])
                        count=count+1
                        if count==3:
                            isN=False
                            count=0
                        atomic_symbols.append(atomic_symbol)
                        xyz_coordinates.append([float(x), float(y), float(z)])
#    atoms = [int(atom) for atom in atomic_symbols]
    return atomic_symbols, xyz_coordinates #,charge 



def main():
    print(read_xyz_file("wasserbulk.xyz",False))
   
   

if __name__  == "__main__":
    main()
