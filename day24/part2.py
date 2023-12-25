import os
import numpy as np

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n")[:-1]

def independent(matrix):
    for i in range(matrix.shape[1]):
        for j in range(matrix.shape[1]):
            if i != j:
                inner_product = np.inner(
                    matrix[:,i],
                    matrix[:,j]
                )
                norm_i = np.linalg.norm(matrix[:,i])
                norm_j = np.linalg.norm(matrix[:,j])
                if np.abs(inner_product - norm_j * norm_i) < 1E-5:
                    return False
    return True

positions = []
velocities = []
n = 0
for line in myinput:
    pos, vel = line.split(" @ ")
    pos = [int(x) for x in pos.split(",")]
    vel = [int(x) for x in vel.split(",")]
    positions.append(pos)
    velocities.append(vel)
    if independent(np.transpose(np.array(velocities))):
        n += 1
    else:
        positions.pop()
        velocities.pop()
    if n == 3:
        break
x1, y1, z1 = positions[0]
x2, y2, z2 = positions[1]
x3, y3, z3 = positions[2]
vx1, vy1, vz1 = velocities[0]
vx2, vy2, vz2 = velocities[1]
vx3, vy3, vz3 = velocities[2]

def F(params):
    x,y,z,vx,vy,vz,n1,n2,n3 = params
    return np.array([
        x + n1*vx - x1 - n1*vx1,
        y + n1*vy - y1 - n1*vy1,
        z + n1*vz - z1 - n1*vz1,
        x + n2*vx - x2 - n2*vx2,
        y + n2*vy - y2 - n2*vy2,
        z + n2*vz - z2 - n2*vz2,
        x + n3*vx - x3 - n3*vx3,
        y + n3*vy - y3 - n3*vy3,
        z + n3*vz - z3 - n3*vz3
    ])

def J(params):
    x,y,z,vx,vy,vz,n1,n2,n3 = params
    return np.array([
        [1, 0, 0, n1, 0, 0, vx - vx1, 0, 0],
        [0, 1, 0, 0, n1, 0, vy - vy1, 0, 0],
        [0, 0, 1, 0, 0, n1, vz - vz1, 0, 0],
        [1, 0, 0, n2, 0, 0, 0, vx - vx2, 0],
        [0, 1, 0, 0, n2, 0, 0, vy - vy2, 0],
        [0, 0, 1, 0, 0, n2, 0, vz - vz2, 0],
        [1, 0, 0, n3, 0, 0, 0, 0, vx - vx3],
        [0, 1, 0, 0, n3, 0, 0, 0, vy - vy3],
        [0, 0, 1, 0, 0, n3, 0, 0, vz - vz3]
    ])

params = np.array([0,0,0,0,0,0,1,5,10])
for i in range(50):
    params = params - np.linalg.inv(J(params))@F(params)
total = np.sum(np.round(params).astype(np.int64)[:3])
print(total)
