from _listenSpeak import listen
from _ai import match , match3
from _dateTime import dateTime

def battery_inspection():
    battery_info = []

    battery_make = listen("Enter the battery make ")
    battery_info.append(battery_make)


    replacement_date = listen("Enter the battery replacement date")  
    dateTime_info = dateTime(replacement_date)
    battery_info.append(dateTime_info)

    text = listen("Enter the battery voltage ")
    pattern = [{"LIKE_NUM":True}]
    matches=match(pattern,text,img=False)
    try:
        battery_voltage = matches[0][0]
        battery_info.append(battery_voltage)
    except:
        battery_info.append(0)

    text = listen("Enter the battery water level ")
    water_level = match3(text)
    battery_info.append(water_level)


    text = listen("Is there any damage to the battery? ")
    match_yes=match([{'LOWER':'yes'}],text)
    damage_condition = 1 if match_yes else 0
    battery_info.append(damage_condition)
    

    text = listen("Is there any leak or rust in the battery? ")
    match_yes=match([{'LOWER':'yes'}],text)
    leak_rust_condition = 1 if match_yes else 0
    battery_info.append(leak_rust_condition)

    return battery_info


