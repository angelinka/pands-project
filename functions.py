# This file was created to separate all the functions which are called from the analysis.py so the code would be easier to understand
# Author: Angelina Belotserkovskaya

# For numerical arrays.
import numpy as np

# Data frames.
import pandas as pd

# For plotting.
import matplotlib.pyplot as plt
import seaborn as sns

# setting background style and figure size
sns.set_style("darkgrid")
sns.set(rc={'figure.figsize':(8,6)})
# we can choose different color pallets, example https://seaborn.pydata.org/tutorial/color_palettes.html
sns.color_palette("bright")

# reads in the dataset from file and assigning column names
iris = 'data/iris.data'
df = pd.read_csv(iris, sep=',', names=["sepal_length", "sepal_width", "petal_length", "petal_width", "class"])

# simple function that just prints text (it's possible to make it so it'll read it from the file but as it isn't much text just typed it here).
def about():
    print ('\n')
    print("'This is perhaps the best known database to be found in the pattern recognition literature. Fisher’s paper is " \
    "a classic in the field and is referenced frequently to this day.' - UCI Machine Learning Repository \n \n" \
    "This is a data set also known as Iris flower data set which was published by British statistician and biologist Ronald Fisher in 1936." \
    "The data set consists of 150 records (50 for each of the three Iris class: Iris setosa, Iris versicolor and Iris virginica). Each class" \
    "in turn have four attributes which were measured: the length and the width of the sepals and petals in centimeters. "
        )
    print('https://en.wikipedia.org/wiki/Iris_flower_data_set')

# overview() function provides insights into the dataset by using some handy methods which come with pandas.
def overview():
    print ('\n')
    text = (f"The Iris DataFrame has {df.ndim} dimensions. It has {df.shape[0]} rows and {df.shape[1]} columns. \nThere are {df.size} elements in total. \n" \
        f"The index of the DataFrame is: {df.index}"
        )
    print(text)
    species_type =df['class'].unique()
    print("\nThe following are the three class or class types of iris in the data set\n",*species_type, sep = " ")
    print("\nThe number of null or missing values in the iris dataframe for each column:\n", df.isnull().sum())
    print(f"\nThe number of non-NA cells for each column or row are: \n{df.count()}")
    print(f"\nA concise summary of the iris DataFrame: \n")
    df.info()

# summary() function uses describe() method on the whole dataset and on separate classes to provide statistical summary of the data.
def summary():
    pd.set_option('display.precision', 2)
    all_summ = df.describe()
    sumSetosa = df[df['class'] == 'Iris-setosa'].describe()
    sumVersicolor = df[df['class'] == 'Iris-versicolor'].describe()
    sumVirginica = df[df['class'] == 'Iris-virginica'].describe()
    combined = ('\nThe following is summary of all data set \n'+ str(all_summ) + "\n\n" + '\nSummary of Setosa class:\n\n' + str(sumSetosa) +\
    '\n\nSummary of Versicolor class:\n\n' + str(sumVersicolor) +  '\n\nSummary of Virginica class:\n\n' + str(sumVirginica) )
    return combined

# this function prints first and last 10 elements of the dataset.
def examples():
    print(f'\n\tFirst 10 elements of the dataset:\n {df.head(10)}' + \
        f'\n\n\tLast 10 elements of the dataset:\n {df.tail(10)}')

# this function is called everytime the user interacts with plots as it offers to view or save the plot
def saveOrView(file, func):
    inp = input('Enter (1) to view the plot or (2) to save to file? ')
    if inp == '1':
        plt.show()
    elif inp == '2':
        plt.savefig('Images/'+file + '.png')
        print('Successfully saved to '+ file+ '.png!')
    else:
        print("Invalid selection!") # error handling: if user selects anything other than specified options
        func() # it just calls the function again

# this function either displays or saves histogram into the file. User can choose between matplotlib or seaborn (more detailed) histogram.
def hist():
    usr_inp = input('For matplotlib histograms choose (1), for seaborn (colour encoded) (2)? ')
    if usr_inp == '1':
        fig, axes = plt.subplots(2, 2, figsize=(10,10)) # this produces a 2x2 grid of plots
        # specifiyng params of the plots and it's location on the grid
        axes[0,0].set_title("Sepal Length")
        axes[0,0].hist(df['sepal_length'], bins=7)
        axes[0,1].set_title("Sepal Width")
        axes[0,1].hist(df['sepal_width'], bins=5)
        axes[1,0].set_title("Petal Length")
        axes[1,0].hist(df['petal_length'], bins=6)
        axes[1,1].set_title("Petal Width")
        axes[1,1].hist(df['petal_width'], bins=6)
        # setting title, specifying fontsize and colour
        fig.suptitle('Histograms with matplotlib (distribution frequency per variable)', fontsize=15, color='#7F069C')
        # passing paramters to saveOrView function (name of the file and funtion name)
        saveOrView('matplHist', hist)
    # creating histogram with seaborn, adding hue, kde, binwidth, alpha(transperancy) and major ticks 
    elif usr_inp == '2':
        fig, axs = plt.subplots(2,2)
        fig.set_size_inches(12, 9)
        sns.histplot(data=df, x='sepal_length', binwidth=0.2, hue='class', kde=True, alpha=0.5, ax=axs[0,0]).tick_params(axis='both',
         which='major', labelsize=10)
        sns.histplot(data=df, x='sepal_width', binwidth=0.2, hue='class', kde=True, alpha=0.5,  ax=axs[0,1]).tick_params(axis='both',
         which='major', labelsize=10)
        sns.histplot(data=df, x='petal_length', binwidth=0.2, hue='class', kde=True, alpha=0.5, ax=axs[1,0]).tick_params(axis='both',
         which='major', labelsize=10)
        sns.histplot(data=df, x='petal_width', binwidth=0.2, hue='class', kde=True, alpha=0.5, ax=axs[1,1]).tick_params(axis='both',
         which='major', labelsize=10)
        plt.suptitle('Histograms & Probability Density Function (PDF)', fontsize=15, color='#7F069C')
        saveOrView('seabHist', hist)
        

# this function displays scatter plot for sepal length v width
def scatter():
    usr_inp = input('For sepal scatterplot  choose (1), for petal scatterplot (2)? ')
    if usr_inp == '1':
        sns.scatterplot(x='sepal_length', y='sepal_width',
                    hue='class', data=df, edgecolor='black', palette="bright")
        plt.tick_params(axis='both', which='major', labelsize=10)
        plt.xlabel("sepal_length (cm)", fontsize=15)
        plt.ylabel("sepal_width (cm)", fontsize=15)
        plt.suptitle('Scatterplot - sepal length v width', fontsize=20, color='#7F069C')
        saveOrView('scatterSep', scatter)       
    elif usr_inp == '2':
        sns.scatterplot(x='petal_length', y='petal_width',
                hue='class', data=df, edgecolor='black', palette="bright")
        plt.tick_params(axis='both', which='major', labelsize=10)
        plt.xlabel("petal_length (cm)", fontsize=15)
        plt.ylabel("petal_width (cm)", fontsize=15)
        plt.suptitle('Scatterplot - petal length v width', fontsize=20, color='#7F069C')
        saveOrView('scatterPet', scatter)
        
# this function displays a pairplot https://seaborn.pydata.org/generated/seaborn.pairplot.html?highlight=pairplot#seaborn.pairplot
def pairPlt():
    sns.pairplot(data=df, hue='class', palette="colorblind", markers=["o", "s", "D"])
    plt.subplots_adjust(top=.95) # creates space above the plot for the title 
    plt.tick_params(axis='both', which='major', labelsize=5) # formats ticks
    # sets title with formatting
    plt.suptitle('Pairplot (scatterplots and marginal distribution of the data)', fontsize=15, color='#7F069C')
    saveOrView('pairplot', pairPlt)
    

# this function creates pairgrid with KDE 
def pairgrid():
    pg = sns.PairGrid(df, hue = 'class', palette='colorblind')
    pg.map_upper(sns.kdeplot, shade=True, alpha=0.5) # creates KDE with shade above the diagonal. # aplha=0.5 so we can see through
    pg.map_lower(sns.kdeplot, alpha=0.5) # creates KDE without shade below the diagonal.
    pg.map_diag(sns.histplot, multiple="stack", element="step") # stacked histogram on the diagonal
    plt.subplots_adjust(top=.95) # creates space above the plot for the title
    plt.tick_params(axis='both', which='major', labelsize=5) # sets ticks
    # sets title and formatting
    plt.suptitle('Pair Grid (KDE scatterplots and histograms)', fontsize=15, color='#7F069C')
    pg.add_legend(bbox_to_anchor=(1, 0.5)) # defines legend location
    saveOrView('pairgrid', pairgrid)

# this function creates a heatmap based on correlation   
def heatMap():
    plt.figure(figsize=(10,11)) # customising figure size
    sns.heatmap(df.corr(), annot=True)
    plt.suptitle('Correlation Heatmap', fontsize=15, color='#7F069C')
    saveOrView('heatmap', heatMap)

# this function creates boxplot grid by each class
def boxplt():
    f, axes = plt.subplots(2,2) # this produces a 2x2 grid of boxplots
    # there are 4 boxplots. axes[0,0] refers to position on grid [row, column]
    # linesize and colour palette defined
    sns.boxplot(x = 'class', y='sepal_length', data = df, ax=axes[0,0], linewidth=0.5, palette='colorblind')
    sns.boxplot(x = 'class', y='sepal_width', data = df, ax=axes[0,1], linewidth=0.5, palette='colorblind')
    sns.boxplot(x = 'class', y='petal_length', data = df, ax=axes[1,0], linewidth=0.5, palette='colorblind')
    sns.boxplot(x = 'class', y='petal_width', data = df, ax=axes[1,1], linewidth=0.5, palette='colorblind')
    # setting x and y labels. Empty string on x axes as names of the flower classes are already specified and it will only 
    #create more clutter
    axes[0,0].set_xlabel(" ")
    axes[0,0].set_ylabel("Sepal length (cm)", fontsize=10)
    axes[0,1].set_xlabel(" ")
    axes[0,1].set_ylabel("Sepal width (cm)", fontsize=10 )
    axes[1,0].set_xlabel(" ")
    axes[1,0].set_ylabel("Petal length (cm)", fontsize=10)
    axes[1,1].set_xlabel(" ")
    axes[1,1].set_ylabel("Petal width (cm)", fontsize=10)
    # title and formatting
    f.suptitle('Boxplots by classes', fontsize=15, color='#7F069C')
    saveOrView('boxplt', boxplt)

# this function creates 4 violin plots on a 2x2 grid by each class
def violin():
    fig, axes = plt.subplots(2, 2, figsize=(12,8))
    sns.violinplot(x = 'class', y='sepal_length', data = df, ax=axes[0,0], palette='colorblind', inner='quartile')
    sns.violinplot(x = 'class', y='sepal_width', data = df, ax=axes[0,1], palette='colorblind', inner='quartile')
    sns.violinplot(x = 'class', y='petal_length', data = df, ax=axes[1,0], palette='colorblind', inner='quartile')
    sns.violinplot(x = 'class', y='petal_width', data = df, ax=axes[1,1], palette='colorblind', inner='quartile')
    # setting x and y labels. Empty string on x axes as names of the flower classes are already specified and it will only 
    #create more clutter
    axes[0,0].set_xlabel(" ")
    axes[0,0].set_ylabel("Sepal length (cm)", fontsize=10)
    axes[0,1].set_xlabel(" ")
    axes[0,1].set_ylabel("Sepal width (cm)", fontsize=10 )
    axes[1,0].set_xlabel(" ")
    axes[1,0].set_ylabel("Petal length (cm)", fontsize=10)
    axes[1,1].set_xlabel(" ")
    axes[1,1].set_ylabel("Petal width (cm)", fontsize=10)
    # title and formatting
    fig.suptitle('Violin plot by classes', fontsize=15, color='#7F069C')
    saveOrView('violin', violin)

# this function shows correlation between attributes, first for the whole data set
# and separated by class    
def corr():
    print("\t\tCorrelation between pairs of variables for the Iris dataset \n")
    print(df.corr())
    print("\n\n\t\tCorrelation between pairs of variables for the Iris dataset by flower type \n")
    print(df.groupby("class").corr())