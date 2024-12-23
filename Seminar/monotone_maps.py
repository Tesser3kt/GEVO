def generate_tuples(n, tpl, tuples):
    if len(tpl) == n:
        tuples.append(tpl)
    else:
        for i in range(1, n+1):
            generate_tuples(n, tpl+(i,), tuples)


def nondecreasing_tuple(tpl):
    for i in range(len(tpl)-1):
        if tpl[i] > tpl[i+1]:
            return False
    return True


n = 3
tuples = []
generate_tuples(n, (), tuples)
tuples = ["".join(str(x) for x in tpl)
          for tpl in tuples if nondecreasing_tuple(tpl)]
print(tuples)
