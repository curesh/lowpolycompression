# lowpolycompression
This is both an investigative and artistic exercise that converts all the frames in a video into low poly frames and sees if it improves compression in native H.264. An extension to this will create a custom encoding algorithm that compresses low poly frames and benchmarks that against the native H.264 compression.

## Samples

### "The Great Wave off Kanagawa" by Hokusai
<img src="/demo/waves.jpg" width = "600">

### Low Poly Compression of "The Great Wave off Kanagawa" (1191 Nodes)
<img src = "/demo/lowpolywaves.jpg" width = "600">

### Burning match video
Screenshot from low poly version of matches video

<img src = "/demo/match_lowpoly_screenshot.png" width = "600">

### Train going over bridge video
Screenshot from low poly version of trains video

<img src = "/demo/trains_lowpoly_screenshot.png" width = "600">

## Samples in demo folder

Please download the sample videos in the demo folder to see the low poly compression of various media.

They look pretty cool, so you should check it out!

### Sample videos
1. Waves scene from interstellar
2. A burning match
3. A train going over a bridge
### Sample images
4. Great Waves off Kanagawa
5. Soccer ball

## How to use

1. Clone git repository

### Install relavent libraries
`pip3 install -r requirements.txt`

### Converting media to poly art

Run the following command on terminal, in the same folder as the python scripts:

  `python3 gen_vid.py [INSERT_IMAGE_OR_VIDEO_FILE_HERE]`
  
## Notes

If you want to increase the number of nodes (triangles) in the frame, in the gen_vid.py file, in lines 15, 34 decrease the node_factor to a value between 0 and 1. If you want to decrease the number of nodes, increase the node factor. (The default is 1.)

## TODO

1. Improve compression algorithm and utilize the videos polygon composition to optimize video storage and program runtime.

2. Run various tests to measure utility.

## Credit
Loosely adapted and improved upon some algorithms from:

Qian, Crystal J. Generating Low-Poly Abstractions. Princeton University, 2016.
