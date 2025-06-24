# Project-Hub-Analyze

**Open-source metrics analysis and A/B testing platform for local deployment**  

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)

Self-hosted solution for collecting application metrics, analyzing trends, planning features, and running A/B tests. Deploys locally via Docker - no cloud dependencies required.

---

## ⚡️ Core Features
| Feature                | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| **📊 Metrics Collection** | Universal API for sending data from any language                            |
| **📈 Data Visualization** | Interactive charts + AI-powered trend analysis (LLM integration)            |
| **🧪 A/B Testing**      | Statistical analysis of experiments with automatic reporting                |
| **🗓 Planning Boards**   | GitHub Projects-like kanban boards for feature development                  |
| **🔔 Notifications**    | Custom alerts via Email/Telegram for metric thresholds                      |
| **📝 Automated Reports** | Scheduled PDF reports with insights and visualizations                      |
| **🌐 Any Language Support** | Universal REST API works with Python, JavaScript, Java, Go, C#, etc.        |

---

## 🛠 Technology Stack
| Component          | Technologies                                                                 |
|--------------------|------------------------------------------------------------------------------|
| **Backend**        | Python + FastAPI (ASGI)                                                      |
| **Frontend**       | React + Redux + Chart.js + Material UI                                       |
| **Databases**      | PostgreSQL (core) + TimescaleDB (time-series) + Redis (caching/queues)       |
| **Infrastructure** | Docker + Docker Compose                                                      |
| **AI Analytics**   | Local LLM integration (Ollama) or OpenAI API                                 |

---

## 🚀 Quick Start

### Prerequisites
- Docker 20.10+
- Docker Compose 2.4+

### Installation
```bash
# 1. Clone repository
git clone https://github.com/your-username/project-hub-analyze.git
cd project-hub-analyze

# 2. Configure environment
cp .env.example .env
# Edit .env file with your preferences

# 3. Start containers
docker compose up -d

# Access services:
# - Backend: http://localhost:8000
# - Frontend: http://localhost:3000
# - PGAdmin: http://localhost:5050 (admin@example.com/admin)
```