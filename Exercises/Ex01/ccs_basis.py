from IPython.display import HTML
from matplotlib import animation, rc
import scipy as scy
import copy
import matplotlib.pyplot as plt
class Particle:
    def __init__(self, r, x, y, vx, vy):
        self.r = r
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
    
    def __repr__(self):
        return str("This is a particle at %0.2f, %0.2f with v=%0.2f,%0.2f nm/timestep" % (self.x,self.y,self.vx,self.vy))
        
def move(p,dt):
    p.x = p.x + p.vx*dt
    p.y = p.y + p.vy*dt
    return p

def reflect(p,box):
    if (p.x + p.r) >= box[0]:
        p.vx = p.vx * (-1)
    if (p.x + p.r) <= p.r:
        p.vx = p.vx * (-1)
    if (p.y + p.r) >= box[1]:
        p.vy = p.vy * (-1)
    if (p.y + p.r) <= p.r:
        p.vy = p.vy * (-1)
    return p

def set_anim_plot(box,only_dot=False):
    if only_dot:
        fig, ax = plt.subplots()
        dot, = ax.plot([], [], 'bo', ms=5.0)
        return dot
    
    else:
    
        fig, ax = plt.subplots()

        ax.set_xlim((0, box[0]))
        ax.set_ylim((0, box[1]))

        plt.xlabel(r'position $x$')
        plt.ylabel(r'position $y$')

        dot, = ax.plot([], [], 'bo', ms=5.0)
        return fig,dot

# def do_animation(fig,frames=1000,interval=20):
#     anim = animation.FuncAnimation(fig, animate, init_func=init,
#                                frames=frames, interval=interval, blit=True)
#     return anim

def init():
    dot.set_data([], [])
    return (dot,)

def animate(i):
    x = data_traj[0,i]
    y = data_traj[1,i]
    dot.set_data(x, y)
    return (dot,)

# Update 1: functions from Ex01

def is_colliding(p1, p2):
    # distance check
    distance = np.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)
    # returns True if distance is less than or equal to
    #  the sum of the radii of the two particles
    return distance <= (p1.r + p2.r)

def elastic_collision(p1, p2):
    # packing the positions and velocities as vectors:
    r1, r2 = np.array([p1.x, p1.y]), np.array([p2.x, p2.y])
    v1, v2 = np.array([p1.vx, p1.vy]), np.array([p2.vx, p2.vy])

    d = np.linalg.norm(r1 - r2)**2
    
    # the final velocities as per the formula
    u1 = v1 - np.dot(v1 - v2, r1 - r2) / d * (r1 - r2)
    u2 = v2 - np.dot(v2 - v1, r2 - r1) / d * (r2 - r1)

    # unpacking the final velocity vector:
    p1.vx, p1.vy = u1
    p2.vx, p2.vy = u2

    return p1, p2

def do_the_simulation(box,num_particles,steps,v_norm=0.5,pbound=True):
    
    particles = [] # list to store the particle objects
    dots = [] # list to store the markers for each particle

    fig, ax = plt.subplots()
    fig, ax = setup_fig_box(fig,ax,box,'System with {0} particles'.format(num_particles))


    for _ in range(num_particles):
        particles.append(Particle(r=0.5,x=rand_coordinate(box[0]),y=rand_coordinate(box[0]),vx=rand_velocity(v_norm),vy=rand_velocity(v_norm)))
        dots.append(ax.plot([], [], 'ro')[0])

    data_traj = np.zeros((num_particles, 4, steps))

    for i in range(steps):
        # at each time step:
        for j, p in enumerate(particles):
            # j - particle index
            # p - particle object
            if pbound:
                periodic_bound(p, box)
            else:
                reflect(p,box)
            
            move(p, 1)
            # input the coordinates to trajectory:
            data_traj[j, :, i] = [p.x, p.y, p.vx, p.vy]

        # checking pairs of particles for collision
        # (Note: this loop was generated with the help of
        # ChatGPT)
        for j in range(num_particles):
            # j - again, particle index
            for k in range(j+1, num_particles):
                # k - loop over particles other than j
                if is_colliding(particles[j], particles[k]):
                    particles[j], particles[k] = elastic_collision(particles[j], particles[k])

    # def init():
    #     for dot in dots:
    #         dot.set_data([], [])
    #     return dots

    # def animate(i):
    #     for j, dot in enumerate(dots):
    #         x = [data_traj[j, 0, i]]
    #         y = [data_traj[j, 1, i]]
    #         dot.set_data(x, y)
    #     return dots

    anim = animation.FuncAnimation(fig, animate, init_func=init,
                                frames=steps, interval=20, blit=True)

    plt.close(fig)
    return data_traj, anim

num_steps = 2000
v_magn=0.5
data_traj, anim = do_the_simulation(box=[20,20],num_particles=50,steps=num_steps,v_norm=v_magn)

HTML(anim.to_html5_video())