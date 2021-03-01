# Image-based sports detection with Deep Learning
## AIT Deep Learning Project Work

The main goal of this project is the classification of sports images with a deep
learning approach. The solution identifies, which sport appears on a given
picture. There are currently different sports supported, like volleyball,
badminton and chess. However, the range of supported sports is freely expandable.

### Team members
- Nóra Almási ([almasinori@gmail.com](mailto:almasinori@gmail.com))
- Barnabás Börcsök ([barnabas.borcsok@gmail.com](mailto:barnabas.borcsok@gmail.com))

## Data Loading
```
python3 sport-detection.py
```

## Dataset

- ~14000 pictures
- 22 labels
- actual image size varies
- image size read into opencv: 64x64, inter cubic interpolation

## Currently supported sports:

- badminton
- baseball
- basketball
- boxing
- chess
- cricket
- fencing
- football
- formula1
- gymnastics
- hockey
- ice hockey
- kabaddi
- motogp
- shooting
- swimming
- table tennis
- tennis
- volleyball
- weight lifting
- wrestling
- wwe

## Dependencies

```
pip3 install tensorflow-gpu
pip3 install tensorflow
pip3 install matplotlib
pip3 install pandas
pip3 install numpy
pip3 install seaborn
```
