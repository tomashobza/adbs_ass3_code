Ra = [
  (1, 3),
  (2, 16),
  (3, 25),
  (4, 9),
  (5, 5),
  (6, 31),
]

Rb = [
  (1, 12),
  (2, 34),
  (3, 17),
  (4, 56),
  (5, 22),
  (6, 34),
]

Sa = [
  (1, 34),
  (2, 22),
  (3, 17)
]

Sb = [
  (1, 7),
  (2, 4),
  (3, 9)
]

def select(rel, min, max):
  return [t[0] for t in rel if min <= t[1] <= max]

def reconstruct(rel, ids):
  return [t for t in rel if t[0] in ids]

def reverse(rel):
  return [(t[1], t[0]) for t in rel]

def join(rel1, rel2):
  rel2_dict = {t[0]: t[1] for t in rel2}
  return [(t[0], rel2_dict.get(t[1])) for t in rel1 if t[1] in rel2_dict]

def voidTail(rel):
  return [t[0] for t in rel]

def my_sum(rel):
  return sum(t[1] for t in rel)

def printRel(rel):
  for t in rel:
    print(t)
  print()

inter1 = select(Ra, 5, 20)
print("inter1:")
printRel(inter1)
inter2 = reconstruct(Rb, inter1)
print("inter2:")
printRel(inter2)
join_input_S = reverse(Sa)
print("join_input_S:")
printRel(join_input_S)
join_res = join(inter2, join_input_S)
print("join_res:")
printRel(join_res)
inter3 = voidTail(join_res)
print("inter3:")
printRel(inter3)
inter4 = reconstruct(Ra, inter3)
print("inter4:")
printRel(inter4)
result = my_sum(inter4)
print("result:")
print(result)