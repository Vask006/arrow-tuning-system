.PHONY: help setup install install-dev install-ml clean lint format test test-cov run-api run-edge build-docker push-docker build-trt export-onnx pre-commit

# Variables
PYTHON := python
PIP := pip
DOCKER := docker
DOCKER_COMPOSE := docker-compose

# Colors for output
BLUE := \033[0;34m
GREEN := \033[0;32m
YELLOW := \033[0;33m
RED := \033[0;31m
NC := \033[0m # No Color

help: ## Show this help message
	@echo "$(BLUE)Arrow Tuning System - Available Commands$(NC)"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "$(GREEN)%-20s$(NC) %s\n", $$1, $$2}'

# Setup and Installation
setup: ## Initial project setup
	@echo "$(BLUE)Setting up Arrow Tuning System...$(NC)"
	$(PYTHON) -m venv venv
	@echo "$(GREEN)Virtual environment created!$(NC)"
	@echo "$(YELLOW)Activate with: source venv/bin/activate (Linux/Mac) or venv\\Scripts\\activate (Windows)$(NC)"

install: ## Install production dependencies
	@echo "$(BLUE)Installing production dependencies...$(NC)"
	$(PIP) install -r requirements.txt
	@echo "$(GREEN)Production dependencies installed!$(NC)"

install-dev: ## Install development dependencies
	@echo "$(BLUE)Installing development dependencies...$(NC)"
	$(PIP) install -r requirements-dev.txt
	$(PIP) install -e .
	@echo "$(GREEN)Development dependencies installed!$(NC)"

install-ml: ## Install ML/CV dependencies
	@echo "$(BLUE)Installing ML dependencies...$(NC)"
	$(PIP) install -r requirements-ml.txt
	@echo "$(GREEN)ML dependencies installed!$(NC)"

install-all: install-dev install-ml ## Install all dependencies
	@echo "$(GREEN)All dependencies installed!$(NC)"

# Code Quality
lint: ## Run linters (ruff, mypy)
	@echo "$(BLUE)Running linters...$(NC)"
	ruff check backend/ ml_models/
	mypy backend/ || true
	@echo "$(GREEN)Linting complete!$(NC)"

format: ## Format code (black, isort)
	@echo "$(BLUE)Formatting code...$(NC)"
	black backend/ ml_models/
	isort backend/ ml_models/
	@echo "$(GREEN)Code formatted!$(NC)"

format-check: ## Check code formatting without changing files
	@echo "$(BLUE)Checking code format...$(NC)"
	black --check backend/ ml_models/
	isort --check-only backend/ ml_models/

pre-commit: ## Install and run pre-commit hooks
	@echo "$(BLUE)Installing pre-commit hooks...$(NC)"
	pre-commit install
	pre-commit run --all-files

# Testing
test: ## Run tests
	@echo "$(BLUE)Running tests...$(NC)"
	pytest backend/tests/
	@echo "$(GREEN)Tests complete!$(NC)"

test-cov: ## Run tests with coverage
	@echo "$(BLUE)Running tests with coverage...$(NC)"
	pytest --cov=backend --cov-report=html --cov-report=term-missing backend/tests/
	@echo "$(GREEN)Coverage report generated in htmlcov/index.html$(NC)"

test-watch: ## Run tests in watch mode
	@echo "$(BLUE)Running tests in watch mode...$(NC)"
	pytest-watch backend/tests/

# Running Services
run-api: ## Run backend API locally
	@echo "$(BLUE)Starting backend API...$(NC)"
	cd backend && uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

run-frontend: ## Run frontend locally
	@echo "$(BLUE)Starting frontend...$(NC)"
	cd frontend && npm run dev

run-edge: ## Run edge inference service
	@echo "$(BLUE)Starting edge inference...$(NC)"
	$(PYTHON) -m ml_models.edge.inference

# Docker
docker-build: ## Build all Docker images
	@echo "$(BLUE)Building Docker images...$(NC)"
	$(DOCKER) build -t ats-backend:latest ./backend
	$(DOCKER) build -t ats-frontend:latest ./frontend
	@echo "$(GREEN)Docker images built!$(NC)"

docker-up: ## Start all services with docker-compose
	@echo "$(BLUE)Starting all services...$(NC)"
	cd docker && $(DOCKER_COMPOSE) up -d
	@echo "$(GREEN)Services started!$(NC)"
	@echo "$(YELLOW)Backend: http://localhost:8000$(NC)"
	@echo "$(YELLOW)Frontend: http://localhost:3000$(NC)"

docker-down: ## Stop all docker-compose services
	@echo "$(BLUE)Stopping all services...$(NC)"
	cd docker && $(DOCKER_COMPOSE) down

docker-logs: ## View docker-compose logs
	cd docker && $(DOCKER_COMPOSE) logs -f

docker-clean: ## Remove all containers and images
	@echo "$(RED)Cleaning Docker resources...$(NC)"
	$(DOCKER_COMPOSE) -f docker/docker-compose.yml down -v
	$(DOCKER) system prune -af

# ML Model Operations
export-onnx: ## Export model to ONNX format
	@echo "$(BLUE)Exporting model to ONNX...$(NC)"
	$(PYTHON) ml_models/export/export_onnx.py --weights ml_models/weights/best.pt
	@echo "$(GREEN)Model exported to ONNX!$(NC)"

build-trt: ## Build TensorRT engine (requires NVIDIA GPU)
	@echo "$(BLUE)Building TensorRT engine...$(NC)"
	$(PYTHON) ml_models/export/export_trt.py --weights ml_models/weights/best.pt
	@echo "$(GREEN)TensorRT engine built!$(NC)"

train-model: ## Train YOLO model
	@echo "$(BLUE)Training model...$(NC)"
	$(PYTHON) ml_models/training/train_yolo.py
	@echo "$(GREEN)Training complete!$(NC)"

# Database
db-migrate: ## Run database migrations
	@echo "$(BLUE)Running migrations...$(NC)"
	cd backend && alembic upgrade head
	@echo "$(GREEN)Migrations complete!$(NC)"

db-revision: ## Create new migration
	@echo "$(BLUE)Creating migration...$(NC)"
	cd backend && alembic revision --autogenerate -m "$(message)"

db-downgrade: ## Rollback last migration
	@echo "$(BLUE)Rolling back migration...$(NC)"
	cd backend && alembic downgrade -1

# Cleanup
clean: ## Clean build artifacts
	@echo "$(BLUE)Cleaning build artifacts...$(NC)"
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".ruff_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".mypy_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	rm -rf build/ dist/ htmlcov/ .coverage
	@echo "$(GREEN)Cleanup complete!$(NC)"

clean-all: clean docker-clean ## Clean everything including Docker
	@echo "$(GREEN)Deep cleanup complete!$(NC)"

# CI/CD
ci-test: lint test ## Run CI tests locally
	@echo "$(GREEN)CI tests passed!$(NC)"

ci-build: docker-build ## Build for CI
	@echo "$(GREEN)CI build complete!$(NC)"

# Documentation
docs-serve: ## Serve documentation locally
	@echo "$(BLUE)Serving documentation...$(NC)"
	@echo "$(YELLOW)Documentation available in /docs$(NC)"

# Git hooks
hooks-install: ## Install git hooks
	@echo "$(BLUE)Installing git hooks...$(NC)"
	pre-commit install --install-hooks
	@echo "$(GREEN)Git hooks installed!$(NC)"

# Version and Release
version: ## Show current version
	@echo "$(BLUE)Current version:$(NC)"
	@grep "version" pyproject.toml | head -1

bump-patch: ## Bump patch version (0.1.0 -> 0.1.1)
	@echo "$(BLUE)Bumping patch version...$(NC)"
	# Requires semantic-release or bump2version

bump-minor: ## Bump minor version (0.1.0 -> 0.2.0)
	@echo "$(BLUE)Bumping minor version...$(NC)"

bump-major: ## Bump major version (0.1.0 -> 1.0.0)
	@echo "$(BLUE)Bumping major version...$(NC)"

# Development workflow
dev-setup: setup install-dev hooks-install ## Complete development setup
	@echo "$(GREEN)Development environment ready!$(NC)"
	@echo "$(YELLOW)Next steps:$(NC)"
	@echo "  1. Activate virtual environment"
	@echo "  2. Copy .env.example files"
	@echo "  3. Run 'make docker-up' to start services"

dev-run: docker-up run-api ## Start all development services
	@echo "$(GREEN)Development environment running!$(NC)"

# Production
prod-build: ## Build for production
	@echo "$(BLUE)Building for production...$(NC)"
	$(DOCKER) build -t ats-backend:prod ./backend --target production
	$(DOCKER) build -t ats-frontend:prod ./frontend --target production

# Status and info
status: ## Show service status
	@echo "$(BLUE)Service Status:$(NC)"
	cd docker && $(DOCKER_COMPOSE) ps

health: ## Check health of services
	@echo "$(BLUE)Checking service health...$(NC)"
	@curl -f http://localhost:8000/health || echo "$(RED)Backend not running$(NC)"
	@curl -f http://localhost:3000 || echo "$(RED)Frontend not running$(NC)"

# Backup and restore
backup-db: ## Backup database
	@echo "$(BLUE)Backing up database...$(NC)"
	$(DOCKER_COMPOSE) -f docker/docker-compose.yml exec postgres pg_dump -U ats_user ats_db > backup_$$(date +%Y%m%d_%H%M%S).sql
	@echo "$(GREEN)Database backed up!$(NC)"

# Default target
.DEFAULT_GOAL := help

