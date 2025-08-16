import numpy as np

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