# iCare

iCare is a python application which makes use of your webcam in order to detect the emotion on your face. iCare uses modules from [MediaPipe](https://google.github.io/mediapipe/) and [OpenCV](https://opencv.org/). Detection of emotions is done mathematically by calculating  difference between various specific points for each emotion.

<img src="./docs/logo/logo_transparent.png" style="height:300px; width:auto" alt="logo" /> 


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install OpenCV and MediaPipe.

```bash
pip install opencv-python
pip install mediapipe
```

## Documentation

Please access the <a src="https://waasiq.github.io/icare/" >documentation</a> at the link.

## Usage
Run the iCareProject\emotions.py for starting the detection.
Individual modules can also be run using the specific module name.

## Future Plans

<ul>
<li>The project was coded in basic OpenCV and Mediapipe without any deep learning libraries.</li>
<li>Future implementation would be to add a Deep Learning module which would be able to detect the emotion using a pre-trained model.</li>
</ul>

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.