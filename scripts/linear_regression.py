from commonimports import *


def linear_regression(roi, time_list, data_list, initial_value=5, slope_value=20, slope_value2=80, value=2):
    # Find t_onset and t_slope
    for val in data_list:
        if val >= initial_value:
            t_onset = time_list[data_list.index(val)]
            break
    for val in data_list:
        if val >= slope_value:
            t_slope = time_list[data_list.index(val)]
            break
    for val in data_list:
        if val >= slope_value2:
            t_slope2 = time_list[data_list.index(val)]
            break


    # Find k1
    k1 = (data_list[time_list.index(t_slope)] - data_list[time_list.index(t_onset)]) / (t_slope - t_onset)

    # Find t_star (method 1)
    model_values = [k1 * i for i in time_list]
    upper_bin_values = [i + value for i in model_values]
    lower_bin_values = [i - value for i in model_values]
    for i, value in enumerate(data_list):
        if time_list[i] >= t_onset:
            if lower_bin_values[i] >= value or value >= upper_bin_values[i]:
                t_star = time_list[i]
                # print("data:", data_list)
                # print("model:", model_values)
                # print("upper", upper_bin_values)
                # print("lower:", lower_bin_values)
                # print("value:", value)
                # print("t_star:", t_star)
                # print("t_onset:", t_onset)
                break

    # # Find t_star (method 2)
    # model_values = [k1 * i for i in time_list]
    # max_ratio = 3
    # for i in range(len(1, model_values)):
    #     diff1 = model_values[i-1] - data_list[i-1]
    #     diff2 = model_values[i] - data_list[i]
    #     ratio = diff2 / diff1
    #     if ratio >= max_ratio:
    #         t_star = time_list[i]
    #         break

    # Find t_100
    t_100 = 0
    for val in data_list:
        if val == 100:
            t_100 = time_list[data_list.index(val)]
            break
    if t_100 == 0:
        print(f"Particle {roi} does not reach 100% corrosion level.")
        t_100 = time_list[len(data_list)-1]

    # # Find k2 (method 1)
    # k2 = (data_list[time_list.index(t_100)] - data_list[time_list.index(t_slope2)]) / (t_100 - t_slope2)

    # Find k2 (method 2)
    k2 = (data_list[time_list.index(t_100)] - model_values[time_list.index(t_star)]) / (t_100 - t_star)

    return roi, k1, k2, t_onset, t_star, t_100


def linear_regression_plotting(k1, k2, t_onset, t_star, t_100, time_list, value=2):
    k1_time = []
    k1_list = []
    k2_time = []
    k2_list = []
    # print(time_list)
    # print(t_onset, t_star, t_100)
    for time in time_list:
        if t_onset <= time <= t_star:
            k1_time.append(time)
            k1_list.append(k1 * time)
            # print(time)
            # print(k1_time)
        elif t_star <= time <= t_100:
            if len(k2_time) == 0:
                k2_time.append(k1_time[-1])
                k2_list.append(k1_list[-1])
            # print("k2 now")
            # print(time)
            # print(k2_time)
            k2_time.append(time)
            k2_list.append(k2 * (time - k1_time[-1]) + k1_list[-1])
    k1_lower = [i - value for i in k1_list]
    k1_upper = [i + value for i in k1_list]
    k2_lower = [i - value for i in k2_list]
    k2_upper = [i + value for i in k2_list]
    plt.plot(k1_time, k1_list, "-", label="k1 model")
    plt.plot(k2_time, k2_list, "-", label="k2 model")
    plt.plot(k1_time, k1_upper, "r--", label="model bounds")
    plt.plot(k1_time, k1_lower, "r--")
    plt.plot(k2_time, k2_upper, "r--")
    plt.plot(k2_time, k2_lower, "r--")
    plt.vlines(t_onset, 0, 110, "gray", linestyles="dashed")
    plt.vlines(t_star, 0, 110, "gray", linestyles="dashed")
    plt.vlines(t_100, 0, 110, "gray", linestyles="dashed")
    return

if __name__ == "__main__":
    roi = 1
    k1 = 1
    k2 = 0.1
    t_onset = 5
    t_star = 55
    t_100 = 89
    time_list = [i for i in range(100)]
    linear_regression_plotting(k1, k2, t_onset, t_star, t_100, time_list, value=5)
    plt.show()
