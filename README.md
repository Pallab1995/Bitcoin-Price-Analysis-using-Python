# 📈 Bitcoin Data Analysis Project  
*Time‑Series Analysis • Volatility Study • Trend Exploration • Streamlit Dashboard*

This project provides a complete analysis of **Bitcoin historical price data** using Python.  
It includes visual insights, a Streamlit dashboard, and detailed statistical exploration.

---

## 📌 Overview  
This analysis focuses on:

- Historical price movement trends  
- Candlestick‑based market interpretation  
- Daily percentage volatility  
- Linear vs Log scale comparisons  
- Monthly, quarterly, and yearly averages  
- Detection of dips, recoveries, and consolidation zones  
- Final **Dashboard PDF** for quick review

📄 **Final Dashboard:** `Bitcoin_dashbord_python_Pallab.pdf`

---

## 📁 Project Structure
```
├── Images/                                  ← All visualizations (PNG charts)
├── app.py                                   ← Streamlit dashboard code
├── Bitcoin Data Analysis_Pallab.ipynb        ← Full notebook analysis
├── Bitcoin_dashbord_python_Pallab.pdf        ← Final compiled dashboard
├── bitcoin_price_Training - Training.csv     ← Dataset used
└── requirement.txt                           ← Dependencies
```

Dataset is included as part of the project (`bitcoin_price_Training - Training.csv`).

---

## 📊 Visualization Insights

### 📌 Candlestick Chart – Bitcoin Historical Price
- Price ranged between **$79–$147**  
- Sharp early‑May correction (~46%)  
- Gradual recovery through June  
- Stabilized near **$100–$110**  

---

### 📌 Change in Price Over Time
- Clear higher‑high trend structure  
- Minor corrections throughout  
- Overall bullish pattern  

---

### 📌 Linear vs Log Closing Price Comparison
- Linear scale exposes raw price jumps  
- Log scale shows smoother percentage growth  
- Log helps observe true long‑term trend  

---

### 📌 Daily Percentage Change
- High volatility with multiple >10% movements  
- Early‑May crash shows strongest negative spike  
- Reflects typical crypto price behavior  

---

### 📌 Monthly, Quarterly & Yearly Averages
- Monthly: dip → recovery → continuation trend  
- Quarterly: Q2 lowest, Q3 strong reversal  
- Yearly: long‑term uptrend intact  

---

## ▶️ Running the Streamlit App

Run the dashboard locally:

```bash
streamlit run app.py
```

---

## 🧩 Installation
Install dependencies:

```bash
pip install -r requirement.txt
```

Run the notebook:

```bash
jupyter notebook "Bitcoin Data Analysis_Pallab.ipynb"
```

---

## 👨‍💻 Author  
**Pallab Sharma**  
Data Analyst | Aspiring AI/ML Engineer  

---

## ⭐ Support  
If you found this project helpful, please ⭐ the repository!
