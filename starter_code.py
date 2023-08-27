'''
    CS5001 2022 Fall
    Hunter(Chenlei Luo)
    Milestone 2
'''
FIGSIZE = (15, 15)
GRAPH_TYPE = 'bar'
SHOW_LENGEND = True
LENGEND_LOCATION = 'upper center'
X_LABEL = "Neighbourhood"
Y_LABEL_A = "Park count"
Y_LABEL_B = "Dog park count"
Y_LABEL_C = "Dog park percentage"
PERCENTAGE_SIGN = "%"
ON_BAR_VALUE_LOCATION = 'center'

from functions import *
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates
import matplotlib.ticker as mtick
from matplotlib.ticker import PercentFormatter

#A. Show the total number of parks per neighbourhood in descending order(Graph View)
def make_park_graph_from_data_frame(df1, xticklabels1, title1):
    '''
    Function -- make_park_graph_from_data_frame
        Creates a graph showing the total number of parks per neighbourhood in descending order
    Parameters: 
        df1 -- a DataFrame
        xticklabels1 -- a list
        title1 -- a string
        Returns a graph showing the total number of parks per neighbourhood in descending order
    '''

    figure1, ax1 = plt.subplots(figsize = FIGSIZE)
    df1.plot(kind = GRAPH_TYPE, legend = SHOW_LENGEND, ax = ax1)
    ax1.legend(loc = LENGEND_LOCATION )
    ax1.set_xticklabels(xticklabels1)
    ax1.set_title(title1)
    figure1.autofmt_xdate()
    for index, value in enumerate(df1[labels[LABEL_ONE]].tolist()):
        plt.text(index, value , str(value), ha = ON_BAR_VALUE_LOCATION)
    plt.xlabel(X_LABEL)
    plt.ylabel(Y_LABEL_A)
    plt.show()

#B. Show the total number of dog parks per neighbourhood in ascending order(Graph View)
def make_dog_park_graph_from_data_frame(df1, xticklabels1, title1):
    '''
    Function -- make_dog_park_graph_from_data_frame
        Creates a graph showing the total number of dog parks per neighbourhood in ascending order
    Parameters: 
        df1 -- a DataFrame
        xticklabels1 -- a list
        title1 -- a string
        Returns a graph showing the total number of dog parks per neighbourhood in ascending order
    '''

    figure1, ax1 = plt.subplots(figsize = FIGSIZE)
    df1.plot(kind = GRAPH_TYPE, legend = SHOW_LENGEND, ax=ax1)
    ax1.legend(loc = LENGEND_LOCATION)
    ax1.set_xticklabels(xticklabels1)
    ax1.set_title(title1)
    figure1.autofmt_xdate()
    for index, value in enumerate(df1[labels[LABEL_TWO]].tolist()):
        plt.text(index, value , str(value), ha = ON_BAR_VALUE_LOCATION)
    plt.xlabel(X_LABEL)
    plt.ylabel(Y_LABEL_B)
    plt.show()

#C. Show the total number of dog park percentage per neighbourhood in descending order(Graph View)
def make_percentage_graph_from_data_frame(df1, xticklabels1, title1):
    '''
    Function -- make_percentage_graph_from_data_frame
        Creates a graph showing the total number of dog park percentage per neighbourhood in descending order
    Parameters: 
        df1 -- a DataFrame
        xticklabels1 -- a list
        title1 -- a string
        Returns a graph showing the total number of dog park percentage per neighbourhood in descending order
    '''

    figure1, ax1 = plt.subplots(figsize = FIGSIZE)
    df1.plot(kind = GRAPH_TYPE, legend = SHOW_LENGEND, ax = ax1)
    ax1.legend(loc = LENGEND_LOCATION)
    ax1.set_xticklabels(xticklabels1)
    ax1.set_title(title1)
    ax1.yaxis.set_major_formatter(mtick.PercentFormatter()) 
    figure1.autofmt_xdate()
    for index, value in enumerate(df1[labels[LABEL_THREE]].tolist()):
        plt.text(index, value , str(value) + PERCENTAGE_SIGN, ha = ON_BAR_VALUE_LOCATION)
    plt.xlabel(X_LABEL)
    plt.ylabel(Y_LABEL_C)
    plt.show()

#D. Show the total number of parks and dog parks per neighbourhood(Graph View)
def make_overall_graph_from_data_frame(df1, xticklabels1, title1):
    '''
    Function -- make_overall_graph_from_data_frame
        Creates a graph showing the total number of parks and dog parks per neighbourhood
    Parameters: 
        df1 -- a DataFrame
        xticklabels1 -- a list
        title1 -- a string
        Returns a graph showing the total number of parks and dog parks per neighbourhood
    '''

    figure1, ax1 = plt.subplots(figsize = FIGSIZE)
    df1.plot(kind = GRAPH_TYPE, legend = SHOW_LENGEND, ax = ax1)
    ax1.legend(loc = LENGEND_LOCATION)
    ax1.set_xticklabels(xticklabels1)
    ax1.set_title(title1)
    figure1.autofmt_xdate()
    plt.xlabel(X_LABEL)
    plt.ylabel(Y_LABEL_A)
    plt.show()