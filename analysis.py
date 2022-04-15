# This is a main file which needs to be run. It performs the analysis of Fisher's Iris data set

# Author: Angelina Belotserkovskaya

# Importing python script with functions which I wrote to be able to call them from here
import functions as f

# main method which calls corresponding functions depending on user selection
def main():
    displayMenu()
    choice = input('Choice: ').strip()

    if choice == '1':
        print ('\n')    
        try:
            f.about()
            exit()
        except Exception as e:
            print('An exceptioin occured', e)
    elif choice == '2':
        try:
            f.overview()
            exit()
        except Exception as e:
            print('An exceptioin occured', e)
    elif choice == '3':
        usr_inp = input('Would you like to save summary to the file (s) or print to console (p)? s/p: ')
        if usr_inp == 's':
            try:
                saveToFile()
                exit()
            except Exception as e:
                print('An exceptioin occured', e)
        elif usr_inp == 'p':
            print(f.summary())
            exit()
        else:
            print('Incorrect selection')
            exit()
    elif choice == '4':
        try:
            f.examples()
            exit()
        except Exception as e:
                print('An exceptioin occured', e)
    elif choice == '5':
        print('Please select the type of plot you would like to see:\n' \
            '1 - Histograms\n' \
            '2 - Scatterplots\n' \
            '3 - Pairplot\n' \
            '4 - KDE pairgrid\n' \
            '5 - Heatmap\n' \
            '6 - Boxplot\n' \
            '7 - Violin plot'
                )
        usr_inp = input("Choice: ")
        if usr_inp == '1':
            try:
                f.hist()
                exit()
            except Exception as e:
                print('An exceptioin occured', e)
        elif usr_inp == '2':
            try:
                f.scatter()
                exit()
            except Exception as e:
                print('An exceptioin occured', e)
        elif usr_inp == '3':
            try:
                f.pairPlt()
                exit()
            except Exception as e:
                print('An exceptioin occured', e)
        elif usr_inp == '4':
            try:
                f.pairgrid()
                exit()
            except Exception as e:
                print('An exceptioin occured', e)
        elif usr_inp == '5':
            try:
                f.heatMap()
                exit()
            except Exception as e:
                print('An exceptioin occured', e)
        elif usr_inp == '6':
            try:
                f.boxplt()
                exit()
            except Exception as e:
                print('An exceptioin occured', e)
        elif usr_inp == '7':
            try:
                f.violin()
                exit()
            except Exception as e:
                print('An exceptioin occured', e)
        else:
            print('Selection not recognised, returning to main menu')
            main()
    elif choice == '6':
        try:
            f.corr()
            exit()
        except Exception as e:
            print('An exceptioin occured', e)
    elif choice == 'x':
        print('Bye!')
    else:
        main()

# this function is saving the output from summary() function into text file
def saveToFile():
    with open('data/summary.txt', 'w') as t:
        t.write(str(f.summary()))
    print('\nFile summary.txt is successfully saved')

# this function is used multiple times in the main() function to get user input on whether they want to 
# continue running the app.
def exit():
    answer = input('\nWould you like to explore  more? y/n: ')
    if answer == 'y':
        main()
    elif answer == 'n':
        print("Thank you for using the app! Bye :)")
    else:
        print("Can you try again? Please select y/n")
        exit()

def displayMenu():  #displaying options of the main menu
    print ('\n')
    print("Welcome to Fisher's Iris data set analysis")
    print ('-'*45, '\n')
    print('Please select one of the following options:\n')
    print("1 - About Fisher's Iris data set")
    print('2 - General Overview of the data set')
    print('3 - Statistical Summary overview by class')
    print('4 - View first and last 10 elements of dataset')
    print('5 - Plots')
    print('6 - Correlation table')
    print('x - Exit application')

if __name__ == "__main__":
	# execute only if run as a script 
	main()
