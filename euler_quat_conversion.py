import numpy as np

def euler_to_quat(roll, pitch, yaw, degrees=False):
    if degrees:
        roll = np.deg2rad(roll)
        pitch = np.deg2rad(pitch)
        yaw = np.deg2rad(yaw)
    
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

def quaternion_to_euler(x, y, z, w, degrees=False):

    norm = np.sqrt(x*x + y*y + z*z + w*w)
    x /= norm
    y /= norm
    z /= norm
    w /= norm

    # Roll
    sinr_cosp = 2 * (w * x + y * z)
    cosr_cosp = 1 - 2 * (x*x + y*y)
    roll = np.arctan2(sinr_cosp, cosr_cosp)
    
    # Pitch
    sinp = np.sqrt(1 + 2 * (w * y - x * z))
    cosp = np.sqrt(1 - 2 * (w * y - x * z))
    pitch = 2 * np.arctan2(sinp, cosp) - np.pi / 2
    
    # Yaw
    siny_cosp = 2 * (w * z + x * y)
    cosy_cosp = 1 - 2 * (y*y + z*z)
    yaw = np.arctan2(siny_cosp, cosy_cosp)
    
    if degrees:
        roll = np.rad2deg(roll)
        pitch = np.rad2deg(pitch)
        yaw = np.rad2deg(yaw)
    return roll, pitch, yaw


if __name__ == "__main__":
    roll, pitch, yaw = 20, 15, 0 
    q = euler_to_quat(roll, pitch, yaw, degrees=True)
    print("Quaternion:", q)

    x = 0.17216259
    y = 0.12854321
    z = -0.02266564
    w = 0.97638259
    e = quaternion_to_euler(x, y, z, w, degrees=True)
    print("Euler angles (degrees):", e)