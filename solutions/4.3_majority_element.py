def majority_element_naive(elements):
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1
    return 0

def majority_element(elements):
    counter = dict()
    counter[elements[0]] = 1
    most_repeated_element = elements[0]

    for e in elements[1:]:
        if e in counter:
            counter[e] += 1
            if counter[e] >= counter[most_repeated_element]: # compare temporary most repeated element only to newly appear element
                most_repeated_element = e                    # to find the most repeated element in least time
        else:
            counter[e] = 1

    if counter[most_repeated_element] > len(elements) / 2:
        return 1
    return 0


if __name__ == '__main__':
    # input_n = 5
    # input_elements = [2, 3, 9, 2, 2]

    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    # print(majority_element_naive(input_elements))
    print(majority_element(input_elements))
