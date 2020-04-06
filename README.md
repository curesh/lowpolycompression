# lowpolycompression
This is an investigative work that sees if converting all the frames in a video into low poly frames improves compression in native H.264. An extension to this will create a custom encoding algorithm that compresses low poly frames and benchmarks that against the native H.264 compression.

## Samples

### "The Great Wave off Kanagawa" by Hokusai
<img src="/demo/waves.jpg" width = "600">

### Low Poly Compression of "The Great Wave off Kanagawa" (1191 Nodes)
<img src = "/demo/lowpolywaves.jpg" width = "600">

## How to use

1. Clone git repository

### Install relavent libraries
`pip3 install -r requirements.txt`

### Converting media to poly art

Run the following command on terminal, in the same folder as the python scripts
  `python3 gen_vid.py [INSERT_IMAGE_OR_VIDEO_FILE_HERE]`
  
## Notes

If you want to increase the number of nodes (triangles) in the frame
