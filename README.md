# TP03 - Power BI Dashboard

In this lab I built an interactive dashboard with Power BI using the TalkingData dataset from TP02.
The original file is too big, so I used a random sample of 0.5% (about 924K rows).

## Files
- `tp3.pbix`: the Power BI report
- `dashboard.png`: screenshot of the dashboard
- `make_sample.py`: Python code used to take the sample
- Report file: summary of my findings

## What I did
- Cleaned the data in Power Query (data types, duplicates, new columns, renamed columns)
- Created 3 measures: Total Clicks, Downloads, Conversion Rate
- Built KPI cards, bar charts, a column chart and a line chart
- Added slicers for Date and OS Version

## Main result
Only about 0.24% of clicks end with a download.
