# People Count System

## Overview
The People Count System is an advanced computer vision project designed to automatically count the number of people in video footage. Utilizing the YOLOv8 model, the system performs real-time object detection and tracking, making it ideal for integration into security and surveillance systems. This technology can be used in various environments, such as retail stores, public transport hubs, and event venues, to monitor foot traffic, manage crowd control, and gather data for analytical purposes.

Key features include its ability to accurately detect and count individuals in diverse settings, support for various video input formats, and easy integration with existing infrastructure. The system also comes with sample data and pre-trained models to facilitate testing and deployment. Its Python-based implementation ensures flexibility and scalability, making it suitable for both small-scale and large-scale applications.
## Features
- **Real-Time Detection**: Counts people in real-time using YOLOv8.
- **Sample Data**: Includes sample video files and a pre-trained model.

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/berkinozturk/People-Count-System.git
   ```

## Usage

Run the script with the sample video file or your own footage:
   ```bash
   python people_count.py 
   ```

The system will display the video with detected individuals highlighted using rectangles. It also provides the capability to draw custom regions of interest within the video frame. This feature allows you to specify particular areas to monitor for more targeted counting and analysis.


