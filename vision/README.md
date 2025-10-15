# Computer Vision Pipeline for Arrow Tuning

This module contains the core computer vision algorithms for arrow flight analysis and tuning.

## Modules

### 1. Detection (`detection/`)
Arrow detection using YOLO v8

- `arrow_detector.py` - YOLO-based arrow detection
- `model_loader.py` - Load and cache models
- `preprocess.py` - Image preprocessing

### 2. Tracking (`tracking/`)
Arrow tracking and pose estimation

- `trajectory_tracker.py` - Track arrow across frames
- `pose_estimator.py` - Estimate arrow orientation
- `kalman_filter.py` - Smooth tracking with Kalman filter

### 3. Analysis (`analysis/`)
Arrow flight dynamics analysis

- `oscillation_analyzer.py` - Measure shaft oscillation
- `trajectory_analyzer.py` - Analyze flight path
- `velocity_calculator.py` - Calculate arrow velocity

### 4. Classification (`classification/`)
Tear pattern classification

- `tear_classifier.py` - CNN-based tear classification
- `pattern_matcher.py` - Template matching for tears
- `confidence_scorer.py` - Classification confidence

### 5. Recommendation (`recommendation/`)
Tuning recommendation engine

- `tuning_advisor.py` - Generate tuning recommendations
- `rule_engine.py` - Expert system rules
- `adjustment_calculator.py` - Calculate precise adjustments

## Usage

```python
from vision import ArrowTuningPipeline

# Initialize pipeline
pipeline = ArrowTuningPipeline(
    detector_model="models/arrow_detector.onnx",
    classifier_model="models/tear_classifier.onnx"
)

# Process video
results = pipeline.process_video("shot001.mp4")

print(f"Tear Type: {results['tear_type']}")
print(f"Recommendations: {results['recommendations']}")
```

