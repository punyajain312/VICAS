from _listenSpeak import listen
from _ai import match


def exterior_inspection():

    exterior_info=[]
    
    text = listen("Is there any rust to the exterior? ")
    match_yes=match([{'LOWER':'yes'}],text)
    rust = 1 if match_yes else 0
    exterior_info.append(rust)

    text = listen("Is there any dent to the exterior? ")
    match_yes=match([{'LOWER':'yes'}],text)
    dent = 1 if match_yes else 0
    exterior_info.append(dent)

    text = listen("Is there any damage to the exterior? ")
    match_yes=match([{'LOWER':'yes'}],text)
    damage = 1 if match_yes else 0
    exterior_info.append(damage)

    text = listen("Is there any oil leak in suspension? ")
    match_yes=match([{'LOWER':'yes'}],text)
    oil = 1 if match_yes else 0
    exterior_info.append(oil)

    return exterior_info

