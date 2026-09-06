"""Write the first 25 Fibonacci numbers to a file, computed iteratively."""

from pathlib import Path

OUTPUT_DIR = Path(__file__).resolve().parent / "output"
OUTPUT_FILE = "fibonacci_recursive_output.txt"


def fib_sequence(count):
    """Return the first `count` Fibonacci numbers, built with a loop."""
    def fib(n):
        if n < 2:
            return n
        return fib(n - 1) + fib(n - 2)
    return [fib(n) for n in range(count)]





def fibonacci(count=25, filename=OUTPUT_FILE):
    """Write `count` Fibonacci numbers to `filename` in the output directory."""
    sequence = fib_sequence(count)

    OUTPUT_DIR.mkdir(exist_ok=True)
    path = OUTPUT_DIR / filename
    with open(path, "w") as f:
        for index, value in enumerate(sequence):
            f.write(f"F({index}) = {value}\n")

    print(f"Wrote {count} Fibonacci numbers to {path}")
    return sequence


if __name__ == "__main__":
    fibonacci()
