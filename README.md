## Overview
This project is a Django + Django REST Framework service that ingests solar inverter metrics, stores them, provides CRUD operations for plants (Usina), inverters (Inversor) and readings (Leitura), and exposes analytics endpoints:
- **Maximum power** per day
- **Average temperature** per day
- **Total energy generation** of an inverter
- **Total energy generation** of a plant

## Tech Stack
- **Python** 3.10+  
- **Django** 5.2.1  
- **Django REST Framework** 3.16.0  
- **django-filter** 25.1  
- **drf-spectacular** 0.28.0 (Swagger / OpenAPI)  
- **PostgreSQL** (or SQLite in development)  
- **Docker & Docker Compose** (optional)  
- **Gunicorn** for production

## Requirements
All Python dependencies are listed in \`requirements.txt\`.

## Local Setup
```bash
# 1. Clone the repo
git clone https://github.com/lucaskrispim/desafio_TECSCI.git
cd desafio_TECSCI

# 2. Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 3. Install Python dependencies
pip install -r requirements.txt

# 4. Apply database migrations
python manage.py migrate

# 5. Seed the database with example metrics
python manage.py seed_metrics --file metrics.json

# 6. Run the development server
python manage.py runserver
```
API will be available at http://localhost:8000/.

## Docker Setup
```bash
# Build and start services
docker-compose build
docker-compose up -d

# Apply migrations & seed inside the web container
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py seed_metrics --file metrics.json
```

## API Endpoints

### CRUD Resources

#### Plants (Usina)
```
GET     /api/usinas/
POST    /api/usinas/
GET     /api/usinas/{id}/
PUT     /api/usinas/{id}/
PATCH   /api/usinas/{id}/
DELETE  /api/usinas/{id}/
```

#### Inverters (Inversor)
```
GET     /api/inversores/
POST    /api/inversores/
GET     /api/inversores/{id}/
PUT     /api/inversores/{id}/
PATCH   /api/inversores/{id}/
DELETE  /api/inversores/{id}/
```

#### Readings (Leitura)
```
GET     /api/leituras/
POST    /api/leituras/
GET     /api/leituras/{id}/
PUT     /api/leituras/{id}/
PATCH   /api/leituras/{id}/
DELETE  /api/leituras/{id}/
```

### Analytics

#### Max Power per Day
```
GET /api/analytics/potencia-max/?inversor_id=<id>&data_inicio=YYYY-MM-DD&data_fim=YYYY-MM-DD
```

#### Avg Temperature per Day
```
GET /api/analytics/temp-media/?inversor_id=<id>&data_inicio=YYYY-MM-DD&data_fim=YYYY-MM-DD
```

#### Energy Generation – Inverter
```
GET /api/analytics/geracao-inversor/?inversor_id=<id>&data_inicio=YYYY-MM-DD&data_fim=YYYY-MM-DD
```

#### Energy Generation – Plant
```
GET /api/analytics/geracao-usina/?usina_id=<id>&data_inicio=YYYY-MM-DD&data_fim=YYYY-MM-DD
```

## Documentation
- **Swagger UI**: http://localhost:8000/api/docs/  
- **OpenAPI Schema**: http://localhost:8000/api/schema/ 
