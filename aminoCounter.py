from gemmi import cif

def countAmino(fileName: str):
    doc = cif.read_file(fileName) # Reads .cif file using gemmi
    acids_count = {} # Creates acids_count dictionary
    block = doc.sole_block() # Identifies the block in the .cif file
    for element in block.find_loop("_entity_poly_seq.mon_id"): # For loop iterates through file till it finds the "_entity_poly_seq.mon_id" loop
        if element in acids_count: 
            acids_count[element] +=1 # Adds to the count of the number of occurences of the element
        else:
            acids_count[element] = 1 # Creates a new key value pair in the dict of the amino acid
    return acids_count

countAmino('7rye.cif')