# 🚀 Gen AI Full Stack Project

A complete **Generative AI based application** that automates:

* 🎥 AI Video Generation
* 📝 SEO Blog Creation
* 🏗 Architecture Design from Requirements

Built using **FastAPI (Backend)** and **React (Frontend UI)**.

---

# 📌 Features

## 🎥 AI Video Generator

* Generates script from trending topics
* Produces video/text output stored in backend

## 📝 SEO Blog Generator

* Generates SEO keywords
* Creates optimized blog content

## 🏗 Architecture Generator

* Converts business requirements into:

  * Modules
  * Database Schema
  * API Endpoints
  * Pseudocode

---

# 🛠 Tech Stack

* **Frontend:** React (Vite)
* **Backend:** FastAPI (Python)
* **AI:** OpenAI API

---

# 📂 Project Structure

```id="u4x5x8"
gen_ai_project/
│── backend/
│     ├── app.py
│     ├── output.mp4
│     ├── blog_output.txt
│     └── architecture_output.txt
│
│── frontend/
│     ├── index.html
│     ├── package.json
│     ├── vite.config.js
│     └── src/
│           ├── main.jsx
│           └── App.jsx
│
│── requirements.txt
```

---

# ⚙️ Setup Instructions

## 🔹 1. Clone the Repository

```id="x3l2z1"
git clone <your-repo-link>
cd gen_ai_project
```

---

## 🔹 2. Backend Setup

```id="k9w2x1"
cd backend
pip install -r ../requirements.txt
```

Run server:

```id="y7p1r9"
python -m uvicorn app:app --reload
```

Open API docs:

```id="r3m8t1"
http://127.0.0.1:8000/docs
```

---

## 🔹 3. Frontend Setup

```id="v8c2n4"
cd frontend
npm install
npm run dev
```

Open:

```id="m5z9a2"
http://localhost:5173
```

---

# 🌐 API Endpoints

| Feature                | Endpoint                 |
| ---------------------- | ------------------------ |
| Video Generator        | `/generate-video`        |
| Blog Generator         | `/generate-blog`         |
| Architecture Generator | `/generate-architecture` |

---

# 📁 Output Files

Generated outputs are stored inside the **backend folder**:

* 🎥 `output.mp4` → Generated video
* 📝 `blog_output.txt` → Blog content
* 🏗 `architecture_output.txt` → Architecture details

---

# 🧠 Key Highlights

* Single backend (simplified design)
* Centralized output storage
* Full-stack integration
* AI-powered automation pipeline

---

# 👨‍💻 Author

**Virendra Kumar Verma**

* Full Stack Developer
* React | Python | FastAPI

---

# ⭐ Note

This is a **prototype project** demonstrating Generative AI pipelines.
It can be extended into a production-level system.

---
