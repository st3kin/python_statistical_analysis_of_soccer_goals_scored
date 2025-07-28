import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pingouin
from scipy.stats import mannwhitneyu

men_results = pd.read_csv('/Users/st3kin/Desktop/Python Projects/football_score_analysis/men_results.csv')

women_results = pd.read_csv('/Users/st3kin/Desktop/Python Projects/football_score_analysis/women_results.csv')


# Converting the date columns

men_results['date'] = pd.to_datetime(men_results['date'])
women_results['date'] = pd.to_datetime(women_results['date'])

# Filtering for FIFA World Cup matches since 2002

men_fifa = men_results[(men_results['tournament'] == 'FIFA World Cup') &
                       (men_results['date'] >= '2002-01-01')]
women_fifa = women_results[(women_results['tournament'] == 'FIFA World Cup') &
                       (women_results['date'] >= '2002-01-01')]

# Creating group and goals_scored columns

men_fifa['group'] = 'men'
women_fifa['group'] = 'women'

men_fifa['goals_scored'] = men_fifa['home_score'] + men_fifa['away_score']
women_fifa['goals_scored'] = women_fifa['home_score'] + women_fifa['away_score']

# Determining distribution using a histogram

men_fifa['goals_scored'].hist()
plt.show()
plt.clf()

# Performing a right-tailed Wilcoxon-Mann-Whitney test with scipy

results = mannwhitneyu(x= women_fifa['goals_scored'],
                       y= men_fifa['goals_scored'],
                       alternative='greater')

# Extracting the p-value as a float

p_val = results.pvalue

# Concluding hypothesis test using sig. level

if p_val <= 0.1:
    result = 'reject'
else:
    result = 'fail to reject'

result_dict = {'p_val': p_val, 'result': result}

print(result_dict)