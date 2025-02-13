# layout_settings

save_file_name = "inference_results_17122024_v2.png"
colors = [("#B78589", 1.0), ("#85B7B3", 1.0)]

eval_labels = ["Precision", "Recall", "F1-score"]
model_list = ["pretrained", "scratch"]
eval_list = ["precision", "recall", "f1score"]
task_list = ["pphase", "sphase"]
window_list = ["w0", "w1"]

tick_fontsize = 14
axis_fontsize = 20
title_fontsize = 22

x_labels = ["no \n adjustment", "0.1 sec \n window size"]
positions = [1, 2, 4, 5]
x_ticks = [1.5, 4.5]
y_ticks = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]

kwargs = dict()
kwargs["set_xticks"] = dict(ticks=x_ticks, labels=x_labels, fontsize=tick_fontsize)
kwargs["set_ylim"] = dict(bottom=-0.025, top=1.025)
kwargs["set_yticks"] = dict(ticks=y_ticks, labels=y_ticks, fontsize=tick_fontsize)
kwargs["grid"] = dict(axis="y", which="major", linestyle="-", color="grey", linewidth=1, alpha=0.5)
kwargs["tick_params"] = dict(axis="both", which="major", left=False, bottom = False)

box_props = dict()
box_props["boxes"] = [dict(facecolor=colors[0], edgecolor="white", linewidth=1.5), dict(facecolor = colors[1], edgecolor="white", linewidth = 1.5)] * 2
box_props["medians"] = [dict(color="white", linewidth=1.0)] * 4
box_props["whiskers"] = [dict(color=colors[0], linewidth=1.5), dict(color=colors[0], linewidth=1.5), dict(color=colors[1], linewidth=1.5), dict(color=colors[1], linewidth=1.5)] * 2
box_props["caps"] = [dict(color=colors[0], linewidth=1.5), dict(color=colors[0], linewidth=1.5), dict(color=colors[1], linewidth=1.5), dict(color=colors[1], linewidth=1.5)] * 2
box_props["fliers"] = [dict(marker="o", markerfacecolor=colors[0], markeredgecolor="white", alpha=1.0), dict(marker="o", markerfacecolor=colors[1], markeredgecolor="white", alpha=1.0)] * 2
