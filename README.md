# MoneyParce

MoneyParce is a full-stack personal finance platform for tracking budgets, syncing financial data, analyzing spending behavior, and generating intelligent financial insights.

## Overview

MoneyParce helps users manage their financial life through a clean web interface that combines budgeting tools, transaction tracking, portfolio analytics, and AI-powered text analysis. The project was built as a finance-focused software platform using a modern full-stack architecture.

## Features

- User dashboard for budgeting, expenses, and financial summaries
- REST API backend for managing financial data and user workflows
- PostgreSQL/MongoDB-based storage for structured financial records
- Plaid-style bank syncing workflow for account and transaction ingestion
- Caching layers for faster dashboard and analytics performance
- NLP pipelines for financial text classification and sentiment analysis
- Dockerized deployment workflow for reproducible local/cloud setup

## Tech Stack

**Frontend:** React, JavaScript, HTML/CSS  
**Backend:** Python, Flask, REST APIs  
**Databases:** PostgreSQL, MongoDB  
**ML/NLP:** OpenAI models, spaCy, scikit-learn  
**Infrastructure:** Docker, AWS EC2  

## Project Highlights

- Built a Flask/React financial platform with REST APIs, database-backed storage, Docker, and AWS EC2 deployment.
- Integrated bank-sync-style workflows, caching layers, and automated pipelines for budgeting and portfolio analytics.
- Developed NLP pipelines achieving 95%+ sentiment classification accuracy on financial text data.

## Running Locally

```bash
git clone https://github.com/abiswas14/MoneyParce.git
cd MoneyParce
