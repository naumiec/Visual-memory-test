from typing import Any, List, Tuple

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


class Plotter(object):
    """
    A class to plot the experiment data.
    """

    def __init__(self, csv_file: str) -> None:
        """
        Initializes the Plotter with the given CSV file.

        :param csv_file: The path to the CSV file containing the experiment data.
        """
        self.data: pd.DataFrame = pd.read_csv(csv_file)
        self.csv_file: str = csv_file
        self.save_dir: str = "plots"
        if not os.path.exists(self.save_dir):
            os.makedirs(self.save_dir)
        self._prepare_data()

    def _prepare_data(self) -> None:
        """
        Prepares the data by adding columns for average time per square and accuracy.
        """
        def average_time_per_square(row: pd.Series) -> float:
            click_times: List[float] = eval(row["Click_times"])
            num_squares: int = len(eval(row["Selected_squares"]))
            if num_squares == 0:
                return np.nan
            return np.abs(np.mean(click_times))

        def calculate_accuracy(row: pd.Series) -> float:
            selected_squares: List[Tuple[int, int]] = eval(row["Selected_squares"])
            clicked_positions: List[Tuple[int, int]] = eval(row["Clicked_positions"])
            correct_clicks: int = sum([1 for pos in clicked_positions if pos in selected_squares])
            total_clicks: int = len(clicked_positions)
            if total_clicks == 0:
                return 0.0
            return correct_clicks / total_clicks

        self.data["Average_time_per_square"] = self.data.apply(average_time_per_square, axis=1)
        self.data["Accuracy"] = self.data.apply(calculate_accuracy, axis=1)

    def _save_plot(self, fig: plt.Figure, filename: str) -> None:
        """
        Saves the given figure to the specified filename.

        :param fig: The figure object to be saved.
        :param filename: The filename to save the plot.
        """
        filepath: str = os.path.join(self.save_dir, filename)
        fig.savefig(filepath)

    def plot_average_time_per_square(self) -> None:
        """
        Plots the average time per square for each stage and saves the plot.
        """
        stages: np.ndarray = self.data["Stage"].unique()
        fig, axs = plt.subplots(2, 2, figsize=(15, 10))
        axs = axs.flatten()
        for idx in range(len(axs)):
            if idx < len(stages):
                stage: Any = stages[idx]
                stage_data: pd.DataFrame = self.data[self.data["Stage"] == stage]
                axs[idx].plot(stage_data["Round"], stage_data["Average_time_per_square"], marker="o")
                axs[idx].set_title(f"Stage {stage} - Average time per square", fontsize=14, fontweight="bold")
                axs[idx].set_ylabel("Average time per square [s]")
                axs[idx].set_xlabel("Round [#]")
                axs[idx].set_ylim(bottom=0)
                axs[idx].grid(True, which="both", linestyle="-", linewidth=0.2)
                axs[idx].xaxis.set_major_locator(plt.MaxNLocator(integer=True))
                axs[idx].set_xticks(np.arange(1, stage_data["Round"].max() + 1))
            else:
                axs[idx].set_visible(False)
        plt.tight_layout()
        filename: str = os.path.splitext(os.path.basename(self.csv_file))[0]
        self._save_plot(fig, f"{filename}_average_time_per_square.png")

    def plot_overall_average_accuracy(self) -> None:
        """
        Plots the overall average accuracy per round and saves the plot.
        """
        rounds: np.ndarray = self.data["Round"].unique()
        average_accuracy_per_round: pd.Series = self.data.groupby("Round")["Accuracy"].mean() * 100
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.plot(average_accuracy_per_round.index, average_accuracy_per_round.values, marker="o")
        ax.set_title("Overall average accuracy per round", fontsize=14, fontweight="bold")
        ax.set_xlabel("Round [#]")
        ax.set_ylabel("Average accuracy [%]")
        ax.set_ylim(0, 110)
        ax.set_xticks(np.arange(1, rounds.max() + 1))
        ax.set_yticks(np.arange(0, 110, 10))
        ax.grid(True, which="both", linestyle="-", linewidth=0.2)
        ax.xaxis.set_major_locator(plt.MaxNLocator(integer=True))

        filename: str = os.path.splitext(os.path.basename(self.csv_file))[0]
        self._save_plot(fig, f"{filename}_overall_average_accuracy.png")
