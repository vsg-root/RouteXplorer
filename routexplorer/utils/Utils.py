from typing import Sequence

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
            f"{percentage:3d}% [" + "■" * (percentage // 10) + "□" * (10 - (percentage // 10)) + f"] - {name}",
            end="\r" if percentage < 100 else "\n"
        )
    
    @staticmethod
    def find(sequence: Sequence[any], target: any) -> bool:
        """check if a given value is present in a sequence.

        Args:
            sequence (Sequence[any]): The sequence of values.
            target (any): The value to check.

        Returns:
            bool: True if the value is present, False otherwise.
        """
        for i in sequence:
            if i == target:
                return True
        return False
