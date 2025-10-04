# Global Temperature Anomaly Analysis (1850–2015)

This project analyzes *global average temperature anomalies* from 1850 to 2015 using Python, Pandas, and Matplotlib.  
It visualizes temperature trends over time, calculates decade averages, applies a rolling average, and highlights the hottest and coldest recorded years.  

---

##  Overview

Climate change is one of the most pressing issues of our time.  
Using historical temperature data (annual.csv), this project aims to:

- Visualize *global temperature anomalies* over the years.  
- Compute and display *average anomalies per decade*.  
- Analyze long-term trends with a *10-year rolling average*.  
- Highlight the *hottest* and *coldest* years in the dataset.

---

##  Features

 Plot yearly temperature anomalies from 1850–2015  
 Calculate and visualize decade-wise average temperatures  
 Apply a 10-year rolling mean to smooth trends  
 Identify and highlight the hottest and coldest years  
 Clean, well-labeled Matplotlib visualizations  

---

##  Project Structure

├── data/
│ └── annual.csv # Temperature dataset (Year, Mean)
├── temperature_analysis.py # Main Python script
└── README.md # Project documentation

yaml
Copy code

---

##  Requirements

Make sure you have Python 3.8+ installed, then install dependencies:

```bash
pip install pandas matplotlib
 How It Works
Data Import:

python
Copy code
df = pd.read_csv("data/annual.csv")
Line Plot (Annual Temperature Anomaly):
Visualizes yearly temperature changes globally.

Bar Chart (Decade Average):
Groups years into decades and plots average anomalies.

Rolling Average (10-Year):
Adds a smoothed red trend line for long-term insight.

Highlight Hottest & Coldest Years:
Annotates the most extreme years on the chart.

 Usage
Run the analysis script:

bash
Copy code
python temperature_analysis.py
It will display four plots sequentially:

Global Average Temperature (1850–2015)

Average Temperature Anomaly by Decade

Global Temperature Anomaly with 10-Year Rolling Average

Global Temperature Anomaly with Highlights (Hottest & Coldest Years)

 Example Outputs
⿡ Annual Temperature Anomaly
A red line graph showing year-by-year global temperature changes.

⿢ Decade Average Temperature
A bar chart comparing each decade’s mean anomaly.

⿣ Rolling Average Trend
A smoother long-term view showing the warming trend.

⿤ Hottest & Coldest Highlights
A clear visualization with the hottest and coldest years labeled.

 Key Code Snippets
python
Copy code
# Calculate decade averages
df["Decade"] = (df["Year"] // 10) * 10
decade_avg = df.groupby("Decade")["Mean"].mean()

# Rolling average
df["Rolling10"] = df["Mean"].rolling(window=10).mean()

# Highlight hottest and coldest years
hottest = df.loc[df["Mean"].idxmax()]
coldest = df.loc[df["Mean"].idxmin()]
 Dataset Info
The dataset annual.csv should contain the following columns:

Column	Description
Year	Year of record (e.g., 1850, 1851, ...)
Mean	Annual mean temperature anomaly (°C)

## Example:

Year	Mean
1850	-0.45
1851	-0.38
1852	-0.36

 ## Insights
A clear upward temperature trend since the mid-20th century.

The last few decades show the highest anomalies on record.

The 10-year rolling average highlights accelerated warming.

 ## Author
Azmi (Germany)
📍 Python Data Visualization Enthusiast


 License
This project is licensed under the MIT License — feel free to use, modify, and distribute with attribution.

 Acknowledgments
Dataset Source: [kaggle]

Inspired by open climate data visualizations.

Built using Python, Pandas, and Matplotlib.

yaml
Copy code
