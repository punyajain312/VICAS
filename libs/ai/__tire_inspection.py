from _listenSpeak import listen
from _ai import match , match3

def tire_inspection():
    tire_data = []

    def get_tire_info(position):
        text = listen(f"Enter tire pressure for {position}")
        pattern = [{"LIKE_NUM":True}]
        matches=match(pattern,text)
        try:
            tire_pressure =  matches[0][0]
        except:
             tire_pressure = 0 

        text = listen(f"Enter tire condition for {position} ")
        tire_condition = match3(text)
        tire_data.append([tire_pressure,tire_condition])
        

    positions = ["Left Front", "Right Front", "Left Rear", "Right Rear"]
    
    for position in positions:
        get_tire_info(position)
    
    return tire_data
