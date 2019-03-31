import pickle
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# pickle_in = open("./data/play_gpsdata.pkl", "rb")
# HalfGameXs, HalfGameYs, desc = pickle.load(pickle_in)
# print(desc)

#colors
num_colors = 17
cm = plt.get_cmap('gist_rainbow')
#ax.set_color_cycle([cm(1.*i/NUM_COLORS) for i in range(NUM_COLORS)])

#set up plotting area
# fig, ax = plt.subplots(figsize=(5, 3))
# ax.set(xlim=(-85.314, 88.5508), ylim=(-87.579, 48.443))

#create data to plot
# x = HalfGameXs
# y = HalfGameYs
# x2, y2 = np.meshgrid()
# scat = ax.scatter(x[::3], F[0, ::3])

class AnimatedScatter(object):
    """An animated scatter plot using matplotlib.animations.FuncAnimation."""
    def __init__(self, numpoints=50):
        pickle_in = open("./data/play_gpsdata.pkl", "rb")
        HalfGameXs, HalfGameYs, desc = pickle.load(pickle_in)
        print(desc)

        self.Xs = iter(HalfGameXs)
        self.Ys = iter(HalfGameYs)

        self.numpoints = numpoints
        self.stream = self.data_stream()

        # Setup the figure and axes...
        self.fig, self.ax = plt.subplots()
        # Then setup FuncAnimation.
        self.ani = animation.FuncAnimation(self.fig, self.update, interval=5,
                                           init_func=self.setup_plot, blit=True)

    def setup_plot(self):
        """Initial drawing of the scatter plot."""
        x, y = next(self.stream)
        self.scat = self.ax.scatter(x, y, animated=True) #c=c, s=s,
        self.ax.axis(xlim=(-85.314, 88.5508), ylim=(-87.579, 48.443))
        return self.scat,

    def data_stream(self):
        """Generate a random walk (brownian motion). Data is scaled to produce
        a soft "flickering" effect."""
        # data = np.random.random((4, self.numpoints))

        # xy = data[:2, :]
        # print(xy)
        # s, c = data[2:, :]
        # xy -= 0.5
        # xy *= 10
        # while True:
        #     xy += 0.03 * (np.random.random((2, self.numpoints)) - 0.5)
        #     s += 0.05 * (np.random.random(self.numpoints) - 0.5)
        #     c += 0.02 * (np.random.random(self.numpoints) - 0.5)
        #     yield data

        while True:
            x = next(self.Xs)
            y = next(self.Ys)

            yield x, y

    def update(self, i):
        """Update the scatter plot."""
        x, y = next(self.stream)
        print(x)
        print(y)

        # Set x and y data...
        self.scat.set_offsets(x, y)
        # # Set sizes...
        # self.scat._sizes = 300 * abs(data[2])**1.5 + 100
        # # Set colors..
        # self.scat.set_array(data[3])

        # We need to return the updated artist for FuncAnimation to draw..
        # Note that it expects a sequence of artists, thus the trailing comma.
        return self.scat,

    def show(self):
        plt.show()

if __name__ == '__main__':
    a = AnimatedScatter()
    a.show()




#animation
# fig = plt.figure()
# ax = plt.axes(xlim=(-85.314, 88.5508), ylim=(-87.579, 48.443))
# scatter_object, = ax.scatter([],[], lw=2)
#
#
# def init():
#     scatter_object.set_data([], [])
#     return scatter_object,
#
#
# def animate(frame_num):
#     x = HalfGameXs[frame_num]
#     y = HalfGameYs[frame_num]
#     scatter_object.set_data(x, y)
#     return scatter_object,
#
#
# anim = animation.FuncAnimation(fig, animate, init_func=init,
#                                frames=len(HalfGameXs), interval=20, blit=False)


# x = [None]*len(fun_array)
# y = [None]*len(fun_array)
#
# for i in range(len(fun_array)):
#
#     x[i] = float(fun_array[i][8])
#     y[i] = float(fun_array[i][9])
#
# colors = (0, 0, 0)
#
# # Plot
# plt.scatter(x, y, c=colors, alpha=0.5, s=30)
# plt.title('Scatter plot of positions')
# plt.xlabel('lat')
# plt.ylabel('long')
# plt.ylim(55.466,55.4667)
# plt.show()