import argparse

# Create argument parser
parser = argparse.ArgumentParser(description="User Information CLI Tool")

# Define arguments
parser.add_argument("--name", required=True, help="User's name")
parser.add_argument("--age", type=int, required=True, help="User's age")

# Parse arguments
args = parser.parse_args()

# Display input
print(f"Name: {args.name}")
print(f"Age: {args.age}")
