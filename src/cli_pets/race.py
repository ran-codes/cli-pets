"""Racing function for CLI Pets."""

import random
import time
from rich.console import Console
from rich.live import Live
from rich.text import Text

console = Console()

PETS = ["🐱", "🐶", "🐰", "🐭", "🐹", "🦊", "🐻", "🐼", "🐨", "🐯"]


def race(distance: int = 50, racers: int = 3) -> None:
    """Race pets across the terminal.

    Args:
        distance: Length of the race track (default: 50)
        racers: Number of racing pets (default: 3)
    """
    ### Setup ----
    pets = random.sample(PETS, min(racers, len(PETS)))
    positions = [0] * len(pets)

    ### Race Loop ----
    with Live(console=console, refresh_per_second=10) as live:
        while max(positions) < distance:
            # Update positions randomly
            for i in range(len(positions)):
                positions[i] += random.randint(0, 2)

            # Render race
            display = Text()
            for i, pet in enumerate(pets):
                pos = min(positions[i], distance)
                line = " " * pos + pet + "\n"
                display.append(line)

            live.update(display)
            time.sleep(0.1)

    ### Declare Winner ----
    winner_idx = positions.index(max(positions))
    console.print(f"\n[bold yellow]🏆 {pets[winner_idx]} wins![/bold yellow]")
