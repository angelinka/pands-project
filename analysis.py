# This is a main file which needs to be run. It performs the analysis of Fisher's Iris data set

# Author: Angelina Belotserkovskaya

# Importing python script with functions to be able to call them from here
import functions as f

# main method which calls corresponding functions depending on user selection
def main():
    displayMenu()

    while True:
        choice = input('Choice: ').strip()

        if choice == '1':
            print ('\n')
            
            try:
                f.about()
                displayMenu()
            except Exception as e:
                print('An exceptioin occured', e)

        elif choice == '2':
            try:
                f.overview()
                displayMenu()
            except Exception as e:
                print('An exceptioin occured', e)
        elif choice == 'x':
            break
        else:
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
