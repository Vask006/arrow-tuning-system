# Quick Start Guide - Arrow Tuning System

Get up and running with arrow flight analysis in 5 minutes!

## 🎯 What You'll Do

1. Record a slow-motion video of an arrow shot through paper
2. Run the analysis software
3. Get instant tuning recommendations

## 📹 Step 1: Record Your Shot

### Equipment Needed:
- Smartphone with slow-motion camera (240 fps minimum)
- Paper tuning setup (large paper sheet at 6-10 feet)
- Good lighting (daylight or bright LED)

### Recording Tips:
```
✓ DO:
  - Use 240 fps or higher
  - Keep camera stable (use tripod)
  - Frame arrow flight and paper impact
  - Ensure good lighting
  - Record from the side

✗ DON'T:
  - Use normal speed video (30/60 fps)
  - Record in dim lighting
  - Shake the camera
  - Block the view
```

### Ideal Setup:
```
        📹 Camera
         |
         v
    Shooter → → → → → 📄 Paper
    (You)       6-10 ft
    
Side view, captures:
- Arrow leaving bow
- Arrow in flight
- Arrow hitting paper
```

## 💻 Step 2: Install Software

### Option A: Use Pre-built Docker Image (Easiest)

```bash
# Download and run
docker pull vask006/arrow-tuning-system:latest
docker run -v $(pwd):/videos vask006/arrow-tuning-system analyze /videos/your-shot.mp4
```

### Option B: Install Locally

```bash
# Clone repository
git clone https://github.com/Vask006/arrow-tuning-system.git
cd arrow-tuning-system

# Install Python dependencies
pip install -r requirements.txt

# Run analysis
python examples/analyze_shot.py your-shot.mp4
```

### Option C: Use Mobile App (Coming Soon)

Download ATS app from:
- iOS App Store
- Google Play Store

## 🔍 Step 3: Analyze Your Shot

### Using Command Line:

```bash
python examples/analyze_shot.py my-shot-001.mp4
```

### Expected Output:

```
============================================================
Arrow Tuning System - Shot Analysis
============================================================

Processing video: my-shot-001.mp4
✓ Detected arrow in 127 frames
✓ Trajectory analyzed
✓ Tear pattern classified

============================================================
ANALYSIS RESULTS
============================================================

Tear Type: HIGH
Confidence: 94.2%

Measurements:
  Arrow Velocity: 287.3 fps
  Oscillation: 3.4°
  Entry Angle: 12.5°

Tuning Recommendations:
  1. Lower nocking point by 1/16 inch
  2. Check top cam timing
  3. Verify d-loop length

Trajectory Points: 127 frames

============================================================

What This Means:

↑ High Tear Detected
  Your nocking point is too high.
  Action: Lower nocking point by 1/16 inch and retest.

============================================================
```

## 🎯 Step 4: Make Adjustments

### Understanding Tear Types:

```
Perfect Tear: ⭕
- Round hole
- Arrow is tuned correctly
→ No changes needed!

High Tear: ⭕↑
- Tear above center
- Nocking point too high
→ Lower nocking point 1/16"

Low Tear: ⭕↓
- Tear below center
- Nocking point too low
→ Raise nocking point 1/16"

Left Tear: ⭕←
- Tear to the left
- Weak spine or rest issue
→ Move rest right or use stiffer arrows

Right Tear: ⭕→
- Tear to the right
- Stiff spine or rest issue
→ Move rest left or use weaker arrows
```

### Making Adjustments:

1. **Make ONE change at a time**
2. **Re-test after each change**
3. **Keep notes of what you changed**
4. **Be patient - tuning takes time**

### Example Tuning Session:

```
Shot 1: High tear detected
Action: Lowered nocking point 1/16"

Shot 2: Still high, but better
Action: Lowered another 1/16"

Shot 3: Perfect tear!
Success: ✓ Arrow is now tuned
```

## 📊 Step 5: Track Your Progress

The system saves all your shots automatically:

```bash
# View your shot history
python examples/view_history.py

# Compare two shots
python examples/compare_shots.py shot-001.mp4 shot-010.mp4
```

## 🚀 Advanced Usage

### Jetson Edge Device

For real-time analysis at the range:

```bash
# On Jetson Nano/Xavier
cd edge
python inference/run_realtime.py --camera-id 0 --fps 240
```

### Mobile App Integration

Connect mobile app to your Jetson device:
1. Find Jetson IP: `hostname -I`
2. Open mobile app
3. Settings → Connect to Edge Device
4. Enter IP address
5. Start shooting!

### Cloud Backup

Upload sessions to cloud:

```bash
python examples/upload_session.py shot-001.mp4 --cloud
```

## 📖 Common Issues

### "No arrow detected"
- Check video quality
- Ensure good lighting
- Verify camera angle
- Use higher frame rate

### "Low confidence score"
- Improve lighting
- Keep camera steady
- Ensure arrow is in frame
- Check focus

### "Inconsistent results"
- Stabilize camera
- Use consistent lighting
- Same shooting distance
- Warm up before testing

## 💡 Pro Tips

1. **Lighting is Critical**
   - Shoot outdoors in daylight, or
   - Use bright LED lights indoors

2. **Camera Position**
   - Side view is best
   - 90° to arrow flight path
   - 6-8 feet from paper

3. **Multiple Shots**
   - Take 3-5 shots
   - System can average results
   - More data = better tuning

4. **Save Your Videos**
   - Keep before/after videos
   - Track your progress
   - Learn from patterns

## 🆘 Getting Help

- **Documentation**: `/docs` directory
- **Examples**: `/examples` directory
- **Issues**: GitHub Issues
- **Community**: Discord (link in README)

## 🎓 Next Steps

1. ✅ Analyze first shot
2. ✅ Make tuning adjustment
3. ✅ Re-test and compare
4. ✅ Achieve perfect tear
5. ✅ Share your success!

---

**Happy Tuning! May all your tears be perfect! 🏹**

