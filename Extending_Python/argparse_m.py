import argparse

# Create an ArgumentParser object
parser = argparse.ArgumentParser(description='Example Argument Parser')

# Add arguments
parser.add_argument('input_file', help='Path to the input file')
parser.add_argument('-o', '--output', help='Path to the output file')

# Optional arguments
parser.add_argument('--verbose', action='store_true', help='Enable verbose mode')

# Parse the command-line arguments
args = parser.parse_args()

# Access the parsed arguments
input_file = args.input_file
output_file = args.output
verbose = args.verbose

# Perform actions based on the arguments
print('Input file:', input_file)
print('Output file:', output_file)
print('Verbose mode:', verbose)