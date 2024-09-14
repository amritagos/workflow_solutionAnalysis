import argparse

def main():
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(description="TCF parameter sweep.")

    # Add arguments for cutoff and max_angle
    parser.add_argument('cutoff', type=float, help='Cutoff value')
    parser.add_argument('max_angle', type=float, help='Maximum angle value')

    # Parse the command line arguments
    args = parser.parse_args()

    # Print the values to the terminal
    print(f"Cutoff: {args.cutoff}")
    print(f"Max Angle: {args.max_angle}")

if __name__ == "__main__":
    main()
