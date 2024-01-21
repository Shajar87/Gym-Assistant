# Gym Assistant: Curls Count Tracker

## Overview

The Gym Assistant project is designed to assist individuals during their workout sessions, specifically focusing on tracking the number of curls performed by a person. Leveraging the power of Mediapipe Pose Detection and OpenCV, this project provides a real-time solution for monitoring and counting curls with accuracy.

## Key Features

- **Mediapipe Pose Detection:** Utilizes the Mediapipe library's pre-trained pose detection model to accurately identify key landmarks on the human body, crucial for tracking curl movements.

- **Real-Time Curls Count:** The assistant provides a real-time display of the number of curls performed, allowing users to track their progress during workout sessions.

- **OpenCV Integration:** OpenCV is seamlessly integrated to handle video input, process frames, and overlay visual cues on the video feed.

- **User-Friendly Interface:** The project aims for simplicity, with an easy-to-understand interface that displays the live video feed, the count of curls, and the correctness of the curl using a container which displays the percentage of the up and down movement.

## How It Works

1. **Pose Detection:** The assistant detects the pose of the user, identifying key body landmarks such as shoulders, elbows, and wrists using a pre-trained model by MediaPipe.

2. **Curl Tracking:** By analyzing the movement of the detected landmarks, the system determines when a curl is initiated and completed.

3. **Real-Time Display:** The live video feed is augmented with overlays, showcasing the count of curls and the correctness of the curl using precnetage container.

## Getting Started

1. **Installation:** Clone the repository and install the required dependencies using requirements.txt file.

2. **Run the Assistant:** Execute the script to start the Gym Assistant and begin tracking curls during your workout.

3. **Customization:** Feel free to customize and extend the project based on your preferences and requirements.

## Contributions

Contributions to enhance the project are welcome! If you have ideas for improvements, bug fixes, or new features, please fork the repository, create a new branch, and submit a pull request.
