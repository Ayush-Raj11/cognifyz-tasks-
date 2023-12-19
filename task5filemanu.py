
############ wap to make the file manipulater ###########


file_path = input("Enter the path to the text file: ")

# Check if the file exists
if not os.path.isfile(file_path):
    print("File not found. Please provide a valid file path.")
else:
    # Read the file and count word occurrences
    with open(file_path, 'r', encoding='utf-8') as file:
        word_counts = {}

        for line in file:
            # Split the line into words and process each word
            for word in line.split():
                # Remove leading and trailing punctuation
                word = word.strip(".,?!()[]{}\"'")

                # Convert to lowercase
                word = word.lower()

                # Count occurrences of each word
                if word:
                    word_counts[word] = word_counts.get(word, 0) + 1

        # Display results in alphabetical order
        sorted_word_counts = sorted(word_counts.items())
        for word, count in sorted_word_counts:
            print(f"{word}: {count}")