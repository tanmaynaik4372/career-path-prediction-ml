import sys
from pathlib import Path
sys.path.append(str(Path.cwd() / "src"))

from common.seed_logging import set_global_seed, get_logger
from common.reporting import Report
from common.paths import PathResolver
import pandas as pd
import matplotlib.pyplot as plt

set_global_seed(42)
log = get_logger("phase01_test")
R = Report(phase=1)
P = PathResolver()

R.stamp("hello from phase01")
df = pd.DataFrame({"x":[1,2,3], "y":[1,4,9]})
R.save_df(df, "tiny_table.csv", index=False)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(df["x"], df["y"], marker="o")
ax.set_title("tiny plot")
R.save_fig(fig, "tiny_plot.png")

print("OK! Paths wired. Resumes would be read from:", P.dataset_path("resumes"))
