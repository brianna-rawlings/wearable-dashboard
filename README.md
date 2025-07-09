# WHOOP Wearable Recovery Dashboard 📊💙

This is an interactive data analysis project using my real WHOOP data.  
It explores how my daily training **strain** and workouts affect my **sleep quality**, **sleep stages**, and **next-day HRV**, to understand the readiness loop that WHOOP measures for athletes and everyday users.

---

## 🚀 **Project Overview**

🔍 **Goal:**  
- Combine multiple WHOOP datasets: **Sleep**, **Workouts/Strain**, and **Physiological Cycles (HRV)**
- Analyze how **training load** impacts **recovery**
- Build visualizations for trends, rolling averages, and correlations
- Package it all in a **Streamlit dashboard** so it feels like a real athlete-facing app

---

## 🗂️ **What’s included**

```
📁 /data/
├── sleeps.csv                  ← Exported WHOOP sleep data
├── workouts.csv                ← Daily training strain and energy metrics
├── physiological_cycles.csv    ← HRV and menstrual cycle exports

📁 /notebooks/
├── wearable_sleep_analysis.ipynb     ← Exploratory analysis & visuals
├── sleep_ml.ipynb                    ← Sleep performance prediction model

📁 /app/
├── sleep_dashboard.py                ← Streamlit dashboard interface

📁 /screenshots/
├── rem_vs_deep_sleep.png
├── strain_vs_sleep_perf.png
...

📝 README.md                   ← Project overview & usage
📄 requirements.txt            ← Python dependencies
```




---

## ⚙️ **Key features**

✅ Import & clean **sleep**, **workouts**, and **HRV**  
✅ Create **daily strain score** from multiple workouts  
✅ Shift HRV data to next-day for true readiness insight  
✅ Visualize:
- Strain vs **Sleep Performance %**
![Strain vs Sleep Performance](screenshots/strain_vs_sleep_perf.png)
- Strain vs **REM** or **Deep Sleep**
![REM vs Deep Sleep](screenshots/rem_vs_deep_sleep.png)
- Strain vs **Next Day HRV**
  ![HRV Regression Plot](screenshots/strain_hrv_regression.png)
- **Calories burned** vs Sleep metrics
✅ Build rolling averages to see trends over weeks  
✅ Interactive **Streamlit app** with tabs for:
  - **Sleep Trends**
  - **Readiness Prediction**
  - **Strain vs Recovery**

---

## 📈 **Example questions answered**

💡 How does a high strain day affect my REM or Deep Sleep? 
![REM vs Deep Sleep](screenshots/rem_vs_deep_sleep.png)

💡 Does burning more calories help or hurt my sleep quality?

💡 Does today’s strain impact my HRV tomorrow?  
![Strain vs Next Day HRV](screenshots/strain_vs_hrv.png)

💡 How do rolling averages reveal patterns hidden in daily noise?

---

## 🖥️ Dashboard Preview

Explore the visuals from the app in action:

![Sleep Trends Tab](screenshots/totalsleepduration.png) 
![Strain vs Recovery Tab](screenshots/strain_vs_sleep_perf.png)

---

## 🧩 **Key tools & skills**

- **Python**, **pandas**, **NumPy** — data cleaning & transformation
- **Matplotlib**, **Streamlit** — visualizations & interactive dashboards
- **scikit-learn** — simple regression for predicting readiness scores
- **Time-series merging & rolling averages** — handling physiological signals
- **Sports tech domain knowledge** — readiness, HRV, strain, recovery

---

## 🎓 **What I learned**

- How to handle **real-world messy wearable data** exports (CSV)
- How to align daily strain and next-day HRV for proper cause-effect
- How to turn raw data into clear, actionable **insights** an athlete or coach can use
- How to build a **mini-version** of a real wearable recovery model like WHOOP or Oura’s

---

## 🚀 **How to run**

1️⃣ Clone this repo and create a Python environment  
2️⃣ Install dependencies:
pip install pandas matplotlib scikit-learn streamlit
3️⃣ Run the Streamlit app:
streamlit run sleep_dashboard.py
4️⃣ Upload your own sleeps.csv, workouts.csv, and physiological_cycles.csv
(or use sample data if you don’t have WHOOP)


---

