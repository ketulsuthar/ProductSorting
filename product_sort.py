
def find_parent_product(p, prods,  products, processed):
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

data = [
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
            "name": "Men",
            "id": 20,
            "parent_id": None
          }
    ]


print(process_products_data(data))








