from lib.lib import eigenValues,myPlot

myPlot(100,0, 5, 50,lambda x: eigenValues(x*10+50,3,2,1))

myPlot(200,-3,7,70,lambda x: eigenValues(300,3,2,0.06*x-2))
