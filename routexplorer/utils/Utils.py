class Utils:
    """
    Utility class for miscellaneous functions.

    Methods:
        generate_load(end: int, progress: int, name: str):
            Generates a loading progress bar.

    """

    @staticmethod
    def generate_load(end: int, progress: int, name: str):
        """
        Generates a loading progress bar.

        Args:
            end (int): The total number of iterations.
            progress (int): The current progress.
            name (str): The name or description of the progress.

        """
        percentage = int((progress / end) * 100)
        print(
            f"{percentage:03}% [" + "■" * (percentage // 10) + "□" * (10 - (percentage // 10)) + f"] - {name}",
            end="\r" if percentage < 100 else "\n"
        )progress // end) * 100
        print(
            f"{percentage:03}% [" + "■" * (percentage // 10) + "□" * (10 - (percentage // 10)) + f"] - {name}",
            end="\r" if percentage < 100 else "\n"
        )
