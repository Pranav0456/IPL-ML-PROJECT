# 🏏 IPL Win Predictor

An end-to-end Machine Learning web application that predicts the win probability of the chasing team in an Indian Premier League (IPL) match based on the current match situation.

---

## 📌 Project Overview
During the second innings of a T20 cricket match, the momentum shifts rapidly with every ball and wicket. This project utilizes historical IPL match data to dynamically estimate match outcome probabilities based on variables such as:
- Batting Team & Bowling Team
- Host City
- Target Score
- Current Score & Overs Completed
- Wickets Lost

---

## 🛠️ Tech Stack & Libraries
- **Language:** Python
- **Machine Learning:** Scikit-Learn (Logistic Regression Pipeline)
- **Data Manipulation:** Pandas, NumPy
- **Web Interface:** Streamlit
- **Deployment:** Streamlit Community Cloud

---

## ⚙️ How It Works
1. **Feature Engineering:** Computes dynamic metrics like Runs Left, Balls Left, Wickets Remaining, Current Run Rate (CRR), and Required Run Rate (RRR).
2. **Preprocessing Pipeline:** Encodes categorical team and city names using `OneHotEncoder` and standardizes input parameters.
3. **Probability Modeling:** A calibrated classification model evaluates real-time game states to return the winning probabilities for both teams.

---

## 🚀 Local Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Pranav0456/IPL-ML-PROJECT.git](https://github.com/Pranav0456/IPL-ML-PROJECT.git)
   cd IPL-ML-PROJECT
