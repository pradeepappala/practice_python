import operator

def person_lister(f):
    def inner(_people):
        return [f(x) for x in sorted(_people, key=lambda y:int(y[2]))]
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    # people = [input().split() for i in range(int(input()))]
    people = ['Mike Thomson 20 M', 'Robert Bustle 32 M', 'Andria Bustle 30 F']
    people = [x.split(' ') for x in people]
    print(*name_format(people), sep='\n')

