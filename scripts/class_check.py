from commonimports import *


# Function Definition
def classA_check(type, data_list, time_list):

    # Set threshold to consider if it is of class A or not
    perc_threshold = 60

    sphase = False
    # Check which type the particle is and return evaluation time (S-phase is always considered class A)
    if type == "Secondary":
        eval_time = 4000
    elif type == "Theta":
        eval_time = 2000
    if type == "S-phase":
        classA = True
        sphase = True

    # Check if threshold is met at evaluation time and return True or False
    if not sphase:
        for i in range(len(data_list)):
            val = data_list[i]
            time = time_list[i]
            if time <= eval_time:
                if val >= perc_threshold:
                    classA = True
                else:
                    classA = False

    return classA

if __name__ == "__main__":
    print(classA_check("S-Phase", [0,1,2,3], [0,1,2,3]))
