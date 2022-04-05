# This is a main file which needs to be run. It performs the analysis of Fisher's Iris data set

# Author: Angelina Belotserkovskaya

def main():
    displayMenu()


def displayMenu():  #displaying options of the main menu
    print ('\n')
    print("Welcome to Fisher's Iris data set analysis")
    print ('-'*45, '\n')
    print('Please select one of the following options:\n')
    print("1 - About Fisher's Iris data set")
    print('2 - Overview of the data set')
    print('3 - Summary overview by class')
    print('4 - Histograms')
    print('5 - Scatterplots')
    print('6 - Boxplots')
    print('7 - Violinplots')
    print('x - Exit application')

if __name__ == "__main__":
	# execute only if run as a script 
	main()
