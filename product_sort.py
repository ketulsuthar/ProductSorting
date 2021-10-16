
def find_parent_product(p, prods,  products, processed):
    """
    :param p: need to process product
    :param prods: dict of child : parent prodcut
    :param products: list of original products
    :param processed: process products index
    :return: return list of child to parent products
    """
    stack = []
    id = p['id']
    while not all(processed):
        index, parent_id = prods[id]
        if not processed[index]:
            stack.append(products[index])
            processed[index] = True
            if not parent_id:
                break
        id = parent_id
    return stack

def process_products_data(products):
    """
    :param products:
    :return:
    """
    result = []
    prods = {}

    processed = [False]* len(products)
    for i, p in enumerate(products):
        prods[p['id']] = (i, p['parent_id'])

    for p in products:
        stack = find_parent_product(p, prods, products, processed)
        while len(stack):
            s = stack.pop()
            result.append(s)

    if not all(processed):
        for index, procd in enumerate(processed):
            if not procd:
                result.append(products[index])

    return result







