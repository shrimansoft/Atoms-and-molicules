from lib.lib import eigenValues2,myPlot     

myPlot(100,-1,5,40,lambda x: eigenValues2(x*10+50,2,2,1))

myPlot(200,-3,7,70,lambda x:eigenValues2(300,2,2,0.06*x-2))
