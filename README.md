# E-commerce AI Services

A Flask-based REST API providing various AI-powered services for an e-commerce platform.

## Features

- User Authentication (Customer/Seller)
- AI Chatbot using Google's Gemini
- Image-based Product Recommendation System
- Anomaly Detection for Product Images
- Product Search by Type
- Sentiment Analysis for Reviews

## Prerequisites

- Python 3.8+
- MongoDB
- Google API Key (for chatbot)

## Installation

1. Clone the repository:
```bash
git clone "your https link"
cd e-commerce-ai-services
```


3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Project Structure

```
FLASK/
├── app/
│   ├── models/         # AI models
│   ├── routes/         # API endpoints
│   ├── utils/          # Utility functions
│   └── config/         # Configuration
├── data/               # Data files
├── run.py             # Application entry point
└── requirements.txt   # Dependencies
```
