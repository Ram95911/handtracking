# handtracking
2. A window will open showing the webcam feed with hand tracking overlay.
3. Place your hand in front of the camera to see the tracking in action.

## How it works

- The script captures video from the default webcam.
- Each frame is converted to RGB color space for MediaPipe processing.
- MediaPipe's hand detection model processes the frame to detect hands.
- If hands are detected, landmarks are drawn on the image.
- The FPS is calculated and displayed on the screen.

## Customization

- You can modify the visualization settings (colors, sizes) in the code.
- Adjust the `hands` object parameters for different detection confidence levels.

## License

This project is open-source and available under the MIT License.

## Acknowledgments

##This project uses the MediaPipe library developed by Google.
pip install -r requirements.txt
