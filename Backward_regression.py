def slope_k1(file_matrix_abs_smooth,file_timesteps,file_matrix_abs_smooth_list):
# Find t_start and slope
    start_val = 5
    for val in file_matrix_abs_smooth:
        if val > start_val:
            t_start = file_timesteps[file_matrix_abs_smooth_list.index(val)]
            val_start = val
            break
    slope_val = 25
    for val in file_matrix_abs_smooth:
        if val == slope_val:
            t_slope = file_timesteps[file_matrix_abs_smooth_list.index(val)]
            val_slope = val
            break
    k1 = (val_slope - val_start) / (t_slope - t_start)
    y_inter1 = val_slope-t_slope*k1
    model_listk1 = [k1 * (i-t_start)+y_inter1 for i in file_timesteps ]
    return t_start, k1, y_inter1, model_listk1

def slope_k2(file_matrix_abs_smooth,file_timesteps,file_matrix_abs_smooth_list):
#Find t100
    margin  = 0.95
    slope100_val = 100
    for val in file_matrix_abs_smooth:
        if val < slope100_val or val> margin*slope100_val:
            t_100slope = file_timesteps[file_matrix_abs_smooth_list.index(val)]
            val_100slope = val
            break
    slope80_val = 75
    for val in file_matrix_abs_smooth:
        if val == slope80_val:
            t_80slope = file_timesteps[file_matrix_abs_smooth_list.index(val)]
            val_80slope = val
            break
    k2 = (val_100slope-val_80slope)/(t_100slope-t_80slope)
    y_inter2 = val_100slope-k2*t_100slope
    model_listk2 = [k2*(i-t_80slope)+y_inter2 for i in file_timesteps]
    return t_100slope, k2, y_inter2, model_listk2

def intersect(k1,y_inter1,k2,y_inter2,file_matrix_abs_smooth_list,file_timesteps):
    t_star = (y_inter2-y_inter1)/(k1-k2)
    if t_star > 600:
        rounded_t_star = round(t_star/10)*10
    else:
        rounded_t_star = round(t_star)
    val_star = file_matrix_abs_smooth_list[file_timesteps.index(rounded_t_star)]
    return t_star, val_star



