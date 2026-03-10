# 🚀 AI Cold Email Generator

An AI-powered tool that automatically generates **personalized cold emails for job applications** by analyzing job descriptions and matching them with relevant portfolio projects.

This project uses **Large Language Models (LLMs), semantic search, and vector databases** to automate a task that usually takes 15–20 minutes.

---

## 📌 Features

- Scrapes job descriptions from company career pages
- Extracts roles, skills, and requirements using LLM
- Matches relevant projects from a portfolio using vector search
- Generates a professional **personalized cold email**
- Simple UI built with Streamlit

---

## 🧠 How It Works

1. **Job Scraping**  
   The user enters a job posting URL.

2. **Information Extraction**  
   The system uses an LLM to extract:
   - Job role
   - Required skills
   - Responsibilities

3. **Semantic Search**  
   The system searches a portfolio database using **vector similarity search**.

4. **Cold Email Generation**  
   A personalized cold email is generated including relevant portfolio links.

---

## 🛠 Tech Stack

- Python
- LangChain
- Llama 3.1 (via Groq)
- ChromaDB
- Streamlit

---
