import pandas as pd
import csv
import plotly.figure_factory as ff
import statistics
import plotly.graph_objects as go
import random

df = pd.read_csv("data.csv")
data = df["temp"].tolist()
population_mean = statistics.mean(data)
population_sd = statistics.stdev(data)
print("Population mean is: ",population_mean)
print("Population Standard DEvation is :-",population_sd)

dataset = []
for i in range (0,1000):
    random_index = random.randint(0,len(data))
    value = data[random_index]
    dataset.append(value)

mean = statistics.mean(dataset)
std_devation = statistics.stdev(dataset)

print("sample mean :-" ,mean)
print ("standard Devation of sample :-", std_devation)

# fig = ff.create_distplot([data],["Temp"],show_hist=False )
# fig.add_trace(go.Scatter(x=[population_mean , population_mean ], y=[0, 0.2], mode="lines", name="MEAN"))
# fig.show()


