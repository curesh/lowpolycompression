# lowpolycompression
This is an investigative work that sees if converting all the frames in a video into low poly frames improves compression in native H.264. An extension to this will create a custom encoding algorithm that compresses low poly frames and benchmarks that against the native H.264 compression.

# How to use

1. Clone git repository

## Install relavent libraries
`pip3 install -r requirements.txt`

## Converting media to poly art

Run the following command on terminal, in the same folder as the python scripts
  `python3 gen_vid.py [INSERT_IMAGE_OR_VIDEO_FILE_HERE]`
  
## Notes

If you want to increase the number of nodes (triangles) in the frame
