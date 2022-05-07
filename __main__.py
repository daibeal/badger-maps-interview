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
        
if(__name__ == "__main__"):
    main()