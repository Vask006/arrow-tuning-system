"""
Main pipeline for arrow flight analysis and tuning recommendations.
"""

import cv2
import numpy as np
from pathlib import Path
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass


@dataclass
class ArrowFrame:
    """Single frame with detected arrow."""
    frame_number: int
    timestamp: float
    bbox: Tuple[int, int, int, int]  # x, y, w, h
    confidence: float
    angle: float  # Arrow orientation in degrees
    center: Tuple[float, float]  # Center point (x, y)


@dataclass
class TuningResult:
    """Result of arrow tuning analysis."""
    tear_type: str  # 'perfect', 'high', 'low', 'left', 'right'
    confidence: float
    recommendations: List[str]
    measurements: Dict[str, float]
    trajectory_frames: List[ArrowFrame]


class ArrowTuningPipeline:
    """
    Complete pipeline for arrow flight analysis and tuning.
    
    This pipeline:
    1. Detects arrows in high-speed video
    2. Tracks arrow trajectory through flight
    3. Measures arrow oscillation and dynamics
    4. Classifies tear pattern at impact
    5. Generates tuning recommendations
    
    Example:
        >>> pipeline = ArrowTuningPipeline()
        >>> result = pipeline.process_video("shot001.mp4")
        >>> print(result.tear_type)
        'high'
        >>> print(result.recommendations)
        ['Lower nocking point by 1/16"', 'Check cam timing']
    """
    
    def __init__(
        self,
        detector_model: Optional[str] = None,
        classifier_model: Optional[str] = None,
        confidence_threshold: float = 0.7,
        fps: int = 240
    ):
        """
        Initialize the arrow tuning pipeline.
        
        Args:
            detector_model: Path to YOLO arrow detection model
            classifier_model: Path to tear pattern classifier
            confidence_threshold: Minimum confidence for detections
            fps: Expected framerate of input video
        """
        self.detector_model = detector_model
        self.classifier_model = classifier_model
        self.confidence_threshold = confidence_threshold
        self.fps = fps
        
        # Will be implemented with actual models
        print(f"Initialized ArrowTuningPipeline (FPS: {fps})")
    
    def process_video(
        self,
        video_path: str,
        start_frame: int = 0,
        end_frame: Optional[int] = None
    ) -> TuningResult:
        """
        Process a video of an arrow shot and return tuning analysis.
        
        Args:
            video_path: Path to video file
            start_frame: Frame to start processing
            end_frame: Frame to end processing (None = until end)
        
        Returns:
            TuningResult with analysis and recommendations
        """
        # Open video
        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            raise ValueError(f"Cannot open video: {video_path}")
        
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        actual_fps = cap.get(cv2.CAP_PROP_FPS)
        
        print(f"Processing video: {Path(video_path).name}")
        print(f"Frames: {total_frames}, FPS: {actual_fps}")
        
        # Process frames
        trajectory_frames: List[ArrowFrame] = []
        frame_num = 0
        
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            
            if frame_num < start_frame:
                frame_num += 1
                continue
            
            if end_frame and frame_num > end_frame:
                break
            
            # Detect arrow in frame
            arrow_detection = self._detect_arrow(frame, frame_num, actual_fps)
            if arrow_detection:
                trajectory_frames.append(arrow_detection)
            
            frame_num += 1
        
        cap.release()
        
        # Analyze trajectory
        measurements = self._analyze_trajectory(trajectory_frames)
        
        # Classify tear pattern (using last few frames)
        tear_type, confidence = self._classify_tear_pattern(trajectory_frames)
        
        # Generate recommendations
        recommendations = self._generate_recommendations(tear_type, measurements)
        
        return TuningResult(
            tear_type=tear_type,
            confidence=confidence,
            recommendations=recommendations,
            measurements=measurements,
            trajectory_frames=trajectory_frames
        )
    
    def _detect_arrow(
        self,
        frame: np.ndarray,
        frame_number: int,
        fps: float
    ) -> Optional[ArrowFrame]:
        """
        Detect arrow in a single frame.
        
        This is a placeholder - actual implementation will use YOLO v8.
        """
        # Placeholder: In real implementation, use YOLO model
        # For now, return None to simulate no detection
        return None
    
    def _analyze_trajectory(
        self,
        trajectory_frames: List[ArrowFrame]
    ) -> Dict[str, float]:
        """
        Analyze arrow trajectory and calculate metrics.
        
        Returns:
            Dictionary with measurements:
            - velocity: Arrow velocity in fps
            - oscillation_amplitude: Maximum shaft flex
            - oscillation_frequency: Oscillation frequency in Hz
            - entry_angle: Angle at paper impact
        """
        if not trajectory_frames:
            return {
                "velocity": 0.0,
                "oscillation_amplitude": 0.0,
                "oscillation_frequency": 0.0,
                "entry_angle": 0.0
            }
        
        # Calculate velocity (simplified)
        if len(trajectory_frames) >= 2:
            first = trajectory_frames[0]
            last = trajectory_frames[-1]
            dx = last.center[0] - first.center[0]
            dy = last.center[1] - first.center[1]
            distance = np.sqrt(dx**2 + dy**2)
            time = (last.timestamp - first.timestamp)
            velocity = distance / time if time > 0 else 0.0
        else:
            velocity = 0.0
        
        # Calculate oscillation (simplified)
        angles = [frame.angle for frame in trajectory_frames]
        oscillation_amplitude = np.std(angles) if angles else 0.0
        
        # Entry angle (last frame)
        entry_angle = trajectory_frames[-1].angle if trajectory_frames else 0.0
        
        return {
            "velocity": velocity,
            "oscillation_amplitude": oscillation_amplitude,
            "oscillation_frequency": 0.0,  # Requires FFT analysis
            "entry_angle": entry_angle
        }
    
    def _classify_tear_pattern(
        self,
        trajectory_frames: List[ArrowFrame]
    ) -> Tuple[str, float]:
        """
        Classify the tear pattern based on arrow trajectory.
        
        Returns:
            Tuple of (tear_type, confidence)
            
        Tear types:
            - 'perfect': Round hole, well-tuned
            - 'high': Tear above center, nock too high
            - 'low': Tear below center, nock too low
            - 'left': Tear to left, weak spine
            - 'right': Tear to right, stiff spine
        """
        # Placeholder: In real implementation, use CNN classifier
        # For now, simple rule-based classification
        
        if not trajectory_frames:
            return "unknown", 0.0
        
        # Use entry angle to determine tear type
        entry_angle = trajectory_frames[-1].angle if trajectory_frames else 0.0
        
        # Simplified classification
        if -5 <= entry_angle <= 5:
            return "perfect", 0.95
        elif entry_angle > 5:
            return "high", 0.85
        elif entry_angle < -5:
            return "low", 0.85
        
        return "perfect", 0.7
    
    def _generate_recommendations(
        self,
        tear_type: str,
        measurements: Dict[str, float]
    ) -> List[str]:
        """
        Generate tuning recommendations based on tear pattern.
        
        Args:
            tear_type: Classified tear type
            measurements: Trajectory measurements
        
        Returns:
            List of actionable tuning recommendations
        """
        recommendations = []
        
        if tear_type == "perfect":
            recommendations.append("✓ Arrow is tuned correctly!")
            recommendations.append("Continue with current setup")
        
        elif tear_type == "high":
            recommendations.append("Lower nocking point by 1/16 inch")
            recommendations.append("Check top cam timing")
            recommendations.append("Verify d-loop length")
        
        elif tear_type == "low":
            recommendations.append("Raise nocking point by 1/16 inch")
            recommendations.append("Check bottom cam timing")
            recommendations.append("Consider stiffer arrow spine")
        
        elif tear_type == "left":
            recommendations.append("Move arrow rest slightly right")
            recommendations.append("Consider stiffer arrow spine")
            recommendations.append("Check centershot alignment")
        
        elif tear_type == "right":
            recommendations.append("Move arrow rest slightly left")
            recommendations.append("Consider weaker arrow spine")
            recommendations.append("Verify cam synchronization")
        
        else:
            recommendations.append("Unable to classify tear pattern")
            recommendations.append("Please retake video with better lighting")
        
        # Add oscillation-based recommendations
        if measurements.get("oscillation_amplitude", 0) > 10.0:
            recommendations.append("High oscillation detected - check arrow spine")
        
        return recommendations


# Convenience function
def analyze_shot(video_path: str, **kwargs) -> TuningResult:
    """
    Convenience function to analyze a single shot.
    
    Args:
        video_path: Path to video file
        **kwargs: Additional arguments for ArrowTuningPipeline
    
    Returns:
        TuningResult with analysis and recommendations
    
    Example:
        >>> result = analyze_shot("my_shot.mp4")
        >>> print(result.tear_type)
        >>> print(result.recommendations)
    """
    pipeline = ArrowTuningPipeline(**kwargs)
    return pipeline.process_video(video_path)

