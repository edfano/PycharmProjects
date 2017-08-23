
#Using pylab
"""The Pylab module is useful for creating plots in an interactive shell, such as
the IDLE shell, as we’ve been doing so far. However, when using matplotlib
outside of the IDLE shell—for example, as part of a larger program—the
pyplot module is more efficient."""

#Customizing the Axes now
from pylab import plot, show, axis

nyc_temp = [53.9, 56.3, 56.4, 53.4, 54.5, 55.8, 56.8, 55.0, 55.3, 54.0, 56.7, 56.4, 57.3]
#axis()
#axis(ymin=0)
"""This would set the range of the x-axis to (0, 12) and
that of the y-axis to (0, 60).
"""
axis([0, 12, 0, 60])
plot(nyc_temp, marker='o')

#legend([2000, 2006, 2012])

show()

