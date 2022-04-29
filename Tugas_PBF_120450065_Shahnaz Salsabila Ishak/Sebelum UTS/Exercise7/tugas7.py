#============================================#
# Nomor 1

def enumerasi(sequence):
  return list(map(lambda i, l: (i, l), range(len(sequence)), list(sequence)))

print(enumerasi('akulupa'))

#============================================#
# Nomor 2
def factorof(angka):
  return list(filter(lambda x: angka%x == 0, range(1, angka+1)))

print(factorof(24))

#============================================#
# Nomor 3
A = [ [3,4], [5,6]]
B = [ [1,2], [7,8]]

def normal_mult(A, B):
  return list(map(lambda ri, rj: list(map(lambda rii, rjj: rii+rjj, ri, rj)), A, B))

def det(matrix):
  return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

C = normal_mult(A,B)
print(det(C))