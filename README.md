# 🔥 IShowSpeedAI – Chat with the Wildest AI on the Internet!

An interactive Streamlit chatbot that mimics the chaotic, high-energy personality of **IShowSpeed** – the GOAT of internet madness. Built for pure fun, memes, and hype. This isn't just a chatbot... it's a digital *stream explosion* 💥

🔴 **Live Demo**: [ishowspeedai.streamlit.app](https://ishowspeedai.streamlit.app)

---

## 🧰 Tools You’ll Need

- 🧠 **OpenAI GPT-4o** – For generating wild, Speed-style replies  
- 🌐 **Streamlit** – For building the frontend UI  
- 🎨 **Custom CSS** – For glowing chaotic aesthetics  
- 🔐 **Streamlit Secrets** – To securely load your OpenAI API key  
- 🐍 **Python (>=3.9)** – Your backend language  

---

## 📁 Project Structure

IShowSpeedAI/
├── speedpersona.py # Main Streamlit app
├── requirements.txt # All dependencies
├── .streamlit/
│ └── secrets.toml # Store your OpenAI API key
├── speed.png # Avatar image
└── README.md

yaml
Copy
Edit

---

## 🚀 How To Run Locally

### 1️⃣ Clone the Repo

```bash
git clone https://github.com/racCC/IShowSpeedAI.git
cd IShowSpeedAI
2️⃣ Set Up Virtual Environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
3️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4️⃣ Add Your API Key
Create a .streamlit/secrets.toml file:

toml
Copy
Edit
OPENAI_API_KEY = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxx"
5️⃣ Run the App
bash
Copy
Edit
streamlit run speedpersona.py
Then open your browser at: http://localhost:8501

✨ Features
🔥 Fully custom Speed-like GPT persona (chaotic, hyped, loud)

🎨 Glowing UI & animated visuals

🖼️ Custom avatars & quote-of-the-day section

💬 Maintains chat history in real-time

🧠 Built with GPT-4o and optimized for entertainment

🧠 Customize It For Any Creator
Want to create your own AI persona?

Edit the SYSTEM_PROMPT in speedpersona.py with a new tone

Swap the images and CSS for a new aesthetic

That’s it — your clone is LIVE ⚡

🛠 Deployment
You can host this app on Streamlit Cloud for free:

Push your code to GitHub

Go to streamlit.io/cloud

Connect your GitHub repo

Add your OpenAI key in secrets.toml via the Streamlit Secrets Manager

💥 BOOM! It’s live.

🙌 Credits
Built with ❤️ by Rachit Pednekar