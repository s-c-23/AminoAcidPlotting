# AminoAcidPlotting
Uses protein file codes to download the corresponding mmCif file from PDB and plot the number of each amino acid in the file
fileWriter: Uses the requests library to get the file from PDB and download it to the computer
aminoCounter: Creates a dict which counts the frequency of each amino acid in the file
barChart: Creates a bar chart that displays the frequencies of each amino acid
mainFile: Links scripts together and runs them
