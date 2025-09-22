import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/annual.csv")

years = df["Year"]
temp = df["Mean"]

plt.figure(figsize=(10,5))
plt.plot(years, temp, color = "red", marker = "o", label = "global_temp anomaly")
plt.xlabel("Years")
plt.ylabel("Temperature (celcius)")
plt.title("Global average temperature (1850-2015)")
plt.grid(True)
plt.legend()
plt.show()


df["Decade"] = (df["Year"] // 10) * 10


decade_avg = df.groupby("Decade")["Mean"].mean()


plt.figure(figsize=(10, 5))
plt.bar(decade_avg.index, decade_avg.values,width=7 , color="skyblue")
plt.xlabel("Decade")
plt.ylabel("Avg Temperature Anomaly (°C)")
plt.title("Average Temperature Anomaly by Decade")
plt.grid(axis="y")
plt.show()


df["Rolling10"] = df["Mean"].rolling(window=10).mean()

plt.figure(figsize=(12, 6))
plt.plot(df["Year"], df["Mean"], color="lightgray", label="Annual Anomaly")
plt.plot(df["Year"], df["Rolling10"], color="red", linewidth=2, label="10-Year Rolling Avg")

plt.xlabel("Year")
plt.ylabel("Temperature Anomaly (°C)")
plt.title("Global Temperature Anomaly with 10-Year Rolling Average")
plt.legend()
plt.grid(True)
plt.show()

hottest = df.loc[df["Mean"].idxmax()]
coldest = df.loc[df["Mean"].idxmin()]

plt.figure(figsize=(12, 6))
plt.plot(df["Year"], df["Mean"], color="lightgray", label="Annual Anomaly")
plt.plot(df["Year"], df["Rolling10"], color="red", linewidth=2, label="10-Year Rolling Avg")


plt.scatter(hottest["Year"], hottest["Mean"], color="darkred", s=80)
plt.text(hottest["Year"], hottest["Mean"]+0.05,
         f"Hottest: {hottest['Year']} ({hottest['Mean']:.2f}°C)",
         color="darkred")


plt.scatter(coldest["Year"], coldest["Mean"], color="blue", s=80)
plt.text(coldest["Year"], coldest["Mean"]-0.15,
         f"Coldest: {coldest['Year']} ({coldest['Mean']:.2f}°C)",
         color="blue")

plt.xlabel("Year")
plt.ylabel("Temperature Anomaly (°C)")
plt.title("Global Temperature Anomaly with Highlights")
plt.legend()
plt.grid(True)
plt.show()
