from commonimports import *


def classA_check(type, data_list, time_list):
    perc_threshold = 60
    sphase = False
    if type == "Secondary":
        eval_time = 4000
    elif type == "Theta":
        eval_time = 2000
    if type == "S-phase":
        sphase = True
        classA = True

    if sphase == False:
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
