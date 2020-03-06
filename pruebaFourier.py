from numpy import loadtxt                                       

data = loadtxt('pitch.txt')                                     

from pylab import plot, show, title

plot(data)
title('ok')                             
xaxix('time0')

show() 
