import matplotlib.pyplot as plt

def plotBar(acidsList):
    plt.bar(*zip(*acidsList.items())) # Creates bar chart from acids_count dictionary
    plt.show() #Displays bar chart