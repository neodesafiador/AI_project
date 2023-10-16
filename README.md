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
When given thousands of images, the first thing we need to do is preprocess all the images. We want to make sure that the input image is in a format that is suitable for the subsequent steps in the pipeline. The preprocessing part may consist of the following steps:
- **Resizing the image**: The input image would be resized to a specific size. This is because the hand detection and hand landmark detection models in the pipeline are trained on images of a specific size.

- **Normalizing the pixel values**: The images' pixel values would be normalized to improve the performance of the hand detection and hand landmark detection models. Pixel normalization involves scaling the pixel values to a specific range. This is done to _reduce the impact of variations in lighting and other factors_ on the performance of the models.

- **Converting the image to grayscale**: The input image may be converted to grayscale. This is because the hand detection and hand landmark detection models in the pipeline are _typically trained on grayscale images_. Grayscale images are easier for the models to process and can improve the accuracy of the results.
Besides the above steps, the preprocessing step may also involve other steps, such as _denoising the image_ and _removing unwanted objects_ from the image.

### Hand detection
After having our images suitable for processing, the next step is to **detect the presence** of hands in those images. The hand detection part of the pipeline is a machine-learning model that has been trained on a dataset of images that contain hands. It works by first **extracting features** from the input image, such as the shape of the hand, the color of the skin, and the position of the hand in the image. Once the hand detection model has done that, it will use these features to classify the image as **containing a hand** or **not containing a hand**. If the model classifies the image as containing a hand, it will also output **a bounding box** around the hand in the image.

### Hand landmark detection
The hand landmark detection part of the MediaPipe Hand Gesture Recognition pipeline is responsible for **detecting the key points** of the hands in an image. These key points, also known as landmarks, are typically located at the **joints of the fingers** and the** palm of the hand**.
For training purposes, **approximately 30,000 real-world images were utilized**, each annotated with these **distinct hand joint locations**. When images possessed **depth information**, this data was incorporated to **grasp the 3D aspect of the hand**. Additionally, computer-generated images of hands were integrated into the training to ensure a comprehensive understanding of various hand positions and their inherent shapes.

<center>
  <figure>
      <img src="https://1.bp.blogspot.com/-8SxmsK5VoJ0/XVrTpMrJDFI/AAAAAAAAEiM/nAa3vuj8a2sjgEPAeMKXD4m09yKUgjVIQCLcBGAs/s640/Screenshot%2B2019-08-19%2Bat%2B9.51.25%2BAM.png"
           alt="hands with landmarks">
      <center><figcaption>Images of hands with detected landmarks</figcaption></center>
  </figure>
</center>

### Gesture recognition
The Hand Landmark Model, after identifying key points or 'skeleton' of the hand, proceeds to **gesture recognition**. The **angles formed by the joints** are analyzed to determine the state of each finger, whether it's bent or straight. Using this information about the fingers, the model then matches the hand shape to a list of known gestures. According to the Research Engineers at Google, this method is effective in **detecting static gestures** with commendable accuracy. It has been calibrated to recognize counting gestures in various cultural norms, such as American, European, and Chinese. Furthermore, the model is capable of identifying specific hand signs like "Thumb up", closed fist, "OK", "Rock", and "Spiderman".

![Example of recognized hand gestures](https://1.bp.blogspot.com/-xmtORGq9oVQ/XVrTP5nvIDI/AAAAAAAAEh8/d7t_e2WVs5sSo94YsPxEfP3JlaBF1EDSwCLcBGAs/s1600/image10.gif)

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
