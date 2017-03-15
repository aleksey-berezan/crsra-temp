# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]
        else:
            self.name = None

def process_queries(queries):
    contacts = {}
    result = []

    for query in queries:
        number = query.number
        name = query.name
        type = query.type
        if type == "add":
            contacts[number] = name
        elif type == "del":
            if number in contacts:
                del contacts[number]
        elif type == "find":
            if number in contacts:
                result.append(contacts[number])
            else:
                result.append("not found")
        else:
            raise Exception("Unknown command: " + type)

    return result

n = int(input())
queries = [Query(input().split()) for i in range(n)]
result = process_queries(queries)
print('\n'.join(result))

