# Project To-Do and history

Data ingestion: Download chat logs via API or scraping.
Storage: PostgreSQL (structured fields: user, timestamp, message, emotes).
Processing: Python (pandas, TensorFlow?).
Visualization: Plotly, Grafana, or a custom FastAPI dashboard.

- TODO: Try to use devcontainers

## Phase 1: Project Setup & Infrastructure

- DONE: Initialize project structure and infrastructure
- DONE: Create monorepo directory structure (backend/, frontend/)
- DONE: Setup pyproject.toml with uv and all Python dependencies
- TODO: Initialize Vite + React + TypeScript project
- TODO: Setup Tailwind CSS and shadcn/ui components
- TODO: Setup CORS configuration for React client
- TODO: Create compose.yml for Kafka, PostgreSQL
- TODO: Setup environment variables template (.env.example), pydantic-settings config

## Phase 2: Database Layer (SQLModel)

- TODO: Plan database architecture
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
- TODO: Add structured logging with structlog

## Phase 6: React Frontend

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

- TODO: Write README with setup instructions
- TODO: Create API documentation with OpenAPI/Swagger
- TODO: Create compose.prod.yml for production
- TODO: Create compose.dev.yml for staging/local

## Analytics

### Chat

Overall stream health and community.

Break chat into time windows (e.g., 30s or 1min bins).
Measure message volume, sentiment, emote usage per window.
Detect recurring patterns (e.g., hype at start, lull in middle, spike at climax).
Skills: Time‑series analysis, window functions in SQL, visualization.

### Topic Modeling

What viewers are talking about during different segments.

Use NLP techniques like LDA or BERTopic on chat text.
Map topics to timestamps.
Compare topic shifts across streams or games.
Skills: NLP, clustering, dimensionality reduction.

### User Behavior Profiling

Different types of chat participants.

Cluster users by activity (lurkers, casual chatters, spammers, power users).
Track how user engagement changes across streams.
Build dashboards showing distribution of user types.
Skills: Clustering, user segmentation, behavioral analytics.

### Emote Burst Detection

Sudden surges in specific emotes (e.g., PogChamp).

Track frequency of each emote over time.
Detect bursts using statistical thresholds.
Correlate bursts with video events (kills, goals, jokes).
Skills: Event detection, anomaly detection, visualization.

### Cross‑Stream Comparative Analytics

How chat differs between streamers or games.

Compare average sentiment, emote usage, message length.
Identify unique “chat signatures” for each streamer.
Build similarity scores between communities.
Skills: Comparative statistics, similarity metrics, dashboards.

### Moderation & Toxicity Trends

What to analyze: How moderation interacts with chat flow.

Detect toxic language using classifiers.
Compare moderation events vs. toxic spikes.
Study effectiveness of moderation strategies.
Skills: NLP classification, ethics in data, correlation analysis.

### Predictive Modeling

What to analyze: Can chat predict future events?

Train models to predict hype moments based on chat features.
Predict streamer actions (e.g., big plays) from chat bursts.
Skills: Machine learning, feature engineering, supervised learning.
