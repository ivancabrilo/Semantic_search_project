# 🎥 Semantic YouTube Search

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.95+-green)
![Docker](https://img.shields.io/badge/Docker-✔-blue)
![AWS ECS](https://img.shields.io/badge/Deployed-AWS%20ECS-orange)

---

## 📖 Overview
I built a **YouTube semantic search tool** using **cosine similarity** (trained on titles and transcripts of each video) for the **Kurzgesagt** YouTube channel.  

🔍 The results are based on the **similarity between the user’s input query** and a combination of video transcripts + titles.  

⚡ I exposed the similarity model through a **FastAPI service**, containerized it with **Docker**, and deployed it on **AWS ECS** to make the API publicly accessible.

---

## ✨ Features
- 🔎 **Semantic Search** → finds videos by meaning, not just keywords  
- ⚡ **FastAPI Backend** → lightweight, high-performance API  
- 📦 **Dockerized** → portable & reproducible deployments  
- ☁️ **AWS ECS Deployment** → API hosted in the cloud  
- 🎨 **Gradio UI** → interactive frontend for quick demo  

---

## 📸 Demo

![Demo](https://github.com/user-attachments/assets/39e6b115-3390-4651-86f7-848f96af763a)

---

## 🛠️ Tech Stack
- **Python** (FastAPI, scikit-learn, NumPy, Pandas)  
- **Gradio** (frontend demo)  
- **Docker** (containerization)  
- **AWS ECS** (deployment)  

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/ivancabrilo/Semantic_search_project-.git
cd Semantic_search_project-
