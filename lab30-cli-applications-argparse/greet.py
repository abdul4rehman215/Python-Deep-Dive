import argparse

# Create argument parser
parser = argparse.ArgumentParser(
    description="A simple greeting CLI application."
)

# Add optional argument
parser.add_argument(
    "--name",
    type=str,
    help="Name of the person to greet"
)

# Parse arguments
args = parser.parse_args()

# Use arguments
if args.name:
    print(f"Hello, {args.name}!")
else:
    print("Hello, Stranger!")
