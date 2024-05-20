from cipher_solver.simple import SimpleSolver
import string
from difflib import SequenceMatcher

def load_dictionary(filename):
    """Load words from a text file into a set."""
    with open(filename, 'r') as file:
        return {word.strip().lower() for word in file}

def remove_punctuation(text):
    """Remove punctuations from a string."""
    return text.translate(str.maketrans('', '', string.punctuation))

def words_not_in_dictionary(string, dictionary):
    """Return a list of words in a string that are not in the dictionary."""
    words = remove_punctuation(string).split()
    return [word.lower() for word in words if word.lower() not in dictionary]

def find_longest_word(words):
    return max(words, key=len)

def find_closest_word(target_word, words):
    max_ratio = 0
    closest_word = None
    for word in words:
        if len(word) != len(target_word):  # Check if lengths are equal
            continue
        ratio = SequenceMatcher(None, target_word, word).ratio()
        if ratio > max_ratio:
            max_ratio = ratio
            closest_word = word
    return closest_word

def find_wrong_alphabets(word1, word2):
    wrong_alphabets = []
    for i, (char1, char2) in enumerate(zip(word1, word2)):
        if char1 != char2:
            wrong_alphabets.append((i, char1))
    return wrong_alphabets

def swap_chars(input_str, mapping):
    """
    Swaps characters in the input string based on the provided mapping.
    
    Args:
        input_str (str): The input string.
        mapping (dict): A dictionary mapping characters to their replacements.
        
    Returns:
        str: The string with characters swapped according to the mapping.
    """
    # Create a translation table using the mapping
    translation_table = str.maketrans(mapping)
    
    # Use the translation table to swap characters in the input string
    output_str = input_str.translate(translation_table)
    
    return output_str


# Load dictionary
dictionary_filename = 'dictionary.txt'  # Change this to your dictionary file
dictionary = load_dictionary(dictionary_filename)



# Solve a cipher.
txt = "ĥj ĵjĥĵinŝesf aŝ vhmjhhmjzthmsf tzmvn gtj ĵsĵsĥsĉs fvh cvĥcjf vĥ ĥj ĵĥvf ivĥjf nsisfvĥgvnuj insctmj hjmvzs. gvzth ejĥjĥmj mnjzcgtĥj gsas vĥ ĥj usevms cjf bsnpth sĥvt etz ctje gt gvzth tzmvn ztz. cjf ŝzŝ vĥ ĥj mnszsajeins cjf nvtnth jĥ ĥj ĥvszs zsejzmv ĥtz nvls cjf mŝf ĵshmv dsncŝnth. ijĥujk tĥt nvjĥgvzth jĥ ĥj ĵjĥjŭs uv sb vz ejĥĵĥt iszj hmjms. us tĥt ĥvgth ĥtzcjf dsndĥŝpth ĵsnmjzmv ĥtz jĥ ĥjdĥjgj cjhmvĥs uŝe usnsmvs ijzth htz. ĉs ĥt jcŭvĵmsh gtut etz. ĥt ŝzŝdsfv nvzcszmth ĥj ivĥj ŝnisĥŝŭvnzs cjf ŭvĥjzmv etĥjzsz ĵvn ĥj ĵtzms uv htj ĉvfes. vcbthmth zŝn ŝzŝ vĥ ĥj hcĥjgtps djntmj uv ĥj invas cjf cjkntlth. ejĥjzmjk tĥt vhmth ĵnvmjf csevzŭt. iszgsĥŝ njcszmt jĥ gt etjz czjivmsz cjnĥsz ctŝ vhmshvhĵvnviĥv iszj ĥvnzjzms vz uŝuvc ajĵtmnsf ĵnt atŝmjpj gtgs. et mnseĵth atŝz uŝemtse uj mveĵs ejĥfŝzj csngsdĥŝpth jĵŝu etz cjf etjz ĵjĥjŭsz cjf ĥj jĥtjf nscsf cjf mtv ĥvcjzmvmsf cjfnjzŝzcsĥsf. hvu et ĵjnsĥthjĥ ĥt uŝe ĥt pjfv ntuth cŝz rt cjf et zvntŭvgŝh cŝnjlsz utnth ĥj ĉjcthms zv vhmth hsnathms ĥj ĵsĵsĥs mtse etntzujz nvpjzmsz."
print(len(txt))
s = SimpleSolver(txt)
# s.solve(method="deterministic")
s.solve(method="random")

# Input string
input_string = s.plaintext()

# Get words not in the dictionary
not_in_dictionary = words_not_in_dictionary(input_string, dictionary)
plaintext = input_string
iteration_count = 0  # Initialize the iteration counter
while iteration_count < 3:
    if not_in_dictionary:
        print("Words not in the dictionary:", not_in_dictionary)
        longest_word = find_longest_word(not_in_dictionary)
        closest_word = find_closest_word(longest_word, dictionary)
        print("Closest word to", longest_word, "is:", closest_word)
        wrong_alphabets = find_wrong_alphabets(longest_word, closest_word)
        print("Alphabets that need to be swapped:")

        for index, char in wrong_alphabets:
            print(f"Swap '{longest_word[index]}' at index {index} with '{closest_word[index]}'")
            char1 = longest_word[index]
            char2 = closest_word[index]
        mapping = {char1: char2, char2: char1}
        plaintext = swap_chars(plaintext, mapping)

        print(plaintext)
        not_in_dictionary = words_not_in_dictionary(plaintext, dictionary)
        iteration_count += 1  # Increment the iteration counter
    else:
        print("[+] All words in the string are in the dictionary.")
        print(plaintext)
        break


