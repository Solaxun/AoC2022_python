def mapt(f, *xs):
    """stop making everything a generator when I want to see the output"""
    return list(map(f,*xs))

def bounding_box_from_points(points):
    """return max and min of x and y from a collection of points"""
    (xmin,xmax),(ymin,ymax) = mapt(lambda *a: (min(a),max(a)),*points)
    return (xmin,xmax,ymin,ymax)

def start_at_zero(points):
    """rasterize points to start at zero e.g. if xmin = -2 and xmax = 8 then
    x will start at 0 and go to 10"""
    xmin,xmax,ymin,ymax = points
    return (0,xmax-xmin,0,ymax-ymin)

def grid_from_points(points,cellvalues='.'):
    """make 2d grid out of bounding box of points, inclusive of x and y range
    e.g. if xmin=0 and xmax=7 the grid is 8 rows"""
    xmin,xmax,ymin,ymax = points = bounding_box_from_points(points)
    xmin,xmax,ymin,ymax = rasterized = start_at_zero(points)
    return [[cellvalues for y in range(ymax+1)] for x in range(xmax+1)]