def rk4(x, dx, y, deriv,params):
    ddx = dx/2.
    d1 = deriv(x,y,params)
    yp = y + d1*ddx
    d2 = deriv(x+ddx,yp,params)
    yp = y + d2*ddx    
    d3 = deriv(x+ddx,yp,params)
    yp = y + d3*dx
    d4 = deriv(x+dx,yp,params)
    return y + dx*( d1 + 2*d2 + 2*d3 + d4 )/6