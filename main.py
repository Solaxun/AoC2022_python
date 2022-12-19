import re

data = open('day15.txt').read()
# data = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
# Sensor at x=9, y=16: closest beacon is at x=10, y=16
# Sensor at x=13, y=2: closest beacon is at x=15, y=3
# Sensor at x=12, y=14: closest beacon is at x=10, y=16
# Sensor at x=10, y=20: closest beacon is at x=10, y=16
# Sensor at x=14, y=17: closest beacon is at x=10, y=16
# Sensor at x=8, y=7: closest beacon is at x=2, y=10
# Sensor at x=2, y=0: closest beacon is at x=2, y=10
# Sensor at x=0, y=11: closest beacon is at x=2, y=10
# Sensor at x=20, y=14: closest beacon is at x=25, y=17
# Sensor at x=17, y=20: closest beacon is at x=21, y=22
# Sensor at x=16, y=7: closest beacon is at x=15, y=3
# Sensor at x=14, y=3: closest beacon is at x=15, y=3
# Sensor at x=20, y=1: closest beacon is at x=15, y=3"""

def manhattan_dist(pt1,pt2):
    return sum(abs(x-y) for x,y in zip(pt1,pt2))

coords = list(map(int,re.findall('\-?\d+',data)))
sensors,beacons = set(),set()
sensor_to_beacondist = {}
for i in range(0,len(coords),4):
    sx,sy,bx,by = coords[i:i+4]
    sensor_to_beacondist[(sx,sy)]=manhattan_dist((sx,sy),(bx,by))
    sensors.add((sx,sy))
    beacons.add((bx,by))

xmin,xmax = 0,0
for x,y in sensors|beacons:
    xmin = min(xmin,x)
    xmax = max(xmax,x)
print(xmin,xmax)
## if any of these along y=10 have a MH to the to any sensor of <= that 
## sensors MH to t's closest beacon, it's not a beacon
points_to_check = []
for x in range(xmin,xmax+1):
    points_to_check.append((x,2000000))
-1,016,402 to 4,322,327
# not_beacon = set()
# for p in points_to_check:
#     for sensor,beacondist in sensor_to_beacondist.items():
#         if manhattan_dist(sensor,p) <= beacondist:
#             not_beacon.add(p)
# print(len(not_beacon - beacons))
# took 1-3 min on my fast laptop, timed out here.  need better approach
# try using max manh dist to beacon to figure out how far a sensor could be
# left or right of xmin/xmax