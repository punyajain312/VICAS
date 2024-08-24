from _listenSpeak import listen
from _ai import match3

def break_inspection():
        
        break_info = []

        text = listen("Enter break fluid level ")
        break_fluid_level = match3(text)
        break_info.append(break_fluid_level)

        text = listen(f"Enter front break condition ")
        break_front = match3(text)
        break_info.append(break_front)

        text = listen(f"Enter rear break condition ")
        break_rear = match3(text)
        break_info.append(break_rear)

        text = listen("Enter emergency brake condition ")
        emergency_brake = match3(text)
        break_info.append(emergency_brake)

        return break_info