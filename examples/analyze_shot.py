"""
Example: Analyze a single arrow shot video

This script demonstrates how to use the Arrow Tuning System
to analyze a high-speed video of an arrow shot and get tuning recommendations.
"""

from vision import ArrowTuningPipeline
import sys


def main():
    """Analyze an arrow shot and print tuning recommendations."""
    
    # Check if video path provided
    if len(sys.argv) < 2:
        print("Usage: python analyze_shot.py <video_path>")
        print("Example: python analyze_shot.py shot001.mp4")
        sys.exit(1)
    
    video_path = sys.argv[1]
    
    print("=" * 60)
    print("Arrow Tuning System - Shot Analysis")
    print("=" * 60)
    print()
    
    # Initialize pipeline
    print("Initializing computer vision pipeline...")
    pipeline = ArrowTuningPipeline(
        confidence_threshold=0.7,
        fps=240  # Adjust to your camera's fps
    )
    print("✓ Pipeline initialized")
    print()
    
    # Process video
    print(f"Processing video: {video_path}")
    print("This may take a few moments...")
    print()
    
    result = pipeline.process_video(video_path)
    
    # Display results
    print("=" * 60)
    print("ANALYSIS RESULTS")
    print("=" * 60)
    print()
    
    print(f"Tear Type: {result.tear_type.upper()}")
    print(f"Confidence: {result.confidence * 100:.1f}%")
    print()
    
    print("Measurements:")
    print(f"  Arrow Velocity: {result.measurements.get('velocity', 0):.1f} px/s")
    print(f"  Oscillation: {result.measurements.get('oscillation_amplitude', 0):.2f}°")
    print(f"  Entry Angle: {result.measurements.get('entry_angle', 0):.1f}°")
    print()
    
    print("Tuning Recommendations:")
    for i, rec in enumerate(result.recommendations, 1):
        print(f"  {i}. {rec}")
    print()
    
    print(f"Trajectory Points: {len(result.trajectory_frames)} frames")
    print()
    
    print("=" * 60)
    
    # Interpret results for user
    print()
    print("What This Means:")
    print()
    
    if result.tear_type == "perfect":
        print("✓ Your arrow is tuned correctly!")
        print("  Continue with your current setup.")
    
    elif result.tear_type == "high":
        print("↑ High Tear Detected")
        print("  Your nocking point is too high.")
        print("  Action: Lower nocking point by 1/16 inch and retest.")
    
    elif result.tear_type == "low":
        print("↓ Low Tear Detected")
        print("  Your nocking point is too low.")
        print("  Action: Raise nocking point by 1/16 inch and retest.")
    
    elif result.tear_type == "left":
        print("← Left Tear Detected")
        print("  Arrow spine may be too weak, or rest needs adjustment.")
        print("  Action: Move rest right slightly or try stiffer arrows.")
    
    elif result.tear_type == "right":
        print("→ Right Tear Detected")
        print("  Arrow spine may be too stiff, or rest needs adjustment.")
        print("  Action: Move rest left slightly or try weaker arrows.")
    
    print()
    print("=" * 60)
    print("Save these recommendations and make ONE adjustment at a time.")
    print("Retest after each change to see the effect.")
    print("=" * 60)


if __name__ == "__main__":
    main()

