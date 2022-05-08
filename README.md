# Programming-and-Scripting

<img src="https://www.svgrepo.com/show/235624/analytics-graph.svg" width="100" height="100">

## Description

This repository was created to complete the project for Programming and Scripting module. 
The aim of the project is to research and analyse the well-known Fisher’s Iris data set using Python programming language.
Python is widely used within data analytics, statistics and machine learning fields as with ability to import third party
modules it makes it easy to analise and visualise big data sets.

## Repository content

There are two main files in this repository:
1. **IrisDataSetAnalysis.ipynb** this is the main file which provides an overview of Fisher’s Iris dataset, investigates the data and attributes of the dataset and provides visual analysis of the data in a user friendly Jupyter notebook format. This file contains more information about the dataset and additional comments and plots which were not included into analysis.py
2. **analysis.py** is the main script, it contains python code which has been used to perform the analysis of the data. The program performs the following:
    - Outputs About section and General Overview of the dataset;
    - Prints out or saves Statistical Summary overview for whole dataset and by classes in a text file;
    - Outputs first and last 10 elements of dataset;
    - Saves or outputs various plots: histograms, scatterplots, pairplot, KDE pairgrid, heatmap, boxplots and violin plots;
    - Outputs correlation table.

Additional files and folders:

1. **functions.py** contains all functions which are called when analyses.py is running. This file was created to separate the function from the main file
ta make it easier to navigate and avoid clutter. This is imported into analysis.py. 
2. **requirements.txt** file contains all the libraries required for script and jupyter notebook to run. 
3. **data** folder contains iris.data (original data set) and text files (which are saved when running the code as explained above)
4. **Images** folder contains images used in jupyter notebook and plots (which are saved when running the code as explained above)

## How to install the notebook

You need to run this notebook in python environment (please refer to packages and dependencies in requirements.txt file) the easiest way to do that is to install Anaconda
1. Download [Anaconda](https://docs.anaconda.com/anaconda/install/index.html). If not using Anaconda can install packages via ***pip install / homebrew install*** (Example: pip install matplotlib).
2. Download [cmder](https://cmder.net) if using Windows. Or use Terminal if on macOS or Linux.

## How to run the notebook

1. Open terminal / cmder.
2. Run command `jupyter notebook` or `jupyter lab` from command line. It's a web application which runs on your local machine (you will be able to see the server running in Terminal/cmder). To stop the application running press control+c and then type 'y' to confirm.
3. The browser page should open up automatically. Select the file you would like to view.

Ypu can also start `jupyter notebook` or `jupyter lab` from Anaconda-Navigator.

You can view the notebook in static or dynamic form by clicking the following images:

[![nbviewer](https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg)](https://nbviewer.org/github/angelinka/pands-project/blob/main/IrisDataSetAnalysis.ipynb)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/angelinka/pands-project/HEAD)

## How to run the scrypt

To run the Python script, first open Terminal/cmder, navigate to the folder downloaded from this repository.
Note, you need to have Python 3 installed with the necessary libraries. Or use Anaconda environment.
Run `python analysis.py` command to interact with the program.
Once the program starts you can choose any options available from the menu to see the analysis of the dataset.  


## Credits
I heavily relied on the seaborn, matplotlib, pandas and stackoverflow resources in creating this repository.

[matplotlib.org](https://matplotlib.org/stable/tutorials/introductory/pyplot.html#sphx-glr-tutorials-introductory-pyplot-py)

[pandas](https://pandas.pydata.org/docs/index.html)

[seaborn](https://seaborn.pydata.org/api.html)

[stackoverflow](https://stackoverflow.com)

## Contact

[angelb511@gmail.com](mailto:angelb511@gmail.com)