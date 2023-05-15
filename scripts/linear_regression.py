from commonimports import *


def linear_regression(roi, data_list, time_list, corr_start_val=7, corr_end_val=99):

    # Find straight line values
    for i, val in enumerate(data_list):
        if val >= corr_start_val:
            str_val1 = val
            t_s = time_list[i]
            break
    for i, val in enumerate(data_list):
        if val >= corr_end_val:
            str_val2 = val
            t_f = time_list[i]
            break

    # Find straight line slope
    try:
        sls = (str_val2 - str_val1) / (t_f - t_s)
    except NameError:
        print(f"Particle {roi} does not reach 100% corroded. Skipping...")
        return False

    # Find distances between data and straight line
    p_slope = -1 / sls
    sli = sls * -t_s + corr_start_val
    dists = []
    dist_times = []
    for i, time in enumerate(time_list):
        if t_s <= time <= t_f:
            val = data_list[i]
            p_intersect = val - p_slope * time
            d_time = (sli - p_intersect) / (p_slope - sls)
            d_val = p_slope * d_time + p_intersect

            d = math.sqrt((val - d_val)**2 + (time - d_time)**2)
            dists.append(d)
            dist_times.append(time)

    # Find t_k from minimum distance
    t_k = dist_times[dists.index(max(dists))]

    # Find k1 using linear regression
    k1_values = data_list[time_list.index(t_s):time_list.index(t_k)]
    k1_times = time_list[time_list.index(t_s):time_list.index(t_k)]
    k1 = LinearRegression().fit(np.array(k1_times).reshape(-1, 1), np.array(k1_values).reshape(-1, 1))

    # Find k2 using linear regression
    k2_values = data_list[time_list.index(t_k):time_list.index(t_f)]
    k2_times = time_list[time_list.index(t_k):time_list.index(t_f)]
    k2 = LinearRegression().fit(np.array(k2_times).reshape(-1, 1), np.array(k2_values).reshape(-1, 1))

    # Set variables
    k1_coef = k1.coef_[0]
    k1_intercept = k1.intercept_[0]
    k2_coef = k2.coef_[0]
    k2_intercept = k2.intercept_[0]

    # Update t_k
    t_k_updated = float(str((k2.intercept_[0] - k1.intercept_[0]) / (k1.coef_[0] - k2.coef_[0]))[1:-1])

    # Update t_f
    t_f_updated = float(str((100 - k2.intercept_[0]) / k2.coef_[0])[1:-1])

    # Create model for k1
    k1_model = []
    for i, time in enumerate(time_list):
        if time >= t_s:
            if time <= t_k_updated:
                k1_model.append([time, k1_coef * time + k1_intercept])

    # Create model for k2
    k2_model = []
    for i, time in enumerate(time_list):
        if time >= t_k_updated:
            if time <= t_f_updated:
                k2_model.append([time, k2_coef * time + k2_intercept])

    # Finalize
    k1_vals = [float(str(k1_coef)[1:-1]), float(str(k1_intercept)[1:-1])]
    k2_vals = [float(str(k2_coef)[1:-1]), float(str(k2_intercept)[1:-1])]

    return roi, k1_vals, k2_vals, t_s, t_k_updated, t_f_updated, k1_model, k2_model


def linear_regression_plotting(k1_model, k2_model, t_s, t_k, t_f):

    # Extract values from k1_model array
    k1_l = []
    k1_t = []
    for elem in k1_model:
        k1_l.append(elem[1])
        k1_t.append(elem[0])

    # Extract values from k2_model array
    k2_l = []
    k2_t = []
    for elem in k2_model:
        k2_l.append(elem[1])
        k2_t.append(elem[0])

    # Plot t_s, t_k, t_f as vertical dashed lines
    plt.vlines(t_s, 0, 110, "gray", linestyles="dashed", label="t_s")
    plt.vlines(t_k, 0, 110, "cyan", linestyles="dashed", label="t_k")
    plt.vlines(t_f, 0, 110, "yellow", linestyles="dashed", label="t_f")

    # Plot k1 and k2 models
    plt.plot(k1_t, k1_l, "green", label="k1 model")
    plt.plot(k2_t, k2_l, "red", label="k2 model")
