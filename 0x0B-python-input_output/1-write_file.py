def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns the number of characters written.

    Args:
        filename (str): The name of the file to write to.
        text (str): The text to be written to the file.

    Returns:
        int: The number of characters written to the file.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            num_characters_written = file.write(text)
        return num_characters_written
    except Exception as e:
        return 0  # Return 0 if there was an error while writing the file

# Example usage:
if __name__ == "__main__":
    nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
    print(nb_characters)

