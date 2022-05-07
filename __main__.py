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

def get_earliest_check_in_date(data: pd.DataFrame) -> pd.DataFrame:
  """
   Returns the customer with the latest check in date
   :param pd.Dataframe data: dataset
   :type data: pd.DataFrame
   :return: Dataframe with customer name
   :rtype: pd.DataFrame
  """
  data['Last Check-In Date'] = pd.to_datetime(data['Last Check-In Date'], infer_datetime_format= True, errors='coerce')
  earliest = min(data['Last Check-In Date'])
  ans = data.loc[data['Last Check-In Date'] == earliest]
  return(ans)

def get_latest_check_in_date(data: pd.DataFrame) -> pd.DataFrame:
  """
   Returns the customer with the earliest check in date
   :param pd.Dataframe data: dataset
   :type data: pd.DataFrame
   :return: Dataframe with customer name
   :rtype: pd.DataFrame
  """
  data['Last Check-In Date'] = pd.to_datetime(data['Last Check-In Date'], infer_datetime_format= True, errors='coerce')
  latest = max(data['Last Check-In Date'])
  ans = data.loc[data['Last Check-In Date'] == latest]
  return(ans)

def get_alphabetic_customer_names(data: pd.DataFrame) -> pd.DataFrame:
  """
   Get customer names in Alphabetic (A-Z) Order
   :param pd.Dataframe data: dataset
   :type data: pd.DataFrame
   :return: Dataframe with customer names
   :rtype: pd.DataFrame
   :raises Error: if the entry dataset has not got the correct headers
  """
 
  warnings.filterwarnings("ignore")

  if(data['First Name'].isnull().sum() != 0):
    logging.warning(f"Found null values in column First Name at { get_nan_index(data, 'First Name')}")
   
  if(data['Last Name'].isnull().sum() != 0):
    logging.warning(f"Found null values in column Last Name at {get_nan_index(data, 'Last Name')}")
    
  data = data.dropna(how='all')
  data['First Name'].fillna(' ', inplace = True)
  data['Last Name'].fillna(' ', inplace = True)
  data['Full Name'] = data[['First Name', 'Last Name']].agg(' '.join, axis=1)
  data['Full Name'] = data['Full Name'].str.strip()
  data = data.sort_values('Full Name', ascending=True)
  return(pd.DataFrame(data['Full Name']))

def get_alphabetic_jobs(data: pd.DataFrame) -> pd.DataFrame:
  """
   Returns a list of the companies user’s jobs ordered alphabetically (A - Z)
   :param pd.Dataframe data: dataset
   :type data: pd.DataFrame
   :return: Dataframe with customer names
   :rtype: pd.DataFrame
   :raises Error: if the entry dataset has not got the correct headers
  """
  
  if(data['Job'].isnull().sum() != 0):
    logging.warning(f"Found null values in column Job at { get_nan_index(data, 'Job')}")
  data = data.sort_values('Job', ascending=True)
  jobs = pd.DataFrame(data['Job'], columns = ["Job"])
  jobs = jobs.dropna()
  return(jobs)

def main():
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

    

    check_required_items(data)
    ans=True
    while ans:
        print ("""
        1. Get customer names in Alphabetic (A-Z) Order
        2. Get customer jobs in Alphabetic (A-Z) Order
        3. Get customer with the earliest check in date
        4. Get customer with the latest check in date
        """)
        ans=input("What would you like to do? ")        
        if ans=="1": 
            print(get_alphabetic_customer_names(data))
        elif ans=="2":
            print(get_alphabetic_jobs(data))
        elif ans=="3":
            print(get_earliest_check_in_date(data))
        elif ans=="4":
            print(get_latest_check_in_date(data))
        elif ans !="":
            print("\n Not Valid Choice Try again") 


if(__name__ == "__main__"):
    main()
