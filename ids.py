from pacman_module.game import Agent, Directions
from pacman_module.util import Stack


def key(state):
    """
    Returns a key that uniquely identifies a Pacman game state.
    
    Args:
        state: a game state. See API or class `pacman.GameState`.
    
    Returns:
        A hashable key tuple.
    """
    food_grid = state.getFood()
    capsules = state.getCapsules()
    return (
        state.getPacmanPosition(),
        tuple(food_grid.asList()),  # Convert food positions to list
        tuple(capsules)
    )


class PacmanAgent(Agent):
    """
    Pacman agent implementing iterative deepening search.
    """

    def __init__(self):
        super().__init__()
        self.moves = None

    def get_action(self, state):
        """
        Returns a legal move based on the current Pacman game state.
        
        Args:
            state: a game state. See API or class `pacman.GameState`.
        
        Returns:
            A legal move as defined in `game.Directions`.
        """
        if self.moves is None or not self.moves:
            self.moves = self.iterative_deepening_search(state)
            if not self.moves:
                return Directions.STOP

        return self.moves.pop(0)

    def depth_limited_search(self, state, limit):
        """
        Depth-limited search from a given state to a specified depth limit.
        """
        stack = Stack()
        stack.push((state, [], 0))  # State, path, current depth
        closed = set()

        while not stack.isEmpty():
            current_state, path, depth = stack.pop()

            if current_state.isWin():
                return path

            if depth >= limit:
                continue  # Skip expanding this node further if depth limit reached

            current_key = key(current_state)
            if current_key not in closed:
                closed.add(current_key)

                for successor, action in current_state.generatePacmanSuccessors():
                    new_path = path + [action]
                    stack.push((successor, new_path, depth + 1))

        return None

    def iterative_deepening_search(self, state):
        """
        Iterative deepening search to find the optimal solution.
        """
        depth = 0
        while True:
            result = self.depth_limited_search(state, depth)
            if result is not None:
                return result
            depth += 1  # Increase depth limit for next iteration

        return []