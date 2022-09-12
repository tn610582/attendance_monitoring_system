# attendance_monitoring_system
Deep Learning based Attendance Monitoring System

## Face detection

### Haar features
Resource: 
 - https://medium.com/analytics-vidhya/what-is-haar-features-used-in-face-detection-a7e531c8332b
 - https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html
In short: 
 - Calculate dark pixal average
 - Calculate white pixal average
 - Calculate average delta
 
 ### Comparsions

|               | Advantages    | Disadvantages |
| ------------- | ------------- | ------------- |
| Harr cascade  | Fastest,light weight(~400KB), low computation power | Low accuracy, high false positive, face can't be rotated |
| Hog + Dlib    | More accurate than Haar | Slower than haar, more calculation, face can't be rotated |
| SSD(opencv DNN) | Better than Haar and hog, deep learning, average model size(~10mb) | Low accurace in dark environment, skin tone affect accuracy |
| CNN(MMOD Dlib) | Best accuracy, low false positive, light weight(~1mb)  | Low detection speed, high calculation cost |