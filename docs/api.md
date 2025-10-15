# API Documentation

## Base URL

```
http://localhost:8000/api/v1
```

## Endpoints

### Health Check

```
GET /health
```

**Response:**
```json
{
  "status": "healthy",
  "version": "0.1.0"
}
```

### Authentication

#### Register
```
POST /auth/register
```

**Request Body:**
```json
{
  "email": "user@example.com",
  "password": "password123",
  "full_name": "John Doe"
}
```

#### Login
```
POST /auth/login
```

**Request:**
```json
{
  "email": "user@example.com",
  "password": "password123"
}
```

**Response:**
```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "token_type": "bearer"
}
```

### Devices

#### List Devices
```
GET /devices
Authorization: Bearer <token>
```

#### Register Device
```
POST /devices
Authorization: Bearer <token>
```

**Request Body:**
```json
{
  "device_id": "device-001",
  "name": "My Device",
  "device_type": "mobile"
}
```

### Metrics

#### Submit Metrics
```
POST /metrics
Authorization: Bearer <token>
```

**Request Body:**
```json
{
  "device_id": "device-001",
  "metrics": [
    {
      "name": "cpu_usage",
      "value": 45.5,
      "timestamp": "2025-01-15T10:00:00Z"
    }
  ]
}
```

## Error Responses

### 401 Unauthorized
```json
{
  "detail": "Could not validate credentials"
}
```

### 404 Not Found
```json
{
  "detail": "Resource not found"
}
```

### 422 Validation Error
```json
{
  "detail": [
    {
      "loc": ["body", "email"],
      "msg": "field required",
      "type": "value_error.missing"
    }
  ]
}
```

