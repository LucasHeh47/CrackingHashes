import hashlib
import create_wordlists

input_string = ""

def hash_string(input_string, algorithm):
    if algorithm.lower() == 'md5':
        hasher = hashlib.md5()
    elif algorithm.lower() == 'sha1':
        hasher = hashlib.sha1()
    elif algorithm.lower() == 'sha256':
        hasher = hashlib.sha256()
    elif algorithm.lower() == 'sha384':
        hasher = hashlib.sha384()
    elif algorithm.lower() == 'sha512':
        hasher = hashlib.sha512()
    else:
        raise ValueError('Unsupported algorithm')

    hasher.update(input_string.encode('utf-8'))
    return hasher.hexdigest()


def get_hash_algorithm():
    while True:
        print("""
        [1] MD5
        [2] SHA1
        [3] SHA256
        [4] SHA384
        [5] SHA512
        """)
        algorithm_chosen = int(input("Your choice: "))
        if algorithm_chosen < 1 or algorithm_chosen > 5:
            print("Try again")
        else:
            break
    match algorithm_chosen:
        case 1:
            return "md5"
        case 2:
            return "sha1"
        case 3:
            return "sha256"
        case 4:
            return "sha384"
        case 5:
            return "sha512"
        case default:
            return "md5"


def compare_hashes(hash1, hash2):
    return hash1.lower() == hash2.lower()


def brute_force(file_name, hash_to_find, hash_algorithm):
    with open("wordlists/" + file_name, 'r', encoding='latin-1') as f:
        print(f"""
        -=Brute Forcing=-
        FILE: {file_name}
        HASH: {hash_to_find}
        ALGORITHM: {hash_algorithm}
        """)
        for line in f:
            try:
                line = line.strip().encode('utf-8').decode('utf-8')
            except UnicodeError:
                print(f"[ERROR] Invalid characters: {line} | Continuing...")
                continue  # Skip lines with invalid characters

            hash_found = hash_string(line, hash_algorithm)
            if compare_hashes(hash_to_find, hash_found):
                return line
        print("Hash not found in " + file_name)

while True:
    print("Lucas' Hash Cracker")
    choice = 0
    while True:
        print("Select an option: ")
        print("""
        [1] Hash String
        [2] Crack Hash
        [3] Create wordlist
        """)
        choice = int(input("Please enter a choice: "))
        if choice < 1 or choice > 3:
            print("Try again")
        else:
            break
    match choice:
        case 1:
            print(hash_string(input("Enter a string: "), get_hash_algorithm()))
            break
        case 2:
            wordlist = input("Please enter a wordlist: ")
            hash_to_crack = input("Enter a hash: ")
            print(brute_force(wordlist, hash_to_crack, get_hash_algorithm()))
            break
        case 3:
            create_wordlists.run()
            break

