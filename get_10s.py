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
# df["sleep"]=np.int64(df["timestamps"])-int(df["timestamps"][0])
df=df.sort_values(by=["timestamps"])
fig,ax=plt.subplots()
ax = fig.add_subplot(111, projection='3d')
track_org=df["timestamps"][0]
time_track=False
df_truncate_10s=None
df_new=None
def animate(i):
    global track_org,df_truncate_10s,df_new,count
    if df_truncate_10s is None and df_new is None:
        df_truncate_10s=df.loc[df["timestamps"]-track_org<=10000]
        df_new=df[~df.isin(df_truncate_10s)]
    else:
        df_new=df_new[~df_new.isin(df_truncate_10s)]
        df_truncate_10s=df_new.loc[df_new["timestamps"]-track_org<=10000]
       
        # df_truncate_10s=df.loc[df_truncate_10s["timestamps"].iloc[-1]]
    # print(df_truncate_10s)
    print(df_truncate_10s)
    Mx_vi=df_truncate_10s["Mx"]
    My_vi=df_truncate_10s["My"]
    Mz_vi=df_truncate_10s["Mz"]
    ax.set_xlim(df["Mx"].min(),df["Mx"].max())
    ax.set_ylim(df["My"].min(),df["My"].max())
    ax.set_zlim(df["Mz"].min(),df["Mz"].max())
    ax.clear()
    ax.scatter(Mx_vi,My_vi,Mz_vi)
    # ax.set_label("change pharse from {} to {}".format(track_org,df_truncate_10s["timestamps"].iloc[-1]))
    track_org=df_truncate_10s["timestamps"].iloc[-1]
    print(track_org)
    print("change pharse")
    print("time org",track_org)
ani = animation.FuncAnimation(
    fig, animate,frames=800, interval=100,repeat=False
)
ani.save("results.gif")
plt.show() 


