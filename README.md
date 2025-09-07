# testproject4

A simple Hello World web service built with Flask and Docker.

## Features

- **Hello World Web Service**: Returns a beautiful HTML page with "Hello World"
- **Health Check Endpoint**: Available at `/health` for monitoring
- **Docker Support**: Fully containerized with Docker Compose
- **Auto-deployment**: GitHub Actions workflow for automatic building and deployment

## Quick Start

### Local Development

1. **Run with Docker Compose:**
   ```bash
   docker-compose up --build
   ```

2. **Access the service:**
   - Main page: http://localhost:5124
   - Health check: http://localhost:5124/health

### Manual Python Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application:**
   ```bash
   python app.py
   ```

3. **Access at:** http://localhost:3000

## GitHub Container Registry Setup

Dieses Projekt ist für automatisches Building und Deployment über GitHub Actions konfiguriert.

### Voraussetzungen

1. **GitHub Container Registry (GHCR) aktivieren:**
   - Gehe zu deinen Repository-Settings
   - Unter "Actions" → "General" → "Workflow permissions"
   - Wähle "Read and write permissions"

2. **Deployment Server konfigurieren:**
   - Setze die Umgebungsvariable `DEPLOYMENT_SERVER_URL` auf deinem Server
   - Beispiel: `export DEPLOYMENT_SERVER_URL="http://your-server.com:3000"`

### Automatischer Workflow

Bei jedem Push auf `main` oder `master`:
1. Docker Image wird gebaut und zu GHCR gepusht
2. Webhook wird an den Deployment-Server gesendet
3. Server pullt das neue Image und startet den Service neu

### Manuelle Deployment

Um manuell zu deployen, sende einen POST-Request an den Webhook-Endpunkt:

```bash
curl -X POST "http://your-server.com:3000/webhook/github" \
  -H "Content-Type: application/json" \
  -d '{    "repository": {      "clone_url": "https://github.com/username/testproject4.git"    },    "ref": "refs/heads/main"  }'
```

## API Endpoints

- `GET /` - Returns HTML Hello World page
- `GET /health` - Returns JSON health status
