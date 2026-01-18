# Student Performance Analysis 📊

## Overview
This project analyzes student performance data using Python and Pandas.
The goal is to understand how different factors like gender affect scores
in reading, writing, and math.

## Tools Used
- Python
- Pandas
- Matplotlib
- Git & GitHub

## Dataset
- students.csv (stored in data/ folder)
- Contains student scores and demographic information

## Key Insights
- Female students scored higher on average in reading and writing
- Male students performed slightly better in math

## How to Run
```bash
python analysis.py


## Output

### Console Output
- Dataset shape: 8 rows × 8 columns
- Columns include:
  - gender
  - math score
  - reading score
  - writing score
- Data types were verified using `df.info()`

### Key Results
- Female students scored highest on average in:
  - Reading
  - Writing
  - Overall performance
- Male students performed slightly better in math

### Visualization
- A bar chart comparing average scores by gender was generated.
- The chart is saved as `gender_scores.png` in the project folder.
