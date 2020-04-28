from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
from random import choice

class RandomWalk():
    def __init__(self, num_points):
        self.num_points=num_points
        self.x_values=[0]
        self.y_values=[0]
        self.z_values=[0]
        
    def fill_walk(self):
        while len(self.x_values)<self.num_points:
            x_directions=choice([-1,1])
            x_distance=choice([0, 1, 2, 3, 4])
            x_step=x_directions*x_distance
            
            y_directions=choice([-1,1])
            y_distance=choice([0, 1, 2, 3, 4])
            y_step=y_directions*y_distance
            
            z_directions=choice([-1,1])
            z_distance=choice([0, 1, 2, 3, 4])
            z_step=z_directions*z_distance
            
            if (x_step==0 and y_step==0 and z_step==0):
                continue
            
            next_x=self.x_values[-1]+x_step
            next_y=self.y_values[-1]+y_step
            next_z=self.z_values[-1]+z_step
            
            self.x_values.append(next_x)
            self.y_values.append(next_y)
            self.z_values.append(next_z)
            
rw=RandomWalk(2000)
rw.fill_walk()

fig=pyplot.figure()
ax=Axes3D(fig)

ax.scatter(rw.x_values, rw.y_values, rw.z_values, s=1, c='Red')
ax.plot(rw.x_values,rw.y_values, rw.z_values, c='Green')


