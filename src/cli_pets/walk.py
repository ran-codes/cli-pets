"""Walking animation function for CLI Pets."""

import time
from rich.console import Console
from rich.text import Text

console = Console()


def walk(pet: str = "🐱", steps: int = 30, speed: float = 0.1) -> None:
    """Animate a pet walking across the terminal.

    Args:
        pet: Emoji character to display (default: cat)
        steps: Number of steps to take (default: 30)
        speed: Seconds between steps (default: 0.1)
    """
    for i in range(steps):
        console.clear()
        text = Text(" " * i + pet)
        console.print(text)
        time.sleep(speed)
    console.print()
