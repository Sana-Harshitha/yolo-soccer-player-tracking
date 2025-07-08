# Soccer Player Re-Identification in Single Video Feed

This project solves the problem of identifying and re-identifying soccer players in a single video. The goal is to assign consistent IDs to players, even if they go out of frame and reappear later. This is part of the DeepThought AI Internship assignment (Option 2).

## Objective

- Detect players in a soccer match video using a pre-trained YOLOv5 model.
- Assign a unique ID to each player.
- Maintain the same ID for players who leave and re-enter the frame.
- Output an annotated video with bounding boxes and IDs.

## Approach

- Use a fine-tuned YOLOv5 model trained on soccer footage.
- Perform frame-by-frame detection and ID assignment.
- Basic heuristic-based tracking is used for maintaining identity across frames.

## Project Structure

```
soccer-reid/
├── model/         # Place YOLOv5 model file here (e.g., soccer_yolov5_custom.pt)
├── video/         # Place input video here (e.g., 15sec_input_720p.mp4)
├── output/        # Output video will be saved here
├── detect.py      # Main detection and ID assignment script
├── test_detect.py # Optional test script for modular functions
├── requirements.txt
└── README.md
```

## Setup

1. Clone the repository:

```
git clone https://github.com/Sana-Harshitha/yolo-soccer-player-tracking.git
cd yolo-soccer-player-tracking
```

2. Create and activate a virtual environment:

```
python -m venv reid-env
reid-env\Scripts\activate         # On Windows
# or
source reid-env/bin/activate     # On Linux/Mac
```

3. Install dependencies:

```
pip install -r requirements.txt
```

## Required Files

- Download the trained YOLOv5 model from this link:  
  https://drive.google.com/file/d/1-5fOSHOSB9UXp_enOoZNAMScrePVcMD/view  
  Place it inside the `model/` folder.

- Download the input video from the assignment folder:  
  https://drive.google.com/drive/folders/1Nx6qH_n0UNUi6L-6i8WknX4dCv2c3VjTZP  
  Place it inside the `video/` folder.

## Running the Code

Once the model and video are placed correctly, run:

```
python detect.py
```

The output video with player boxes and consistent IDs will be saved in the `output/` folder.

## Notes

- This project is built for the single-feed player re-identification task.
- The folders `model/`, `video/`, and `output/` are kept empty in the repository. Add your own files for testing.
- The project is modular and can be extended further using Deep SORT or embedding-based tracking in the future.

## Author

Developed by Sana Harshitha 
