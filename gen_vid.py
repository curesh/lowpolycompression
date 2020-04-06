import sys
from poly_img import PolyImg
import cv2 as cv
import time
import filetype
import numpy as np

start_time = time.time()
arg_type = str(filetype.guess(sys.argv[1]))
if arg_type.find('image')+1:
  image = cv.imread(sys.argv[1])

  # Optionally include node_factor as a param to increase or decrease number of img_triangles
  # Higher node_factor means more triangles (Default: 1)
  img = PolyImg(image, blur=4, rate=0.8)
  poly_img_real, max_nodes = img.plot_nodes(False)
  print("Max-nodes: ", max_nodes)
  # cv.imwrite(('poly_img_' + str(sys.argv[1])[0:-4] + '.jpg'), np.float32(poly_img_real))
  cv.imwrite(('poly_img_sample.jpg'), np.float32(poly_img_real))

elif arg_type.find('video')+1:
  img_array = []
  vidcap = cv.VideoCapture(sys.argv[1])
  success,image = vidcap.read()
  print("Frame dimensions: ", image.shape)
  avg_max_nodes = 0
  nframes = 0
  while success:
    height, width, layers = image.shape
    size = (width,height)

    # Optionally include node_factor as a param to increase or decrease number of img_triangles
    # Higher node_factor means more triangles (Default: 1)
    image = PolyImg(image, blur = 4, rate = 0.8)
    poly_image, max_nodes = image.plot_nodes(False)
    img_array.append(poly_image)
    success,image = vidcap.read()
    avg_max_nodes += max_nodes
    nframes += 1
  # out = cv.VideoWriter('poly_vid_' + str(sys.argv[1])[0:-4] + '.avi',cv.VideoWriter_fourcc(*'DIVX'), 15, size)
  out = cv.VideoWriter('poly_vid_sample.mp4',cv.VideoWriter_fourcc(*'DIVX'), 15, size)

  for i in range(len(img_array)):
    out.write(img_array[i])
  out.release()
  print("Average Max Nodes: ", avg_max_nodes/nframes)
else:
    print("Error, incorrect file type. Please supply an image or a video.")
    sys.exit()

print("Total time elapsed: ", time.time()-start_time)
