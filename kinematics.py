import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def rot_x(theta):
    c, s = np.cos(theta), np.sin(theta)
    return np.array([[1, 0, 0, 0],
                     [0, c,-s, 0],
                     [0, s, c, 0],
                     [0, 0, 0, 1]])

def rot_y(theta):
    c, s = np.cos(theta), np.sin(theta)
    return np.array([[ c, 0, s, 0],
                     [ 0, 1, 0, 0],
                     [-s, 0, c, 0],
                     [ 0, 0, 0, 1]])

def rot_z(theta):
    c, s = np.cos(theta), np.sin(theta)
    return np.array([[c,-s, 0, 0],
                     [s, c, 0, 0],
                     [0, 0, 1, 0],
                     [0, 0, 0, 1]])
def trans_x(a):
    return np.array([[1,0,0,a],
                     [0,1,0,0],
                     [0,0,1,0],
                     [0,0,0,1]])

def calculate_fk(q):
    L = 1
    positions = [np.array([0,0,0])] 
    T = np.eye(4)
    
    T = rot_y(q[0]) @ trans_x(L)
    positions.append(T[:3,3].copy())
    
    T = T @ rot_z(q[1]) @ trans_x(L)
    positions.append(T[:3,3].copy())
    
    T = T @ rot_y(q[2]) @ trans_x(L)
    positions.append(T[:3,3].copy())
    
    T = T @ rot_z(q[3]) @ trans_x(L)
    positions.append(T[:3,3].copy())
    
    return np.array(positions)

# Example joint angles in degrees
angles_deg = [0, 0, 0, 90]
angles_rad = [np.deg2rad(a) for a in angles_deg]

# Get joint positions
points = calculate_fk(angles_rad)
print(points)

# Visualization
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.set_box_aspect([1,1,1])             # equal aspect
ax.set_xlim(-4.5, 4.5); ax.set_ylim(-4.5, 4.5); ax.set_zlim(-4.5, 4.5)
ax.view_init(elev=20, azim=-60)        # pick a clear angle


# Plot links
ax.plot(points[:,0], points[:,1], points[:,2], '-o', linewidth=3, markersize=6, color='blue')

# Highlight end-effector
ax.scatter(points[-1,0], points[-1,1], points[-1,2], color='red', s=100, label='End-effector')

# Axes labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Equal aspect ratio
ax.set_box_aspect([1,1,1])
ax.legend()
plt.title('4-DOF Robot Visualization')
plt.show()