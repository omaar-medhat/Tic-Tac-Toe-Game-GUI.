# **Tic Tac Toe Game (GUI)**

## **Description**

This is a simple **Tic Tac Toe** game implemented using the `tkinter` library in Python. The game features a graphical user interface (GUI) where two players can take turns playing the game on a 3x3 grid. The game checks for **wins** or **ties** and displays the result. Players can also reset the game at any time to start a new match.

## **Features**

* **Two players**: Player "X" and Player "O" can take turns.
* **Win detection**: The game automatically detects when a player wins.
* **Tie detection**: The game checks for a tie when all spaces are filled with no winner.
* **Reset functionality**: The game can be reset to start a new match.

## **Requirements**

* Python 3.x
* `tkinter` library (usually comes pre-installed with Python)

## **How to Run**

1. **Download or Clone the Repository**:

   * Download the `.py` file containing the game code or clone the repository.

2. **Install Python**:

   * Ensure you have **Python 3.x** installed on your system. You can check your version of Python by running:

   ```bash
   python --version
   ```

3. **Run the Game**:

   * Open your terminal or command prompt.
   * Navigate to the folder where the `tic_tac_toe.py` file is located.
   * Run the following command:

   ```bash
   python tic_tac_toe.py
   ```

4. **Play the Game**:

   * A window will open showing the Tic Tac Toe board.
   * Players will take turns clicking the buttons to place their "X" or "O" on the grid.
   * The game will announce the winner or indicate a tie when the game ends.
   * Use the "Reset" button to start a new game.

## **How to Play**

* Player **X** always goes first.
* Click any of the empty squares to place your mark.
* The game will detect if a player has won or if the game is a tie and show the result.
* After a game ends, you can click the "Reset" button to start a new game.

## **Code Explanation**

* **Main Game Logic**:

  * The board is represented as a list with 9 elements (`["-"] * 9`), where each element corresponds to a square on the Tic Tac Toe grid.
  * The function `checkforwin()` checks the board for a winning combination, which includes horizontal, vertical, and diagonal wins.
  * The function `checkfortie()` checks if the board is full without a winner, indicating a tie.
* **GUI**:

  * The `tkinter` library is used to create the graphical interface.
  * Buttons are created for each square on the Tic Tac Toe grid, and a status label displays whose turn it is.
  * The "Reset" button allows players to start a new game.

## **Example Screenshot**

When you run the program, the window will look like this:

```
+---+---+---+
| X | O | X |
+---+---+---+
| O | X | O |
+---+---+---+
| X | O | X |
+---+---+---+

Current Status: "X's Turn"
```
