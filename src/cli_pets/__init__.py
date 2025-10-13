"""CLI Pets - Animated terminal pets for your command line."""

# 1. Setup ----
import random
import time
from rich.console import Console
from rich.live import Live
from rich.text import Text

console = Console()

PETS = ["🐱", "🐶", "🐰", "🐭", "🐹", "🦊", "🐻", "🐼", "🐨", "🐯"]


# 2. Functions ----


## 2.1 Greeting ----
def greet() -> None:
    """Print a friendly greeting with a random pet."""
    pet = random.choice(PETS)
    console.print(f"[bold green]Hello from CLI Pets! {pet}[/bold green]")


## 2.2 Walking Animation ----
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


## 2.3 Racing ----
def race(distance: int = 50, racers: int = 3) -> None:
    """Race pets across the terminal.

    Args:
        distance: Length of the race track (default: 50)
        racers: Number of racing pets (default: 3)
    """
    ### 2.3.1 Setup ----
    pets = random.sample(PETS, min(racers, len(PETS)))
    positions = [0] * len(pets)

    ### 2.3.2 Race Loop ----
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

    ### 2.3.3 Declare Winner ----
    winner_idx = positions.index(max(positions))
    console.print(f"\n[bold yellow]🏆 {pets[winner_idx]} wins![/bold yellow]")
