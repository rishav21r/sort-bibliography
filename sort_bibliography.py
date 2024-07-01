def sort_bibliography(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            lines = file.readlines()

        if not lines:
            raise ValueError("The input file is empty.")

        # Separate the "Bibliography" heading from the actual references
        heading = lines[0]
        references = lines[1:]

        if not references:
            raise ValueError("No references found in the input file.")

        # Function to find duplicates
        def find_duplicates(references):
            seen = set()
            duplicates = set()
            unique_references = []

            for ref in references:
                if ref in seen:
                    duplicates.add(ref)
                else:
                    seen.add(ref)
                    unique_references.append(ref)

            return unique_references, duplicates

        # Find and print duplicates
        unique_references, duplicates = find_duplicates(references)
        if duplicates:
            print("Duplicate entries found:")
            for duplicate in duplicates:
                print(duplicate)
        else:
            print("No duplicate entries found.")

        # Sort references alphabetically
        sorted_references = sorted(unique_references, key=lambda ref: ref.split(",")[0].strip())

        # Write the sorted references to the output file
        with open(output_file, 'w') as file:
            file.write(heading)
            for ref in sorted_references:
                file.write(ref)

        print(f"Sorted bibliography has been written to {output_file}")

    except FileNotFoundError:
        print(f"Error: The file {input_file} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Replace 'input.txt' with the name of your input file and 'sorted_output.txt' with the desired output file name
sort_bibliography('input.txt', 'sorted_output.txt')
