"""Greeting function for CLI Pets."""

import random
from rich.console import Console

console = Console()

PETS = ["🐱", "🐶", "🐰", "🐭", "🐹", "🦊", "🐻", "🐼", "🐨", "🐯"]


def greet() -> None:
    """Print a friendly greeting with a random pet."""
    pet = random.choice(PETS)
    console.print(f"[bold green]Hello from CLI Pets! {pet}[/bold green]")
