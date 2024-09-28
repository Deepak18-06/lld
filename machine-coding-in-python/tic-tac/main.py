from abc import ABC, abstractmethod
from typing import List, Tuple

class Player:
    def __init__(self, name: str, symbol: str):
        self.name = name
        self.symbol = symbol

class Board:
    def __init__(self):
        self.board = [['-' for _ in range(3)] for _ in range(3)]

    def update(self, x: int, y: int, symbol: str) -> bool:
        if self.is_valid_move(x, y):
            self.board[x][y] = symbol
            return True
        return False

    def is_valid_move(self, x: int, y: int) -> bool:
        return 0 <= x < 3 and 0 <= y < 3 and self.board[x][y] == '-'

    def is_full(self) -> bool:
        return all(cell != '-' for row in self.board for cell in row)

    def get_state(self) -> List[List[str]]:
        return [row[:] for row in self.board]

class GameState(ABC):
    @abstractmethod
    def handle(self, game: 'Game') -> None:
        pass

class PlayingState(GameState):
    def handle(self, game: 'Game') -> None:
        game.play_turn()

class GameOverState(GameState):
    def handle(self, game: 'Game') -> None:
        game.display_result()

class WinningStrategy(ABC):
    @abstractmethod
    def check_win(self, board: Board, symbol: str) -> bool:
        pass

class LinearWinningStrategy(WinningStrategy):
    def check_win(self, board: Board, symbol: str) -> bool:
        # Check rows, columns and diagonals
        state = board.get_state()
        for i in range(3):
            if all(state[i][j] == symbol for j in range(3)) or \
               all(state[j][i] == symbol for j in range(3)):
                return True
        return all(state[i][i] == symbol for i in range(3)) or \
               all(state[i][2-i] == symbol for i in range(3))

class Game:
    def __init__(self, board: Board, players: List[Player], winning_strategy: WinningStrategy):
        self.board = board
        self.players = players
        self.current_player_index = 0
        self.state: GameState = PlayingState()
        self.winning_strategy = winning_strategy

    def play(self) -> None:
        while isinstance(self.state, PlayingState):
            self.state.handle(self)

    def play_turn(self) -> None:
        current_player = self.players[self.current_player_index]
        self.display_board()
        print(f"{current_player.name}'s turn ({current_player.symbol})")

        while True:
            try:
                x, y = map(int, input("Enter row and column (0-2) separated by space: ").split())
                if self.board.update(x, y, current_player.symbol):
                    break
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Please enter two numbers separated by space.")

        if self.winning_strategy.check_win(self.board, current_player.symbol):
            self.state = GameOverState()
            self.winner = current_player
        elif self.board.is_full():
            self.state = GameOverState()
            self.winner = None
        else:
            self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def display_board(self) -> None:
        for row in self.board.get_state():
            print(" ".join(row))
        print()

    def display_result(self) -> None:
        self.display_board()
        if self.winner:
            print(f"{self.winner.name} wins!")
        else:
            print("It's a draw!")

class GameFactory:
    @staticmethod
    def create_game() -> Game:
        board = Board()
        player1 = Player("Player 1", "X")
        player2 = Player("Player 2", "O")
        winning_strategy = LinearWinningStrategy()
        return Game(board, [player1, player2], winning_strategy)

# Usage
if __name__ == "__main__":
    game = GameFactory.create_game()
    game.play()