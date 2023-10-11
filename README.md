# AI Project - *Hand Gesture Recognition*

Group members: **Quang Dang, Katsuki Oike**

## Overview
After working together, we decided that our project would be **Hand Gesture Recognition**, a combination of the two previous ideas: Headball and Air Canvas. We will dive deeper into how machines can learn to recognize hand gestures, with the aim of implementing this technology to play some simple games. 

## Milestones

- [ ] **Understand the process behind hand tracking**
- [ ] **Implement Hand Gesture Recognition into an application**

## MediaPipe's Machine Learning Pipeline for Hand Gesture Recognition
Machine Learning Pipeline for Hand Gesture Recognition is a cross-platform, open-source pipeline that can be used to detect and recognize hand gestures in real time. According to our group's research, it is a multi-stage pipeline that consists of the following steps:
- [Preprocessing](#Preprocessing)
- [Hand detection](#Hand-detection)
- [Hand landmark detection](#Hand-landmark-detection)
- [Gesture recognition](#Gesture-recognition)

<center>
  <figure>
      <img src="https://1.bp.blogspot.com/-jy9hueRc-5I/XVrS-xDKR7I/AAAAAAAAEhY/2pA9c6rzMwchn5UUAAK69or9j4dKA_AiwCLcBGAs/s640/image1.png"
           alt="pipeline overview">
      <center><figcaption>An overview of the hand perception pipeline.</figcaption></center>
  </figure>
</center>

### Preprocessing
When given thousands of images, the first thing to do is to preprocess all the images. We want to make sure that the input image is in a format that is suitable for the subsequent steps in the pipeline. The preprocessing part may consist of the following steps:
- **Resizing the image**: The input image would be resized to a specific size. This is because the hand detection and hand landmark detection models in the pipeline are trained on images of a specific size.

- **Normalizing the pixel values**: The images' pixel values would be normalized to improve the performance of the hand detection and hand landmark detection models. Pixel normalization involves scaling the pixel values to a specific range. This is done to _reduce the impact of variations in lighting and other factors_ on the performance of the models.

- **Converting the image to grayscale**: The input image may be converted to grayscale. This is because the hand detection and hand landmark detection models in the pipeline are _typically trained on grayscale images_. Grayscale images are easier for the models to process and can improve the accuracy of the results.
Besides the above steps, the preprocessing step may also involve other steps, such as _denoising the image_ and _removing unwanted objects_from the image.

### Hand detection
### Hand landmark detection
### Gesture recognition


## References
**Custom Hand Gesture Recognition with Hand Landmarks Using Google’s Mediapipe + OpenCV in Python**

https://youtu.be/a99p_fAr6e4

**Advanced Computer Vision with Python - Full Course** 

https://youtu.be/01sAkU_NvOY

**OpenCV**

https://opencv.org/

**On-Device, Real-Time Hand Tracking with MediaPipe**

https://blog.research.google/2019/08/on-device-real-time-hand-tracking-with.html

**Official MediaPipe Documentation**

https://developers.google.com/mediapipe
