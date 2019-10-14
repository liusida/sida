from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

# input hand shape should be [5,4,6]
def show_hand(hand, fname=None, show_origin=False, view_point="front", scale="fit"):
    finger_colors = ["#000055", "#111155", "#222255", "#333355", "#444455"]
    fig, (ax) = plt.subplots(nrows=1, ncols=1, figsize=[7,5], subplot_kw=dict(projection='3d'))
    for finger in range(5):
        for bone in range(4):
            ax.plot(xs=hand[finger,bone,::3], ys=hand[finger,bone,1::3], zs=hand[finger,bone,2::3], color=finger_colors[finger], lw=6-bone)

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")

    if show_origin:
        ax.scatter(0,0,0, s=5)

    if scale=="fit":
        ax.set_xlim(np.min(hand[:,:,::3]), np.max(hand[:,:,::3]))
        ax.set_ylim(np.min(hand[:,:,1::3]), np.max(hand[:,:,1::3]))
        ax.set_zlim(np.min(hand[:,:,2::3]), np.max(hand[:,:,2::3]))
    elif scale=="unit":
        view_scale=1
        ax.set_xlim([-view_scale,view_scale])
        ax.set_ylim([-view_scale,view_scale])
        ax.set_zlim([-view_scale,view_scale])

    if view_point == "front":
        ax.view_init(elev=90, azim=-90)
    elif view_point == "side":
        ax.view_init(elev=0, azim=0)
    else:
        pass

    if fname is None:
        plt.show()
    else:
        plt.savefig(fname)
