
def find_parent_product(p, prods,  products, processed, stack=[]):
    """

    :param p: need to process product
    :param prods: dict of child : parent prodcut
    :param products: list of original products
    :param processed: process products index
    :return: return list of child to parent products
    """
    id = p['id']
    if id in processed:
        return stack
    index, parent_id = prods[id]
    if parent_id:
        stack.append(products[index])
        processed.add(id)
        index, _ = prods[parent_id]
        print(index)
        find_parent_product(products[index], prods, products, processed, stack)
    else:
        stack.append(products[index])
        processed.add(id)

    print(stack)
    return stack

def process_products_data(products):
    """


    :param products:
    :return:
    """
    result = []
    prods = {}

    processed = set()
    for i, p in enumerate(products):
        prods[p['id']] = (i, p['parent_id'])
    for p in products:
        stack = find_parent_product(p, prods, products, processed, [])
        while len(stack):
            s = stack.pop()
            result.append(s)

    if not all(processed):
        for index, procd in enumerate(processed):
            if not procd:
                result.append(products[index])

    return result