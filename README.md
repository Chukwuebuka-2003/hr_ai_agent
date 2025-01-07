# 📚 AI-Powered HR Tools

An AI-driven CrewAI Multi-Agent application that offers two powerful tools:
1. **Resume Reviewer:** Upload a resume (PDF or DOCX) and receive professional feedback.
2. **HR Question Assistant:** Ask HR-related questions and get expert advice.

## 🚀 Features
- **Multi-Agent System:** Utilizes CrewAI to coordinate specialized agents for detailed analysis and feedback.
- **Resume Reviewer:** Provides structured analysis and actionable feedback on uploaded resumes.
- **HR Question Assistant:** Delivers practical, scenario-based HR solutions.
- **Seamless Integration:** Powered by advanced LLMs via the Groq API.
- **User-Friendly Interface:** Built with Streamlit for an interactive experience.

## 🛠️ Tech Stack
- **Agents Framework:** CrewAI
- **Frontend:** Streamlit
- **Backend:** Hosted at [https://ebuka-hrai.onrender.com](https://ebuka-hrai.onrender.com)
- **LLM:** Groq API
- **PDF Parsing:** PyPDF2
- **Document Parsing:** python-docx
- **Communication:** REST API

![image](https://github.com/user-attachments/assets/4bc72754-2e13-4422-a3f6-53d0fcd06734)


## 📦 Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Chukwuebuka-2003/hr_ai_agent.git
   cd hr_ai_agent
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up environment variables:
   ```env
   GROQ_API_KEY=your_api_key_here
   ```
4. Start the frontend application:
   ```bash
   streamlit run hrai.py
   ```

## 🌐 Usage
1. Open the Streamlit app in your browser.
2. Navigate between **Resume Reviewer** and **HR Question Assistant** tabs.
3. Upload a resume or ask an HR-related question.
4. Receive AI-powered insights instantly.

## ⚙️ Backend API
The backend is hosted at: **[https://ebuka-hrai.onrender.com](https://ebuka-hrai.onrender.com)**

### Endpoints
- **Resume Reviewer:** `POST /resume`
- **HR Question Assistant:** `POST /hr`

## 🧠 How CrewAI Multi-Agent System Works
- **Agents:** Specialized agents handle tasks like resume analysis, feedback generation, and HR question analysis.
- **Tasks:** Each agent is assigned specific tasks with clear goals and expected outputs.
- **Crew Coordination:** Agents collaborate to produce coherent and high-quality outputs.

## 🤝 Contributions
Contributions are welcome! Fork the repository and submit a pull request.


## 📧 Contact
For any queries, reach out via [GitHub Issues](https://github.com/Chukwuebuka-2003/hr_ai_agent/issues).
