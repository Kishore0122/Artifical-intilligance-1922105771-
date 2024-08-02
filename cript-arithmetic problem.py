import itertools

def solve_cryptarithm():
    letters = 'SENDMORY'
    digits = '0123456789'
    
    assert len(letters) <= len(digits), "More unique letters than available digits."

    for perm in itertools.permutations(digits, len(letters)):
        mapping = dict(zip(letters, perm))

        if mapping['S'] == '0' or mapping['M'] == '0':
            continue
        
        send = int(''.join(mapping[letter] for letter in 'SEND'))
        more = int(''.join(mapping[letter] for letter in 'MORE'))
        money = int(''.join(mapping[letter] for letter in 'MONEY'))
        
        if send + more == money:
            print(f"SEND = {send}, MORE = {more}, MONEY = {money}")
            print(f"Mapping: {mapping}")
            return

solve_cryptarithm()
