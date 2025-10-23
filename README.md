# tiktok

tiktok-incremental-scraper/
├── requirements.txt
├── railway.json
├── Dockerfile
├── .env.example
├── .gitignore
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── database/
│   │   ├── __init__.py
│   │   ├── models.py
│   │   └── manager.py
│   ├── scraping/
│   │   ├── __init__.py
│   │   ├── scrapfly_client.py
│   │   ├── tiktok_scraper.py
│   │   └── incremental_logic.py
│   └── utils/
│       ├── __init__.py
│       └── config.py
└── scripts/
    ├── init_db.py
    └── scheduler.py
