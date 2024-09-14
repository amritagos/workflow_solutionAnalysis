import argparse
from pathlib import Path


def main():
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(
        description="Process angles and write to an optional output file."
    )

    # Add arguments for file path, cutoff, and max_angle
    parser.add_argument("file_path", type=Path, help="Path to the input file")
    parser.add_argument("cutoff", type=float, help="Cutoff value")
    parser.add_argument("max_angle", type=float, help="Maximum angle value")

    # Add an optional argument for the output file path
    parser.add_argument(
        "-o", "--output", type=Path, default=None, help="Optional output file path"
    )

    # Parse the command line arguments
    args = parser.parse_args()

    # Prepare the result to be written
    result = f"File Path: {args.file_path}\nCutoff: {args.cutoff}\nMax Angle: {args.max_angle}\n"

    # If an output file is specified, write the result to it
    if args.output:
        with open(args.output, "w") as output_file:
            output_file.write(result)
        print(f"Results written to {args.output}")
    else:
        # Otherwise, print the result to the terminal
        print(result)


if __name__ == "__main__":
    main()
