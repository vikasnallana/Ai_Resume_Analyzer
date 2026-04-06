# 🤖 AI Resume Analyzer

An AI-powered Resume Analyzer built using **Streamlit** and **Google Gemini API** that evaluates resumes against job roles or descriptions and provides intelligent feedback.

---

## 🚀 Features

### 📄 Resume Upload
- Supports **PDF** and **DOCX** formats
- Extracts text using Python libraries

### 🎯 Job Matching
- Enter a **job role** OR paste a **job description**
- Flexible input handling

### 🤖 AI-Powered Analysis
- Uses **Gemini API** for intelligent evaluation
- Provides:
  - ✅ Match Percentage
  - ✅ Matching Skills
  - ❌ Missing Skills
  - 💪 Strengths
  - 📈 Improvements
  - 💯 ATS Score
  - 📝 Final Feedback

### 🎨 Clean UI
- Built with **Streamlit**
- Dark theme + responsive layout
- Simple and user-friendly interface

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit  
- **Backend:** Python  
- **AI Model:** Google Gemini API  
- **Libraries:**
  - PyPDF2
  - python-docx
  - python-dotenv

---

## 📂 Project Structure

```
resume_analyzer/
│
├── app.py
├── utils.py
├── gemini_api.py
├── requirements.txt
├── .env (not included)
├── .gitignore
```
## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```
In the terminal
git clone https://github.com/your-username/Ai_Resume_Analyzer.git
cd Ai_resume_analyzer

Run - pip install -r requirements.txt

Create a .env file - 
GEMINI_API_KEY=your_api_key_here
place you api key there

Run this command in terminal- 
streamlit run app.py
```
