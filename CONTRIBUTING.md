# Contributing to Arrow Tuning System

Thank you for your interest in contributing to ATS!

## Development Workflow

1. Fork the repository
2. Create a feature branch: `git checkout -b feat/your-feature`
3. Make your changes
4. Run tests: `pytest` (backend), `npm test` (frontend), `flutter test` (mobile)
5. Commit: `git commit -m "feat: add new feature"`
6. Push: `git push origin feat/your-feature`
7. Create a Pull Request

## Coding Standards

### Python (Backend)
- Follow PEP 8
- Use type hints
- Add docstrings (Google style)
- Format with `black` and `isort`
- Lint with `ruff`

### TypeScript (Frontend)
- Use TypeScript strict mode
- Follow ESLint rules
- Format with Prettier
- Use functional components

### Dart (Mobile)
- Follow Effective Dart
- Use `flutter format`
- Run `flutter analyze`

## Commit Convention

We use [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation
- `chore:` - Maintenance
- `test:` - Tests

## Testing

- **Backend**: Minimum 80% coverage
- **Frontend**: Test components and utilities
- **Mobile**: Test widgets and logic

## Questions?

Open an issue or discussion on GitHub!

