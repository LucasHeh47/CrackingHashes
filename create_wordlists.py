import itertools
import os
import re


def generate_strings(input_string):
    num_placeholders = input_string.count('%')
    if num_placeholders == 0:
        return [input_string]

    indices = [i for i, char in enumerate(input_string) if char == '%']
    combinations = itertools.product(range(10), repeat=num_placeholders)
    generated_strings = []

    for combination in combinations:
        new_string = list(input_string)
        for idx, value in zip(indices, combination):
            new_string[idx] = str(value)
        generated_strings.append(''.join(new_string))

    return generated_strings


def replace_file_name_with_content(input_string):
    file_pattern = re.compile(r'\b\w+\.txt\b')
    file_names = file_pattern.findall(input_string)
    num_placeholders = input_string.count('%')

    for file_name in file_names:
        with open("wordlists/" + file_name, 'r') as f:
            content_lines = f.read().splitlines()
            content_with_placeholders = "\n".join([line + '%' * num_placeholders for line in content_lines])

        # Replace the file name in the input_string with the content_with_placeholders
        # and remove any trailing '%' characters from the input_string
        input_string = input_string.replace(file_name + '%', content_with_placeholders)

    return input_string




def run():
    print("""
    CREATING A WORDLIST

    TIPS:

    Random Number: %
    Ex.
    Input: TEST-%%
    Output:
    TEST-01
    TEST-02
    ...

    Include file content: file.txt
    Ex.
    Input: file.txt-%%
    Output:
    word1-01
    word1-02
    ...
    word2-01
    word2-02
    ...

    """)
    output_file = input("Enter the output file name: ")

    with open("wordlists/" + output_file, 'w') as f:
        input_string = input("Enter string: ")
        input_string = replace_file_name_with_content(input_string)
        lines = input_string.splitlines()

        for line in lines:
            strings = generate_strings(line)

            for s in strings:
                f.write(s + "\n")
