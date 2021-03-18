#########################################################################################################
### Generates a CSV file from text ###
#########################################################################################################

### Import ###
import glob
import os
from pathlib import Path

### Default labels ###
exp_none = "NONE"
exp_yes = "YES"
exp_off = "OFF"
result_missing = "NA"

### Labels as they appear on the pdf file and text file ###
exp1 = "manufacturers name"
exp2 = "date of accident"
exp3 = "time of accident"
#exp4 = "am"
#exp5 = "pm"
#exp6 = "city" #problem of none
#exp7 = "state vehicle is registered in:"
#exp8 = "moving"

### Labels for vehicle damage ###
exp9_1 = "major"
exp9_2 = "unknown"
exp9_3 = "none"
exp9_4 = "moderate"
exp9_5 = "minor"
result_9_3 = "no damage"

### Labels for weather ###
exp19_A_1 = "weather a 1"
exp19_A_2 = "weather a 2"
exp19_B_1 = "weather b 1"
exp19_B_2 = "weather b 2"
exp19_C_1 = "weather c 1"
exp19_C_2 = "weather c 2"
exp19_D_1 = "weather d 1"
exp19_D_2 = "weather d 2"
exp19_E_1 = "weather e 1"
exp19_E_2 = "weather e 2"
exp19_F_1 = "weather f 1"
exp19_F_2 = "weather f 2"
exp19_G_1 = "weather g 1"
exp19_G_2 = "weather g 2"

result19_A = "clear"
result19_B = "cloudy"
result19_C = "raining"
result19_D = "snowing"
result19_E = "fog/visibility"
result19_F = "other"
result19_G = "wind"

### Labels for lighting ###
exp20_A_1 = "lighting a 1"
exp20_A_2 = "lighting a 2"
exp20_B_1 = "lighting b 1"
exp20_B_2 = "lighting b 2"
exp20_C_1 = "lighting c 1"
exp20_C_2 = "lighting c 2"
exp20_D_1 = "lighting d 1"
exp20_D_2 = "lighting d 2"
exp20_E_1 = "lighting e 1"
exp20_E_2 = "lighting e 2"

result20_A = "daylight"
result20_B = "dusk-dawn"
result20_C = "dark-street lights"
result20_D = "dark-no street lights"
result20_E = "dark-street lights not functioning"

### Labels for roadway surface ###
exp21_A_1 = "roadway a 1"
exp21_A_2 = "roadway a 2"
exp21_B_1 = "roadway b 1"
exp21_B_2 = "roadway b 2"
exp21_C_1 = "roadway c 1"
exp21_C_2 = "roadway c 2"
exp21_D_1 = "roadway d 1"
exp21_D_2 = "roadway d 2"

result21_A = "dry"
result21_B = "wet"
result21_C = "snowy-icy"
result21_D = "slippery - muddy, oily"

### Labels for road conditons ###
exp22_A_1 = "road conditions a 1"
exp22_A_2 = "road conditions a 2"
exp22_B_1 = "road conditions b 1"
exp22_B_2 = "road conditions b 2"
exp22_C_1 = "road conditions c 1"
exp22_C_2 = "road conditions c 2"
exp22_D_1 = "road conditions d 1"
exp22_D_2 = "road conditions d 2"
exp22_E_1 = "road conditions e 1"
exp22_E_2 = "road conditions e 2"
exp22_F_1 = "road conditions f 1"
exp22_F_2 = "road conditions f 2"
exp22_G_1 = "road conditions g 1"
exp22_G_2 = "road conditions g 2"
exp22_H_1 = "road conditions h 1"
exp22_H_2 = "road conditions h 2"

result22_A = "holes and deep rut"
result22_B = "loose material on roadway"
result22_C = "obstruction on roadway"
result22_D = "construction repair zone"
result22_E = "reduced road width"
result22_F = "flooded"
result22_G = "other"
result22_H = "no unusual conditions"

### Labels for movement preceding collision ###
exp23_A_1 = "movement a 1"
exp23_A_2 = "movement a 2"
exp23_B_1 = "movement b 1"
exp23_B_2 = "movement b 2"
exp23_C_1 = "movement c 1"
exp23_C_2 = "movement c 2"
exp23_D_1 = "movement d 1"
exp23_D_2 = "movement d 2"
exp23_E_1 = "movement e 1"
exp23_E_2 = "movement e 2"
exp23_F_1 = "movement f 1"
exp23_F_2 = "movement f 2"
exp23_G_1 = "movement g 1"
exp23_G_2 = "movement g 2"
exp23_H_1 = "movement h 1"
exp23_H_2 = "movement h 2"
exp23_I_1 = "movement i 1"
exp23_I_2 = "movement i 2"
exp23_J_1 = "movement j 1"
exp23_J_2 = "movement j 2"
exp23_K_1 = "movement k 1"
exp23_K_2 = "movement k 2"
exp23_L_1 = "movement l 1"
exp23_L_2 = "movement l 2"
exp23_M_1 = "movement m 1"
exp23_M_2 = "movement m 2"
exp23_N_1 = "movement n 1"
exp23_N_2 = "movement n 2"
exp23_O_1 = "movement o 1"
exp23_O_2 = "movement o 2"
exp23_P_1 = "movement p 1"
exp23_P_2 = "movement p 2"
exp23_Q_1 = "movement q 1"
exp23_Q_2 = "movement q 2"
exp23_R_1 = "movement r 1"
exp23_R_2 = "movement r 2"

result23_A = "stopped"
result23_B = "proceeding straight"
result23_C = "ran off road"
result23_D = "making right turn"
result23_E = "making left turn"
result23_F = "making U turn"
result23_G = "backing"
result23_H = "slowing-stopping"
result23_I = "passing other vehicle"
result23_J = "changing lanes"
result23_K = "parking manuever"
result23_L = "entering traffic"
result23_M = "other unsafe turning"
result23_N = "x-ing into opposing lane"
result23_O = "parked"
result23_P = "merging"
result23_Q = "traveling wrong way"
result23_R = "other"

### Labels for type of collison ###
exp24_A_1 = "type a 1"
exp24_A_2 = "type a 2"
exp24_B_1 = "type b 1"
exp24_B_2 = "type b 2"
exp24_C_1 = "type c 1"
exp24_C_2 = "type c 2"
exp24_D_1 = "type d 1"
exp24_D_2 = "type d 2"
exp24_E_1 = "type e 1"
exp24_E_2 = "type e 2"
exp24_F_1 = "type f 1"
exp24_F_2 = "type f 2"
exp24_G_1 = "type g 1"
exp24_G_2 = "type g 2"
exp24_H_1 = "type h 1"
exp24_H_2 = "type h 2"

result24_A = "head-on"
result24_B = "side swipe"
result24_C = "rear end"
result24_D = "broadside"
result24_E = "hit object"
result24_F = "overturned"
result24_G = "vehicle/pedestrian"
result24_H = "other"

### Labels for other associated factors ###
exp25_A_YES = "other a yes"
exp25_B = "other b"
exp25_C = "other c"
exp25_D = "other d"
exp25_E = "other e"
exp25_F = "other f"
exp25_G = "other g"
exp25_H_YES = "other h yes"
exp25_I = "other i"
exp25_J = "other j"
exp25_K = "other k"
exp25_L = "other l"

result25_A_YES = "cvc section violation cited"
result25_B = "vision obscurement"
result25_C = "inattention"
result25_D = "stop n go traffic"
result25_E = "entering leaving ramp"
result25_F = "previous collision"
result25_G = "unfamiliar with road"
result25_H_YES = "defective weh equipment cited"
result25_I = "uninvolved vehicle"
result25_J = "other"
result25_K = "none apparent"
result25_L = "runaway vehicle"

### Labels for mode given and user defined ###
exp_mode1 = "autonomy"
exp_mode2 = "non-autonomy"
result_mode1 = "Autonomous"
result_mode2 = "Conventional"

### Labels for user defined speed n context ###
exp26_1 = "speed1"
exp27_1 = "speed2"
exp28_1 = "speed3"
exp29_1 = "speed4"
exp26_2 = "context1"
exp27_2 = "context2"
exp28_2 = "context3"
exp29_2 = "context4"

### Label for vehicle2 ###
exp30_2 = "vehicle2 "

### Label for delimiter ###
delimiter = ":"

### Labels for user defined section trackers ###
SECTION_TRACKER1 = "" # section tracker for e.g., if no value is found in a section for the veh 1 or common column, then enter NA

SECTION_TRACKER2 = "" # section tracker for e.g., if no value is found in a section for the veh 2 column, then enter NA

### Maps vehicle damage level.                                                   ###
### @param1     inputStr    string       Yes or empty                            ###
### @param2     exp         string       One of {minor, moderate, none, unknown} ###
### @return     inputStr or exp if set                                           ###
def map_vehicle_damage(inputStr, exp):
    if inputStr != "" and inputStr != exp_none.lower():
        if exp == exp9_1:
            inputStr = exp
        if exp == exp9_2:
            inputStr = exp
        if exp == exp9_3:
            #change to the result value, else none result will not be printed to file
            inputStr = result_9_3 
        if exp == exp9_4:
            inputStr = exp
        if exp == exp9_5:
            inputStr = exp  

    return inputStr

### Maps weather. After scanning all the weather fields, if no value is selected assign "NA"    ###
### @param1     inputStr                string          Yes or empty                            ###
### @param2     exp                     string          exp example: weather a                  ###
### @return     "NA" or value if set    string          value example: clear                    ###            
def map_weather(inputStr, exp):
     #19 a-g weather
    global SECTION_TRACKER1
    global SECTION_TRACKER2
    if exp == exp19_A_1:
        SECTION_TRACKER1 = ""
    if exp == exp19_A_2:
        SECTION_TRACKER2 = ""
    
    if exp == exp19_A_1 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result19_A        
        SECTION_TRACKER1 = SECTION_TRACKER1 + delimiter + inputStr
    if exp == exp19_A_2 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result19_A 
        SECTION_TRACKER2 = SECTION_TRACKER2 + delimiter + inputStr
    if exp == exp19_B_1 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result19_B 
        SECTION_TRACKER1 = SECTION_TRACKER1 + delimiter + inputStr
    if exp == exp19_B_2 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result19_B 
        SECTION_TRACKER2 = SECTION_TRACKER2 + delimiter + inputStr
    if exp == exp19_C_1 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result19_C 
        SECTION_TRACKER1 = SECTION_TRACKER1 + delimiter + inputStr
    if exp == exp19_C_2 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result19_C 
        SECTION_TRACKER2 = SECTION_TRACKER2 + delimiter + inputStr
    if exp == exp19_D_1 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result19_D 
        SECTION_TRACKER1 = SECTION_TRACKER1 + delimiter + inputStr
    if exp == exp19_D_2 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result19_D 
        SECTION_TRACKER2 = SECTION_TRACKER2 + delimiter + inputStr
    if exp == exp19_E_1 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result19_E
        SECTION_TRACKER1 = SECTION_TRACKER1 + delimiter + inputStr
    if exp == exp19_E_2 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result19_E 
        SECTION_TRACKER2 = SECTION_TRACKER2 + delimiter + inputStr
    if exp == exp19_F_1 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result19_F
        SECTION_TRACKER1 = SECTION_TRACKER1 + delimiter + inputStr
    if exp == exp19_F_2 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result19_F 
        SECTION_TRACKER2 = SECTION_TRACKER2 + delimiter + inputStr
    if exp == exp19_G_1 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result19_G 
        SECTION_TRACKER1 = SECTION_TRACKER1 + delimiter + inputStr
    if exp == exp19_G_2 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result19_G 
        SECTION_TRACKER2 = SECTION_TRACKER2 + delimiter + inputStr
    if exp == exp19_G_1 and SECTION_TRACKER1 == "":    
       inputStr = result_missing       
    if exp == exp19_G_2 and SECTION_TRACKER2 == "":
        inputStr = result_missing
      
    return inputStr

### Maps lighting. After scanning all the lighting fields, if no value is selected assign "NA"  ###
### @param1     inputStr                string          Yes or empty                            ###
### @param2     exp                     string          exp example: lighting a                 ###
### @return     "NA" or value if set    string          value example: daylight                 ###     
def map_lighting(inputStr, exp):
    #20  a-e Lighting
    global SECTION_TRACKER1
    global SECTION_TRACKER2  
    if exp == exp20_A_1:
        SECTION_TRACKER1 = ""
    if exp == exp20_A_2:
        SECTION_TRACKER2 = ""
    if exp == exp20_A_1 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result20_A        
        SECTION_TRACKER1 = SECTION_TRACKER1 + delimiter + inputStr
    if exp == exp20_A_2 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result20_A         
        SECTION_TRACKER2 = SECTION_TRACKER2 + delimiter + inputStr
    if exp == exp20_B_1 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result20_B 
        SECTION_TRACKER1 = SECTION_TRACKER1 + delimiter + inputStr
    if exp == exp20_B_2 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result20_B 
        SECTION_TRACKER2 = SECTION_TRACKER2 + delimiter + inputStr
    if exp == exp20_C_1 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result20_C 
        SECTION_TRACKER1 = SECTION_TRACKER1 + delimiter + inputStr
    if exp == exp20_C_2 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result20_C 
        SECTION_TRACKER2 = SECTION_TRACKER2 + delimiter + inputStr
    if exp == exp20_D_1 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result20_D 
        SECTION_TRACKER1 = SECTION_TRACKER1 + delimiter + inputStr
    if exp == exp20_D_2 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result20_D 
        SECTION_TRACKER2 = SECTION_TRACKER2 + delimiter + inputStr
    if exp == exp20_E_1 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result20_E 
        SECTION_TRACKER1 = SECTION_TRACKER1 + delimiter + inputStr
    if exp == exp20_E_2 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result20_E 
        SECTION_TRACKER2 = SECTION_TRACKER2 + delimiter + inputStr
    if exp == exp20_E_1 and SECTION_TRACKER1 == "":    
       inputStr = result_missing       
    if exp == exp20_E_2 and SECTION_TRACKER2 == "":
        inputStr = result_missing
       
    return inputStr

### Maps roadway surface. After scanning all the roadway surface fields, if no value is selected assign "NA"  ###
### @param1     inputStr                string          Yes or empty                                          ###
### @param2     exp                     string          exp example: roadway surface a                        ###
### @return     "NA" or value if set    string          value example: wet                                    ###   
def map_roadway_surface(inputStr, exp):
    #21 a-d roadway surface
    global SECTION_TRACKER1
    global SECTION_TRACKER2  
    if exp == exp21_A_1:
        SECTION_TRACKER1 = ""
    if exp == exp21_A_2:
        SECTION_TRACKER2 = ""
    if exp == exp21_A_1 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result21_A
        SECTION_TRACKER1 = SECTION_TRACKER1 + delimiter + inputStr
    if exp == exp21_A_2 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result21_A 
        SECTION_TRACKER2 = SECTION_TRACKER2 + delimiter + inputStr
    if exp == exp21_B_1 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result21_B 
        SECTION_TRACKER1 = SECTION_TRACKER1 + delimiter + inputStr
    if exp == exp21_B_2 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result21_B 
        SECTION_TRACKER2 = SECTION_TRACKER2 + delimiter + inputStr
    if exp == exp21_C_1 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result21_C 
        SECTION_TRACKER1 = SECTION_TRACKER1 + delimiter + inputStr
    if exp == exp21_C_2 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result21_C 
        SECTION_TRACKER2 = SECTION_TRACKER2 + delimiter + inputStr
    if exp == exp21_D_1 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result21_D 
        SECTION_TRACKER1 = SECTION_TRACKER1 + delimiter + inputStr
    if exp == exp21_D_2 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result21_D 
        SECTION_TRACKER2 = SECTION_TRACKER2 + delimiter + inputStr
    if exp == exp21_D_1 and SECTION_TRACKER1 == "":    
       inputStr = result_missing       
    if exp == exp21_D_2 and SECTION_TRACKER2 == "":
        inputStr = result_missing 

    return inputStr

### Maps roadway conditions. After scanning all the roadway conditions fields, if no value is selected assign "NA"  ###
### @param1     inputStr                string          Yes or empty                                                ###
### @param2     exp                     string          exp example: roadway conditions f                           ###
### @return     "NA" or value if set    string          value example: flooded                                      ###   
def map_roadway_conditions(inputStr, exp):
    #22 a-H roadway conditions
    global SECTION_TRACKER1
    global SECTION_TRACKER2  
    if exp == exp22_A_1:
        SECTION_TRACKER1 = ""
    if exp == exp22_A_2:
        SECTION_TRACKER2 = ""
    if exp == exp22_A_1 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result22_A 
        SECTION_TRACKER1 = SECTION_TRACKER1 + delimiter + inputStr
    if exp == exp24_A_2 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result22_A 
        SECTION_TRACKER2 = SECTION_TRACKER2 + delimiter + inputStr
    if exp == exp22_B_1 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result22_B 
        SECTION_TRACKER1 = SECTION_TRACKER1 + delimiter + inputStr
    if exp == exp22_B_2 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result22_B 
        SECTION_TRACKER2 = SECTION_TRACKER2 + delimiter + inputStr
    if exp == exp22_C_1 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result22_C 
        SECTION_TRACKER1 = SECTION_TRACKER1 + delimiter + inputStr
    if exp == exp22_C_2 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result22_C 
        SECTION_TRACKER2 = SECTION_TRACKER2 + delimiter + inputStr
    if exp == exp22_D_1 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result22_D 
        SECTION_TRACKER1 = SECTION_TRACKER1 + delimiter + inputStr
    if exp == exp22_D_2 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result22_D 
        SECTION_TRACKER2 = SECTION_TRACKER2 + delimiter + inputStr
    if exp == exp22_E_1 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result22_D 
        SECTION_TRACKER1 = SECTION_TRACKER1 + delimiter + inputStr
    if exp == exp22_E_2 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result22_E 
        SECTION_TRACKER2 = SECTION_TRACKER2 + delimiter + inputStr
    if exp == exp22_F_1 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result22_F 
        SECTION_TRACKER1 = SECTION_TRACKER1 + delimiter + inputStr
    if exp == exp22_F_2 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result22_F 
        SECTION_TRACKER2 = SECTION_TRACKER2 + delimiter + inputStr
    if exp == exp22_G_1 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result22_G 
        SECTION_TRACKER1 = SECTION_TRACKER1 + delimiter + inputStr
    if exp == exp22_G_2 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result22_G 
        SECTION_TRACKER2 = SECTION_TRACKER2 + delimiter + inputStr
    if exp == exp22_H_1 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result22_H 
        SECTION_TRACKER1 = SECTION_TRACKER1 + delimiter + inputStr
    if exp == exp22_H_2 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result22_H 
        SECTION_TRACKER2 = SECTION_TRACKER2 + delimiter + inputStr
    if exp == exp22_H_1 and SECTION_TRACKER1 == "":    
       inputStr = result_missing       
    if exp == exp22_H_2 and SECTION_TRACKER2 == "":
        inputStr = result_missing

    return inputStr

### Maps movement preceding collision. After scanning all the movement preceding collision fields, if no value is selected assign "NA" ###
### @param1     inputStr                string          Yes or empty                                                                   ###
### @param2     exp                     string          exp example: movement preceding collision a                                    ###
### @return     "NA" or value if set    string          value example: stopped                                                         ###       
def map_movement_collision(inputStr, exp):
    #23 a-r Movement (preceding collision)
    global SECTION_TRACKER1
    global SECTION_TRACKER2  
    if exp == exp23_A_1:
        SECTION_TRACKER1 = ""
    if exp == exp23_A_2:
        SECTION_TRACKER2 = ""
    if exp == exp23_A_1 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result23_A
        SECTION_TRACKER1 = SECTION_TRACKER1 + delimiter + inputStr
    if exp == exp23_A_2 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result23_A 
        SECTION_TRACKER2 = SECTION_TRACKER2 + delimiter + inputStr
    if exp == exp23_B_1 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result23_B
        SECTION_TRACKER1 = SECTION_TRACKER1 + delimiter + inputStr
    if exp == exp23_B_2 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result23_B 
        SECTION_TRACKER2 = SECTION_TRACKER2 + delimiter + inputStr
    if exp == exp23_C_1 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result23_C
        SECTION_TRACKER1 = SECTION_TRACKER1 + delimiter + inputStr
    if exp == exp23_C_2 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result23_C 
        SECTION_TRACKER2 = SECTION_TRACKER2 + delimiter + inputStr
    if exp == exp23_D_1 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result23_D
        SECTION_TRACKER1 = SECTION_TRACKER1 + delimiter + inputStr
    if exp == exp23_D_2 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result23_D
        SECTION_TRACKER2 = SECTION_TRACKER2 + delimiter + inputStr
    if exp == exp23_E_1 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result23_E
        SECTION_TRACKER1 = SECTION_TRACKER1 + delimiter + inputStr
    if exp == exp23_E_2 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result23_E
        SECTION_TRACKER2 = SECTION_TRACKER2 + delimiter + inputStr
    if exp == exp23_F_1 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result23_F
        SECTION_TRACKER1 = SECTION_TRACKER1 + delimiter + inputStr
    if exp == exp23_F_2 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result23_F
        SECTION_TRACKER2 = SECTION_TRACKER2 + delimiter + inputStr 
    if exp == exp23_G_1 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result23_G
        SECTION_TRACKER1 = SECTION_TRACKER1 + delimiter + inputStr
    if exp == exp23_G_2 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result23_G
        SECTION_TRACKER2 = SECTION_TRACKER1 + delimiter + inputStr            
    if exp == exp23_H_1 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result23_H
        SECTION_TRACKER1 = SECTION_TRACKER1 + delimiter + inputStr
    if exp == exp23_H_2 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result23_H
        SECTION_TRACKER2 = SECTION_TRACKER2 + delimiter + inputStr   
    if exp == exp23_I_1 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result23_I
        SECTION_TRACKER1 = SECTION_TRACKER1 + delimiter + inputStr
    if exp == exp23_J_2 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result23_J
        SECTION_TRACKER2 = SECTION_TRACKER2 + delimiter + inputStr 
    if exp == exp23_I_1 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result23_I
        SECTION_TRACKER1 = SECTION_TRACKER1 + delimiter + inputStr
    if exp == exp23_I_2 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result23_I
        SECTION_TRACKER2 = SECTION_TRACKER2 + delimiter + inputStr 
    if exp == exp23_J_1 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result23_J
        SECTION_TRACKER1 = SECTION_TRACKER1 + delimiter + inputStr
    if exp == exp23_J_2 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result23_J
        SECTION_TRACKER2 = SECTION_TRACKER2 + delimiter + inputStr 
    if exp == exp23_K_1 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result23_K
        SECTION_TRACKER1 = SECTION_TRACKER1 + delimiter + inputStr
    if exp == exp23_K_2 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result23_K
        SECTION_TRACKER2 = SECTION_TRACKER2 + delimiter + inputStr 
    if exp == exp23_L_1 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result23_L
        SECTION_TRACKER1 = SECTION_TRACKER1 + delimiter + inputStr
    if exp == exp23_L_2 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result23_L
        SECTION_TRACKER2 = SECTION_TRACKER2 + delimiter + inputStr
    if exp == exp23_M_1 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result23_M
        SECTION_TRACKER1 = SECTION_TRACKER1 + delimiter + inputStr
    if exp == exp23_M_2 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result23_M
        SECTION_TRACKER2 = SECTION_TRACKER2 + delimiter + inputStr 
    if exp == exp23_N_1 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result23_N
        SECTION_TRACKER1 = SECTION_TRACKER1 + delimiter + inputStr
    if exp == exp23_N_2 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result23_N
        SECTION_TRACKER2 = SECTION_TRACKER2 + delimiter + inputStr 
    if exp == exp23_O_1 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result23_O
        SECTION_TRACKER1 = SECTION_TRACKER1 + delimiter + inputStr
    if exp == exp23_O_2 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result23_O
        SECTION_TRACKER2 = SECTION_TRACKER2 + delimiter + inputStr  
    if exp == exp23_P_1 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result23_P
        SECTION_TRACKER1 = SECTION_TRACKER1 + delimiter + inputStr
    if exp == exp23_P_2 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result23_P
        SECTION_TRACKER2 = SECTION_TRACKER2 + delimiter + inputStr  
    if exp == exp23_Q_1 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result23_Q
        SECTION_TRACKER1 = SECTION_TRACKER1 + delimiter + inputStr
    if exp == exp23_Q_2 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result23_Q
        SECTION_TRACKER2 = SECTION_TRACKER2 + delimiter + inputStr  
    if exp == exp23_R_1 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result23_R
        SECTION_TRACKER1 = SECTION_TRACKER1 + delimiter + inputStr
    if exp == exp23_R_2 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result23_R
        SECTION_TRACKER2 = SECTION_TRACKER2 + delimiter + inputStr    
    if exp == exp23_R_1 and SECTION_TRACKER1 == "":    
       inputStr = result_missing       
    if exp == exp23_R_2 and SECTION_TRACKER2 == "":
        inputStr = result_missing

    return inputStr

### Maps type of collisions. After scanning all the type of collisions fields, if no value is selected assign "NA"  ###
### @param1     inputStr                string          Yes or empty                                                ###
### @param2     exp                     string          exp example: type of collision a                            ###
### @return     "NA" or value if set    string          value example: head-on                                      ###   
def map_type_collisions(inputStr, exp):
    #24 a-h type (of collision)
    global SECTION_TRACKER1
    global SECTION_TRACKER2  
    if exp == exp24_A_1:
        SECTION_TRACKER1 = ""
    if exp == exp24_A_2:
        SECTION_TRACKER2 = ""
    if exp == exp24_A_1 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):        
        inputStr = result24_A        
        SECTION_TRACKER1 = SECTION_TRACKER1 + delimiter + inputStr
    if exp == exp24_A_2 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result24_A
        SECTION_TRACKER2 = SECTION_TRACKER2 + delimiter + inputStr
    if exp == exp24_B_1 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result24_B
        SECTION_TRACKER1 = SECTION_TRACKER1 + delimiter + inputStr
    if exp == exp24_B_2 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result24_B
        SECTION_TRACKER2 = SECTION_TRACKER2 + delimiter + inputStr
    if exp == exp24_C_1 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result24_C
        SECTION_TRACKER1 = SECTION_TRACKER1 + delimiter + inputStr
    if exp == exp24_C_2 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result24_C
        SECTION_TRACKER2 = SECTION_TRACKER2 + delimiter + inputStr
    if exp == exp24_D_1 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result24_D
        SECTION_TRACKER1 = SECTION_TRACKER1 + delimiter + inputStr
    if exp == exp24_D_2 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result24_D
        SECTION_TRACKER2 = SECTION_TRACKER2 + delimiter + inputStr
    if exp == exp24_E_1 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result24_E
        SECTION_TRACKER1 = SECTION_TRACKER1 + delimiter + inputStr
    if exp == exp24_E_2 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result24_E
        SECTION_TRACKER2 = SECTION_TRACKER2 + delimiter + inputStr
    if exp == exp24_F_1 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result24_F
        SECTION_TRACKER1 = SECTION_TRACKER1 + delimiter + inputStr
    if exp == exp24_F_2 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result24_F
        SECTION_TRACKER2 = SECTION_TRACKER2 + delimiter + inputStr
    if exp == exp24_G_1 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result24_G
        SECTION_TRACKER1 = SECTION_TRACKER1 + delimiter + inputStr
    if exp == exp24_G_2 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result24_G
        SECTION_TRACKER2 = SECTION_TRACKER2 + delimiter + inputStr
    if exp == exp24_H_1 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result24_H 
        SECTION_TRACKER1 = SECTION_TRACKER1 + delimiter + inputStr
    if exp == exp24_H_2 and (inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower()):
        inputStr = result24_H 
        SECTION_TRACKER2 = SECTION_TRACKER2 + delimiter + inputStr
    if exp == exp24_H_1 and SECTION_TRACKER1 == "":    
       inputStr = result_missing  
    if exp == exp24_H_2 and SECTION_TRACKER2 == "":
        inputStr = result_missing
    
    return inputStr

### Maps other associated factors                                                                                   ###
### @param1     inputStr                string          Yes or empty                                                ###
### @param2     exp                     string          exp example: other associated factor(s) a                   ###
### @return     "NA" or value if set    string          value example: entering/leaving ramp                        ###       
def map_associated_factors(inputStr, exp):
    #25 other (associated factors)    
    if exp == exp25_A_YES and inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower():
        inputStr = result25_A_YES
    elif exp == exp25_A_YES and (inputStr == "" or inputStr == exp_none.lower() and inputStr == exp_off.lower()):
        inputStr = result_missing
    
    if exp == exp25_H_YES and inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower():
        inputStr = result25_H_YES
    elif exp == exp25_H_YES and (inputStr == "" or inputStr == exp_none.lower() and inputStr == exp_off.lower()):
        inputStr = result_missing

    if exp == exp25_B and inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower():
        inputStr = result25_B  
    elif exp == exp25_B and (inputStr == "" or inputStr == exp_none.lower() and inputStr == exp_off.lower()):
        inputStr = result_missing

    if exp == exp25_C and inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower():
        inputStr = result25_C  
    elif exp == exp25_C and (inputStr == "" or inputStr == exp_none.lower() and inputStr == exp_off.lower()):
        inputStr = result_missing

    if exp == exp25_D and inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower():
        inputStr = result25_D  
    elif exp == exp25_D and (inputStr == "" or inputStr == exp_none.lower() and inputStr == exp_off.lower()):
        inputStr = result_missing

    if exp == exp25_E and inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower():
        inputStr = result25_E  
    elif exp == exp25_E and (inputStr == "" or inputStr == exp_none.lower() and inputStr == exp_off.lower()):
        inputStr = result_missing
        
    if exp == exp25_F and inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower():
        inputStr = result25_F  
    elif exp == exp25_F and (inputStr == "" or inputStr == exp_none.lower() and inputStr == exp_off.lower()):
        inputStr = result_missing

    if exp == exp25_G and inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower():
        inputStr = result25_G  
    elif exp == exp25_G and (inputStr == "" or inputStr == exp_none.lower() and inputStr == exp_off.lower()):
        inputStr = result_missing

    #H is done up as yes no
    if exp == exp25_I and inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower():
        inputStr = result25_I  
    elif exp == exp25_I and (inputStr == "" or inputStr == exp_none.lower() and inputStr == exp_off.lower()):
        inputStr = result_missing

    if exp == exp25_J and inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower():
        inputStr = result25_J  
    elif exp == exp25_J and (inputStr == "" or inputStr == exp_none.lower() and inputStr == exp_off.lower()):
        inputStr = result_missing

    if exp == exp25_K and inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower():
        inputStr = result25_K 
    elif exp == exp25_K and (inputStr == "" or inputStr == exp_none.lower() and inputStr == exp_off.lower()):
        inputStr = result_missing

    if exp == exp25_L and inputStr != "" and inputStr != exp_none.lower() and inputStr != exp_off.lower():
        inputStr = result25_L  
    elif exp == exp25_L and (inputStr == "" or inputStr == exp_none.lower() and inputStr == exp_off.lower()):
        inputStr = result_missing

    return inputStr

### Maps other associated factors                                                                                   ###
### @param1     inputStr                string          example: stopped in traffic                                 ###
### @param2     exp                     string                                                                      ###
### @return     "NA" or inputStr as is  string                                                                      ### 
def map_vehicle2_state(inputStr, exp):    
    if exp == exp30_2 and (inputStr == "" or inputStr == exp_none.lower()):
        inputStr = result_missing

    return inputStr

### Maps vehicle driving mode autonomous or conventional                                                            ### 
### @param1     inputStr                string                                                                      ###
### @param2     exp                     string                                                                      ###
### @return     Mode or inputStr as is  string                                                                      ### 
def map_mode(inputStr, exp):
   if inputStr != "" and inputStr != exp_none.lower(): 
       if exp == exp_mode1:
           inputStr = result_mode1
       if exp == exp_mode2:
           inputStr = result_mode2
       
   return inputStr

### Maps the inputStr value to corresponding string per the form dropdown values, based on exp string
### @param1     inputStr                string                                                                      ###
### @param2     exp                     string                                                                      ###
### @return     inputStr as mapped      string                                                                      ### 
def map_value(inputStr, exp): 
    inputStr = map_vehicle_damage(inputStr, exp)
    inputStr = map_weather(inputStr, exp)    
    inputStr = map_lighting(inputStr, exp)
    inputStr = map_roadway_surface(inputStr, exp)    
    inputStr = map_roadway_conditions(inputStr, exp)    
    inputStr = map_movement_collision(inputStr, exp)    
    inputStr = map_type_collisions(inputStr, exp)    
    inputStr = map_associated_factors(inputStr, exp)
    inputStr = map_vehicle2_state(inputStr, exp)
    inputStr = map_mode(inputStr, exp)
    
    return inputStr

### Appends result, string exp to match on a sting line - case insensitive; if result found append.\n"              ###
### @param1     each_file_csv           file       csv file to which to append the content from text file           ###
### @param2     exp                     string     expression to be checked on the line for e.g., weather a         ###
### @param3     line                    string     current line from the text file such as weather a                ###
### @return     value mapped            string                                                                      ### 
def find_n_append(each_file_csv, exp, line):
    exp_len = len(exp)    
    exp = exp.lower()
    line = line.lower()
    line = ' '.join(line.split()) # removing multiple spaces in between words 
    if line.find(exp) == 0:
        index = line.index(exp)        
        value = line[index + exp_len:]
        value = value.strip() 
        value = value.replace(',','')
        print ("line is {:s} \n value is {:s} \n exp is {:s}".format( line, value, exp))       
        value = map_value(value, exp)          
        if value != "" and value != exp_none.lower() and value != exp_off.lower():  
            each_file_csv.append(value)
#2 cols for 2 vehicles. c1 not chosen, c2 chosen or c1 chosen at last row, c2 chosen b4 or c1 no selection/c2 selected. c2 is added in c1. 
#single select or no select in each col supported. multi-select in each col not supported.
        if exp == exp19_G_2 or exp == exp20_E_2 or exp == exp21_D_2 or exp == exp22_H_2 or exp == exp23_R_2 or exp == exp24_H_2: 
            each_file_csv.pop()
            each_file_csv.pop()            
            each_file_csv.append(SECTION_TRACKER1[1:len(SECTION_TRACKER1)])
            each_file_csv.append(SECTION_TRACKER2[1:len(SECTION_TRACKER2)])
        #print ("mapped value is {:s}".format(value))
        return value

### Writes company  date, time to csv if the input line contains these values                                       ###
### @param1     each_file_csv           file       csv file to which to append the content from text file           ###
### @param2     each_line               string     current line from the text file - may be of interest or not      ###
def call_company_date_time_desc_exp(each_file_csv,each_line):
    find_n_append(each_file_csv, exp1, each_line)
    find_n_append(each_file_csv, exp2, each_line)
    find_n_append(each_file_csv, exp3, each_line)

### Writes vehicle damage info to csv if the input line contains these values                                       ###
### @param1     each_file_csv           file       csv file to which to append the content from text file           ###
### @param2     each_line               string     current line from the text file - may be of interest or not      ###
def call_vehicle_damage_exp(each_file_csv,each_line):
    find_n_append(each_file_csv, exp9_1, each_line)
    find_n_append(each_file_csv, exp9_2, each_line)
    find_n_append(each_file_csv, exp9_3, each_line)
    find_n_append(each_file_csv, exp9_4, each_line)
    find_n_append(each_file_csv, exp9_5, each_line)

### Writes vehicle damage info to csv if the input line contains these values                                       ###
### @param1     each_file_csv           file       csv file to which to append the content from text file           ###
### @param2     each_line               string     current line from the text file - may be of interest or not      ###
def call_weather_exp(each_file_csv,each_line):
    find_n_append(each_file_csv, exp19_A_1, each_line)    
    find_n_append(each_file_csv, exp19_B_1, each_line)    
    find_n_append(each_file_csv, exp19_C_1, each_line)   
    find_n_append(each_file_csv, exp19_D_1, each_line)
    find_n_append(each_file_csv, exp19_E_1, each_line)
    find_n_append(each_file_csv, exp19_F_1, each_line)
    find_n_append(each_file_csv, exp19_G_1, each_line)
    find_n_append(each_file_csv, exp19_A_2, each_line)
    find_n_append(each_file_csv, exp19_B_2, each_line)
    find_n_append(each_file_csv, exp19_C_2, each_line)
    find_n_append(each_file_csv, exp19_D_2, each_line)    
    find_n_append(each_file_csv, exp19_E_2, each_line)
    find_n_append(each_file_csv, exp19_F_2, each_line)
    find_n_append(each_file_csv, exp19_G_2, each_line)

### Writes lighting info to csv if the input line contains these values                                             ###
### @param1     each_file_csv           file       csv file to which to append the content from text file           ###
### @param2     each_line               string     current line from the text file - may be of interest or not      ###
def call_lighting_exp(each_file_csv,each_line):
    find_n_append(each_file_csv, exp20_A_1, each_line)
    find_n_append(each_file_csv, exp20_A_2, each_line)
    find_n_append(each_file_csv, exp20_B_1, each_line)
    find_n_append(each_file_csv, exp20_B_2, each_line)
    find_n_append(each_file_csv, exp20_C_1, each_line)
    find_n_append(each_file_csv, exp20_C_2, each_line)
    find_n_append(each_file_csv, exp20_D_1, each_line)
    find_n_append(each_file_csv, exp20_D_2, each_line)
    find_n_append(each_file_csv, exp20_E_1, each_line)
    find_n_append(each_file_csv, exp20_E_2, each_line)

### Writes road surface info to csv if the input line contains these values                                         ###
### @param1     each_file_csv           file       csv file to which to append the content from text file           ###
### @param2     each_line               string     current line from the text file - may be of interest or not      ###
def call_road_surface_exp(each_file_csv,each_line):
    find_n_append(each_file_csv, exp21_A_1, each_line)
    find_n_append(each_file_csv, exp21_A_2, each_line)
    find_n_append(each_file_csv, exp21_B_1, each_line)
    find_n_append(each_file_csv, exp21_B_2, each_line)
    find_n_append(each_file_csv, exp21_C_1, each_line)
    find_n_append(each_file_csv, exp21_C_2, each_line)
    find_n_append(each_file_csv, exp21_D_1, each_line)
    find_n_append(each_file_csv, exp21_D_2, each_line)

### Writes road condition info to csv if the input line contains these values                                       ###
### @param1     each_file_csv           file       csv file to which to append the content from text file           ###
### @param2     each_line               string     current line from the text file - may be of interest or not      ###
def call_road_condition_exp(each_file_csv,each_line):
    find_n_append(each_file_csv, exp22_A_1, each_line)
    find_n_append(each_file_csv, exp22_A_2, each_line)
    find_n_append(each_file_csv, exp22_B_1, each_line)
    find_n_append(each_file_csv, exp22_B_2, each_line)
    find_n_append(each_file_csv, exp22_C_1, each_line)
    find_n_append(each_file_csv, exp22_C_2, each_line)
    find_n_append(each_file_csv, exp22_D_1, each_line)
    find_n_append(each_file_csv, exp22_D_2, each_line)
    find_n_append(each_file_csv, exp22_E_1, each_line)
    find_n_append(each_file_csv, exp22_E_2, each_line)
    find_n_append(each_file_csv, exp22_F_1, each_line)
    find_n_append(each_file_csv, exp22_F_2, each_line)
    find_n_append(each_file_csv, exp22_G_1, each_line)
    find_n_append(each_file_csv, exp22_G_2, each_line)
    find_n_append(each_file_csv, exp22_H_1, each_line)
    find_n_append(each_file_csv, exp22_H_2, each_line)

### Writes movement preceding collision info to csv if the input line contains these values                         ###
### @param1     each_file_csv           file       csv file to which to append the content from text file           ###
### @param2     each_line               string     current line from the text file - may be of interest or not      ###
def call_movement_proceeding_collision_exp(each_file_csv,each_line):
    find_n_append(each_file_csv, exp23_A_1, each_line)
    find_n_append(each_file_csv, exp23_A_2, each_line)
    find_n_append(each_file_csv, exp23_B_1, each_line)
    find_n_append(each_file_csv, exp23_B_2, each_line)
    find_n_append(each_file_csv, exp23_C_1, each_line)
    find_n_append(each_file_csv, exp23_C_2, each_line)
    find_n_append(each_file_csv, exp23_D_1, each_line)
    find_n_append(each_file_csv, exp23_D_2, each_line)
    find_n_append(each_file_csv, exp23_E_1, each_line)
    find_n_append(each_file_csv, exp23_E_2, each_line)
    find_n_append(each_file_csv, exp23_F_1, each_line)
    find_n_append(each_file_csv, exp23_F_2, each_line)
    find_n_append(each_file_csv, exp23_G_1, each_line)
    find_n_append(each_file_csv, exp23_G_2, each_line)
    find_n_append(each_file_csv, exp23_H_1, each_line)
    find_n_append(each_file_csv, exp23_H_2, each_line)
    find_n_append(each_file_csv, exp23_I_1, each_line)
    find_n_append(each_file_csv, exp23_I_2, each_line)
    find_n_append(each_file_csv, exp23_J_1, each_line)
    find_n_append(each_file_csv, exp23_J_2, each_line)
    find_n_append(each_file_csv, exp23_K_1, each_line)
    find_n_append(each_file_csv, exp23_K_2, each_line)
    find_n_append(each_file_csv, exp23_L_1, each_line)
    find_n_append(each_file_csv, exp23_L_2, each_line)
    find_n_append(each_file_csv, exp23_M_1, each_line)
    find_n_append(each_file_csv, exp23_M_2, each_line)
    find_n_append(each_file_csv, exp23_N_1, each_line)
    find_n_append(each_file_csv, exp23_N_2, each_line)
    find_n_append(each_file_csv, exp23_O_1, each_line)
    find_n_append(each_file_csv, exp23_O_2, each_line)
    find_n_append(each_file_csv, exp23_P_1, each_line)
    find_n_append(each_file_csv, exp23_P_2, each_line)
    find_n_append(each_file_csv, exp23_Q_1, each_line)
    find_n_append(each_file_csv, exp23_Q_2, each_line)
    find_n_append(each_file_csv, exp23_R_1, each_line)
    find_n_append(each_file_csv, exp23_R_2, each_line)

### Writes type of collision info to csv if the input line contains these values                                    ###
### @param1     each_file_csv           file       csv file to which to append the content from text file           ###
### @param2     each_line               string     current line from the text file - may be of interest or not      ###
def call_type_of_collision_exp(each_file_csv,each_line):    
    find_n_append(each_file_csv, exp24_A_1, each_line)    
    find_n_append(each_file_csv, exp24_B_1, each_line)   
    find_n_append(each_file_csv, exp24_C_1, each_line)    
    find_n_append(each_file_csv, exp24_D_1, each_line)    
    find_n_append(each_file_csv, exp24_E_1, each_line)    
    find_n_append(each_file_csv, exp24_F_1, each_line) 
    find_n_append(each_file_csv, exp24_G_1, each_line)
    find_n_append(each_file_csv, exp24_H_1, each_line)  

    find_n_append(each_file_csv, exp24_A_2, each_line)
    find_n_append(each_file_csv, exp24_B_2, each_line)
    find_n_append(each_file_csv, exp24_C_2, each_line)
    find_n_append(each_file_csv, exp24_D_2, each_line)
    find_n_append(each_file_csv, exp24_E_2, each_line)
    find_n_append(each_file_csv, exp24_F_2, each_line)
    find_n_append(each_file_csv, exp24_G_2, each_line)
    find_n_append(each_file_csv, exp24_H_2, each_line)

### Writes other associated factor(s) info to csv if the input line contains these values                           ###
### @param1     each_file_csv           file       csv file to which to append the content from text file           ###
### @param2     each_line               string     current line from the text file - may be of interest or not      ###    
def call_other_assoc_factor_exp(each_file_csv,each_line):
    find_n_append(each_file_csv, exp25_A_YES, each_line)
    find_n_append(each_file_csv, exp25_B, each_line)
    find_n_append(each_file_csv, exp25_C, each_line)
    find_n_append(each_file_csv, exp25_D, each_line)
    find_n_append(each_file_csv, exp25_E, each_line)
    find_n_append(each_file_csv, exp25_F, each_line)
    find_n_append(each_file_csv, exp25_G, each_line)
    find_n_append(each_file_csv, exp25_H_YES, each_line)
    find_n_append(each_file_csv, exp25_I, each_line)
    find_n_append(each_file_csv, exp25_J, each_line)
    find_n_append(each_file_csv, exp25_K, each_line)
    find_n_append(each_file_csv, exp25_L, each_line)

### Writes speed and context (which are derived values via NLP processing) info to csv if the input line contains these values ###
### @param1     each_file_csv           file       csv file to which to append the content from text file                      ###
### @param2     each_line               string     current line from the text file - may be of interest or not                 ###
def call_speed_context_exp(each_file_csv,each_line):
    find_n_append(each_file_csv, exp26_1, each_line)
    find_n_append(each_file_csv, exp26_2, each_line)
    find_n_append(each_file_csv, exp27_1, each_line)
    find_n_append(each_file_csv, exp27_2, each_line)
    find_n_append(each_file_csv, exp28_1, each_line)
    find_n_append(each_file_csv, exp28_2, each_line)
    find_n_append(each_file_csv, exp29_1, each_line)
    find_n_append(each_file_csv, exp29_2, each_line)

### Writes vehicle2 state info to csv if the input line contains these values                                       ###
### @param1     each_file_csv           file       csv file to which to append the content from text file           ###
### @param2     each_line               string     current line from the text file - may be of interest or not      ###
def call_vehicle2_state(each_file_csv,each_line):
    find_n_append(each_file_csv, exp30_2, each_line)

### Reads from the input txt file and writes to the single master CSV output file that combines inputs from multiple text files  ###
### @param1     csv_file                    file       csv file to which to append the content                                   ###
### @param2     txt_dir                     string     input text file directory                                                 ###
### @param2     form_to_txt_file_name       string     input text filename                                                       ###
def write_CSV(csv_file, txt_dir, form_to_txt_file_name):   
    each_file_csv = []    
    file_path = open(os.path.join(txt_dir, form_to_txt_file_name), 'r')
    for each_line in file_path:
        call_company_date_time_desc_exp(each_file_csv,each_line)
        call_vehicle_damage_exp(each_file_csv,each_line)
        call_weather_exp(each_file_csv,each_line)
        call_lighting_exp(each_file_csv,each_line) 
        call_road_surface_exp(each_file_csv,each_line)
        call_road_condition_exp(each_file_csv,each_line)            
        call_movement_proceeding_collision_exp(each_file_csv,each_line)
        call_type_of_collision_exp(each_file_csv,each_line) 
        call_other_assoc_factor_exp(each_file_csv,each_line)
        call_speed_context_exp(each_file_csv,each_line)
        call_vehicle2_state(each_file_csv,each_line)        
        find_n_append(each_file_csv, exp_mode1, each_line)
        find_n_append(each_file_csv, exp_mode2, each_line)

    #print (each_file_csv)
    for item in each_file_csv:
            csv_file.write("%s , " % item)        
    csv_file.write("\n") 
    file_path.close()
  
