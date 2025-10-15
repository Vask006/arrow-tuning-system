# Development Guide

## Quick Start with Makefile

All development tasks can be run using the Makefile:

```bash
# See all available commands
make help

# Initial setup
make dev-setup

# Run services
make docker-up
make run-api
make run-frontend
```

## Available Make Commands

### Setup and Installation
```bash
make setup           # Create virtual environment
make install         # Install production dependencies
make install-dev     # Install development dependencies
make install-ml      # Install ML dependencies
make install-all     # Install everything
```

### Code Quality
```bash
make lint            # Run linters (ruff, mypy)
make format          # Format code (black, isort)
make format-check    # Check formatting without changes
make pre-commit      # Install and run pre-commit hooks
```

### Testing
```bash
make test            # Run tests
make test-cov        # Run tests with coverage report
make test-watch      # Run tests in watch mode
```

### Running Services
```bash
make run-api         # Start backend API (port 8000)
make run-frontend    # Start frontend (port 3000)
make run-edge        # Start edge inference service
```

### Docker
```bash
make docker-build    # Build all Docker images
make docker-up       # Start all services
make docker-down     # Stop all services
make docker-logs     # View logs
make docker-clean    # Remove all containers/images
```

### ML Model Operations
```bash
make export-onnx     # Export model to ONNX
make build-trt       # Build TensorRT engine
make train-model     # Train YOLO model
```

### Database
```bash
make db-migrate      # Run migrations
make db-revision message="description"  # Create new migration
make db-downgrade    # Rollback last migration
make backup-db       # Backup database
```

### Cleanup
```bash
make clean           # Clean build artifacts
make clean-all       # Deep clean (including Docker)
```

### CI/CD
```bash
make ci-test         # Run CI tests locally
make ci-build        # Build for CI
```

### Development Workflow
```bash
make dev-setup       # Complete dev setup
make dev-run         # Start all dev services
```

## Development Workflow

### 1. Initial Setup

```bash
# Clone repository
git clone https://github.com/Vask006/arrow-tuning-system.git
cd arrow-tuning-system

# Set up development environment
make dev-setup

# Activate virtual environment
# Linux/Mac:
source venv/bin/activate
# Windows:
venv\Scripts\activate
```

### 2. Configure Environment

```bash
# Copy environment files
cp backend/.env.example backend/.env
cp frontend/.env.example frontend/.env.local
cp mobile/.env.example mobile/.env

# Edit .env files with your settings
```

### 3. Start Development

```bash
# Option A: Use Docker (Recommended)
make docker-up

# Option B: Run services individually
# Terminal 1: Backend
make run-api

# Terminal 2: Frontend
make run-frontend
```

### 4. Make Changes

```bash
# Format code before committing
make format

# Run linters
make lint

# Run tests
make test

# Or run all quality checks
make ci-test
```

### 5. Commit Changes

```bash
# Stage changes
git add .

# Commit (pre-commit hooks will run automatically)
git commit -m "feat: add new feature"

# Push
git push origin your-branch
```

## Testing

### Backend Tests

```bash
# Run all backend tests
pytest backend/tests/

# Run with coverage
make test-cov

# Run specific test file
pytest backend/tests/test_api/test_auth.py -v

# Run with markers
pytest -m "not slow"
```

### Frontend Tests

```bash
cd frontend

# Run tests
npm test

# Run in watch mode
npm test -- --watch

# E2E tests
npm run test:e2e
```

### Mobile Tests

```bash
cd mobile

# Run tests
flutter test

# Run with coverage
flutter test --coverage
```

## Code Style

### Python

- **Formatting**: Black (line length 100)
- **Import sorting**: isort (black profile)
- **Linting**: Ruff
- **Type checking**: mypy (strict mode)

```bash
# Auto-format
make format

# Check only
make format-check
```

### TypeScript

- **Formatting**: Prettier
- **Linting**: ESLint
- **Type checking**: TypeScript compiler

```bash
cd frontend
npm run lint
npm run format
```

### Flutter

- **Formatting**: dart format
- **Linting**: flutter analyze

```bash
cd mobile
flutter format .
flutter analyze
```

## Git Workflow

### Branch Naming

- `feat/feature-name` - New features
- `fix/bug-description` - Bug fixes
- `docs/what-changed` - Documentation
- `refactor/what-changed` - Code refactoring
- `test/what-added` - Test additions

### Commit Messages

Follow [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <subject>

<body>

<footer>
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `style`: Code style (formatting)
- `refactor`: Code refactoring
- `perf`: Performance improvement
- `test`: Tests
- `chore`: Maintenance
- `ci`: CI/CD changes

Examples:
```bash
git commit -m "feat(auth): add JWT refresh token endpoint"
git commit -m "fix(api): resolve race condition in metrics ingestion"
git commit -m "docs: update API documentation"
```

## Debugging

### Backend

```bash
# Run with debugger
python -m debugpy --listen 5678 -m uvicorn app.main:app --reload

# View logs
tail -f backend/logs/app.log

# Check database
docker-compose exec postgres psql -U ats_user -d ats_db
```

### Frontend

```bash
# Run with debugging
cd frontend
npm run dev

# Check console in browser DevTools
# React DevTools extension recommended
```

### Docker

```bash
# View logs
make docker-logs

# Execute commands in container
docker-compose exec backend bash
docker-compose exec postgres psql -U ats_user -d ats_db

# Inspect container
docker inspect ats-backend
```

## Troubleshooting

### Port Already in Use

```bash
# Find process using port
lsof -i :8000  # Linux/Mac
netstat -ano | findstr :8000  # Windows

# Kill process
kill -9 <PID>  # Linux/Mac
taskkill /PID <PID> /F  # Windows
```

### Database Connection Issues

```bash
# Check if postgres is running
docker-compose ps

# Reset database
docker-compose down -v
docker-compose up -d postgres
make db-migrate
```

### Docker Issues

```bash
# Remove everything and start fresh
make clean-all
make docker-up
```

### Pre-commit Hooks Not Running

```bash
# Reinstall hooks
make hooks-install

# Or manually
pre-commit uninstall
pre-commit install
```

## Performance

### Profiling Backend

```bash
# Install profiler
pip install py-spy

# Profile running server
py-spy top --pid <uvicorn-pid>

# Generate flame graph
py-spy record -o profile.svg --pid <uvicorn-pid>
```

### Monitoring

```bash
# Start with monitoring
docker-compose --profile monitoring up -d

# Access:
# Prometheus: http://localhost:9090
# Grafana: http://localhost:3001
```

## Documentation

### API Documentation

```bash
# Start backend
make run-api

# Open browser
# Swagger UI: http://localhost:8000/docs
# ReDoc: http://localhost:8000/redoc
```

### Generate Documentation

```bash
# API docs are auto-generated from code
# See: backend/app/api/

# Additional docs in /docs directory
```

## Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Next.js Documentation](https://nextjs.org/docs)
- [Flutter Documentation](https://flutter.dev/docs)
- [Docker Documentation](https://docs.docker.com/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [TimescaleDB Documentation](https://docs.timescale.com/)

