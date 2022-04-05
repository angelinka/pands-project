# This file was created to separate all the functions which are called from the analysis.py so the code would be easier to understand
# Author: Angelina Belotserkovskaya

# For numerical arrays.
import numpy as np

# Data frames.
import pandas as pd

# For plotting.
import matplotlib.pyplot as plt
import seaborn as sns

# reads in the dataset
iris = 'data/iris.data'
df = pd.read_csv(iris, sep=',', names=["sepal_length", "sepal_width", "petal_length", "petal_width", "class"])

def about():
    print ('\n')
    print("'This is perhaps the best known database to be found in the pattern recognition literature. Fisher’s paper is " \
    "a classic in the field and is referenced frequently to this day.' - UCI Machine Learning Repository \n \n" \
    "This is a data set also known as Iris flower data set which was published by British statistician and biologist Ronald Fisher in 1936." \
    "The data set consists of 150 records (50 for each of the three Iris species: Iris setosa, Iris versicolor and Iris virginica). Each species" \
    "in turn have four attributes which were measured: the length and the width of the sepals and petals in centimeters. "
        )
    print('https://en.wikipedia.org/wiki/Iris_flower_data_set')


def overview():
    print ('\n')
    text = (f"The Iris DataFrame has {df.ndim} dimensions. It has {df.shape[0]} rows and {df.shape[1]} columns. \nThere are {df.size} elements in total. \n" \
        f"The index of the DataFrame is: {df.index}"
        )
    print(text)
    species_type =df['class'].unique()
    print("\nThe following are the three class or species types of iris in the data set \n",*species_type, sep = " ")
    print("\nThe number of null or missing values in the iris dataframe for each column: \n", df.isnull().sum())
    print(f"\nThe number of non-NA cells for each column or row are: \n{df.count()}")
    print(f"\nA concise summary of the iris DataFrame: \n")
    df.info()


    