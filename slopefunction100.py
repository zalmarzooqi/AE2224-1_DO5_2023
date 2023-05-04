def slope(file_matrix_abs_smooth,file_timesteps,file_matrix_abs_smooth_list):
# Find t_start and slope
    start_val = 80
    for val in file_matrix_abs_smooth:
        if val > start_val:
            t_start = file_timesteps[file_matrix_abs_smooth_list.index(val)]
            val_start = val
            break
    slope_val = 100
    for val in file_matrix_abs_smooth:
        if val == slope_val:
            t_slope = file_timesteps[file_matrix_abs_smooth_list.index(val)]
            val_slope = val
            break
    slope_est = (val_slope - val_start) / (t_slope - t_start)
    y_intercept = val_slope-t_slope*slope_est
    model_list = [slope_est * (i-t_start)+y_intercept for i in file_timesteps ]

    # Find t_star
    max_ratio = 3
    for i in range(1, len(file_matrix_abs_smooth_list)):
        diff1 = model_list[i-1] - file_matrix_abs_smooth_list[i-1]
        diff2 = model_list[i] - file_matrix_abs_smooth_list[i]
        ratio = diff2 / diff1
        if ratio > max_ratio:
            t_star = file_timesteps[i]
            break
    return slope_est, model_list, t_star