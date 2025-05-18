Netflix Clone with AI Chatbot and Text-to-Speech
A full-stack Netflix clone application built with a custom login page and AI-powered features integrated using IBM Cloud services. After logging in, users are redirected to a home page that includes a chatbot (IBM Watson Assistant) and voice interaction through IBM Watson Text-to-Speech (TTS).

🚀 Features
🔐 Login Page with Username & Password authentication

🏠 Home Page with sleek UI and Netflix-like layout

💬 AI Chatbot using IBM Watson Assistant

🗣️ Text-to-Speech (TTS) using IBM Watson TTS

🎨 Built with HTML, CSS, JavaScript, React.js

🛠️ Backend using Node.js + Express.js

🛠️ Tech Stack
Frontend	Backend	AI/Cloud Services
HTML, CSS, JS	Node.js, Express.js	IBM Watson Assistant
React.js		IBM Watson Text-to-Speech

🔧 Installation
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-username/netflix-clone-ai.git
cd netflix-clone-ai
2. Backend Setup
Go to the backend/ directory:

bash
Copy
Edit
cd backend
npm install
Add your IBM Watson API keys and credentials in a .env file:

ini
Copy
Edit
WATSON_ASSISTANT_APIKEY=your_api_key
WATSON_ASSISTANT_URL=your_url
WATSON_TTS_APIKEY=your_tts_api_key
WATSON_TTS_URL=your_tts_url
Start the backend server:

bash
Copy
Edit
node index.js
3. Frontend Setup
In a new terminal, go to the frontend/ directory:

bash
Copy
Edit
cd ../frontend
npm install
npm start
🧠 IBM Watson Services
Watson Assistant (Chatbot)
Used to power a conversational chatbot embedded on the home page. It helps simulate user interaction like FAQs, suggestions, etc.

Watson Text-to-Speech
Used to convert chatbot responses into audio, enabling users to hear chatbot replies for better accessibility.

🖼️ Screenshots
Login Page	Home Page with Chatbot

📁 Project Structure
php
Copy
Edit
netflix-clone-ai/
├── backend/
│   └── index.js
├── frontend/
│   ├── src/
│   │   ├── App.js
│   │   └── components/
│   │       ├── LoginPage.js
│   │       └── HomePage.js
│   └── public/
├── .env
├── README.md
✨ Future Improvements
Integrate face authentication using TensorFlow.js or face-api.js

Improve chatbot intelligence using custom-trained intents

Add recommendation engine for personalized movie lists

🙌 Acknowledgements
IBM Watson Cloud

React.js

Node.js

Express.js

📬 Contact
sanjeevni dhir
📧sanjeevnidhir05@gmail.com
🔗 https://www.linkedin.com/in/sanjeevni-dhir-441143281/
