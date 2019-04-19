from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

fig = plt.figure()
m1 = Basemap(projection='cyl',llcrnrlat=21.3,urcrnrlat=21.6,llcrnrlon=111.2,urcrnrlon=111.5,resolution='f')


m1.drawcoastlines(linewidth = 0.5)
#m1.drawmapboundary(fill_color = [0.70200,0.8588,0.9098])
#m1.drawmapboundary(fill_color = [0.25098,0.85098,1],linewidth = 0.5)
m1.drawmapboundary(fill_color = [0.72159, 0.89411,1],linewidth = 0.5)
m1.fillcontinents(color = [0.5, 0.5, 0.5])
parallels=np.arange(21.3,21.7,0.1)
m1.drawparallels(parallels,labels=[1,0,0,0],fontsize =8,linewidth = 0.3)
meridians = np.arange(111.1,111.7,0.1)
m1.drawmeridians(meridians,labels=[0,0,1,0],fontsize =8,linewidth = 0.3)
x1,y1 = m1(111.384, 21.4383)
m1.scatter(x1, y1, marker = 'v', color = 'k',s=100)

ax = fig.add_axes([0.1, 0.55, .4 ,.4])
#a = plt.axes([0.08, 0.45, .4, .4], facecolor='k')
m2 = Basemap(projection='cyl',llcrnrlat=15,urcrnrlat=25,llcrnrlon=105,urcrnrlon=115,resolution='h')
m2.drawcoastlines(linewidth = 0.3)
#m2.drawmapboundary(fill_color = [0.70200,0.8588,0.9098])
#m2.drawmapboundary(fill_color = [0.25098,0.85098,1],linewidth = 0.5)
m2.drawmapboundary(fill_color = [0.72159, 0.89411,1],linewidth = 0.5)
m2.fillcontinents(color = [0.5, 0.5, 0.5])
parallels=np.arange(15,25,5)
m2.drawparallels(parallels,labels=[1,0,0,0],fontsize =8,linewidth = 0.3)
meridians = np.arange(105,116,5)
m2.drawmeridians(meridians,labels=[0,0,1,0],fontsize =8,linewidth = 0.3)
#m2.drawcountries(linewidth = 0.3)
a1,a2,b1,b2= [21.3, 21.6,111.2, 111.5 ]
b1,a1 = m2(111.2,21.3)
b1,a2 = m2(111.2,21.6)
b2,a1 = m2(111.5,21.3)
b2,a2 = m2(111.5,21.6)
m2.plot([b1,b2],[a1,a1],c = 'r')
m2.plot([b1,b2],[a2,a2],c = 'r')
m2.plot([b1,b1],[a1,a2],c = 'r')
m2.plot([b2,b2],[a1,a2],c = 'r')
plt.show()


