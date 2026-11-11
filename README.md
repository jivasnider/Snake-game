# Snake Game

A classic Snake game written in Python. Steer the snake to eat the food, grow longer with every bite, and try to beat your high score without hitting the walls or your own tail.

## Demo
<img width="640" height="640" alt="vlc-record-2026-11-11-20h43m34s-Super Snake Game-" src="https://github.com/user-attachments/assets/c03b6921-6e7e-405f-8a79-d16331a95ca0" />


## Features

- Smooth snake movement controlled with the arrow keys
- Food appears at random positions and the snake grows when it eats
- Live scoreboard with a saved high score
- Game over when the snake hits a wall or its own tail
- Object-oriented design with separate classes for the snake, food and scoreboard

## Controls

| Key | Action |
|-----|--------|
| `↑` | Move up |
| `↓` | Move down |
| `←` | Move left |
| `→` | Move right |

## Requirements

- Python 3.8 or newer
- No extra libraries are needed. The game uses `turtle`, which ships with Python (it needs Tkinter, included in the standard Windows and macOS installers).

## Run locally

```bash
git clone https://github.com/jivasnider/Snake-game.git
cd Snake-game
python main.py
```

On macOS/Linux you may need to use `python3 main.py` instead.

## Project structure

```
Snake-game/
├── main.py         # Game setup and main loop
├── snake.py        # Snake class: movement, growth and controls
├── food.py         # Food class: random placement
├── scoreboard.py   # Score display and high score handling
├── data.txt        # Stores the high score
└── images/         # Demo GIF
```

## What I learned

- Object-oriented programming in Python (classes, inheritance, methods)
- Building a game loop and handling keyboard input
- Detecting collisions with walls, food and the snake's own body
- Reading and writing a file to save the high score
- Splitting a project into multiple modules
