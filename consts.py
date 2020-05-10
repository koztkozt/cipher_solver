# flake8: noqa

import numpy as np

# English alphabet has 26 letters.
STANDARD_ALPHABET_SIZE = 26

# Source: http://norvig.com/mayzner.html
# The frequency of the letters in the English alphabet.
ENGLISH_LETTER_FREQUENCIES = {
    "e": 0.1249,
    "t": 0.0928,
    "a": 0.0804,
    "o": 0.0764,
    "i": 0.0757,
    "n": 0.0723,
    "s": 0.0651,
    "r": 0.0628,
    "h": 0.0505,
    "l": 0.0407,
    "d": 0.0382,
    "c": 0.0334,
    "u": 0.0273,
    "m": 0.0251,
    "f": 0.0240,
    "p": 0.0214,
    "g": 0.0187,
    "w": 0.0168,
    "y": 0.0166,
    "b": 0.0148,
    "v": 0.0105,
    "k": 0.0054,
    "x": 0.0023,
    "j": 0.0016,
    "q": 0.0012,
    "z": 0.0009,
}

# Source: http://norvig.com/mayzner.html
# This is a (26 x 26) array containing the digram frequencies for the English language
# and # is used for scoring potential solutions. The row corresponds to the first letter
# and the column to the second. For example, the frequency for the digram "df" would be
# at row 4 and column 6, i.e. DIGRAM_FREQS_ENGLISH[3][5], with the value 0.00003.
# fmt: off
DIGRAM_FREQS_ENGLISH = np.array([
    [0.00003, 0.00230, 0.00448, 0.00368, 0.00012, 0.00074, 0.00205, 0.00014, 0.00316, 0.00012, 0.00105, 1.00087, 0.00285, 1.00985, 0.00005, 0.00203, 0.00002, 1.00075, 0.00871, 1.00487, 0.00119, 0.00205, 0.00060, 0.00019, 0.00217, 0.00012],
    [0.00146, 0.00011, 0.00002, 0.00002, 0.00576, 0.00000, 0.00000, 0.00001, 0.00107, 0.00023, 0.00000, 0.00233, 0.00003, 0.00002, 0.00195, 0.00001, 0.00000, 0.00112, 0.00046, 0.00017, 0.00185, 0.00004, 0.00000, 0.00000, 0.00176, 0.00000],
    [0.00538, 0.00001, 0.00083, 0.00002, 0.00651, 0.00001, 0.00001, 0.00598, 0.00281, 0.00000, 0.00118, 0.00149, 0.00003, 0.00001, 0.00794, 0.00001, 0.00005, 0.00149, 0.00023, 0.00461, 0.00163, 0.00000, 0.00000, 0.00000, 0.00042, 0.00001],
    [0.00151, 0.00003, 0.00003, 0.00043, 0.00765, 0.00003, 0.00031, 0.00005, 0.00493, 0.00005, 0.00000, 0.00032, 0.00018, 0.00008, 0.00188, 0.00002, 0.00001, 0.00085, 0.00126, 0.00003, 0.00148, 0.00019, 0.00008, 0.00000, 0.00050, 0.00000],
    [0.00688, 0.00027, 0.00477, 1.00168, 0.00378, 0.00163, 0.00120, 0.00026, 0.00183, 0.00005, 0.00016, 0.00530, 0.00374, 1.00454, 0.00073, 0.00172, 0.00057, 2.00048, 1.00339, 0.00413, 0.00031, 0.00255, 0.00117, 0.00214, 0.00144, 0.00005],
    [0.00164, 0.00000, 0.00001, 0.00000, 0.00237, 0.00146, 0.00001, 0.00000, 0.00285, 0.00000, 0.00000, 0.00065, 0.00001, 0.00000, 0.00488, 0.00000, 0.00000, 0.00213, 0.00006, 0.00082, 0.00096, 0.00000, 0.00000, 0.00000, 0.00009, 0.00000],
    [0.00148, 0.00000, 0.00000, 0.00003, 0.00385, 0.00001, 0.00025, 0.00228, 0.00152, 0.00000, 0.00000, 0.00061, 0.00010, 0.00066, 0.00132, 0.00000, 0.00000, 0.00197, 0.00051, 0.00015, 0.00086, 0.00000, 0.00001, 0.00000, 0.00026, 0.00000],
    [0.00926, 0.00004, 0.00001, 0.00003, 3.00075, 0.00002, 0.00000, 0.00001, 0.00763, 0.00000, 0.00000, 0.00013, 0.00013, 0.00026, 0.00485, 0.00001, 0.00000, 0.00084, 0.00015, 0.00130, 0.00074, 0.00000, 0.00005, 0.00000, 0.00050, 0.00000],
    [0.00286, 0.00099, 0.00699, 0.00296, 0.00385, 0.00203, 0.00255, 0.00002, 0.00023, 0.00001, 0.00043, 0.00432, 0.00318, 2.00433, 0.00835, 0.00089, 0.00011, 0.00315, 1.00128, 1.00123, 0.00017, 0.00288, 0.00001, 0.00022, 0.00000, 0.00064],
    [0.00026, 0.00000, 0.00000, 0.00000, 0.00052, 0.00000, 0.00000, 0.00000, 0.00003, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00054, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00059, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
    [0.00017, 0.00001, 0.00000, 0.00001, 0.00214, 0.00002, 0.00003, 0.00003, 0.00098, 0.00000, 0.00000, 0.00011, 0.00002, 0.00051, 0.00006, 0.00001, 0.00000, 0.00003, 0.00048, 0.00001, 0.00003, 0.00000, 0.00002, 0.00000, 0.00006, 0.00000],
    [0.00528, 0.00007, 0.00012, 0.00253, 0.00829, 0.00053, 0.00006, 0.00002, 0.00624, 0.00000, 0.00020, 0.00577, 0.00023, 0.00006, 0.00387, 0.00019, 0.00000, 0.00010, 0.00142, 0.00124, 0.00135, 0.00035, 0.00013, 0.00000, 0.00425, 0.00000],
    [0.00565, 0.00090, 0.00004, 0.00001, 0.00793, 0.00004, 0.00001, 0.00001, 0.00318, 0.00000, 0.00000, 0.00005, 0.00096, 0.00009, 0.00337, 0.00239, 0.00000, 0.00003, 0.00093, 0.00001, 0.00115, 0.00000, 0.00001, 0.00000, 0.00062, 0.00000],
    [0.00347, 0.00004, 0.00416, 1.00352, 0.00692, 0.00067, 0.00953, 0.00011, 0.00339, 0.00011, 0.00052, 0.00064, 0.00028, 0.00073, 0.00465, 0.00006, 0.00006, 0.00009, 0.00509, 1.00041, 0.00079, 0.00052, 0.00006, 0.00003, 0.00098, 0.00004],
    [0.00057, 0.00097, 0.00166, 0.00195, 0.00039, 1.00175, 0.00094, 0.00021, 0.00088, 0.00007, 0.00064, 0.00365, 0.00546, 1.00758, 0.00210, 0.00224, 0.00001, 1.00277, 0.00290, 0.00442, 0.00870, 0.00178, 0.00330, 0.00019, 0.00036, 0.00003],
    [0.00324, 0.00001, 0.00001, 0.00001, 0.00478, 0.00001, 0.00000, 0.00094, 0.00123, 0.00000, 0.00001, 0.00263, 0.00016, 0.00001, 0.00361, 0.00137, 0.00000, 0.00474, 0.00055, 0.00106, 0.00105, 0.00000, 0.00001, 0.00000, 0.00012, 0.00000],
    [0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00148, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
    [0.00686, 0.00027, 0.00121, 0.00189, 1.00854, 0.00032, 0.00100, 0.00015, 0.00728, 0.00001, 0.00097, 0.00086, 0.00175, 0.00160, 0.00727, 0.00042, 0.00001, 0.00121, 0.00397, 0.00362, 0.00128, 0.00069, 0.00013, 0.00001, 0.00248, 0.00001],
    [0.00218, 0.00008, 0.00155, 0.00005, 0.00932, 0.00017, 0.00002, 0.00315, 0.00550, 0.00000, 0.00039, 0.00056, 0.00065, 0.00009, 0.00398, 0.00191, 0.00007, 0.00006, 0.00405, 1.00053, 0.00311, 0.00001, 0.00024, 0.00000, 0.00057, 0.00000],
    [0.00530, 0.00003, 0.00026, 0.00001, 1.00205, 0.00006, 0.00002, 3.00556, 1.00343, 0.00000, 0.00000, 0.00098, 0.00026, 0.00010, 1.00041, 0.00004, 0.00000, 0.00426, 0.00337, 0.00171, 0.00255, 0.00001, 0.00082, 0.00000, 0.00227, 0.00004],
    [0.00136, 0.00089, 0.00188, 0.00091, 0.00147, 0.00019, 0.00128, 0.00001, 0.00101, 0.00001, 0.00005, 0.00346, 0.00138, 0.00394, 0.00011, 0.00136, 0.00000, 0.00543, 0.00454, 0.00405, 0.00001, 0.00003, 0.00000, 0.00004, 0.00005, 0.00002],
    [0.00140, 0.00000, 0.00000, 0.00000, 0.00825, 0.00000, 0.00000, 0.00000, 0.00270, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00071, 0.00000, 0.00000, 0.00001, 0.00001, 0.00000, 0.00002, 0.00000, 0.00000, 0.00000, 0.00005, 0.00000],
    [0.00385, 0.00001, 0.00001, 0.00004, 0.00361, 0.00002, 0.00000, 0.00379, 0.00374, 0.00000, 0.00001, 0.00015, 0.00001, 0.00079, 0.00222, 0.00001, 0.00000, 0.00031, 0.00035, 0.00007, 0.00001, 0.00000, 0.00000, 0.00000, 0.00002, 0.00000],
    [0.00030, 0.00000, 0.00026, 0.00000, 0.00022, 0.00002, 0.00000, 0.00004, 0.00039, 0.00000, 0.00000, 0.00001, 0.00000, 0.00000, 0.00003, 0.00067, 0.00000, 0.00000, 0.00000, 0.00047, 0.00005, 0.00002, 0.00000, 0.00003, 0.00003, 0.00000],
    [0.00016, 0.00004, 0.00014, 0.00007, 0.00093, 0.00001, 0.00003, 0.00001, 0.00029, 0.00000, 0.00000, 0.00015, 0.00024, 0.00013, 0.00150, 0.00025, 0.00000, 0.00008, 0.00097, 0.00017, 0.00001, 0.00000, 0.00003, 0.00000, 0.00000, 0.00002],
    [0.00025, 0.00000, 0.00000, 0.00000, 0.00050, 0.00000, 0.00000, 0.00001, 0.00012, 0.00000, 0.00000, 0.00001, 0.00000, 0.00000, 0.00007, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00002, 0.00000, 0.00000, 0.00000, 0.00002, 0.00003],
])
# fmt: on
