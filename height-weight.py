import random
import plotly.figure_factory as ff
import statistics
import plotly.graph_objects as go
import csv
import pandas as pd

df=pd.read_csv("data.csv")
height_list=df["Height(Inches)"].tolist()
weight_list=df["Weight(Pounds)"].tolist()

hmean=statistics.mean(height_list)
hmedian=statistics.median(height_list)
hmode=statistics.mode(height_list)
hstd_deviation=statistics.stdev(height_list)

wmean=statistics.mean(weight_list)
wmedian=statistics.median(weight_list)
wmode=statistics.mode(weight_list)
wstd_deviation=statistics.stdev(weight_list)

print("The Mean(Average) of Height =", hmean)
print("The Median of Height =", hmedian)
print("The Mode of Height =", hmode)
print("The Standard Deviation of Height =", hstd_deviation)

print("The Mean(Average) of Weight =", wmean)
print("The Median of Weight =", wmedian)
print("The Mode of Weight =", wmode)
print("The Standard Deviation of Weight =", wstd_deviation)

hfirststd_dev_start,hfirststd_dev_end= hmean-hstd_deviation,hmean+hstd_deviation
hsecondstd_dev_start,hsecondstd_dev_end= hmean-(2*hstd_deviation),hmean+(2*hstd_deviation)
hthirdstd_dev_start,hthirdstd_dev_end= hmean-(3*hstd_deviation),hmean+(3*hstd_deviation)

wfirststd_dev_start,wfirststd_dev_end= wmean-wstd_deviation,wmean+wstd_deviation
wsecondstd_dev_start,wsecondstd_dev_end= wmean-(2*wstd_deviation),wmean+(2*wstd_deviation)
wthirdstd_dev_start,wthirdstd_dev_end= wmean-(3*wstd_deviation),wmean+(3*wstd_deviation)

hvalues_under_firststd_dev=[result for result in height_list if result > hfirststd_dev_start and result < hfirststd_dev_end]
hvalues_under_secondstd_dev=[result for result in height_list if result > hsecondstd_dev_start and result < hsecondstd_dev_end]
hvalues_under_thirdstd_dev=[result for result in height_list if result > hthirdstd_dev_start and result < hthirdstd_dev_end]

wvalues_under_firststd_dev=[result for result in weight_list if result > wfirststd_dev_start and result < wfirststd_dev_end]
wvalues_under_secondstd_dev=[result for result in weight_list if result > wsecondstd_dev_start and result < wsecondstd_dev_end]
wvalues_under_thirdstd_dev=[result for result in weight_list if result > wthirdstd_dev_start and result < wthirdstd_dev_end]

print("{}% of the data lies between first std_deviation of height".format(len(hvalues_under_firststd_dev)*100/len(height_list)))
print("{}% of the data lies between second std_deviation of height".format(len(hvalues_under_secondstd_dev)*100/len(height_list)))
print("{}% of the data lies between third std_deviation of height".format(len(hvalues_under_thirdstd_dev)*100/len(height_list)))

print("{}% of the data lies between first std_deviation of weight".format(len(wvalues_under_firststd_dev)*100/len(weight_list)))
print("{}% of the data lies between second std_deviation of weight".format(len(wvalues_under_secondstd_dev)*100/len(weight_list)))
print("{}% of the data lies between third std_deviation of weight".format(len(wvalues_under_thirdstd_dev)*100/len(weight_list)))

fig=ff.create_distplot([height_list],["Height"], show_hist=False)
fig.add_trace(go.Scatter(x=[hmean,hmean], y=[0,0.18], mode="lines", name="hmean"))
fig.add_trace(go.Scatter(x=[hfirststd_dev_start,hfirststd_dev_start], y=[0,0.18], mode="lines", name="1st std_deviation start of height"))
fig.add_trace(go.Scatter(x=[hfirststd_dev_end,hfirststd_dev_end], y=[0,0.18], mode="lines", name="1st std_deviation end of height"))
fig.show()

fig=ff.create_distplot([weight_list],["Weight"], show_hist=False)
fig.add_trace(go.Scatter(x=[wmean,wmean], y=[0,0.05], mode="lines", name="wmean"))
fig.add_trace(go.Scatter(x=[wfirststd_dev_start,wfirststd_dev_start], y=[0,0.05], mode="lines", name="1st std_deviation start of weight"))
fig.add_trace(go.Scatter(x=[wfirststd_dev_end,wfirststd_dev_end], y=[0,0.05], mode="lines", name="1st std_deviation end of weight"))
fig.show()