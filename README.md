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
<img width="1920" height="1080" alt="Screenshot (583)" src="https://github.com/user-attachments/assets/e70faf8f-ac35-4e6c-8c25-ff863cb4b7e6" />
<img width="1920" height="1080" alt="Screenshot (584)" src="https://github.com/user-attachments/assets/190d93a8-d38d-42e3-978e-107b8307e059" />
<img width="1920" height="1080" alt="Screenshot (585)" src="https://github.com/user-attachments/assets/5a43a153-6481-4f06-8fe2-458a9dd507df" />
<img width="1920" height="1080" alt="Screenshot (586)" src="https://github.com/user-attachments/assets/840fbc0d-7264-417e-a1cb-aff368332930" />


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
