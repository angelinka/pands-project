# Programming-and-Scripting

<img src="https://www.svgrepo.com/show/235624/analytics-graph.svg" width="100" height="100">

## Description

This repository was created to complete the project for Programming and Scripting module. 
The aim of the project is to research and analyse the well-known Fisher’s Iris data set using Python programming language.
Python is widely used within data analytics, statistics and machine learning fields as with ability to import third party
modules it makes it easy to analise and visualise big data sets.

## Repository content

There are two main files in this repository:
1. **IrisDataSetAnalysis.ipynb** provides an overview of Fisher’s Iris data set, investigates the data and attributes of the data frame and provides visual analysis of the data in a user friendly Jupyter notebook format.
2. **analysis.py** is the main script, it contains python code which has been used to perform the analysis of the data. The program performs the following:
    - Outputs About section and General Overview of the dataset;
    - Prints out or saves Statistical Summary overview for whole dataset and by classes in a text file;
    - Outputs first and last 10 elements of dataset;
    - Saves or outputs various plots: histograms, scatterplots, pairplot, KDE pairgrid, heatmap, boxplots and violin plots;
    - Outputs correlation table.
Additional files and folders:
1. **functions.py** contains all functions which are called when analyses.py is running. This file was created to separate the function from the main file
ta make it easier to navigate and avoid clutter. This is imported into analysis.py.  
2. **data** folder contains iris.data (original data set) and text files (which are saved when running the code as explained above)
3. **Images** folder contains images used in jupyter notebook and plots (which are saved when running the code as explained above)

## How to install the notebook

You need to run this notebook in python environment (please refer to packages and dependencies in requirements.txt file) the easiest way to do that is to install Anaconda
1. Download [Anaconda](https://docs.anaconda.com/anaconda/install/index.html). If not using Anaconda can install packages via ***pip install / homebrew install*** (Example: pip install matplotlib).
2. Download [cmder](https://cmder.net) if using Windows. Or use Terminal if on macOS or Linux.

## How to run the notebook

1. Open terminal / cmder.
2. Run command `jupyter notebook` or `jupyter lab` from command line. It's a web application which runs on your local machine (you will be able to see the server running in Terminal/cmder). To stop the application running press control+c and then type 'y' to confirm.
3. The browser page should open up automatically. Select the file you would like to view.

## How to run the scrypt

To run the Python script, first open Terminal/cmder, navigate to the folder downloaded from this repository.
Note, you need to have Python 3 installed with the necessary libraries. Or use Anaconda environment.
Run `python analysis.py` command to interact with the program.
Once the program starts you can choose any options available from the menu to see the analysis of the dataset.  


References
Seaborn methods used:
https://seaborn.pydata.org/generated/seaborn.PairGrid.html?highlight=pairgrid#seaborn.PairGrid
https://seaborn.pydata.org/generated/seaborn.kdeplot.html
https://seaborn.pydata.org/tutorial/color_palettes.html
https://seaborn.pydata.org/generated/seaborn.histplot.html
https://seaborn.pydata.org/generated/seaborn.pairplot.html
https://seaborn.pydata.org/generated/seaborn.violinplot.html
https://seaborn.pydata.org/generated/seaborn.heatmap.html?highlight=heatmap#seaborn.heatmap
https://seaborn.pydata.org/generated/seaborn.boxplot.html?highlight=boxplot#seaborn.boxplot
Pandas methods used:
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.corr.html
Other:
https://htmlcolorcodes.com/
https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/