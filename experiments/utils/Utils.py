from typing import Sequence, List

class Utils:
    """
    Utility class for miscellaneous functions.

    Methods:
        generate_load(end: int, progress: int, name: str):
            Generates a loading progress bar.

    """
    @staticmethod
    def __min_heapify(arr, length, i, key):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2


        if left < length and key(arr[i]) < key(arr[left]):
            largest = left

        if right < length and key(arr[i]) < key(arr[right]):
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i] 

            Utils.__min_heapify(arr, length, largest, key)

    @staticmethod
    def heap_sort(arr: List[any], length: int, key = lambda x: x):
        for i in range(length//2 - 1, -1, -1):
            Utils.__min_heapify(arr, length, i, key)

        for i in range(length-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]  # swap
            Utils.__min_heapify(arr, i, 0, key)

    @staticmethod
    def fix(sequence: List[float]) -> List[float]:
        len_sequece = len(sequence)
        output = [float(0)] * len_sequece
        for i in range(len_sequece):
            if sequence[i] >= 0:
                output[i] = float(int(sequence[i]))
            else:
                output[i] = float(int(sequence[i]) + 1)
        return output
    
    @staticmethod
    def get_min(sequence: Sequence[any], key = lambda x: x):
        min_idx = 0
        for i in range(len(sequence)):
            if key(sequence[i]) < key(sequence[min_idx]):
                min_idx = i
        return sequence[min_idx]
    
    @staticmethod
    def get_max(sequence: Sequence[any], key = lambda x: x):
        max_idx = 0
        for i in range(len(sequence)):
            if key(sequence[i]) > key(sequence[max_idx]):
                max_idx = i
        return sequence[max_idx]
    
    @staticmethod
    def get_largest(a, b):
        if b > a:
            return b
        return a
    
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
