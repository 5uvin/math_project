import numpy as np

def euler_to_quat(roll, pitch, yaw):
    
    cy = np.cos(yaw * 0.5)
    sy = np.sin(yaw * 0.5)
    cp = np.cos(pitch * 0.5)
    sp = np.sin(pitch * 0.5)
    cr = np.cos(roll * 0.5)
    sr = np.sin(roll * 0.5)

    w = cr * cp * cy + sr * sp * sy
    x = sr * cp * cy - cr * sp * sy
    y = cr * sp * cy + sr * cp * sy
    z = cr * cp * sy - sr * sp * cy
    
    return np.array([x, y, z, w])

if __name__ == "__main__":
    roll, pitch, yaw = 20, 15, 0 
    q = euler_to_quat(roll, pitch, yaw)
    print("Quaternion:", q)