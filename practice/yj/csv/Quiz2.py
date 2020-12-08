from matplotlib.pyplot import *
title('plot graph')
plot([1, 2, 3, 4], [10, 20, 30, 40], marker='.', color= 'green', label = '1st')
plot([1, 2, 3, 4], [30, 15, 25, 10], marker= '^' ,color = 'pink', label = '2nd')
# plot([1, 2, 3, 4], [15, 25, 15, 25], linestyle= '-.' ,color = 'red', label = '3rd')
# plot([1, 2, 3, 4], [20, 10, 30, 5], linestyle= '-' ,color = 'blue', label = '4th')
legend()
show()
