# Arrow Tuning System (ATS)

> **Privacy-first, edge-optimized performance tuning and analytics platform**

[![CI](https://github.com/Vask006/arrow-tuning-system/workflows/Backend%20CI/badge.svg)](https://github.com/Vask006/arrow-tuning-system/actions)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/)
[![Node](https://img.shields.io/badge/node-20.x-green.svg)](https://nodejs.org/)
[![Flutter](https://img.shields.io/badge/flutter-3.x-blue.svg)](https://flutter.dev/)

## 🎯 Overview

Arrow Tuning System is a production-grade platform for real-time performance monitoring, computer vision analytics, and edge-optimized ML inference. Built with privacy-first principles, ATS processes data on-device by default and only transmits derived metrics.

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     Mobile/Edge Devices                      │
│  (Flutter + On-device YOLO/PyTorch Inference)               │
└───────────────────────┬─────────────────────────────────────┘
                        │ mTLS (Metrics Only)
┌───────────────────────▼─────────────────────────────────────┐
│                     API Gateway                              │
│              (FastAPI + JWT/OAuth2)                          │
└───────────────────┬─────────────────┬───────────────────────┘
                    │                 │
         ┌──────────▼──────┐   ┌─────▼──────────┐
         │   TimescaleDB   │   │     Redis      │
         │  (Time-series)  │   │   (Cache/RT)   │
         └─────────────────┘   └────────────────┘
                    │
         ┌──────────▼──────────────┐
         │   Next.js Dashboard     │
         │  (Real-time Analytics)  │
         └─────────────────────────┘
```

## 📁 Project Structure

```
arrow-tuning-system/
├── backend/              # FastAPI backend services
│   ├── app/             # Application code
│   ├── tests/           # pytest tests
│   ├── alembic/         # Database migrations
│   ├── pyproject.toml   # Python dependencies
│   └── Dockerfile
├── frontend/            # Next.js 14 dashboard
│   ├── src/app/         # App Router pages
│   ├── src/lib/         # Utilities
│   ├── package.json     # Node dependencies
│   └── Dockerfile
├── mobile/              # Flutter mobile app
│   ├── lib/             # Dart code
│   ├── pubspec.yaml     # Flutter dependencies
│   └── test/
├── ml-models/           # ML model training & export
│   ├── training/        # Training scripts
│   └── export/          # ONNX exports
├── docker/              # Docker configurations
│   └── docker-compose.yml
├── .github/workflows/   # CI/CD pipelines
└── docs/                # Documentation
```

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- Node.js 20.x+
- Flutter 3.x+
- Docker & Docker Compose

### Using Docker Compose (Recommended)

```bash
# Clone repository
git clone https://github.com/Vask006/arrow-tuning-system.git
cd arrow-tuning-system

# Start all services
docker-compose -f docker/docker-compose.yml up -d

# Access services
# Backend API: http://localhost:8000
# Frontend: http://localhost:3000
# API Docs: http://localhost:8000/docs
```

### Manual Setup

#### Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -e ".[dev]"
cp .env.example .env
uvicorn app.main:app --reload
```

#### Frontend

```bash
cd frontend
npm install
cp .env.example .env.local
npm run dev
```

#### Mobile

```bash
cd mobile
flutter pub get
cp .env.example .env
flutter run
```

## 📊 Tech Stack

### Backend
- **FastAPI** - High-performance async API framework
- **SQLAlchemy** - Async ORM with TimescaleDB
- **Pydantic v2** - Data validation and serialization
- **Redis** - Caching and real-time features
- **Loguru** - Structured logging
- **Alembic** - Database migrations

### Frontend
- **Next.js 14** - React framework with App Router
- **TypeScript** - Type-safe JavaScript
- **Tailwind CSS** - Utility-first styling
- **TanStack Query** - Data fetching and caching
- **Axios** - HTTP client

### Mobile
- **Flutter 3.x** - Cross-platform mobile framework
- **Riverpod** - State management
- **Dio** - HTTP client
- **Shared Preferences** - Local storage

### ML/CV
- **PyTorch 2.x** - Deep learning framework
- **Ultralytics YOLO** - Object detection
- **ONNX Runtime** - Cross-platform inference
- **TensorRT** - NVIDIA GPU acceleration

## 🧪 Testing

```bash
# Backend tests
cd backend
pytest --cov=app

# Frontend tests
cd frontend
npm test

# Mobile tests
cd mobile
flutter test
```

## 🔒 Security

- Environment-based secrets
- JWT/OAuth2 authentication
- mTLS for device communication
- Input validation (Pydantic)
- Rate limiting (Redis)
- CORS configuration

## 🔐 Privacy

- On-device ML inference by default
- Minimal data transmission
- Opt-in raw data upload
- Configurable retention policies
- GDPR compliant

## 📚 Documentation

- [API Documentation](docs/api.md) - REST API reference
- [Architecture](docs/architecture.md) - System design
- [Deployment](docs/deployment.md) - Production deployment
- [Contributing](CONTRIBUTING.md) - Contribution guidelines

## 🛠️ Development

### Code Quality

```bash
# Backend
cd backend
black .
isort .
ruff check .

# Frontend
cd frontend
npm run lint

# Mobile
cd mobile
flutter format .
flutter analyze
```

### Commit Convention

We follow [Conventional Commits](https://www.conventionalcommits.org/):

```
feat: add user authentication
fix: resolve race condition
docs: update API documentation
chore: bump dependencies
```

## 🚢 Deployment

### Docker

```bash
docker-compose -f docker/docker-compose.yml up -d
```

### Cloud Platforms

- AWS: ECS + RDS + ElastiCache
- Google Cloud: Cloud Run + Cloud SQL
- Azure: Container Apps + PostgreSQL

See [deployment guide](docs/deployment.md) for details.

## 📝 License

MIT License - see [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 📧 Contact

- **Repository**: [https://github.com/Vask006/arrow-tuning-system](https://github.com/Vask006/arrow-tuning-system)
- **Issues**: [GitHub Issues](https://github.com/Vask006/arrow-tuning-system/issues)
- **Discussions**: [GitHub Discussions](https://github.com/Vask006/arrow-tuning-system/discussions)

---

**Built with ❤️ for performance enthusiasts and privacy advocates**
