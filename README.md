# Investigating Goal Scoring Patterns in International Soccer

## Overview

This project investigates a data-driven hypothesis in international football: **Are more goals scored in women’s matches than men’s?** Drawing from years of watching and reporting on international tournaments, this analysis seeks to validate a common perception using statistical testing.

The focus is limited to **official FIFA World Cup matches** (excluding qualifiers and friendlies) played **since 2002-01-01**. The analysis uses match data scraped from a trusted online source and performs a non-parametric statistical test to assess the difference in average goals per match.

## Key Question

**Are more goals scored in women’s international soccer matches than in men’s?**

🧪 **Statistical Hypotheses**

- **Null Hypothesis (H₀):** The mean number of goals scored in women’s matches is equal to that of men’s  
- **Alternative Hypothesis (Hₐ):** The mean number of goals scored in women’s matches is **greater** than in men’s  
- **Significance Level (α):** 0.10

---

## Data Cleaning and Preparation

🖥️ **Script:** [`1_clean_match_data.py`](https://github.com/yourusername/football_score_analysis/blob/main/1_clean_match_data.py)

- Loaded `men_results.csv` and `women_results.csv`  
- Filtered data to only include **FIFA World Cup matches since 2002-01-01**  
- Created a new `goals_scored` column by summing `home_score` and `away_score`  
- Labeled each row with a gender `group` for comparison  
- Visualized match goal distributions with histograms

---

## Statistical Analysis

🖥️ **Script:** [`2_goals_hypothesis_test.py`](https://github.com/yourusername/football_score_analysis/blob/main/2_goals_hypothesis_test.py)

- Compared average goals per match between men's and women's games  
- Checked assumptions for parametric tests (e.g., normality, equal variances)  
- Due to non-normal distribution and unequal variance, used **Mann-Whitney U test** (non-parametric)  
- Conducted a **one-sided test** to assess whether women’s matches tend to have more goals

📈 **Test Summary:**

- **Test Used:** Mann–Whitney U (independent, one-sided)  
- **Null Hypothesis (H₀):** Distribution of goals in women’s matches is the same as or less than men’s  
- **Alternative Hypothesis (Hₐ):** Distribution of goals in women’s matches is stochastically greater  
- **p-value:** *< 0.10*  
- **Decision:** Reject H₀

💡 **Conclusion:**

- The test provides statistically significant evidence (at the 10% level) that **more goals are scored in women’s international matches** compared to men’s.
- Although the effect size is moderate, the results support the original hypothesis and justify deeper journalistic exploration.

---

## Key Findings

📊 **Goal Distributions:**

- Women’s matches show a **higher average** number of goals and a wider distribution  
- Men’s matches are **more tightly clustered** around 2–3 goals  
- Outlier matches (8+ goals) are more common in women’s competitions

🔎 **Visuals (Generated in Scripts):**

- Side-by-side histograms of total match goals by gender  
- Boxplots comparing goal distributions  
- ECDF plots showing cumulative goal probabilities

---

## Editorial Implications

✍️ These results suggest valuable angles for reporting:

1. **Spectator Value:**  
   More goals could indicate higher entertainment value in women’s matches—an insight for marketing and broadcasting.

2. **Tactical Contrast:**  
   Higher scoring might reflect tactical differences, such as open play styles or defensive structuring across genders.

3. **Evolution Over Time:**  
   Consider examining whether scoring patterns have narrowed or widened over the past two decades.

---

## Technical Details

- **Language:** Python 3.12.6  
- **Libraries:** pandas, matplotlib, seaborn, scipy, numpy  
- **Statistical Test:** Mann–Whitney U (via `scipy.stats.mannwhitneyu`)  
- **Development Tools:** JupyterLab, VS Code  
- **Data Source:** Scraped from [international football results archive](https://www.example-source.com)  
- **Data Format:** CSV (`men_results.csv`, `women_results.csv`)

---

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT)

---

## Author

Developed by [st3kin](https://github.com/st3kin)  
Project repository: [https://github.com/st3kin/football_score_analysis](https://github.com/st3kin/football_score_analysis)

