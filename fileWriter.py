import requests

def writeFile(proteinCode: str):
    url = "http://files.rcsb.org/download/"+proteinCode+".cif"
    print(url)
    r = requests.get(url, allow_redirects = True) # Opens up protein file from PDB
    open(proteinCode+'.cif','wb').write(r.content) # Writes file to the computer
    print(proteinCode + '.cif')
    return (proteinCode + '.cif')