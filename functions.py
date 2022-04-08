# This file was created to separate all the functions which are called from the analysis.py so the code would be easier to understand
# Author: Angelina Belotserkovskaya

# For numerical arrays.
import numpy as np

# Data frames.
import pandas as pd

# For plotting.
import matplotlib.pyplot as plt
import seaborn as sns

# reads in the dataset from file
iris = 'data/iris.data'
df = pd.read_csv(iris, sep=',', names=["sepal_length", "sepal_width", "petal_length", "petal_width", "class"])

# simple function that just prints text (it's possible to make it so it'll read it from the file but as it isn't much text just typed it here).
def about():
    print ('\n')
    print("'This is perhaps the best known database to be found in the pattern recognition literature. Fisher’s paper is " \
    "a classic in the field and is referenced frequently to this day.' - UCI Machine Learning Repository \n \n" \
    "This is a data set also known as Iris flower data set which was published by British statistician and biologist Ronald Fisher in 1936." \
    "The data set consists of 150 records (50 for each of the three Iris species: Iris setosa, Iris versicolor and Iris virginica). Each species" \
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
    print("\nThe following are the three class or species types of iris in the data set\n",*species_type, sep = " ")
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

def hist():
    usr_inp = input('For matplotlib histograms choose (1), for seaborn (colour encoded) (2)? ')
    if usr_inp == '1':
        fig, axes = plt.subplots(2, 2, figsize=(10,10))
    
        axes[0,0].set_title("Sepal Length")
        axes[0,0].hist(df['sepal_length'], bins=7)

        axes[0,1].set_title("Sepal Width")
        axes[0,1].hist(df['sepal_width'], bins=5);

        axes[1,0].set_title("Petal Length")
        axes[1,0].hist(df['petal_length'], bins=6);

        axes[1,1].set_title("Petal Width")
        axes[1,1].hist(df['petal_width'], bins=6);
        inp = input('Would you like to view the plot (1) or to save to file (2): ')
        if inp == '1':
            plt.show()
        elif inp == '2':
            plt.savefig('Images/matplHist.png')
            print('Successfully saved to matplHist.png!')
        else:
            print("Invalid selection!")
            hist()
    elif usr_inp == '2':
        fig, axs = plt.subplots(2,2)
        fig.set_size_inches(12, 9)
        sns.histplot(data=df, x='sepal_length', binwidth=0.2, hue='class', kde=True, alpha=0.5, ax=axs[0,0]).tick_params(axis='both', which='major', labelsize=10)
        sns.histplot(data=df, x='sepal_width', binwidth=0.2, hue='class', kde=True, alpha=0.5,  ax=axs[0,1]).tick_params(axis='both', which='major', labelsize=5)
        sns.histplot(data=df, x='petal_length', binwidth=0.2, hue='class', kde=True, alpha=0.5, ax=axs[1,0]).tick_params(axis='both', which='major', labelsize=5)
        sns.histplot(data=df, x='petal_width', binwidth=0.2, hue='class', kde=True, alpha=0.5, ax=axs[1,1]).tick_params(axis='both', which='major', labelsize=5)
        inp = input('Would you like to view the plot (1) or to save to file (2): ')
        if inp == '1':
            plt.show()
        elif inp == '2':
            plt.savefig('Images/seabHist.png')
            print('Successfully saved to seabHist.png!')
        else:
            print("Invalid selection!")
            hist()