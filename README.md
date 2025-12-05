# Twichist

## Project Idea

- Fetch, analyze and visualize twitch chat data.

## Golden Path

- Python 3.14
- Twitch chat fetcher
- Client: ReactJS, ShadCn
- Server: FastAPI, Pydantic
- Tasks: faststream, kafka
- DB: PostgreSQL, asyncpg

## Links

- https://github.com/Brisppy/twitch-archiver

# Project To-Do and history

- TODO: Try to use devcontainers

## Phase 1: Project Setup & Infrastructure

- DONE: Initialize project structure and infrastructure
- DONE: Create monorepo directory structure (backend/, frontend/)
- DONE: Setup pyproject.toml with uv and all Python dependencies
- TODO: Create compose.yml for Kafka, PostgreSQL
- TODO: Setup environment variables template (.env.example), pydantic-settings config

## Phase 2: Database Layer (SQLModel)

- TODO: Create SQLModel table models (Channel, ChatMessage, ChannelStats)
- TODO: Create API schema models (Create/Read variants)
- TODO: Setup async database connection with SQLModel
- TODO: Implement ChannelRepository with CRUD operations
- TODO: Implement ChatMessageRepository with bulk insert and queries
- TODO: Implement ChannelStatsRepository for analytics data
- TODO: Create Alembic migrations setup

## Phase 3: Fetcher Module (Helix API)

- TODO: Create OAuth token manager with auto-refresh
- TODO: Implement async HelixClient (httpx) for REST endpoints
- TODO: Implement EventSub WebSocket client for real-time chat
- TODO: Create BaseTask abstract class for polling tasks
- TODO: Implement ChatStreamTask, with tests

## Phase 4: FastStream Worker (Kafka Consumers)

- TODO: Setup FastStream app with Kafka broker configuration
- TODO: Create consumer for twitch.chat.raw topic
- TODO: Implement message processor (parse, validate, enrich)
- TODO: Implement sentiment analysis processor
- TODO: Implement emote extraction and counting logic
- TODO: Implement stats aggregation service (hourly/daily rollups)

## Phase 5: FastAPI Server

- TODO: Setup FastAPI app with lifespan (init DB, shutdown)
- TODO: Create common dependencies (Autorization, DB)
- TODO: Implement /api/channels routes (CRUD)
- TODO: Implement /api/channels/{id}/messages routes (paginated)
- TODO: Implement /api/channels/{id}/stats routes
- TODO: Add request validation and error handling middleware
- TODO: Setup CORS configuration for React client
- TODO: Add structured logging with structlog

## Phase 6: React Frontend

- TODO: Initialize Vite + React + TypeScript project
- TODO: Setup Tailwind CSS and shadcn/ui components
- TODO: Create API client with fetch/axios and types
- TODO: Setup React Query for data fetching and caching
- TODO: Create useWebSocket hook for live chat connection
- TODO: Implement DashboardLayout component with sidebar
- TODO: Implement ChannelSelector component
- TODO: Implement StatsCards component (message count, users, etc.)
- TODO: Implement ChatFeed component with virtual scrolling
- TODO: Implement ChatMessage component with emote/badge rendering
- TODO: Implement ChatFilters component (search, user, time range)
- TODO: Implement MessageVolumeChart (line/area chart)
- TODO: Implement SentimentPieChart component
- TODO: Implement ActivityHeatmap component
- TODO: Create Dashboard page (main view)
- TODO: Create ChannelDetail page
- TODO: Add dark mode toggle with theme persistence

## Phase 7: Testing & Quality Assurance

- TODO: Add pre-commit hooks (ruff, basedpyright, biome)
- TODO: Setup pytest with async, parallel support for Python tests
- TODO: Write unit tests for all components
- TODO: Write unit tests for Helix client
- TODO: Write integration tests for API endpoints
- TODO: Setup Vitest for React component tests
- TODO: Write tests for React hooks and components

## Phase 8: Documentation & Deployment

- Write README with setup instructions
- Create API documentation with OpenAPI/Swagger
- Create docker-compose.prod.yml for production
- Create docker-compose.prod.yml for staging/local
