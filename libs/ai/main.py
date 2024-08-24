from __header import headerfrom __tire_inspection import tire_inspection
from __battery_inspection import battery_inspection
from __exterior_inspection import exterior_inspection
from __brakes_inspection import break_inspection
from __engine_inspection import engine_inspection

h = header()
t = tire_inspection()
b1 = battery_inspection()
e1 = exterior_inspection()
b2 = break_inspection()
e2 = engine_inspection()

print(h,t,b1,e1,b2,e2)
