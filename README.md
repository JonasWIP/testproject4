# testproject4

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
