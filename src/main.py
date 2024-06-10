from Experiment import Experiment

from typing import Any


def main() -> int:
    """
    Main function to run the experiment and plot the results.

    :return: 0 if the experiment was successful.
    """
    #experiment = Experiment(fullscreen=False)
    experiment = Experiment()
    result: int = experiment.run()

    print("Experiment result: ", result)

    return 0


if __name__ == "__main__":
    """
    The following code block will execute only if the script is run directly,
    and not if it is imported as a module in another script.
    """
    main()
