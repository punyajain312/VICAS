from _listenSpeak import listen
from _ai import match ,match3_color

def engine_inspection():

    engine_info=[]

    text = listen("Is there any rust to the engine? ")
    match_yes=match([{'LOWER':'yes'}],text)
    rust = 1 if match_yes else 0
    engine_info.append(rust)

    text = listen("Is there any dent to the engine? ")
    match_yes=match([{'LOWER':'yes'}],text)
    dent = 1 if match_yes else 0
    engine_info.append(dent)

    text = listen("Is there any damage to the engine? ")
    match_yes=match([{'LOWER':'yes'}],text)
    damage = 1 if match_yes else 0
    engine_info.append(damage)

    text = listen("Enter engine oil condition ")
    match_good=match([{'LOWER':'good'}],text)
    oil_condition = 1 if match_good else 0
    engine_info.append(oil_condition)

    text = listen(f"Enter engine oil color ")
    engine_oil_color = match3_color(text)
    engine_info.append(engine_oil_color)

    text = listen("Enter brake fluid condition ")
    match_good=match([{'LOWER':'good'}],text)
    brake_fluid_condition = 1 if match_good else 0
    engine_info.append(brake_fluid_condition)

    text = listen(f"Enter brake fluid color ")
    break_fluid_color = match3_color(text)
    engine_info.append(break_fluid_color)

    text = listen("Is there any oil leak in engine? ")
    match_yes=match([{'LOWER':'yes'}],text)
    oil = 1 if match_yes else 0
    engine_info.append(oil)

    return engine_info
