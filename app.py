import streamlit as st
import pickle
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="IPL Win Predictor",
    page_icon="🏏",
    layout="centered"
)

# Custom Styling
st.markdown("""
    <style>
    .main-title {
        text-align: center;
        font-size: 2.2rem;
        font-weight: 800;
        color: #ff4b4b;
        margin-bottom: 0px;
    }
    .sub-title {
        text-align: center;
        color: #888888;
        font-size: 1rem;
        margin-bottom: 25px;
    }
    .card {
        padding: 1.2rem;
        border-radius: 12px;
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        text-align: center;
        margin-bottom: 10px;
    }
    .team-name {
        font-size: 1.15rem;
        font-weight: 600;
    }
    .win-pct {
        font-size: 2.2rem;
        font-weight: 800;
        color: #00e676;
    }
    .loss-pct {
        font-size: 2.2rem;
        font-weight: 800;
        color: #ff5252;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🏏 IPL Match Win Predictor</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Real-time Chase Probability Estimator</div>', unsafe_allow_html=True)

# Load Trained Model
pipe = pickle.load(open('pipe.pkl', 'rb'))

teams = [
    'Sunrisers Hyderabad',
    'Mumbai Indians',
    'Royal Challengers Bangalore',
    'Kolkata Knight Riders',
    'Kings XI Punjab',
    'Chennai Super Kings',
    'Rajasthan Royals',
    'Delhi Capitals'
]

cities = [
    'Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
    'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
    'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
    'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
    'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
    'Sharjah', 'Mohali', 'Bengaluru'
]

col1, col2 = st.columns(2)
with col1:
    batting_team = st.selectbox('🏏 Batting Team (Chasing)', sorted(teams))
with col2:
    bowling_team = st.selectbox('🎯 Bowling Team (Defending)', sorted(teams))

selected_city = st.selectbox('📍 Host City / Venue', sorted(cities))
target = st.number_input('🎯 Target Score to Chase', min_value=1, step=1, value=180)

col3, col4, col5 = st.columns(3)
with col3:
    score = st.number_input('Current Score', min_value=0, step=1, value=50)
with col4:
    overs = st.number_input('Overs Completed', min_value=0.0, max_value=20.0, step=0.1, value=6.0)
with col5:
    wickets = st.number_input('Wickets Fallen', min_value=0, max_value=10, step=1, value=2)

if st.button('⚡ Predict Probability', use_container_width=True):
    if batting_team == bowling_team:
        st.error("Batting आणि Bowling साठी वेगवेगळे संघ निवडा.")
    else:
        runs_left = target - score
        balls_left = 120 - int(overs * 6)
        wickets_left = 10 - wickets

        crr = (score / overs) if overs > 0 else 0.0
        rrr = ((runs_left * 6) / balls_left) if balls_left > 0 else 0.0

        input_df = pd.DataFrame({
            'batting_team': [batting_team],
            'bowling_team': [bowling_team],
            'city': [selected_city],
            'runs_left': [runs_left],
            'balls_left': [balls_left],
            'wickets': [wickets_left],
            'total_runs_x': [target],
            'crr': [crr],
            'rrr': [rrr]
        })

        result = pipe.predict_proba(input_df)
        loss = round(result[0][0] * 100)
        win = round(result[0][1] * 100)

        st.markdown("---")
        st.subheader("📊 Win Probability")

        res1, res2 = st.columns(2)
        with res1:
            st.markdown(f"""
                <div class="card">
                    <div class="team-name">{batting_team}</div>
                    <div class="win-pct">{win}%</div>
                    <small>Chance of Winning</small>
                </div>
            """, unsafe_allow_html=True)
            st.progress(win / 100)

        with res2:
            st.markdown(f"""
                <div class="card">
                    <div class="team-name">{bowling_team}</div>
                    <div class="loss-pct">{loss}%</div>
                    <small>Chance of Winning</small>
                </div>
            """, unsafe_allow_html=True)
            st.progress(loss / 100)