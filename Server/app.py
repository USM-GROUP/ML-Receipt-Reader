from c_point import point
import functions as func

p = point(0, 5)
q = point(5, 0)
r = point(0, 0)
s = point(6, 4)

midpoint_pq = func.get_midpoint(p,q)
midpoint_rs = func.get_midpoint(r,s)

slope = func.get_slope(p,q)
func.is_on_line(midpoint_pq, midpoint_rs, slope)