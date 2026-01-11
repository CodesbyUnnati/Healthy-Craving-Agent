# 🥗 Healthy Craving Agent

**An AI-powered Nutritionist & Chef that turns your guilty pleasures into healthy treasures.**

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![LangGraph](https://img.shields.io/badge/AI-LangGraph-orange)
![FastAPI](https://img.shields.io/badge/API-FastAPI-green)
![Docker](https://img.shields.io/badge/Container-Docker-blue)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-red)

## 📖 About
This application is an **AI Microservice** designed to help users make healthier food 🥗 choices. It doesn't just give generic advice; it uses a sophisticated **AI Agent workflow** to:
1.  **Analyze** the user's craving (e.g., "I want a double cheeseburger 🍔") to identify unhealthy components.
2.  **Validate** if the input is actually food (rejecting nonsense inputs).
3.  **Generate** a specific, creative "Healthy Swap" recipe that mimics the flavor profile of the original craving using nutritious ingredients 🥦.

---

## 🏗️ How I Built This (The Architecture)
This project was built in **6 Engineering Phases**, moving from a simple script to a cloud-native application:

* **Phase 1: The Brain 🧠 (LangGraph & Groq)**
    * Designed a State Graph with two AI Agents: `Analyst` (identifies problems) and `Chef` (creates solutions).
    * Used **Llama 3.3** via Groq for ultra-fast inference.
    * Implemented **Conditional Logic** to reject invalid inputs (e.g., "12345").
* **Phase 2: The API (FastAPI)**
    * Wrapped the AI logic🤔 in a robust REST API using **FastAPI**.
    * Implemented **Pydantic** models for strict data validation.
* **Phase 3: Containerization (Docker)**
    * Packaged the application into a lightweight Docker🐳 image (`python:slim`).
    * Configured environment variables for secure API key injection.
* **Phase 4: Orchestration (Kubernetes & Helm)**
    * Deployed the container to a local Kubernetes cluster using **Kind**.
    * Created a custom **Helm Chart** to manage deployment configuration and secrets.
* **Phase 5: The Interface (Streamlit)**
    * Built a user-friendly frontend in Python using **Streamlit**.
    * Refactored the app to allow direct module imports for faster cloud performance.
* **Phase 6: Cloud Deployment**
    * Deployed the final application to **Streamlit Community Cloud** for global access.

---

## 🚀 Getting Started

### Prerequisites
* Python 3.9+
* Docker 🐳 (for container mode)
* A [Groq API Key](https://console.groq.com/) (Free)

### 2. Setup Secrets
Create a .env file in the root directory:

```
GROQ_API_KEY="gsk_your_actual_key_here"
```

## 🏃‍♀️ Run Method 1: Streamlit 

Run the application directly on your machine with a beautiful UI.

### 🔗- https://healthy-craving-agent.streamlit.app/ 

## 🐳 Run Method 2: Docker (Production Style)

Run the backend API in an isolated container.

 1. Clone the Repository
```bash
git clone [https://github.com/CodesbyUnnati/Healthy-Craving-Agent.git](https://github.com/CodesbyUnnati/Healthy-Craving-Agent.git)
cd Healthy-Craving-Agent
```

2. Build the Image
```
docker build -t healthy-agent:v1 .
```
3. Run the Container

```
docker run -p 8000:8000 --env-file .env healthy-agent:v1
```
4. Test the API Go to http://localhost:8000/docs to see the Swagger UI.
5. On the UI, Click on POST, expand it and click on Try it Out, then, in the Request Body, Add your craving and click Execute. You should see your response in the Responses box.

## ☸️ Run Method 3: Kubernetes (DevOps Style)
Deploy to a local cluster using Helm.

1. Create Cluster (using Kind)

```
kind create cluster --name healthy-cluster
kind load docker-image healthy-agent:v1 --name healthy-cluster
```
2. Install via Helm (Ensure your API key is set in charts/healthy-agent/values.yaml)
```
helm upgrade --install my-agent ./charts/healthy-agent \
  --set env.GROQ_API_KEY="paste_your_actual_API_KEY_here"
```
3. Forward Port

```
kubectl port-forward service/my-agent-healthy-agent 8080:80
```
Access the API at http://localhost:8080/docs.

## 📂 Project Structure

```
Healthy-Craving-Agent/
├── app/
│   ├── graph.py       # The AI Logic (LangGraph)
│   ├── frontend.py    # The User Interface (Streamlit)
│   ├── main.py        # The API Server (FastAPI)
│   └── models.py      # Data Validation (Pydantic)
├── charts/            # Helm Charts for Kubernetes
├── Dockerfile         # Blueprint for building the container
├── requirements.txt   # Python dependencies
└── README.md          # You are here!
```
