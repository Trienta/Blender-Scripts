import bpy
from math import atan2, sqrt

cyl = bpy.context.object
if cyl:
    flt = cyl.copy()
    me = flt.data.copy()
    flt.data = me    
    bpy.context.collection.objects.link(flt)
    
min_r = float("inf")
    
for v in me.vertices:
    x, y, z = v.co
    r = v.co.xy.length
    theta = atan2(x, y)
    v.co = theta, r, z
    min_r = min(r, min_r)
       
for v in me.vertices:
    v.co.x *= min_r  
    v.co.y -= min_r

flt.location.y += min_r
