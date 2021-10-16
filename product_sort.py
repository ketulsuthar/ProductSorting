
def find_parent_product(p, prods,  products, processed, stack=[]):
    """
    it serach all the prodcut until parent found for it.
    :param p: need to process product
    :param prods: dict of child : parent prodcut
    :param products: list of original products
    :param processed: set of process products id
    :param stack: list of proceed products
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
        find_parent_product(products[index], prods, products, processed, stack)
    else:
        stack.append(products[index])
        processed.add(id)
    return stack

def process_products_data(products):
    """ it prcoess list of product and sore product based on parent product
    :param products: list of products
    :return: return sorted product.
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


if __name__ == "__main__":
    data = [
              {
                "name": "Men",
                "id": 20,
                "parent_id": 51
              },
              {
                "name": "Accessories",
                "id": 1,
                "parent_id": 20,
              },
              {
                "name": "Watches",
                "id": 57,
                "parent_id": 1
              },
              {
                "name": "Watches1",
                "id": 51,
                "parent_id": None
              },
        ]


    print(process_products_data(data))