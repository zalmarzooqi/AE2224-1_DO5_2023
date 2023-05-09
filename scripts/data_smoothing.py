from commonimports import *


def data_smoothing(original_list, window_size=15):
    weights = np.repeat(1.0, window_size) / window_size
    smooth_list = np.convolve(original_list, weights, 'valid')
    return smooth_list.tolist()
