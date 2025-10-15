# Architecture

## Overview

Arrow Tuning System is a privacy-first, edge-optimized platform for performance monitoring.

## Components

### Backend (FastAPI)
- JWT authentication
- Async SQLAlchemy with TimescaleDB
- Redis for caching
- RESTful API

### Frontend (Next.js 14)
- Server-side rendering
- TanStack Query for data fetching
- Tailwind CSS styling
- Real-time dashboards

### Mobile (Flutter)
- Cross-platform iOS/Android
- Riverpod state management
- On-device ML inference
- Offline-first architecture

### ML Models
- YOLO v8 for object detection
- PyTorch training
- ONNX export for deployment
- TensorRT optimization

## Data Flow

1. Mobile device collects metrics
2. On-device processing with ML
3. Derived metrics sent to backend
4. Stored in TimescaleDB
5. Cached in Redis
6. Displayed on dashboard

## Security

- JWT tokens for authentication
- bcrypt for password hashing
- HTTPS/mTLS for communication
- Input validation with Pydantic

## Privacy

- On-device ML inference
- Minimal data transmission
- Configurable retention policies
- GDPR compliance

