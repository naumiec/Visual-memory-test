from typing import List, Dict, Any

import pandas as pd
import json
import os


class Converter(object):
    """
    Class to convert and save results data to different file formats.
    """

    def __init__(self, results_list: List[Dict[str, Any]], filename: str) -> None:
        """
        Initialize the Converter with a list of results and a filename.

        :param results_list: List of dictionaries containing the results data.
        :param filename: The base name of the file to save the data (without extension).
        :return: None
        """
        self.results_list = results_list
        self.results_df = pd.DataFrame(results_list)
        self.filename = filename

    def __str__(self) -> str:
        """
        Return a string representation of the Converter object.

        :return: String representation of the Converter object.
        """
        return f"Converter with results for: {self.filename}"

    def save_to_csv(self) -> None:
        """
        Save the results data to a CSV file.

        The file will be named with the provided filename and a .csv extension.

        :return: None
        """
        self.results_df.to_csv(f"{self.filename}.csv", index=False)

    def save_to_txt(self) -> None:
        """
        Save the results data to a TXT file.

        The file will be named with the provided filename and a .txt extension.
        Each result will be formatted with keys and values on separate lines.

        :return: None
        """
        with open(f"{self.filename}.txt", 'w') as file:
            for result in self.results_list:
                file.write(f"Session: {result['Session']}\n")
                file.write(f"Stage: {result['Stage']}\n")
                file.write(f"Round: {result['Round']}\n")
                file.write(f"Selected_squares: {result['Selected_squares']}\n")
                file.write(f"Clicked_positions: {result['Clicked_positions']}\n")
                file.write(f"Mistakes_in_stage: {result['Mistakes_in_stage']}\n")
                file.write(f"Click_times: {result['Click_times']}\n")
                file.write("\n")

    def save_to_json(self) -> None:
        """
        Save the results data to a JSON file.

        The file will be named with the provided filename and a .json extension.

        :return: None
        """
        with open(f"{self.filename}.json", 'w') as file:
            json.dump(self.results_list, file, indent=4)
