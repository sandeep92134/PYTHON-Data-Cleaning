# import pandas, numpy, and matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
nls97 = pd.read_csv("https://raw.githubusercontent.com/sandeep92134/PYTHON-Data-Cleaning/master/Chapter%205/datasets/nls97.csv")
nls97.set_index("personid", inplace=True)
covidtotals = pd.read_csv("https://raw.githubusercontent.com/sandeep92134/PYTHON-Data-Cleaning/master/Chapter%205/datasets/covidtotals.csv", parse_dates=["lastdate"])

covidtotals.set_index("iso_code", inplace=True)

# do a violin plot of sat verbal scores
sns.violinplot(nls97.satverbal, color="wheat", orient="v")
plt.title("Violin Plot of SAT Verbal Score")
plt.ylabel("SAT Verbal")
plt.text(0.08, 780, 'outlier threshold', horizontalalignment='center', size='x-small')
plt.text(0.065, nls97.satverbal.quantile(0.75), '3rd quartile', horizontalalignment='center', size='x-small')
plt.text(0.05, nls97.satverbal.median(), 'Median', horizontalalignment='center', size='x-small')
plt.text(0.065, nls97.satverbal.quantile(0.25), '1st quartile', horizontalalignment='center', size='x-small')
plt.text(0.08, 210, 'outlier threshold', horizontalalignment='center', size='x-small')
plt.text(-0.4, 500, 'frequency', horizontalalignment='center', size='x-small')
plt.show()

# get some descriptives
nls97.loc[:, ['weeksworked16','weeksworked17']].describe()

# show weeks worked for 2016 and 2017
myplt = sns.violinplot(data=nls97.loc[:, ['weeksworked16','weeksworked17']])
myplt.set_title("Violin Plots of Weeks Worked")
myplt.set_xticklabels(["Weeks Worked 2016","Weeks Worked 2017"])
plt.show()

# do a violin plot of wage income by gender
nls97["maritalstatuscollapsed"] = nls97.maritalstatus.\
  replace(['Married','Never-married','Divorced','Separated','Widowed'],\
  ['Married','Never Married','Not Married','Not Married','Not Married']) 
sns.violinplot(nls97.gender, nls97.wageincome, hue=nls97.maritalstatuscollapsed, scale="count")
plt.title("Violin Plots of Wage Income by Gender and Marital Status")
plt.xlabel('Gender')
plt.ylabel('Wage Income 2017')
plt.legend(title="", loc="upper center", framealpha=0, fontsize=8)
plt.tight_layout()
plt.show()

# do a violin plot of weeks worked by degree attainment
nls97 = nls97.sort_values(['highestdegree'])
myplt = sns.violinplot('highestdegree','weeksworked17', data=nls97)
myplt.set_xticklabels(myplt.get_xticklabels(), rotation=60, horizontalalignment='right')
myplt.set_title("Violin Plots of Weeks Worked by Highest Degree")
myplt.set_xlabel('Highest Degree Attained')
myplt.set_ylabel('Weeks Worked 2017')
plt.tight_layout()
plt.show()

plt.legend(title="", loc="upper center", framealpha=0, fontsize=8)
sns.violinplot(nls97.gender, nls97.wageincome, hue=nls97.maritalstatuscollapsed, scale="count")
sns.violinplot(x=nls97.gender, y=nls97.wageincome, hue=nls97.maritalstatuscollapsed, scale="count")
sns.violinplot(y=nls97.wageincome, x=nls97.gender,  hue=nls97.maritalstatuscollapsed, scale="count")
