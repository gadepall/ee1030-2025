import ctypes as ct
import numpy as np
import matplotlib.pyplot as plt
from   numpy.ctypeslib import ndpointer


lib = ct.CDLL ( './libmatfun.so' )

for f in ( 'semi_major' , 'semi_minor' ,
           'focal_distance' , 'latus_rectum' ):
    getattr ( lib , f ).argtypes = [ ct.c_double , ct.c_double ]
    getattr ( lib , f ).restype  =  ct.c_double

lib.ellipse_points.argtypes = [
    ct.c_double , ct.c_double , ct.c_int ,
    ndpointer ( ct.c_double , flags = 'C_CONTIGUOUS' ),
    ndpointer ( ct.c_double , flags = 'C_CONTIGUOUS' )
]

e , D = 5 / 8 , 10

a = lib.semi_major     ( e , D )
b = lib.semi_minor     ( e , D )
c = lib.focal_distance ( e , D )
l = lib.latus_rectum   ( e , D )

print ( l )                           # prints 9.75


N = 1000
x = np.empty ( N )
y = np.empty ( N )

lib.ellipse_points ( a , b , N , x , y )

fig , ax = plt.subplots ( figsize = ( 12 , 8 ) )

ax.plot    ( x , y , 'b-' , lw = 2 )
ax.scatter ( [  c , -c ] , [ 0 , 0 ] , color = 'r' , s = 50 )
ax.plot    ( [  c , -c ] , [ 0 , 0 ] , 'r--' , lw = 1 )

ax.plot    ( [  c ,  c ] , [ -l / 2 ,  l / 2 ] , 'g' , lw = 3 )
ax.plot    ( [ -c , -c ] , [ -l / 2 ,  l / 2 ] , 'g' , lw = 3 )

ax.plot ( [ -a ,  a ] , [ 0 , 0 ] , 'k--' , alpha = .5 )
ax.plot ( [  0 ,  0 ] , [ -b , b ] , 'k--' , alpha = .5 )

ax.text (  a + .3 , 0       , f'A ( {a} )' )
ax.text ( -a - 1 , 0        , f"A' ( -{a} )" )
ax.text ( .3 ,  b + .3      , f'B ( {b:.2f} )' )
ax.text ( .3 , -b - .6      , f"B' ( -{b:.2f} )" )
ax.text (  c + .2 ,  l / 2  , f'ℓ = {l:.2f}' )
ax.text ( -c - 1 ,  l / 2   , f'ℓ = {l:.2f}' )

ax.set_aspect ( 'equal' )
ax.set_xlim   ( -10 , 10 )
ax.set_ylim   ( -8  , 8  )
ax.set_title  ( f'Ellipse  e = {e}   D = {D}' )
ax.grid       ( alpha = .3 )

plt.tight_layout ( )
plt.show ( )
