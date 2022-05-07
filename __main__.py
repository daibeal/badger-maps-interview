#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Dairon Andrés Benites ALdaz"
__copyright__ = "Copyright 2022, @daibeal"
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Dairon Andrés Benites ALdaz"
__email__ = "contact@andresbenites.es"
__status__ = "Production"

# Load libraries

import numpy as np
import pandas as pd
import logging
import warnings


# Load file
def load_file(file_path : str) -> pd.DataFrame:
    try:
        data = pd.read_csv(file_path)
        return(data)
    except:
        logging.exception("Error loading file...")

# Set required fields
required_items = ['Street', 'Zip', 'City', 'Last Check-In Date', 'Company']

def check_required_items(data):
    # Check nulls in all required fields
    for required_item in required_items:
        null_count = data[required_item].isnull().sum()
        if(null_count > 1):
            logging.warning(f"Found {null_count} null values in {required_item}")
        elif(null_count == 1):
            logging.warning(f"Found {null_count} null value in {required_item}")
        else:
            print(f'No null values found in {required_item}')
            
def get_nan_index(data :pd.DataFrame, col_name : str):
  try:
    res = data.loc[pd.isna(data[col_name]), :].index
    return(res)
  except:
    return(-1)

def main():
    # Load file
    try:
        import tkinter as tk
        from tkinter import filedialog, messagebox
        root = tk.Tk()
        root.withdraw()
        messagebox.showinfo("Information","Please select the file to be processed")
        file_path = filedialog.askopenfilename(filetypes=[("CSV files","*.csv")])
        data = load_file(file_path)
    except:
        logging.error("Error loading file throught GUI...")
        logging.info("Launching alternative ...")
        file_path = input("Please enter the file path: ")
        data = load_file(file_path)
    # Check required items
    check_required_items(data)
        
if(__name__ == "__main__"):
    main()