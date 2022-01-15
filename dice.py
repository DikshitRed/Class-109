import random
import plotly.figure_factory as ff
import statistics
import plotly.graph_objects as go

dice_count=[]

for i in range(0,1000):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    dice_count.append(dice1+dice2)

mean=sum(dice_count)/len(dice_count)
median=statistics.median(dice_count)
mode=statistics.mode(dice_count)
std_deviation=statistics.stdev(dice_count)

print("The Mean(Average) =", mean)
print("The Median =", median)
print("The Mode =", mode)
print("The Standard Deviation =", std_deviation)

firststd_dev_start,firststd_dev_end= mean-std_deviation,mean+std_deviation
secondstd_dev_start,secondstd_dev_end= mean-(2*std_deviation),mean+(2*std_deviation)
thirdstd_dev_start,thirdstd_dev_end= mean-(3*std_deviation),mean+(3*std_deviation)

values_under_firststd_dev=[result for result in dice_count if result > firststd_dev_start and result < firststd_dev_end]
values_under_secondstd_dev=[result for result in dice_count if result > secondstd_dev_start and result < secondstd_dev_end]
values_under_thirdstd_dev=[result for result in dice_count if result > thirdstd_dev_start and result < thirdstd_dev_end]

print("{}% of the data lies between first std_deviation".format(len(values_under_firststd_dev)*100/len(dice_count)))
print("{}% of the data lies between second std_deviation".format(len(values_under_secondstd_dev)*100/len(dice_count)))
print("{}% of the data lies between third std_deviation".format(len(values_under_thirdstd_dev)*100/len(dice_count)))

fig=ff.create_distplot([dice_count],["Dice Count"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean], y=[0,0.18], mode="lines", name="mean"))
fig.add_trace(go.Scatter(x=[firststd_dev_start,firststd_dev_start], y=[0,0.18], mode="lines", name="1st std_deviation start"))
fig.add_trace(go.Scatter(x=[firststd_dev_end,firststd_dev_end], y=[0,0.18], mode="lines", name="1st std_deviation end"))
fig.show()