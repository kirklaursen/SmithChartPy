# import sys
# import os
# import numpy
# import matplotlib
# import skrf as rf       # scikit-rf

from skrf import Network, Frequency
from matplotlib import pyplot as plt

# print(sys.version)
# print(os.system('pwd'))
from skrf.data import ring_slot     # import some sample data
# ring_slot = Network('ring slot.s2p')      # read a sample s2p file
print(ring_slot)

# %matplotlib inline
# rf.style()

ring_slot.plot_s_smith(draw_labels=True)
# plt.figure(figsize=(3, 3), dpi=100)      # set size to 5"x5" with 100 dpi
# plt.axis('equal')               # set axes equal so that it shows up as a real circle
plt.show()
