import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
from matplotlib.patches import Patch

# Define dissertation tasks for the Mar-Aug 2025 timeline
tasks = [
    {"name": "Proposal Submission", "start": "2025-03-01", "end": "2025-03-20"},
    {"name": "Define System & Boundaries", "start": "2025-04-01", "end": "2025-05-15"},
    {"name": "Indicator Development & Classification", "start": "2025-04-01", "end": "2025-05-15"},
    {"name": "Data Acquisition (DfT, ONS, NAEI)", "start": "2025-04-01", "end": "2025-08-15"},
    {"name": "Metric Calculation & Normalization", "start": "2025-05-15", "end": "2025-08-15"},
    {"name": "Result Interpretation & Trade-offs", "start": "2025-05-15", "end": "2025-08-15"},
    {"name": "Extended Results Discussion", "start": "2025-05-15", "end": "2025-08-15"},
    {"name": "Initial Literature Review Research", "start": "2025-03-01", "end": "2025-04-30"},
    {"name": "Extended Literature Review", "start": "2025-05-01", "end": "2025-08-15"},
    {"name": "Final Submission And Analysis", "start": "2025-08-01", "end": "2025-08-30"}
]

# Formatting and Logic
for t in tasks:
    t["start_dt"] = datetime.strptime(t["start"], "%Y-%m-%d")
    t["end_dt"] = datetime.strptime(t["end"], "%Y-%m-%d")
    t["duration"] = (t["end_dt"] - t["start_dt"]).days

def get_color(duration):
    if duration <= 30: return "green"
    elif 31 <= duration <= 90: return "orange"
    else: return "red"

# Plotting Configuration
fig, ax = plt.subplots(figsize=(14, 8))
y_labels = [t["name"] for t in tasks]
colors = [get_color(t["duration"]) for t in tasks]

for i, t in enumerate(tasks):
    ax.barh(i, t["duration"], left=t["start_dt"], color=colors[i], edgecolor='black', height=0.6)

# Aesthetics
ax.set_yticks(range(len(tasks)))
ax.set_yticklabels(y_labels, fontsize=12)
ax.set_title("Gantt Chart: Sustainability Assessment of the UK Car Fleet", fontsize=16, pad=20)
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
ax.grid(True, linestyle='--', alpha=0.6)

# Professional Legend
legend_elements = [
    Patch(facecolor='green', edgecolor='black', label='Short (≤ 30 days)'),
    Patch(facecolor='orange', edgecolor='black', label='Medium (31-90 days)'),
    Patch(facecolor='red', edgecolor='black', label='Long (> 90 days)')
]
ax.legend(handles=legend_elements, loc='upper right', frameon=True)

plt.tight_layout()
plt.savefig("Dissertation_Gantt_Chart.png", dpi=300)