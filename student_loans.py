from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import pandas as pd
from pprint import pprint
import os

from data_frame_utils import create_csv, create_data_frame, create_plots
from get_html import get_html, get_uls
from handle_uls import handle_uls


def get_data():
    html = get_html()
    uls_dict = get_uls(html)
    data = handle_uls(uls_dict)
    data_frame = create_data_frame(data)
    create_csv(data_frame)
    create_plots(data_frame)
    


if __name__ == '__main__':
    get_data()