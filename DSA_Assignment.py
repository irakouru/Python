def find_permutations(elements):
    generated_permutations = []
    current_permutation = ""
    elements_to_permute = elements[:]

    def permutation(generated_permutations, current_permutation, elements_to_permute):


        if len(elements_to_permute) != 0:
            for element in elements_to_permute:
                next_permutation = current_permutation + element
                remaining_elements = elements_to_permute.copy()
                remaining_elements.remove(element)
                permutation(generated_permutations, next_permutation, remaining_elements) 

        else:
            generated_permutations.append(current_permutation)


    permutation(generated_permutations, current_permutation, elements_to_permute)

    return generated_permutations

# Example:
input_list = ["1", "2", "3", "4"]
result = find_permutations(input_list)
print(result)

