import numpy as np
import pandas as pd

def calc_area_percentage(filepath, idx, margin):
    #read excel with area data
    f = pd.read_excel(filepath)
    #get area of surrounding rectangle
    A_box = (int(f["Width"][idx-1]) + 2*margin + 1)*(int(f["Heig/rht"][idx-1]) + 2*margin + 1)
    #get area of particle
    A_part = f["Area"][idx-1]
    #get ratio
    ratio = A_part/A_box

    return ratio



