from pacman_module.game import Agent, Directions
from pacman_module.util import Queue


def key(state):
    """Return a key that uniquely identifies a Pacman game state.

    Args:
        state: a game state. See API or class `pacman.GameState`.

    Returns:
        A hashable key tuple.
    """
    food_grid = state.getFood()
    capsules = state.getCapsules()
    return (
        state.getPacmanPosition(),
        tuple(food_grid.asList()),  # Convert boolean grid to list of coordinates
        tuple(capsules)
    )


class PacmanAgent(Agent):
    """Pacman agent that performs breadth-first search (BFS) to find solutions."""

    def __init__(self):
        super().__init__()
        self.moves = None

    def get_action(self, state):
        """Return a legal move based on the Pacman game state.

        Args:
            state: a game state. See API or class `pacman.GameState`.

        Returns:
            A legal move as defined in `game.Directions`.
        """
        if self.moves is None or not self.moves:
            self.moves = self.bfs(state)
            if not self.moves:
                return Directions.STOP

        return self.moves.pop(0)

    def bfs(self, state):
        """Perform a breadth-first search to determine legal moves.

        Args:
            state: a game state. See API or class `pacman.GameState`.

        Returns:
            A list of legal moves.
        """
        fringe = Queue()
        fringe.push((state, []))
        closed = set()

        while not fringe.isEmpty():
            current, path = fringe.pop()

            if current.isWin():
                return path

            current_key = key(current)
            if current_key not in closed:
                closed.add(current_key)

                for successor, action in current.generatePacmanSuccessors():
                    if action not in path:  # Avoid adding cycles
                        new_path = path + [action]
                        fringe.push((successor, new_path))

        return []