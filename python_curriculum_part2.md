# Kurikulum Python: Data Analytics & Automation
## Part 2: Intermediate Data Analytics (Hari 61-120)

### MINGGU 10-11: Advanced Pandas & Data Cleaning (Hari 61-77)

**Hari 61: Pandas Time Series - Part 1**
* DateTime indexing
* Resampling data
* Rolling windows
* Date range generation

Project: Stock Price Analyzer
- Load historical stock data
- Set datetime index
- Resample to different frequencies (daily to monthly)
- Calculate moving averages
- Identify trends

**Hari 62: Pandas Time Series - Part 2**
* Time zone handling
* Period dan timestamp
* Date offsets
* Time-based filtering

Project: Website Traffic Analyzer
- Load web traffic logs dengan timestamps
- Analyze traffic by hour/day/month
- Peak hours identification
- Weekly patterns analysis
- Export insights

**Hari 63: Advanced Data Cleaning - Missing Data**
* Missing data detection strategies
* Forward fill dan backward fill
* Interpolation methods
* Dropping vs imputing decisions

Project: Survey Data Cleaner
- Load survey data dengan missing values
- Analyze missing patterns
- Apply different imputation strategies
- Compare results
- Document cleaning decisions
- Quality report

**Hari 64: Advanced Data Cleaning - Outliers**
* Outlier detection methods (IQR, Z-score)
* Visualization untuk outliers
* Handling strategies
* Impact analysis

Project: Sales Data Outlier Handler
- Detect outliers dalam sales data
- Visualize dengan box plots
- Analyze impact on statistics
- Apply cleaning strategies
- Before/after comparison report

**Hari 65: Data Transformation Techniques**
* Normalization dan standardization
* Log transformation
* Binning dan categorization
* Feature engineering basics

Project: Customer Segmentation Preprocessor
- Load customer data
- Normalize numerical features
- Create age groups (binning)
- Categorize spending levels
- Engineer new features
- Prepare data untuk analysis

**Hari 66: Advanced String Operations in Pandas**
* str accessor methods
* Pattern extraction
* String splitting advanced
* Handling mixed data types

Project: Product Name Standardizer
- Load product data dengan inconsistent names
- Extract brand, model, size
- Standardize formats
- Remove duplicates
- Create clean product catalog

**Hari 67: Working with Multi-level Indexes**
* Creating hierarchical indexes
* Indexing dan slicing MultiIndex
* Stacking dan unstacking
* Cross-sections

Project: Regional Sales Hierarchy
- Create multi-level index (region, city, store)
- Analyze sales at different levels
- Cross-sectional analysis
- Hierarchical aggregations
- Formatted reports

**Hari 68-69: Data Validation & Quality Checks (2 hari)**
* Schema validation
* Range checks
* Consistency checks
* Data quality metrics

Project: Automated Data Quality Checker
- Create validation rules engine
- Check data types, ranges, patterns
- Identify duplicates
- Cross-field validation
- Generate quality score
- Detailed quality report
- Flagging system untuk issues

**Hari 70: Pandas Performance Optimization**
* Efficient data types
* Vectorization vs loops
* Memory usage optimization
* Query optimization

Project: Large Dataset Handler
- Load large CSV file
- Optimize data types
- Compare performance (loops vs vectorization)
- Memory profiling
- Chunking strategies
- Performance benchmark report

**Hari 71: Advanced Merging & Concatenation**
* Complex join scenarios
* Merge validation
* Handling merge conflicts
* Indicator columns

Project: Multi-Source Data Integrator
- Merge customer, transaction, product data
- Handle missing keys
- Resolve duplicates
- Validate merge results
- Data lineage tracking
- Integration report

**Hari 72: Reshape & Pivot Advanced**
* Advanced pivot tables
* Crosstabs
* Melt dan wide-to-long conversion
* Custom aggregations

Project: Survey Response Analyzer
- Reshape survey data (wide to long)
- Create pivot tables untuk analysis
- Cross-tabulation untuk categories
- Multi-level aggregations
- Export multiple views

**Hari 73: Working with Excel Files**
* Reading multiple sheets
* Writing to Excel dengan formatting
* ExcelWriter advanced
* Handling formulas

Project: Excel Report Generator
- Read data dari multiple sources
- Create multi-sheet workbook
- Apply formatting (colors, fonts, borders)
- Add summary sheet
- Include formulas
- Professional Excel output

**Hari 74: Introduction to SQL with Pandas**
* SQL basics overview
* read_sql() dan to_sql()
* SQLite integration
* Query dari Python

Project: SQLite Database Manager
- Create SQLite database
- Import CSV data to tables
- Run SQL queries dari Python
- Join tables dengan SQL
- Export results back to pandas
- Database backup

**Hari 75-77: Comprehensive Data Cleaning Project (3 hari)**

Project: Real-World Dataset Cleaning Pipeline
Hari 75: Data Assessment
- Load messy real-world dataset
- Exploratory data analysis
- Identify all quality issues
- Document cleaning plan

Hari 76: Data Cleaning Implementation
- Handle missing values
- Remove duplicates
- Fix data types
- Standardize formats
- Handle outliers
- Validate transformations

Hari 77: Documentation & Reporting
- Create data dictionary
- Document cleaning steps
- Before/after statistics
- Quality improvement metrics
- Reproducible cleaning script
- Final cleaned dataset

### MINGGU 12-13: Statistical Analysis & EDA (Hari 78-91)

**Hari 78: Descriptive Statistics Deep Dive**
* Central tendency measures
* Dispersion measures
* Distribution shapes
* Skewness dan kurtosis

Project: Dataset Profiler
- Automated statistical profiling
- Distribution analysis
- Outlier summary
- Correlation overview
- Statistical report generation

**Hari 79: Exploratory Data Analysis (EDA) Framework**
* EDA best practices
* Systematic exploration approach
* Question formulation
* Hypothesis generation

Project: EDA Template Creator
- Create reusable EDA notebook
- Automated data overview
- Visual exploration
- Statistical summaries
- Insight documentation template

**Hari 80: Correlation Analysis**
* Correlation types (Pearson, Spearman)
* Correlation matrices
* Correlation vs causation
* Multicollinearity detection

Project: Feature Correlation Analyzer
- Calculate correlations
- Heatmap visualization
- Identify highly correlated features
- Correlation strength interpretation
- Feature selection recommendations

**Hari 81: Distribution Analysis**
* Normal distribution
* Skewed distributions
* Distribution tests
* Q-Q plots

Project: Distribution Fitter
- Test multiple distributions
- Goodness-of-fit tests
- Visual distribution comparison
- Best-fit distribution identification
- Distribution parameters estimation

**Hari 82: Hypothesis Testing - Part 1**
* Statistical hypothesis concept
* t-tests (one sample, two sample)
* p-values interpretation
* Type I and Type II errors

Project: A/B Test Analyzer
- Compare two groups (A/B test data)
- Perform t-test
- Calculate effect size
- Interpret results
- Recommendation report

**Hari 83: Hypothesis Testing - Part 2**
* Chi-square tests
* ANOVA
* Non-parametric tests
* Test selection guide

Project: Marketing Campaign Evaluator
- Test effectiveness across multiple segments
- ANOVA untuk multiple groups
- Chi-square untuk categorical associations
- Statistical conclusions
- Business recommendations

**Hari 84: Confidence Intervals**
* Confidence interval concept
* Calculating CIs untuk means
* Sample size determination
* Margin of error

Project: Survey Results Analyzer dengan CI
- Calculate statistics dari survey
- Compute confidence intervals
- Visualize dengan error bars
- Interpret uncertainty
- Sample size recommendations

**Hari 85: Data Visualization Best Practices**
* Chart type selection
* Color theory
* Accessibility considerations
* Storytelling dengan data

Project: Visualization Style Guide
- Create company visualization standards
- Reusable plotting functions
- Color palettes
- Template library
- Example gallery

**Hari 86: Advanced Matplotlib Customization**
* Custom styles
* Annotation advanced
* Inset plots
* Animation basics

Project: Interactive Report Generator
- Customized plot templates
- Annotation untuk insights
- Multiple visualization types
- Professional styling
- PDF report export

**Hari 87: Seaborn Advanced Techniques**
* FacetGrid dan PairGrid
* Complex statistical plots
* Custom color palettes
* Theme customization

Project: Multi-dimensional Data Explorer
- FacetGrid untuk multi-variable analysis
- Statistical relationship plots
- Custom visualization themes
- Comprehensive visual report

**Hari 88: Introduction to Plotly**
* Interactive plotting basics
* Plotly Express
* Hover information
* Export interactive plots

Project: Interactive Sales Dashboard
- Interactive line charts
- Drill-down capabilities
- Hover details
- Filter options
- Export to HTML

**Hari 89-91: Comprehensive EDA Project (3 hari)**

Project: Complete Exploratory Data Analysis
Hari 89: Initial Exploration
- Load dan understand dataset
- Data cleaning if needed
- Basic statistics
- Initial visualizations
- Question formulation

Hari 90: Deep Analysis
- Distribution analysis
- Correlation studies
- Hypothesis testing
- Segment analysis
- Pattern identification

Hari 91: Insights & Presentation
- Key findings summary
- Interactive visualizations
- Statistical evidence
- Business recommendations
- Professional presentation
- Jupyter notebook documentation

### MINGGU 14-15: Introduction to Automation (Hari 92-105)

**Hari 92: OS Module Deep Dive**
* File system operations
* Environment variables
* Process management
* Path operations

Project: Automated Backup System
- Backup files based on extension
- Create dated backup folders
- Log backup operations
- Verify backup integrity
- Email notification (simple)

**Hari 93: pathlib Advanced**
* Modern path handling
* Glob patterns
* Iterating directories
* Path methods

Project: File Organization System
- Scan downloads folder
- Organize by type dan date
- Rename files systematically
- Move to structured folders
- Generate organization report

**Hari 94: Subprocess Module**
* Running external commands
* Capturing output
* Error handling
* Shell vs direct execution

Project: System Information Gatherer
- Run system commands
- Collect system stats
- Parse command output
- Generate system report
- Schedule checks

**Hari 95: Scheduling with Python**
* Time-based automation
* schedule library
* Cron-like functionality
* Background tasks

Project: Daily Report Automation
- Schedule daily data fetch
- Process dan analyze data
- Generate report
- Send email notification
- Log automation runs

**Hari 96: Working with Zip Files**
* Creating zip archives
* Extracting zip files
* Password protection
* Archive manipulation

Project: Backup Compression Tool
- Compress folders to zip
- Organize backups by date
- Clean old backups
- Encryption option
- Space savings report

**Hari 97: Email Automation - Part 1**
* SMTP basics
* Sending simple emails
* Email formatting
* Attachments

Project: Email Report Sender
- Generate data report
- Format as HTML email
- Attach CSV files
- Send to recipients list
- Delivery confirmation log

**Hari 98: Email Automation - Part 2**
* Email templates
* Reading emails (IMAP)
* Processing attachments
* Email filtering

Project: Automated Email Processor
- Read emails dari inbox
- Extract attachments
- Process data files
- Save to database
- Send confirmation replies
- Error notifications

**Hari 99: Web Scraping - Part 1**
* HTML structure basics
* requests library review
* BeautifulSoup introduction
* Parsing HTML

Project: News Headline Scraper
- Scrape news website
- Extract headlines dan links
- Parse publication dates
- Save to CSV
- Schedule daily scraping

**Hari 100: Web Scraping - Part 2**
* CSS selectors
* Navigating HTML tree
* Handling dynamic content basics
* Scraping ethics

Project: Product Price Tracker
- Scrape product prices
- Track price changes
- Alert on price drops
- Historical price chart
- Deal finder

**Hari 101: Working with Forms & POST Requests**
* HTML forms understanding
* POST request data
* Session handling
* Authentication basics

Project: Automated Form Submitter
- Login to website
- Fill forms programmatically
- Submit data
- Handle responses
- Session management

**Hari 102: PDF Generation**
* PDF creation dengan reportlab
* Adding text dan images
* Tables in PDF
* Multi-page PDFs

Project: Automated Invoice Generator
- Load invoice data
- Generate professional PDF
- Include company logo
- Table formatting
- Batch invoice creation

**Hari 103: Excel Automation Advanced**
* openpyxl deep dive
* Cell formatting
* Charts in Excel
* Formulas manipulation

Project: Automated Excel Dashboard
- Import data to Excel
- Apply formatting
- Create pivot tables
- Generate charts
- Save workbook
- Email to stakeholders

**Hari 104-105: Automation Project Integration (2 hari)**

Project: End-to-End Automation Pipeline
Hari 104: Pipeline Setup
- Daily data collection (web scraping)
- Data cleaning dan validation
- Store in database
- Error handling

Hari 105: Reporting & Distribution
- Generate analysis reports
- Create visualizations
- PDF report generation
- Email distribution
- Logging dan monitoring
- Schedule automation

### MINGGU 16-17: Advanced Automation & APIs (Hari 106-120)

**Hari 106: REST API Basics Review**
* HTTP methods deep dive
* Status codes
* Headers dan authentication
* API documentation reading

Project: Multi-API Data Aggregator
- Connect to 3+ public APIs
- Aggregate data
- Handle rate limits
- Store results
- Error recovery

**Hari 107: Working with JSON APIs**
* Complex JSON parsing
* Nested data extraction
* JSON to DataFrame conversion
* API pagination handling

Project: GitHub Repository Analyzer
- Fetch repository data via GitHub API
- Parse complex JSON
- Extract statistics
- Create analysis report
- Track changes over time

**Hari 108: API Authentication Methods**
* API keys
* OAuth basics
* Token management
* Secure credential storage

Project: Authenticated API Client
- Implement API key authentication
- OAuth 2.0 flow
- Token refresh
- Secure config management
- Multiple API integration

**Hari 109: Rate Limiting & Retries**
* Rate limit detection
* Exponential backoff
* Request queuing
* Caching strategies

Project: Robust API Wrapper
- Rate-limited API client
- Automatic retry logic
- Caching mechanism
- Request logging
- Performance metrics

**Hari 110: Building Simple APIs - Flask Intro**
* Flask installation
* Creating routes
* Returning JSON
* GET dan POST handling

Project: Personal Data API
- Create API untuk your data
- CRUD endpoints
- JSON responses
- Basic validation
- API documentation

**Hari 111: Database Integration - SQLite Advanced**
* Database design basics
* Complex queries
* Transactions
* Performance optimization

Project: Data Warehouse Builder
- Design database schema
- Import data dari multiple sources
- Create efficient queries
- Data integrity checks
- Backup automation

**Hari 112: Environment Variables & Config Management**
* python-decouple library
* .env files
* Configuration best practices
* Secret management

Project: Configurable Application
- Refactor previous projects
- Use environment variables
- Multiple environment support
- Secure credential storage
- Config validation

**Hari 113: Logging Best Practices**
* Logging module advanced
* Log levels
* Log formatting
* Log rotation

Project: Enterprise Logging System
- Structured logging
- Different log levels
- File dan console output
- Log rotation
- Error tracking

**Hari 114: Command Line Interfaces (CLI)**
* argparse library
* Click library introduction
* User-friendly CLI design
* Help documentation

Project: Data Analytics CLI Tool
- CLI untuk data operations
- Multiple commands (load, clean, analyze, export)
- Arguments dan options
- Progress indicators
- Help documentation

**Hari 115: Virtual Environments & Package Management**
* venv dan virtualenv
* requirements.txt
* pip advanced usage
* Package distribution basics

Project: Project Setup Automation
- Virtual environment creator
- Auto-install dependencies
- Project structure generator
- Documentation templates
- Git initialization

**Hari 116-118: Capstone Automation Project (3 hari)**

Project: Automated Business Intelligence System
Hari 116: Data Collection Layer
- Multiple data source integration
- Web scraping untuk external data
- API data fetching
- Database storage
- Schedule automation

Hari 117: Processing & Analysis Layer
- Data cleaning pipeline
- Statistical analysis
- Trend detection
- Alert system
- Quality checks

Hari 118: Reporting & Distribution Layer
- Automated dashboard generation
- PDF report creation
- Email distribution
- Slack/Teams notification
- Error handling dan logging
- Complete documentation

**Hari 119: Testing & Debugging**
* Unit testing introduction
* pytest basics
* Test coverage
* Debugging automation scripts

Project: Test Suite untuk Previous Projects
- Write unit tests
- Integration tests
- Test automation
- Coverage report
- CI/CD basics introduction

**Hari 120: Month 4 Review & Portfolio**
* Review all automation concepts
* Best practices consolidation
* Portfolio organization

Project: Portfolio Showcase
- GitHub repository organization
- Professional README files
- Documentation enhancement
- Demo videos/screenshots
- Project categorization
- Skills showcase

---

## Progress Check - Hari 120
Setelah 120 hari, Anda seharusnya sudah:
✓ Master Pandas untuk data manipulation
✓ Comfortable dengan statistical analysis
✓ Bisa membuat comprehensive visualizations
✓ Understand automation workflows
✓ Experience dengan APIs dan web scraping
✓ Database integration skills
✓ Professional portfolio di GitHub

**Next Phase Preview**: Hari 121-180 akan fokus pada advanced analytics, machine learning basics, advanced automation workflows, dan cloud integration.
