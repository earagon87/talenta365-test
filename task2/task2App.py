import tkinter as tk
import string
import unittest

SPANISH_ALPHABET = list(string.ascii_uppercase)  # Assuming only uppercase letters
SPANISH_ALPHABET.insert(14, 'Ñ')  # Adding "Ñ" as the 15th Spanish letter, as ASCII considers it a special char


def number_to_col_name(number, alphabet=SPANISH_ALPHABET):
    """
    Returns the Excel-style column name for a given number, using the given alphabet.

    e.g. If given the Spanish alphabet:
        1 --> "A"
        15 --> "Ñ"
        27 --> "Z"
        28 --> "AA"
        29 --> "AB"
        55 --> "BA"
    """
    col_name = ""
    alphabet_len = len(alphabet)

    while number:
        number, r = divmod(number, alphabet_len)
        if r == 0:
            number -= 1
            r = alphabet_len

        col_name = f"{get_alphabet_letter(r, alphabet=alphabet)}{col_name}"

    return col_name


def get_alphabet_letter(position, alphabet=SPANISH_ALPHABET):
    """
    Returns the letter corresponding to the given relative position within the given alphabet.
    Any invalid position returns None.

    e.g. If given the Spanish alphabet:
        1 --> "A"
        15 --> "Ñ"
        27 --> "Z"
    """
    if position not in range(1, len(alphabet)+1):
        raise ValueError

    return  alphabet[position-1]

def convert_to_excel_name(entryField):
    result_lbl['text'] = ""
    try:
        result_lbl.configure(text = "Result: " + number_to_col_name(int(entryField.get())))
    except:
        result_lbl.configure(text = "Invalid data. Please enter a valid number!!")
        

def make_form(root):
    
    row = tk.Frame(root)
    entry_label = tk.Label(row, width=22, text="Enter a number: ", anchor='w')
    entry_field = tk.Entry(row)
    entry_field.insert(0, "0")
    row.pack(side=tk.TOP, 
                fill=tk.X, 
                padx=5, 
                pady=5)
    entry_label.pack(side=tk.LEFT)
    entry_field.pack(side=tk.RIGHT, 
                expand=tk.YES, 
                fill=tk.X)
    return entry_field

class TestSuite(unittest.TestCase):

    def test_number_to_col_name(self):
        self.assertEqual(number_to_col_name(1), "A")
        self.assertEqual(number_to_col_name(15), "Ñ")
        self.assertEqual(number_to_col_name(27), "Z")
        self.assertEqual(number_to_col_name(28), "AA")
        self.assertEqual(number_to_col_name(54), "AZ")
        self.assertEqual(number_to_col_name(55), "BA")
        self.assertEqual(number_to_col_name(81), "BZ")
        self.assertEqual(number_to_col_name(82), "CA")

    def test_get_alphabet_letter(self):
        self.assertEqual(get_alphabet_letter(1), "A")
        self.assertEqual(get_alphabet_letter(15), "Ñ")
        self.assertEqual(get_alphabet_letter(27), "Z")
        self.assertRaises(ValueError, get_alphabet_letter, 0)
        self.assertRaises(ValueError, get_alphabet_letter, 28)
        self.assertRaises(ValueError, get_alphabet_letter, -3)

if __name__ == '__main__':

    # Uncomment in case you want to run test cases
    #unittest.main()

    root = tk.Tk()
    root.title("Number to Excel-style convertor")

    result_lbl = tk.Label(root)
    result_lbl.pack(side=tk.BOTTOM)

    field = make_form(root)
    submit_btn = tk.Button(root, text='Convert', highlightbackground='#3E4149',
           command=(lambda e=field: convert_to_excel_name(e)))
    submit_btn.pack(side=tk.LEFT, padx=5, pady=5)
    root.mainloop()

