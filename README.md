# Webcam Motion Detection Alert System

A Python-based security system that uses your computer's webcam to detect motion and send email alerts with captured images when movement is detected.

## Features

- Real-time motion detection using webcam
- Automatic email notifications with captured images
- Configurable motion sensitivity
- Clean and efficient image management
- Multi-threaded processing for better performance

## Requirements

- Python 3.x
- OpenCV (cv2)
- SMTP access for email functionality

## Installation

1. Clone the repository:
```bash
git clone https://github.com/AhmadTawil1/webcam-alert.git
cd webcam-alert
```

2. Install the required packages:
```bash
pip install opencv-python
```

3. Configure email settings:
   - Open `emailing.py`
   - Update the following variables with your email credentials:
     - `PASSWORD`: Your email app password
     - `SENDER`: Your email address
     - `RECEIVER`: Recipient email address

## Usage

1. Run the main script:
```bash
python main.py
```

2. The program will:
   - Start your webcam
   - Begin monitoring for motion
   - Send email alerts when motion is detected
   - Save captured images in the `images` directory

3. Press 'q' to quit the program

## How It Works

The system uses computer vision techniques to:
1. Capture video from the webcam
2. Convert frames to grayscale and apply Gaussian blur
3. Compare consecutive frames to detect motion
4. When significant motion is detected:
   - Capture and save the image
   - Send an email notification with the image attached
   - Clean up old images

## Security Note

- The system uses Gmail's SMTP server for sending emails
- Make sure to use an app password instead of your main email password
- Keep your email credentials secure and never share them

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is open source and available under the MIT License. 