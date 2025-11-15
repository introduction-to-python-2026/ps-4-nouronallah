def split_before_each_uppercase(formula):
    start = 0
    end = 1
    elements_1st = []

    if not formula:
        return elements_1st

    while end < len(formula):
        if formula[end].isupper():
elements_1st.append(formula[start:end])
           start = end
        end+=1
   elements_1st.append(formula[start:])

   return elements_1st

def split_at_first_digit(formula):
    for char_index, char in
enumerate(formula):
        if char.isdigit():
            return formula[:char_index],
int(formula[char_index:])
    return formula, 1
