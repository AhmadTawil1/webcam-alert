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
- python-dotenv (for environment variables)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/AhmadTawil1/webcam-alert.git
cd webcam-alert
```

2. Install the required packages:
```bash
pip install opencv-python python-dotenv
```

3. Configure email settings:
   - Create a new file named `.env` in the project root directory
   - Add the following variables to the `.env` file:
     ```
     EMAIL_PASSWORD=your_email_app_password
     EMAIL_SENDER=your_email@gmail.com
     EMAIL_RECEIVER=recipient_email@gmail.com
     ```
   - Replace the values with your actual email credentials
   - Make sure to use an app password for Gmail (not your regular password)
   - Never commit the `.env` file to version control

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
- Email credentials are stored in environment variables for security
- Make sure to use an app password instead of your main email password
- Keep your `.env` file secure and never share it
- The `.env` file is already in `.gitignore` to prevent accidental commits

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is open source and available under the MIT License. 