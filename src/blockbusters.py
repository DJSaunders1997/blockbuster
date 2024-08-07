
# Imports
#https://stackoverflow.com/questions/46525981/how-to-plot-x-y-z-coordinates-in-the-shape-of-a-hexagonal-grid
import matplotlib
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon
matplotlib.use('Agg')  # Use the Agg backend for non-interactive environments
import numpy as np
import random

# Specify coordinates
coord = [

# center line top to bottom
[0, 2, -2],
[0, 1, -1],
[0, 0, 0],
[0, -1, 1],

# line right of center
[1, 2, -3],
[1, 1, -2],
[1, 0, -1],
[1, -1, 0],
[1, -2, 1],

# right most line
[2, 1, -3],
[2, 0, -2],
[2, -1, -1],
[2, -2, 0],

# line left of center
[-1, 3, -2],
[-1, 2, -1],
[-1, 1, 0],
[-1, 0, 1],
[-1, -1, 2],


# left most line
[-2, 3, -1],
[-2, 2, 0],
[-2, 1, 1],
[-2, 0, 2],

]

# Logic functions

# Creates 2 blockbusters plots and saves them to one figure
def create_2_plots():

	num_hex = 22
	num_missing = 3

	randomlist = random.sample(range(1,1+num_hex+num_missing), num_hex)
	labels = list(map(str, randomlist))

	randomlist2 = random.sample(range(1,1+num_hex+num_missing), num_hex)
	labels2 = list(map(str, randomlist2))

	# Horizontal cartesian coords
	hcoord = [c[0] for c in coord]
	# Vertical cartersian coords
	vcoord = [2. * np.sin(np.radians(60)) * (c[1] - c[2]) /3. for c in coord]

	fig, ax = plt.subplots(2,1)
	#ax[0].set_aspect('equal')
	#ax[1].set_aspect('equal')

	# Add some coloured hexagons
	for x, y, label in zip(hcoord, vcoord, labels):
		hex = RegularPolygon((x, y), numVertices=6, radius=2. / 3.,
							orientation=np.radians(30),
							facecolor='w', alpha=1, edgecolor='k')
		ax[0].add_patch(hex)

		# Also add a text label
		ax[0].text(x, y+0.35, label, ha='center', va='center', size=12)

	# Also add scatter points in hexagon centres
	ax[0].scatter(hcoord, vcoord, alpha=0) # Adds invisible centroids, not sure why its needed but it is

	# Add some coloured hexagons
	for x, y, label in zip(hcoord, vcoord, labels2):
		hex = RegularPolygon((x, y), numVertices=6, radius=2. / 3.,
							orientation=np.radians(30),
							facecolor='w', alpha=1, edgecolor='k')
		ax[1].add_patch(hex)

		# Also add a text label
		ax[1].text(x, y+0.35, label, ha='center', va='center', size=12)

	# Also add scatter points in hexagon centres
	ax[1].scatter(hcoord, vcoord, alpha=0) # Adds invisible centroids, not sure why its needed but it is

	ax[0].axis('off') # Remove unnecessary axis
	ax[1].axis('off') # Remove unnecessary axis

	# remove figure margins https://stackoverflow.com/questions/18619880/matplotlib-adjust-figure-margin
	plt.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0, hspace=0)

	plt.close(fig)	# Close fig to produce more than 20 and save memory

	return fig

def create_pdf(num_pages):
	# Each page has 2 plots on it
	# Therefore if 6 people are playing 1 round 3 pages should be printed.

	print('CREATING PDF')

	pp = PdfPages(f'blockbuster-{num_pages}-pages.pdf')

	for i in range(num_pages):

		plot = create_2_plots()

		plot.set_size_inches([8.5,11])

		pp.savefig(plot) # bbox_inches='tight' can help full page with figure

	pp.close()

	print('PDF CREATED')

# Test functions
create_pdf(4)

