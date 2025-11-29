# n8n Workflow Popularity System 🚀

A data-driven system that aggregates and analyzes popularity signals from **YouTube**, the **n8n Community Forum**, and **Google Trends** to identify high-impact automation workflows.

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Production-green)
![Status](https://img.shields.io/badge/Status-Live-success)

## 📋 Overview
This project solves the challenge of finding "what's actually popular" in the n8n automation space. Instead of just counting views, it calculates **engagement ratios** (Like-to-View) and **community activity** (Forum Replies) to surface workflows that users find genuinely valuable.

## ✨ Features
*   **Multi-Source Ingestion:**
    *   **YouTube Data API v3:** Fetches video metrics (Views, Likes, Comments).
    *   **Discourse API (n8n Forum):** Scrapes top monthly threads for community buzz.
    *   **Google Trends:** Monitors keyword search volume for automation topics.
*   **Smart Metrics:** Implements a `like_to_view_ratio` to filter out clickbait.
*   **REST API:** Fully documented API built with **FastAPI**.
*   **Automation:** Built-in scheduler (Cron-job style) for daily data updates.
*   **Segmentation:** Filters data by Platform (YouTube/Forum/Google) and Country (US/IN/Global).

## 📸 Live Evidence
Here is the system running and returning real data via the Swagger UI:


## 🛠️ Tech Stack
*   **Core:** Python 3.9+
*   **API Framework:** FastAPI + Uvicorn
*   **Data Fetching:** `google-api-python-client`, `requests`, `pytrends`
*   **Scheduling:** `schedule` library
*   **Storage:** Local JSON Database (No SQL setup required for demo)

---

## 🚀 Setup & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Smita-04/n8n-popularity-system.git
cd n8n-popularity-system
