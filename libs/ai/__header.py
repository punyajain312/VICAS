from _listenSpeak import listen
from _ai import match
from _dateTime import dateTime

def header():
    header_values = []
    
    truck_serial_number = listen("Enter truck serial number")
    header_values.append( truck_serial_number)
    
    truck_model = listen("Enter truck model")
    header_values.append( truck_model)

    inspection_id = listen("Enter inspection id")
    header_values.append( inspection_id)

    date_time = listen("Enter date time") 
    dateTime_info= dateTime(date_time)
    header_values.append( dateTime_info)

    location = listen("Enter location")
    header_values.append( location)

    geoCoordinates = listen("Enter geo Coordinates")
    header_values.append( geoCoordinates)

    text = listen("Enter service meter hours")
    pattern = [{"LIKE_NUM":True}]
    matches=match(pattern,text,img=False)
    try:
        service_meter_hours = matches[0][0]
        header_values.append(service_meter_hours)
    except:
        header_values.append(0)

    customer_name = listen("Enter customer name")
    header_values.append( customer_name)

  
    CAT_id = listen("Enter CAT id")
    header_values.append( CAT_id)

    return header_values

