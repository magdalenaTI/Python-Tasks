import copy

def plugboard(the_text, matches):
    from_set_to_str = ""
    ready = ""

    for character in the_text:
        new_matches = ""
        for one_pair in  matches:
            if character in one_pair:
               new_matches = ''.join(one_pair)
               from_set_to_str = copy.deepcopy(one_pair)
               from_set_to_str.remove(character) 
               res=''.join(from_set_to_str)
               ready += res
               break
        if character not in new_matches:
            ready += character
    return ready

def rotor(the_text, matches):
    ready=""

    for character in the_text:
        if character == " ":
             ready += " "
        if character in matches: 
            res = matches.get(character)
            ready += res
    return ready

def enigma_encrypt(plugboard_position, rotor_position):
    def encryptor(func):
        def encrypt_print(txt):
            first = plugboard(txt, plugboard_position)
            result = rotor(first, rotor_position)
            return func(result)
        return encrypt_print
    return encryptor

def enigma_decrypt(plugboard_position, rotor_position):
    def decryptor(func):
        def decrypt_print(txt):
            res = {v: k for k, v in rotor_position.items()}
            first = rotor(txt, res)
            result = plugboard(first, plugboard_position)
            return func(result)
        return decrypt_print
    return decryptor





plugboard_position = [{'a', 'c'}, {'t', 'z'}]
rotor_position = {'v': 'd', 'd': 'v', 'y': 'u', 'n': 'n', 'i': 'w', 'z': 'p',
                  's': 'e', 'x': 's', 'h': 'f', 'b': 'x', 'u': 'c', 'p': 'q',
                  'r': 'g', 'q': 'j', 'e': 't', 'l': 'y', 'o': 'z', 'g': 'o',
                  'k': 'b', 't': 'h', 'j': 'm', 'a': 'a', 'w': 'i', 'f': 'l',
                  'm': 'r', 'c': 'k'}

rotor('enigma', rotor_position) # tnwora
plugboard('enigma', plugboard_position) # enigmc

encryptor = enigma_encrypt(plugboard_position=plugboard_position,
                           rotor_position=rotor_position)
decryptor = enigma_decrypt(plugboard_position=plugboard_position,
                           rotor_position=rotor_position)

encrypt_print = encryptor(print)
decrypt_print = decryptor(print)

encrypt_print('enigma') # tnwork
decrypt_print('tnwork') # enigma   
