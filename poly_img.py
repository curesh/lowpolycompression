import cv2 as cv
import numpy as np
from scipy import signal
from matplotlib import pyplot as plt
from scipy.spatial import Delaunay
import sys

class PolyImg:

  # A LOWER node factor results in more triangles
  # node_factor should always be positive
  def __init__(self, image, blur, rate, node_factor = 1):
    self.blur = blur
    if node_factor <= 0
      print("Error: The node_factor is less than or equal to 0.")
      sys.exit()
    self.node_factor = node_factor
    self.rate = rate
    self.orig = image

  def _preprocess(self, img):
    # Convert image to greyscale
    gs_luminosities = [0.07, 0.72, 0.21]
    grey = cv.transform(img, np.array(gs_luminosities).reshape((1, 3)))

    # Blur image
    blur = cv.blur(grey, (self.blur, self.blur))

    # Get the edges
    canny_kernel = np.array([[1, 1, 1],
                             [1, -8, 1],
                             [1, 1, 1]])
    edges = cv.filter2D(blur, -1, canny_kernel)
    return edges

  # Computes a thresholding value for how many adjacent nodes a node should /
  # /have, to be considered a potential triangle vertex
  def _get_edge_threshold(self, img, nodes_convolution):
    threshold = np.sum(nodes_convolution)/nodes_convolution.size
    return threshold

  # Gets the nodes that will be triangle vertices in the delauny triangulation
  def _get_nodes(self, img):
    # Turns matrix of edges into a matrix of nodes which show amount of /
    # /adjecent edges
    nodes_convolution = signal.convolve2d(img, np.ones((3, 3))/9)

    edge_threshold = self._get_edge_threshold(img,nodes_convolution)

    # Only includes nodes in densely populated areas (lots of adjacent nodes)
    # This is determined by the edge_threshold
    sparse_nodes = nodes_convolution > edge_threshold

    nodes = np.transpose(sparse_nodes.nonzero())

    # Computes how many triangle vertices (nodes) should be in the final image
    max_nodes = min(int(self.node_factor*len(nodes)/140), 4000, len(nodes))

    # Randomly selects max_nodes nodes from the total set of potential nodes
    selected_idx = np.random.randint(len(nodes), size = max_nodes)
    nodes = nodes[selected_idx, :]

    # Adds image corners as nodes to be used in Delaunay triang.
    nodes = np.append(nodes, [[0,0]], axis = 0)
    nodes = np.append(nodes, [[0,self.orig.shape[1]]], axis = 0)
    nodes = np.append(nodes, [[self.orig.shape[0],0]], axis = 0)
    nodes = np.append(nodes, [[self.orig.shape[0], self.orig.shape[1]]], axis = 0)
    return nodes, max_nodes

  # Returns the Delaunay Triangulation of some nodes
  def _create_triangles(self, nodes):
    tri = Delaunay(nodes)
    return tri

  # Generates Low-poly image, given triangle vertices
  # plot-bool determines whether to plot the image within this function
  # triangles is a data structure containing information about the triangles to/
  # /be plotted in an image
  # nodes is an array of selected points that will be vertices of the triangles
  def gen_low_poly(self, nodes, triangles, plot_bool):
    width = self.orig.shape[0]
    height = self.orig.shape[1]
    nodes = np.array(nodes)
    img_triangles = np.full((width+1,height+1,3), 0, dtype = np.uint8)
    rgb = (0,0,0)

    # Plots each triangle and colors them in
    for triangle in triangles.simplices:
      triangle_coords = np.array([ [nodes[triangle[i]][1], nodes[triangle[i]][0]] for i in range(3)])
      cv.polylines(img_triangles,[triangle_coords], True, (0,255,1))

      # Color of triangle is based on average color values of selected coords/
      # /in original image
      centroid = np.sum(triangle_coords,axis = 0)//3 - 1
      rgb = self.orig[centroid[1]][centroid[0]]
      rgb = tuple([int(x) for x in rgb])
      cv.fillPoly(img_triangles, [triangle_coords], rgb)
    # If plot_bool is true, the image is plotted
    if plot_bool:
        cv.imshow("Nodes", img_triangles)
        cv.waitKey(0)
        cv.destroyAllWindows()
    return img_triangles

  # Returns the low poly image
  def plot_nodes(self, plot_bool):
    pp_img = self._preprocess(self.orig)
    nodes, max_nodes = self._get_nodes(pp_img)
    triangles = self._create_triangles(nodes)

    return self.gen_low_poly(nodes,triangles, plot_bool), max_nodes

  # Returns the pre-processed image
  def get_low_poly(self):
    pp_img = self._preprocess(self.orig)
    return pp_img

  # Plots the pre-processed image
  def show_low_poly(self):
    cv.imshow("Low Poly image", self.get_low_poly())
    cv.waitKey(0)
