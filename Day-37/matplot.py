'''
import matplotlib.pyplot as plt
h=[1,2,3,4,5]
v=[50,60,70,80,90]
plt.plot(h,v,color="red",marker="o",linestyle="-",linewidth=1,alpha=1,label="visitors")
plt.title("websites visitors per hour")
plt.xlabel("hour of day")
plt.ylabel("number of visitors")
plt.legend()
plt.grid(True,linestyle="--",alpha=0.5)
plt.show()

import matplotlib.pyplot as plt
pro=["lap","mobile","tablet","headphones","watch"]
sales=[250,400,150,300,180]
plt.bar(pro,sales,color="green",edgecolor='red',alpha=0.5,width=0.5)
plt.title("product sales comparsion")
plt.xlabel("products")
plt.ylabel("unitssold")
plt.show()

import matplotlib.pyplot as plt
pro=["lap","mobile","tablet","headphones","watch"]
sales=[250,400,150,300,180]
plt.barh(pro,sales,color='pink')
plt.title("product sales comparsion")
plt.xlabel("products")
plt.ylabel("unitssold")
plt.show()

import matplotlib.pyplot as plt
marks=[45,55,60,72,68,90,55,67,70,
       85,40,60,75,78,82,95,50,65,
       58,73,77,69,71,88,92,59,70]
plt.hist(marks,bins=8,histtype='bar',color='red',edgecolor='black',density=False)
plt.title("Distribution of Student marks")
plt.xlabel("Marks Range")
plt.ylabel("Number of Students")
plt.show()

import matplotlib.pyplot as plt
brands=['apple','samsung','xiamoi','oppo','others']
sheet=[30,25,20,10,15]
plt.pie(sheet,
        labels=brands,
        autopct="%d%%",
        startangle=180,
        colors=["gold","skyblue","lightcoral","lightgreen","violet"],
        explode=[0,0.3,0,0,0],
        shadow='True')
plt.title("Mobile Phone Market Share")
plt.show()

import matplotlib.pyplot as plt
spend=[2,4,5,7,8,10,11,12]
sales=[27,25,28,35,40,48,50,52]
profit=[200,250,90,350,40,80,500,520]
colors=[8,1,2,3,5,6,7,4]
plt.scatter(spend,sales,
            s=profit,
            c=colors,
            cmap='Reds',
            alpha=0.8,
            edgecolors="black",
            linewidths=1.2
            )
plt.title("Advertising Spend vs Sales (with Color & Size)", fontsize=14, fontweight="bold")
plt.xlabel("Ad Spend ($1000s)", fontsize=12)
plt.ylabel("Sales ($1000s)", fontsize=12)

plt.colorbar(label="Sales Value")

plt.grid(True, linestyle="--", alpha=0.2)
plt.show()


import matplotlib.pyplot as plt

scores = [
    [ 70, 85, 90, 92, 88, 76, 95,9],
    [65, 70, 68, 72, 75, 80, 85, 78],
    [90, 92, 94, 96, 88, 91, 89, 93],
    [62, 60, 61, 90, 65, 63, 67, 61],
    [70, 85, 8, 50, 92, 91, 100, 89]
]
plt.boxplot(scores,
            patch_artist=True,
            medianprops=dict(color="red"),
            whiskerprops=dict(color="green"),
            capprops=dict(color="black"),
            notch=False,
            vert=False,
            labels=["A", "B", "C", "D", "E"])

plt.title("Exam Scores Distribution Across Classes")
plt.xlabel("Classes")
plt.ylabel("Scores")
plt.grid(True, linestyle="--", alpha=0.7)

plt.show()


import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
visitors = [120, 150, 170, 200, 180, 220, 250]

plt.fill_between(days, visitors,
                 color="skyblue", alpha=0.5,
                 label="Website Visitors")

plt.plot(days, visitors, color="blue", linewidth=1)
plt.title("Website Visitors Over a Week")
plt.xlabel("Day of Week")
plt.ylabel("Number of Visitors")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.show()


import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data = np.array([
    [30, 32, 31, 29, 28, 27, 26],
    [33, 34, 32, 30, 29, 28, 27],
    [35, 36, 34, 33, 31, 30, 29],
    [37, 38, 35, 34, 32, 31, 30],
    [36, 37, 34, 32, 31, 30, 29]
])

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

weeks = ["Week 1", "Week 2", "Week 3", "Week 4", "Week 5"]

sns.heatmap(data,
            annot=True,
            fmt=".2f",
            cmap="YlOrRd",
            linewidths=0.5,
            xticklabels=days,
            yticklabels=weeks)

plt.title("Weekly Temperature Heatmap", fontsize=14, fontweight="bold")
plt.xlabel("Days of the Week")
plt.ylabel("Weeks")
plt.show()


import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
sales = [120, 135, 150, 160, 170, 200, 220]
profit = [30, 40, 45, 50, 55, 70, 80]

plt.figure(figsize=(10, 8))

plt.subplot(2, 2, 1)
plt.plot(days, sales, marker="o", color="blue")
plt.title("Sales Over Days")
plt.grid(True)

plt.subplot(2, 2, 2)
plt.bar(days, sales, color="orange")
plt.title("Sales Bar Chart")

plt.subplot(2, 2, 3)
plt.scatter(sales, profit, color="green", s=100, edgecolors="black")
plt.title("Sales vs Profit")

plt.subplot(2, 2, 4)
plt.pie(sales, labels=days, autopct="%1.1f%%", startangle=90)
plt.title("Sales Distribution")

plt.tight_layout()
plt.show()

'''