crawler-service/
├── crawler/
│   ├── spiders/
│   │   ├── base_spider.py          # shared logic, rate limiting, dedup
│   │   ├── wellfound_spider.py
│   │   ├── yc_spider.py
│   │   ├── remotive_spider.py
│   │   └── github_boards_spider.py
│   ├── parsers/
│   │   ├── ats_detector.py         # figures out which ATS a career page uses
│   │   ├── lever_parser.py
│   │   ├── greenhouse_parser.py
│   │   └── generic_parser.py       # fallback for custom career pages
│   ├── pipelines/
│   │   ├── dedup_pipeline.py       # Redis-based deduplication
│   │   ├── filter_pipeline.py      # stack matching logic
│   │   └── emit_pipeline.py        # pushes to Redis Streams
│   ├── models.py                   # JobPosting dataclass
│   └── settings.py
├── Dockerfile
├── requirements.txt
└── scrapy.cfg

