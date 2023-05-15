from commonimports import *


def data_smoothing(original_list, window_size=51, poly_order=3):
    smoothed_data = scipy.signal.savgol_filter(original_list, window_size, poly_order)
    return smoothed_data.tolist()
