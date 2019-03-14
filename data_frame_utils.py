from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
from pprint import pprint
import os

from sys import platform as sys_pf
if sys_pf == 'darwin':
    import matplotlib
    matplotlib.use("TkAgg")
import matplotlib.pyplot as plt





def create_data_frame(data_dict):
    data_length = len(data_dict['loan_status'])
    index = list(range(1, data_length + 1))
    data_frame = pd.DataFrame(data_dict, index=index)
    return data_frame

def create_plots(data_frame):
    plot_interest_rates(data_frame)
    # plot_principal_balances(data_frame)
    plt.show()

def plot_interest_rates(data_frame):
    bar_graph = data_frame[['interest_rate']].plot(kind='bar')
    plt.title('Interest Rates')
    plt.xlabel('Loans')
    plt.ylabel('%')

def plot_principal_balances(data_frame):
    bar_graph = data_frame[['principal_balance']].plot(kind='bar')
    plt.title('Principal Balance')
    plt.xlabel('Loans')
    plt.ylabel('$')


def create_csv(data_frame):
    file_name = 'student_loans.csv'
    cwd = os.getcwd()
    file_path = os.path.join(cwd, file_name)
    data_frame.to_csv(file_path)