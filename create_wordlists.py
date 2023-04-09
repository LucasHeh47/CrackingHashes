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
    file_pattern = re.compile(r'\{(\w+\.txt)\}')
    file_names = file_pattern.findall(input_string)
    num_placeholders = input_string.count('%')

    combined_content = []

    for file_name in file_names:
        with open("wordlists/" + file_name, 'r') as f:
            content_lines = f.read().splitlines()
            if combined_content:
                new_combined_content = []
                for line1 in combined_content:
                    for line2 in content_lines:
                        new_combined_content.append(line1 + line2 + '%' * num_placeholders)
                combined_content = new_combined_content
            else:
                combined_content = [line + '%' * num_placeholders for line in content_lines]

        input_string = input_string.replace('{' + file_name + '}', '')

    input_string = input_string.replace('%' * num_placeholders, "\n".join(combined_content))

    return input_string


def run():
    print("""
    CREATING A WORDLIST

    TIPS:

    Random Number: %          File Content               Combine files
    Ex.                       Ex.                        Ex.
    Input: TEST-%%            Input: {pokemon.txt}%      Input {adjectives.txt}{animals.txt}
    Output:                   Output:                    Output:
    TEST-01                   Pikachu0                   SuperCat
    TEST-02                   Pikachu1                   SuperDog
    TEST-03                   Pikachu2                   CharmingCat
    ...                       ...                        ...

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
