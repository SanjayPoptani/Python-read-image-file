# Python-read-image-file
Read an image file using opencv library in python.
Run "pip install opencv-python" in Anaconda Prompt to install opencv library for use

OpenCV (Open Source Computer Vision) is a computer vision library that contains various functions to perform operations on pictures or videos. 
It was originally developed by Intel but was later maintained by Willow Garage and is now maintained by Itseez. 
This library is cross-platform that is it is available on multiple programming languages such as Python, C++ etc.

cv2.waitKey() is a keyboard binding function. Its argument is the time in milliseconds. The function waits for specified milliseconds for any keyboard event.
If you press any key in that time, the program continues. If 0 is passed, it waits indefinitely for a key stroke. It can also be set to detect specific key strokes like, 
if key a is pressed etc which we will discuss below.

cv2.destroyAllWindows() simply destroys all the windows we created. 
If you want to destroy any specific window, use the function cv2.destroyWindow() where you pass the exact window name as the argument.

