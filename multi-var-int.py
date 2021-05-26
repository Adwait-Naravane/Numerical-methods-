import numpy as np

class MVF:
  dx = 0.0001
  
  def __init__(self, f):
    self.f = f
  
  def value(self, args):
    return self.f(*args)

  def grad(self, args):
    return np.array([f(*np.array(args + dx*np.identity(len(args))[i])) - f(*np.array(args)) for i in range(len(args))])/dx

  def integral(self, start, end, tol):
    V = abs(np.prod(np.array(end) - np.array(start))) 
    fbar = (1/tol)*(np.sum(f(*[np.random.uniform(start[i],end[i],tol) for i in range(len(end))])))
 #monte-carlo integration.

    return fbar*V
f = lambda x,y,z : x*y*z
p = MVF(f)

p.integral([0,0,0],[1,1,1],100000)
''' Monte carlo integration is faster for higher dimensional functions than trapezoidal method, but it gives a good bit of variance. 
    The variance can be calculated by variance = (1/(N)^0.5)*(sum(f^2(x_i)) - mean(f)^2)^0.5 '''
