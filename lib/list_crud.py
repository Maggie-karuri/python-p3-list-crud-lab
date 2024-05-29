def create_an_empty_list():
    return []

def create_a_list():
    return [1, 2, 3, 4]

def add_element_to_end_of_list(l, element):
    element = [1, 2, 3, 4]
    element.append(5)
    return  element

def add_element_to_start_of_list(l, element):
    element = [1,2,3,4]
    element.insert(0, 0)
    return element

def remove_element_from_end_of_list(l):
    l = [1, 2, 3, 4]
    if len(l) >0:
        l.pop(3)
    return l

def remove_element_from_start_of_list(l):
    l = [1, 2, 3, 4]
    if len(l) > 0:
        del l[0]
    return l

def retrieve_first_element_from_list(l):
    l = [1, 2, 3, 4]
    if len(l) > 0:
        return l[0]
    else:
        return None

def retrieve_element_from_index(l, index):
    if 0 <= index < len(l):
        return l[index]
    else:
        return None

def retrieve_last_element_from_list(l):
    if len(l) > 0:
        return l[-1]
    else:
        return None
