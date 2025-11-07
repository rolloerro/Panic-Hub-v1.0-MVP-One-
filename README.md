![Build Status](https://github.com/rolloerro/Panic-Hub-v1.0-MVP-One-/actions/workflows/docker-build.yml/badge.svg)

# 🧠 Panic Hub v1.0 (MVP-One)

> **Distributed Microservice Hub** for coordinating panic-assistance bots — part of the **Digital WM Ecosystem** 🩺

---

## 🚀 Описание

**Panic Hub** — это центральный узел (hub), объединяющий несколько Telegram-ботов для помощи при панических атаках.  
Он построен по микросервисной архитектуре и включает три ключевых компонента:

| Компонент | Назначение |
|------------|------------|
| **Hub (FastAPI)** | Центральная точка входа, маршрутизация и API |
| **Orchestrator** | Управление логикой и маршрутизация запросов между ботами |
| **Mock Panic Bot** | Тестовый бот для отладки и демонстрации связей |

---

## 🧩 Архитектура
```text
┌────────────────────┐
│      Hub API       │  ← http://localhost:8000
└───────┬────────────┘
        │
        ▼
┌────────────────────┐
│   Orchestrator     │  ← http://localhost:8001
└───────┬────────────┘
        │
        ▼
┌────────────────────┐
│  Panic Mock Bot    │  ← http://localhost:8002
└────────────────────┘
⚙️ Запуск проекта
🐳 Через Docker Compose
bash
Копировать код
docker compose up --build
После сборки сервисы будут доступны:

Hub → http://localhost:8000

Orchestrator → http://localhost:8001

Mock Bot → http://localhost:8002

🧠 API Hub (Swagger UI)
После запуска открой:
👉 http://localhost:8000/docs

Доступные эндпоинты:

/ — приветственное сообщение

/health — проверка состояния

/bots — список доступных ботов

/orchestrator — маршрутизация

🔄 CI/CD
Проект включает GitHub Actions pipeline (.github/workflows/docker-build.yml),
который автоматически:

Проверяет сборку контейнеров

Поднимает тестовую среду

Проверяет endpoint /health

Завершает контейнеры

📦 Структура проекта
css
Копировать код
panic-hub/
├── hub/
│   ├── main.py
│   └── Dockerfile
├── orchestrator/
│   ├── logic/
│   │   └── intent_classifier.py
│   └── Dockerfile
├── mock_panic_bot/
│   ├── main.py
│   └── Dockerfile
├── docker-compose.yml
└── .github/workflows/docker-build.yml
🧬 Roadmap
✅ MVP v1.0 — базовый пайплайн с mock-ботом
🔜 v2.0 — интеграция реальных ботов (Iron Nerves, PanicHelper и др.)
🔜 v3.0 — подключение базы данных и логирования событий
🔜 v4.0 — интеграция AI (NLP intent detection)
┌──────────────────────────────┐
│          Git Push            │
│ (commit → GitHub main branch)│
└──────────────┬───────────────┘
               │
               ▼
      ┌────────────────┐
      │  GitHub Action │
      │ docker-build.yml │
      └───────┬────────┘
              │
              ▼
   ┌────────────────────┐
   │  Build Containers  │
   │ (Hub, Orchestrator,│
   │  Mock Panic Bot)   │
   └─────────┬──────────┘
             │
             ▼
   ┌────────────────────┐
   │  Run Integration   │
   │     Tests          │
   │   /health check    │
   └─────────┬──────────┘
             │
             ▼
   ┌────────────────────┐
   │   CI Result Badge  │
   │  ✅ Passed / ❌ Fail│
   └────────────────────┘

👨‍🔬 Автор
Digital WM / RolloErro
💡 Telegram: @rolloerro

Made with ❤️ and calm mind — even during panic attacks.
