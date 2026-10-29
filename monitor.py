import pandas as pd
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset

reference = pd.DataFrame({
    "age": [22, 25, 30, 35, 40, 45, 50, 28, 33, 38],
    "salary": [20, 25, 30, 40, 50, 55, 60, 27, 35, 45]
})
current = pd.DataFrame({
    "age": [50, 55, 60, 62, 65, 58, 52, 61, 57, 63],
    "salary": [70, 75, 80, 85, 90, 78, 72, 82, 77, 88]
})

report = Report(metrics=[DataDriftPreset()])
report.run(reference_data=reference, current_data=current)
report.save_html("drift_report.html")
print("Report saved: drift_report.html")