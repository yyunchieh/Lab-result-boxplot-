from matplotlib.lines import Line2D

ax1_legend_labels = ["Mean ± 1.96 × Std"]
ax2_legend_labels = ["p-value <= 0.05", "p-value > 0.05"]

custom_legend = [
          Line2D([0], [0], marker="o", color="black", markersize=6, linestyle="None"),
          Line2D([0, 1], [0, 0], color="black", linewidth=2)
]

legend_loc = "lower left"
bbox_to_anchor=(1.05, 0.5)
legend_fontsize = 14

legend_kwarg = dict(labelspacing=1.0,
                    handlelength=1.2,
                    handleheight=1.2,
                    handletextpad=1.5,
                    borderpad=1.5,
                    borderaxespad=0.0)