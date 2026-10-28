
import pandas as pd
from evidently import Report
from evidently.presets import DataDriftPreset

# 1. Original data: our reference dataset
reference_data = pd.DataFrame({
    "age": [20, 22, 24, 25, 27, 28, 30, 32, 35, 38],
    "income": [
        25000, 27000, 29000, 30000, 32000,
        33000, 35000, 37000, 40000, 42000
    ]
})

# 2. New data: our current dataset
# The values have changed to simulate data drift.
current_data = pd.DataFrame({
    "age": [25, 28, 30, 33, 35, 38, 40, 42, 45, 50],
    "income": [
        35000, 38000, 40000, 43000, 45000,
        48000, 52000, 55000, 60000, 70000
    ]
})

# 3. Configure the data drift report
report = Report([
    DataDriftPreset()
])

# 4. Compare current data against reference data
snapshot = report.run(
    current_data=current_data,
    reference_data=reference_data
)

# 5. Save the report as an HTML file
snapshot.save_html("data_drift_report.html")

print("Data monitoring completed successfully!")
print("Report saved as data_drift_report.html")
