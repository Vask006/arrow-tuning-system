# Arrow Tuning System (ATS)

> **Privacy-first, edge-optimized performance tuning and analytics platform**

[![CI](https://github.com/Vask006/arrow-tuning-system/workflows/CI/badge.svg)](https://github.com/Vask006/arrow-tuning-system/actions)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## 🎯 Overview

Arrow Tuning System is a production-grade platform for real-time performance monitoring, computer vision analytics, and edge-optimized ML inference. Built with privacy-first principles, ATS processes data on-device by default and only transmits derived metrics.

## 🚀 Quick Start

```bash
git clone https://github.com/Vask006/arrow-tuning-system.git
cd arrow-tuning-system

# Using Docker Compose (Recommended)
docker-compose -f docker/docker-compose.yml up -d
```

## 📁 Project Structure

- **backend/** - FastAPI + Python 3.11 + async SQLAlchemy
- **frontend/** - Next.js 14 + TypeScript + Tailwind CSS
- **mobile/** - Flutter 3.x + Riverpod
- **ml-models/** - PyTorch 2.x + YOLO + ONNX
- **docker/** - Docker Compose configuration

## 📊 Tech Stack

**Backend**: FastAPI, SQLAlchemy, Pydantic v2, Redis, TimescaleDB  
**Frontend**: Next.js 14, TypeScript, Tailwind, shadcn/ui  
**Mobile**: Flutter, Riverpod, Freezed, GoRouter  
**ML/CV**: PyTorch, Ultralytics YOLO, ONNX Runtime

## 📝 License

MIT License - See LICENSE file

---

**Built with ❤️ for performance enthusiasts and privacy advocates**

