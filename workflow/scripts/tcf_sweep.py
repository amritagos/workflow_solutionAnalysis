import argparse
from pathlib import Path


def main():
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(
        description="Process angles and write to an optional output file."
    )

    # Add arguments for file path, cutoff, and max_angle
    parser.add_argument("-i", "--file_path", type=Path, help="Path to the input file")
    parser.add_argument("cutoff", type=float, help="Cutoff value")
    parser.add_argument("max_angle", type=float, help="Maximum angle value")
    parser.add_argument("-o", "--output", type=Path, help="Output file directory path")

    # Parse the command line arguments
    args = parser.parse_args()

    # Prepare the result to be written
    result = f"File Path: {args.file_path}\nCutoff: {args.cutoff}\nMax Angle: {args.max_angle}\n"

    outfile = args.output / "out.txt"

    args.output.mkdir(exist_ok=True)

    with open(outfile, "w") as f:
        f.write(result)


if __name__ == "__main__":
    main()
