import pandas as pd
import numpy as np
import time
import math
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
#using animation matplotlib
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
import time
import matplotlib.pyplot as plt

fig,ax=plt.subplots()
ax = fig.add_subplot(111, projection='3d')

df_new=df.query("sleep != 0 & sleep <10100")
Mx=df_new["Mx"]
My=df_new["My"]
Mz=df_new["Mz"]
track_org=df["timestamps"][0]
time_track=df["timestamps"][0]
def custom_interval(frame_number, base_interval=df_new["sleep"].min(), max_interval=df_new["sleep"].max()):
    # Custom interval function: increase delay gradually as frame number increases
    time.sleep(df_new["sleep"][frame_number]/1000)
def init():
    MX=df[df["sleep"]==0]["Mx"]
    MY=df[df["sleep"]==0]["My"]
    MZ=df[df["sleep"]==0]["Mz"]
    ax.scatter(MX,MY,MZ)    
def animate(i):
    global time_track
    
    print("df",df["timestamps"][i] )
    time_tracking=df["timestamps"][i] - time_track
    # print("time track",time_track)
    # print(time_tracking)
    time.sleep(abs(time_tracking/1000))
    time_track=df["timestamps"][i]
    Mx_vi=df[df["timestamps"]==df["timestamps"][i]]["Mx"]
    My_vi=df[df["timestamps"]==df["timestamps"][i]]["My"]
    Mz_vi=df[df["timestamps"]==df["timestamps"][i]]["Mz"]
    ax.scatter(Mx_vi,My_vi,Mz_vi)
    ax.set_xlim(df["Mx"].min(),df["Mx"].max())
    ax.set_ylim(df["My"].min(),df["My"].max())
    ax.set_zlim(df["Mz"].min(),df["Mz"].max())
    
    # print(Mx,My,Mz)

   
ani = animation.FuncAnimation(
    fig, animate,init_func=init,frames=df["Mx"].unique().size, interval=5
)
# ani.save("results.gif")
plt.show() 



