# Edge Deployment (Jetson Nano/Xavier NX)

Real-time arrow detection and analysis on NVIDIA Jetson devices.

## Hardware Requirements

### Minimum (Entry Level)
- **Jetson Nano 4GB** - $99
- **240 fps camera** (e.g., GoPro HERO)
- **LED light** (optional)
- **Power supply** (5V 4A)

### Recommended (Professional)
- **Jetson Xavier NX** - $399
- **480-1000 fps camera** (e.g., Chronos, Edgertronic)
- **LED lighting system**
- **Power supply** (9-20V)

### Optimal (Research/Commercial)
- **Jetson Orin Nano/NX**
- **1000+ fps camera**
- **Professional lighting**

## Software Setup

### 1. Flash JetPack

Download and flash JetPack 5.1.2:
- Using NVIDIA SDK Manager, or
- Using SD card image

### 2. Install Dependencies

```bash
# Update system
sudo apt-get update
sudo apt-get upgrade

# Install OpenCV with CUDA support
sudo apt-get install libopencv-dev

# Install PyTorch for Jetson
wget https://nvidia.box.com/shared/static/...torch-2.0.0-cp38-cp38-linux_aarch64.whl
pip3 install torch-*.whl

# Install ultralytics (YOLO v8)
pip3 install ultralytics

# Install project requirements
cd arrow-tuning-system/edge
pip3 install -r requirements-jetson.txt
```

### 3. Model Optimization

Convert ONNX models to TensorRT for maximum performance:

```bash
# Arrow detector
python3 scripts/optimize_model.py \
  --onnx ../ml-models/arrow-detection/arrow_detector.onnx \
  --output models/arrow_detector_fp16.trt \
  --precision fp16 \
  --workspace 2048

# Tear classifier
python3 scripts/optimize_model.py \
  --onnx ../ml-models/tear-classifier/tear_classifier.onnx \
  --output models/tear_classifier_fp16.trt \
  --precision fp16 \
  --workspace 1024
```

## Camera Setup

### Supported Cameras

1. **USB Cameras**
   - Logitech C920/C922 (60-120 fps)
   - Microsoft LifeCam Studio (60 fps)

2. **MIPI CSI Cameras**
   - Raspberry Pi Camera v2 (90 fps)
   - IMX219 sensor (up to 240 fps)

3. **High-Speed Cameras**
   - GoPro HERO (240 fps via USB)
   - Chronos 1.4 (1000+ fps via Ethernet)
   - Edgertronic SC series (professional)

### Test Camera

```bash
# Test USB camera
python3 test_camera.py --device /dev/video0 --fps 240

# Test CSI camera
python3 test_camera.py --device csi://0 --fps 240

# Test network camera
python3 test_camera.py --device rtsp://192.168.1.100:8554/stream
```

## Running Inference

### Real-Time Mode

```bash
python3 inference/run_realtime.py \
  --camera-id 0 \
  --fps 240 \
  --detector models/arrow_detector_fp16.trt \
  --classifier models/tear_classifier_fp16.trt \
  --display  # Show visualization window
```

### Video Processing Mode

```bash
python3 inference/process_video.py \
  --input shot001.mp4 \
  --output results/ \
  --detector models/arrow_detector_fp16.trt \
  --classifier models/tear_classifier_fp16.trt
```

### API Server Mode

```bash
# Start REST API server
python3 inference/server.py \
  --host 0.0.0.0 \
  --port 5000 \
  --detector models/arrow_detector_fp16.trt
```

Then access via:
```bash
curl -X POST http://jetson-ip:5000/analyze \
  -F "video=@shot001.mp4"
```

## Performance Optimization

### TensorRT Precision Modes

- **FP32** - Full precision, slowest, highest accuracy
- **FP16** - Half precision, 2x faster, 99% accuracy
- **INT8** - 8-bit precision, 4x faster, 95% accuracy (requires calibration)

### Benchmarks (Jetson Xavier NX)

| Model | Precision | Latency | FPS |
|-------|-----------|---------|-----|
| Arrow Detector | FP32 | 25ms | 40 |
| Arrow Detector | FP16 | 8ms | 125 |
| Tear Classifier | FP32 | 15ms | 66 |
| Tear Classifier | FP16 | 5ms | 200 |
| **Full Pipeline** | FP16 | **45ms** | **22** |

### Memory Usage

- Models loaded: ~500 MB
- Per-frame buffer: ~10 MB
- Total RAM usage: ~1.5 GB

## Hardware Integration

### LED Control

```python
# control_leds.py
import RPi.GPIO as GPIO

LED_PIN = 18  # GPIO pin for LED control

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

# Turn on LEDs
GPIO.output(LED_PIN, GPIO.HIGH)

# Turn off LEDs
GPIO.output(LED_PIN, GPIO.LOW)
```

### Trigger System

```python
# trigger_capture.py
import RPi.GPIO as GPIO

TRIGGER_PIN = 23  # GPIO pin for external trigger

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIGGER_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Wait for trigger
GPIO.wait_for_edge(TRIGGER_PIN, GPIO.FALLING)
print("Triggered! Starting capture...")
```

## Power Management

### Power Modes (Jetson Xavier NX)

```bash
# Maximum performance
sudo nvpmodel -m 0
sudo jetson_clocks

# Balanced mode
sudo nvpmodel -m 2

# Power-save mode
sudo nvpmodel -m 6
```

### Monitor Power and Temperature

```bash
# Install monitoring tools
sudo pip3 install jetson-stats

# Monitor in real-time
jtop
```

## Troubleshooting

### Camera Not Detected

```bash
# List video devices
v4l2-ctl --list-devices

# Test camera directly
gst-launch-1.0 v4l2src device=/dev/video0 ! xvimagesink
```

### Low FPS

1. Check power mode: `sudo nvpmodel -q`
2. Enable jetson_clocks: `sudo jetson_clocks`
3. Use TensorRT FP16 models
4. Reduce camera resolution

### Out of Memory

1. Close other applications
2. Use smaller batch sizes
3. Use INT8 precision
4. Add swap space

## Remote Access

### Setup SSH

```bash
# Enable SSH
sudo systemctl enable ssh
sudo systemctl start ssh

# Find IP address
hostname -I
```

### VNC for GUI

```bash
# Install VNC server
sudo apt-get install vino

# Enable VNC
gsettings set org.gnome.Vino enabled true
```

## Production Deployment

### Systemd Service

Create `/etc/systemd/system/ats-inference.service`:

```ini
[Unit]
Description=Arrow Tuning System Inference Service
After=network.target

[Service]
Type=simple
User=jetson
WorkingDirectory=/home/jetson/arrow-tuning-system/edge
ExecStart=/usr/bin/python3 inference/server.py
Restart=always

[Install]
WantedBy=multi-user.target
```

Enable and start:
```bash
sudo systemctl enable ats-inference
sudo systemctl start ats-inference
```

## Safety and Best Practices

1. **Always** use protective housing for Jetson in archery environment
2. **Mount securely** to prevent vibration during shooting
3. **Protect** camera lens with transparent shield
4. **Ground** all electrical components properly
5. **Test** thoroughly before live use

## Support

For issues specific to Jetson deployment:
- NVIDIA Developer Forums
- Jetson Community Discord
- Project GitHub Issues

