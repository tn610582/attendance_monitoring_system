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

 ### Comparsions CN

|               | 优势    | 劣势 |
| ------------- | ------------- | ------------- |
| Harr cascade  | 速度最快，轻量（～400kb），适合小算力设备 | 准确度低，偶尔误报，无旋转不变性 |
| Hog + Dlib    | 比Harr准确率高 | 速度小于Harr，更大计算量，无旋转不变性，Dlib兼容问题 |
| SSD(opencv DNN) | 准确率高, deep learning, 模型正常大小(~10mb) | 准确度对光照有要求，肤色影响准确率 |
| CNN(MMOD Dlib) | 最准确，误报率低，模型小（~1mb）| 速度慢，计算量大，Dlib兼容问题 |