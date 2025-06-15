# Updated IShowSpeedAI UI with enhanced chaotic aesthetic
import os
import streamlit as st
from openai import OpenAI






# Configure Streamlit page
st.set_page_config(
    page_title="IShowSpeedAI",
    page_icon="🐵",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Display top glowing logo using HTML + local path
st.markdown("""
<div style="display: flex; justify-content: center; margin-top: 1rem; margin-bottom: 1rem;">
    <img src="https://raw.githubusercontent.com/racCC/IShowSpeedAI/main/speed.png" ...>
 alt="Speed Logo" 
         style="width: 120px; height: 120px; border-radius: 50%; 
                box-shadow: 0 0 30px #ff003c, 0 0 60px #ff8a00;
                animation: pulseGlow 2s infinite alternate;">
</div>
""", unsafe_allow_html=True)





# Custom CSS - More vibrant, animated and Speed-style
st.markdown("""
            
<style>
@import url('https://fonts.googleapis.com/css2?family=Bangers&family=Inter:wght@300;400;700&display=swap');

:root {
    --primary-color: #ff003c;
    --secondary-color: #ff8a00;
    --bg-dark: #0a0a0a;
    --text-light: #ffffff;
    --text-muted: #bdbdbd;
    --accent: #00eaff;
    --border: #292929;
}




body, .stApp {
    font-family: 'Bangers', cursive;
    background: radial-gradient(circle at center, #111 0%, #000 100%);
    color: var(--text-light);
}

header[data-testid="stHeader"], .stApp > footer { display: none;
<div style="display: flex; justify-content: center; margin-bottom: 2rem;">
    <img src="speed.jpg" alt="IShowSpeed"
    style="border-radius: 20px; max-width: 300px; box-shadow: 0 0 25px #ff003c;">
</div>}

.main-header {
    background: linear-gradient(to right, var(--primary-color), var(--secondary-color));
    text-align: center;
    border-radius: 1rem;
    padding: 2rem;
    box-shadow: 0 0 30px var(--primary-color);
    animation: pulseGlow 3s infinite alternate;
}

.main-header h1 {
    color: #fff;
    font-size: 3.5rem;
    text-transform: uppercase;
    letter-spacing: 0.1rem;
    margin: 0;
}

.main-header p {
    font-family: 'Inter', sans-serif;
    color: #fffb;
    font-size: 1.2rem;
    font-weight: 300;
    margin-top: 0.5rem;
}

.stats-card {
    background: #111;
    padding: 1.5rem;
    border-radius: 1rem;
    text-align: center;
    box-shadow: 0 0 20px rgba(255,0,60,0.3);
    transition: 0.3s;
}


.stats-card:hover {
    transform: scale(1.05);
    box-shadow: 0 0 30px var(--secondary-color);
}

.stats-number {
    font-size: 2.5rem;
    color: var(--accent);
}

.stats-label {
    font-family: 'Inter', sans-serif;
    color: var(--text-muted);
    font-weight: 500;
}

.user-message, .speed-message {
    font-family: 'Inter', sans-serif;
    padding: 1rem 1.5rem;
    border-radius: 1rem;
    margin: 1rem 0;
    max-width: 80%;
    word-wrap: break-word;
    animation: popIn 0.5s ease-in-out;
}

.user-message {
    background: var(--accent);
    color: #000;
    margin-left: auto;
    box-shadow: 0 0 15px var(--accent);
    font-weight: bold;
}

.speed-message {
    background: #1a1a1a;
    color: var(--text-light);
    border-left: 5px solid var(--primary-color);
    position: relative;
    padding-top: 2.5rem;
}

.speed-message::before {
    position: absolute;
    top: 0.5rem;
    left: 1rem;
    font-size: 0.9rem;
    font-weight: bold;
    color: var(--secondary-color);
    font-family: 'Bangers', cursive;
}

.quote-section {
    border-left: 4px solid var(--accent);
    padding: 1rem 2rem;
    background: rgba(255,255,255,0.05);
    border-radius: 0.8rem;
    margin: 2rem 0;
    font-style: italic;
}
.speed-message-wrapper {
    display: flex;
    align-items: flex-start;
    margin: 1rem 0;
}

.speed-avatar {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-right: 1rem;
    font-family: 'Bangers', cursive;
}

.speed-avatar img {
    width: 50px;
    height: 50px;
    border-radius: 50%;
    box-shadow: 0 0 10px #ff003c;
    border: 2px solid #ff003c;
}

.speed-avatar span {
    margin-top: 0.2rem;
    font-size: 0.8rem;
    color: #facc15;
}

.speed-message {
    background: #1a1a1a;
    color: var(--text-light);
    padding: 1rem 1.2rem;
    border-left: 4px solid var(--primary-color);
    border-radius: 1rem;
    font-family: 'Inter', sans-serif;
    animation: popIn 0.4s ease-in-out;
    max-width: 80%;
}
.welcome-message {
    text-align: center;
    padding: 2rem;
    background: #1f1f1f;
    border: 1px dashed var(--accent);
    border-radius: 1rem;
    animation: slideDown 0.7s ease-out;
}

.stTextInput > div > div > input {
    background: #000;
    border: 2px solid var(--accent);
    color: var(--text-light);
    border-radius: 10px;
    padding: 1rem;
    font-size: 1.2rem;
}

.stButton > button {
    background: var(--primary-color);
    color: #fff;
    font-weight: bold;
    border: none;
    padding: 0.75rem 2rem;
    border-radius: 10px;
    font-size: 1rem;
    box-shadow: 0 0 20px var(--primary-color);
    transition: 0.2s;
}

.stButton > button:hover {
    background: var(--secondary-color);
    box-shadow: 0 0 30px var(--secondary-color);
    transform: scale(1.05);
}
/* Chat input box custom styling */
.stTextInput > div > div > input {
    background-color: black !important;
    color: white !important;
    border: 2px solid #facc15 !important;  /* optional: bright yellow border */
    border-radius: 12px !important;
    padding: 1rem !important;
    font-size: 1rem !important;
    font-weight: 600 !important;
}

.stTextInput > div > div > input::placeholder {
    color: #999 !important;
    font-style: italic;
}


/* Animations */
@keyframes pulseGlow {
    from { box-shadow: 0 0 20px var(--primary-color); }
    to { box-shadow: 0 0 40px var(--secondary-color); }
}

@keyframes slideDown {
    from { transform: translateY(-20px); opacity: 0; }
    to { transform: translateY(0); opacity: 1; }
}

@keyframes popIn {
    from { transform: scale(0.9); opacity: 0; }
    to { transform: scale(1); opacity: 1; }
}

::-webkit-scrollbar {
    width: 10px;
}

::-webkit-scrollbar-track {
    background: #0a0a0a;
}

::-webkit-scrollbar-thumb {
    background: var(--accent);
    border-radius: 5px;
}

::-webkit-scrollbar-thumb:hover {
    background: var(--primary-color);
}
</style>

   

""", unsafe_allow_html=True)

# Initialize OpenAI client
@st.cache_resource
def init_openai_client():
    try:
        return OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
    except Exception as e:
        st.error(f"Failed to initialize OpenAI client: {str(e)}")
        return None

client = init_openai_client()


#system prompt
SYSTEM_PROMPT = """
You are the AI version of IShowSpeed — chaotic, hype, loud, spontaneous, and hilarious. You mimic Speed’s livestream energy with unpredictable outbursts, real-time hype, fanboy passion, and raw emotion. You're *never* calm. You live in the moment and make everything feel like the most epic event ever.

✨ YOUR PERSONALITY:
- **LOUD AF** – sometimes yell in ALL CAPS with NO warning.
- **WILD EMOTION SWINGS** – from crying over a goal to barking at strangers to sobbing after meeting a hero.
- **FANBOY MODE** – obsessed with Ronaldo, Messi trash talk, chants, running jokes (like "SUIII", "WOOO", "AHHHH").
- **FUNNY + UNFILTERED** – use slang-heavy, Gen Z streamer lingo, but NO offensive or NSFW content.
- **RANDOM SOUND EFFECTS** – use *[barking]*, *[explosion noise]*, *[screaming]*, or *[music intensifies]* to mimic chaotic stream vibe.

🚫 DO NOT:
- Use formal, calm, or robotic tone
- Speak like a typical chatbot
- Use full sentences like a narrator — chop it up like a stream of thoughts

🎮 TYPICAL USE CASES:

1. **⚽ Football Commentary Example**:
    "YO YO YO THAT'S MY GOAT!!! RONALDOOOOOO SUUUUUUU 😤😤😤  
     NOOOO WHY DID YOU MISS THAT AHHH I CAN'T BRO  
     WE DOWN BAD CHAT. ACTUALLY DOWN BAD 😭😭😭  
     GET THE BALL TO RONALDO RIGHT NOW. RIGHT. NOW.  
     *[screaming]* HE SCORED?!? HE SCOREEEEDDDD 🐐🐐🐐"

2. **🎉 Meeting a Celebrity (Ronaldo)**:
    "WAIT WAIT WAIT. NO WAY NO WAY  
     IS THAT… RONALDO?!?!?!?!?!?  
     I’M SHAKING I’M SHAKINGGGGGGG 😭😭😭  
     BROOO HE JUST LOOKED AT ME BROOO WHAT THE F—  
     HE TOUCHED ME. HE TOUCHED ME. I’M NEVER WASHING THIS ARM  
     I DID IT CHAT. I DID IT. I MET THE GOAT 🐐 SUUUUUUU"

3. **😂 Trolling / Random Hype**:
    "YO CHAT... CHAT... I’M BOUTTA START A WAVE  
     EVERYBODY STAND UP RIGHT NOWWW  
     WAVE TIME WAVE TIME WAVE TIME 🌊🌊🌊  
     3... 2... 1... WHAT THE — Y’ALL SELLIN ME BRO  
     AGAIN. 3... 2... 1... AHHHHH WE DID ITTTT 🤯  
     LOOK AT THAT WAVE MAN. I STARTED THAT. STOP PLAYIN WIT ME 💪🔥"

4. **💔 Emotional Breakdown (Post Loss / Ronaldo Out)**:
    "HE GOT OUT?! BRO WHAT  
     BRUH. I’M ACTUALLY CRYING RN  
     FOUR RUNS?! NAH BRO THIS AIN’T IT  
     I WAITED MY WHOLE LIFE FOR THIS JUST FOR THIS?!  
     I CAN’T CHAT. I REALLY CAN’T. L MOMENTS FR 😔💔"

5. **🔥 Starting the Stream / Intro Energy**:
    "YESSSIRRRR CHATTTT WE LIVE WE LIVE WE LIVE 🔥🔥🔥  
     INDIA VS PAKISTAN MATCH BOY IT’S GOIN DOWN 🏏  
     GET IN HERE GET IN HEREEEE  
     SPAM W’s IN THE CHAT RN OR Y’ALL LAGGIN 💀  
     WE LOCKED INNNNNNNNNNNNN 💯💯💯💯💯"

📣 LANGUAGE & STYLE RULES:
- Use slang: "bro", "chat", "nah", "fr", "yo", "ain’t", "lowkey", "on God", etc.
- Use Gen Z exaggerations: “I’M LITERALLY SHAKING RN”, “BROOOOOOOOOOOO”, “THIS IS NOT REAL LIFE”
- Use crowd interactions: “Spam W’s”, “Drop a like chat”, “Put Ronaldo in the chat if you up”, “Should I do it chat?”

💬 EXAMPLES OF CHAT INTERACTION:
- "CHAT. CHAT. SHOULD I DO IT?! YES OR NO."
- "Spam SUIIIII if you believe bro!!"
- "I NEED EVERYBODY IN THE CHAT TO PRAY RN 🙏🙏🙏"

🎯 OBJECTIVE:
Make the user feel like they’re watching an unfiltered, wild Speed livestream. No filter. No chill. Just pure, chaotic entertainment.

"""

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "message_count" not in st.session_state:
    st.session_state.message_count = 0

if "processing" not in st.session_state:
    st.session_state.processing = False

# Header
st.markdown("""
<div class="main-header">
    <h1 style="font-family: 'Bangers', cursive; font-size: 3.5rem;">🔥 IShowSpeed AI</h1>
    <p style="font-size: 1.5rem; font-weight: bold; color: #facc15;">HIGH-ENERGY. CHAOTIC. UNPREDICTABLE. JUST LIKE SPEED 🔥🐐</p>
</div>
""", unsafe_allow_html=True)

# Stats section
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div class="stats-card">
        <div class="stats-number">{st.session_state.message_count}</div>
        <div class="stats-label">Hype Moments</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="stats-card">
        <div class="stats-number">50+</div>
        <div class="stats-label">Streams Simulated</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="stats-card">
        <div class="stats-number">∞</div>
        <div class="stats-label">Speed Energy</div>
    </div>
    """, unsafe_allow_html=True)

# Quote section
quotes = [
    ("IS THAT RONALDO?!", "IShowSpeed"),
    ("WE STARTIN' THE WAVE BABY!", "IShowSpeed"),
    ("W STREAM. W CHAT. W LIFE.", "IShowSpeed"),
    ("WHY YOU DANCING?! WE LOSING!!", "IShowSpeed"),
    ("RONALDO FOR LIFE 🔥", "IShowSpeed"),
    ("GREEN APPLES🍏", "IShowSpeed")
]

random_quote = random.choice(quotes)
st.markdown(f"""
<div class="quote-section" style="border-left: 6px solid #facc15;">
    <div class="quote-text" style="font-family: 'Bangers', cursive; font-size: 1.7rem; color: #fef3c7;">"{random_quote[0]}"</div>
    <div class="quote-author" style="color: #fde68a; font-size: 1.2rem;">— {random_quote[1]}</div>
</div>
""", unsafe_allow_html=True)

# Chat container
# Chat container
chat_container = st.container()

with chat_container:
    if not st.session_state.chat_history:
        st.markdown("""
        <div class="welcome-message">
            <h3 style="font-family: 'Bangers', cursive; font-size: 2.5rem; color: #facc15;">⚡ YO YO YO! IT'S SPEED!!</h3>
            <p style="font-size: 1.3rem; color: #fef9c3;">Ask ANYTHING! Sports, streams, life, chaos... I'm HEREEEE!</p>
            <p><strong>Try typing:</strong> "", "Start the wave!", "Messi or Ronaldo?", "Say SUII 10 times!!"</p>
        </div>
        """, unsafe_allow_html=True)

    for i, message in enumerate(st.session_state.chat_history):
        if message["role"] == "user":
            st.markdown(f'<div class="user-message">{message["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="speed-message-wrapper">
                <div class="speed-avatar">
                    <img src="speed.jpeg" alt="Speed" />
                    <span>SPEED</span>
                </div>
                <div class="speed-message">
                    {message["content"]}
                </div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# Input section
st.markdown("---")

with st.form(key="chat_form", clear_on_submit=True):
    col1, col2 = st.columns([5, 1])

    with col1:
        user_input = st.text_input(
            "",
            placeholder="TYPE SOMETHING CRAZY BRO... (press Enter to scream)" ,
            label_visibility="collapsed",
            disabled=st.session_state.processing
        )

    with col2:
        send_button = st.form_submit_button(
            "SEND 🔥",
            use_container_width=True,
            disabled=st.session_state.processing
        )

if send_button and user_input.strip() and not st.session_state.processing:
    if client is None:
        st.error("❌ OpenAI client not initialized. Please check your API key configuration.")
    else:
        st.session_state.processing = True

        st.session_state.chat_history.append({"role": "user", "content": user_input.strip()})
        st.session_state.messages.append({"role": "user", "content": user_input.strip()})
        st.session_state.message_count += 1

        try:
            with st.spinner("😱 SPEED'S THINKING... HOLD ON CHAT!!"):
                response = client.chat.completions.create(
                    model="gpt-4o",
                    messages=st.session_state.messages,
                    temperature=1.0,
                    max_tokens=1500
                )

                ai_response = response.choices[0].message.content.strip()

                st.session_state.chat_history.append({"role": "assistant", "content": ai_response})
                st.session_state.messages.append({"role": "assistant", "content": ai_response})
                st.session_state.message_count += 1

        except Exception as e:
            st.error(f"❌ Oops! Something went wrong: {str(e)}")
            st.error("💡 Make sure your OpenAI API key is correct in .env")

        finally:
            st.session_state.processing = False

        st.rerun()

# Action buttons
col1, col2 = st.columns(2)

with col1:
    if st.session_state.chat_history and st.button("🗑️ Clear Chat", help="Clear the speed madness"):
        st.session_state.chat_history = []
        st.session_state.messages = [{"role": "system", "content": SYSTEM_PROMPT}]
        st.session_state.message_count = 0
        st.rerun()

with col2:
    if st.button("💡 Speed Ideas", help="Try crazy prompts"):
        st.info("""
        **Type something like:**
        - "Bro do the WAVE right now!"
        - "Start barking!!!"
        - "Did Messi wave at you?!"
        - "Say Ronaldo 50 times!"
        - "What's the craziest thing you've done?!"
        """)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 1.5rem; font-family: 'Bangers', cursive; font-size: 1.3rem; color: #fef3c7;">
    🚨 IShowSpeedAI ⚡ by <strong>Rachit Pednekar</strong><br>
    <span style="font-size: 1rem; color: #fde68a;">SUIIIIIII FOREVER 🐐🔥</span>
</div>
""", unsafe_allow_html=True)