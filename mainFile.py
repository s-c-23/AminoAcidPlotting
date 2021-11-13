from fileWriter import *
from aminoCounter import *
from barChart import *

fileNames = {'6ij6','4eyl','1m1j'}

for file in fileNames: 

    fileName = writeFile(file)
    acid_count = countAmino(fileName)
    plotBar(acid_count)