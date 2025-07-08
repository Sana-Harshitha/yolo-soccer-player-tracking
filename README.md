

```markdown
#  Soccer Player Re-Identification in Single Video Feed

This project tackles the problem of identifying and re-identifying soccer players in a single video. The goal is to assign consistent IDs to players, even if they briefly go out of frame and return, simulating real-time player tracking.

##  Objective
Given a 15-second clip, detect players using a pre-trained YOLOv5 model and assign consistent IDs throughout the video.

##  Approach
- Detect players frame by frame using the provided object detection model.
- Assign unique IDs initially, then maintain them for returning players.
- Save an annotated video with bounding boxes and IDs.

## Project Structure
```

soccer-reid/
├── model/       # (Place downloaded model here)
├── video/       # (Place input video here)
├── output/      # (Output saved here)
├── detect.py
├── test\_detect.py
├── requirements.txt
└── README.md

````

##  Setup
```bash
git clone https://github.com/Sana-Harshitha/yolo-soccer-player-tracking.git
cd yolo-soccer-player-tracking
python -m venv reid-env
reid-env\Scripts\activate   # or source reid-env/bin/activate on Linux/Mac
pip install -r requirements.txt
````

##  Downloads

* Model: [Download YOLOv5 model](https://drive.google.com/file/d/1-5fOSHOSB9UXp_enOoZNAMScrePVcMD/view) → place in `model/`
* Video: [Assignment folder](https://drive.google.com/drive/folders/1Nx6qH_n0UNUi6L-6i8WknX4dCv2c3VjTZP?usp=sharing) → place in `video/`

## Run

```bash
python detect.py
```

Output will be saved in `output/`.

## Note

* `.gitignore` is set to exclude large files (models, videos, outputs).

