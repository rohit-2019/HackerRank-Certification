def getBattery(events):
    charge = 50
    for i in events:
        if charge+i>100:
            charge=100
        else:
            charge+=i
    return charge