import pandas as pd
import numpy as np
import time
import math
#using animation matplotlib
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
import time
import matplotlib.pyplot as plt
df=pd.read_csv("ML_B4_Khoanh vung nhieu/20221031_100743_targets_nhieu_nhieu.csv")
'''
Mx=r*cos(e)*sin(az)
My=r.cos(e)*cos(az)
Mz=r.sin(e)
Với e là elevation ,r là range , az là azimuths
'''
df["Mx"]=df["ranges"]*(np.cos(df["elevations"])*np.sin(df["azimuths"]))
df["My"]=df["ranges"]*(np.cos(df["elevations"])*np.cos(df["azimuths"]))
df["Mz"]=df["ranges"]*(np.sin(df["elevations"]))
df["sleep"]=np.int64(df["timestamps"])-int(df["timestamps"][0])
df=df.sort_values(by=["timestamps"],ascending=False)
fig,ax=plt.subplots()
ax = fig.add_subplot(111, projection='3d')
track_org=df["timestamps"][0]
time_track=df["timestamps"][0]
def animate(i):
    global time_track,track_org
    
    print("df",df["timestamps"][i] )
    #theo dõi timestamps theo từng điểm
    time_track=df["timestamps"][i]
    '''
    lấy ra toàn bộ các điểm trong 1 chu kì 10s
    '''
    Mx_vi=df[df["timestamps"]-track_org<10100]["Mx"]
    My_vi=df[df["timestamps"]-track_org<10100]["My"]
    Mz_vi=df[df["timestamps"]-track_org<10100]["Mz"]
    ax.scatter(Mx_vi,My_vi,Mz_vi)
    ax.set_xlim(df["Mx"].min(),df["Mx"].max())
    ax.set_ylim(df["My"].min(),df["My"].max())
    ax.set_zlim(df["Mz"].min(),df["Mz"].max())
    if time_track-track_org>10100:
        ax.clear()
        track_org=time_track
        print("change pharse")
        print("time org",track_org)
        print("time tracking",time_track)
ani = animation.FuncAnimation(
    fig, animate,frames=df["Mx"].unique().size, interval=5
)
ani.save("results.gif")
# plt.show() 


