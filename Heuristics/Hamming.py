from Heuristics.HeuristicInterface import HeuristicInterface


class Hamming(HeuristicInterface):
    def calc(puzzle: list[list, list, list]) -> int:
        """
        This function solves the Puzzle based on Hamming heuristic
        :param puzzle: The unsolved puzzle
        :return: The solved puzzle
        """
        # enumerate won't work because it will only be 3 at max
        sum, counter = 0, 0
        for row in range(len(puzzle)):
            for col in range(len(puzzle[0])):
                if puzzle[row][col] != 0 and puzzle[row][col] != counter:
                    sum += 1
                counter += 1
        return sum
