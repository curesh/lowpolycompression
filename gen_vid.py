import sys
from poly_img import PolyImg
import cv2 as cv
import glob
import time
import filetype

start_time = time.time()
arg_type = filetype.guess(sys.argv[1])
if arg_type.find('image'):
  image = cv.imread(sys.argv[1])
  img = PolyImg(image, blur=4, rate=0.8)
  img.plot_nodes(True)

elif arg_type.find('video'):
  img_array = []
  vidcap = cv.VideoCapture(sys.argv[1])
  success,image = vidcap.read()
  print("Frame dimensions: ", image.shape)
  avg_max_nodes = 0
  nframes = 0
  while success:
    height, width, layers = image.shape
    size = (width,height)
    image = PolyImg(image, blur = 4, rate = 0.8)
    poly_image, max_nodes = image.plot_nodes(False)
    img_array.append(poly_image)
    success,image = vidcap.read()
    avg_max_nodes += max_nodes
    nframes += 1
  out = cv.VideoWriter('poly_vid_' + str(sys.argv[1])[0:-4] + '.avi',cv.VideoWriter_fourcc(*'DIVX'), 15, size)

  for i in range(len(img_array)):
    out.write(img_array[i])
  out.release()

else:
    print("Error, incorrect file type. Please supply an image or a video.")
    sys.exit()
    
print("Total time elapsed: ", time.time()-start_time)
print("Average Max Nodes: ", avg_max_nodes/nframes)
