grades = [25,30,18]
#a vector, more in general a tensor



def vector_add(v,w):
    '''Adds corresponding elements'''
    assert len(v) == len(w), "vectors must be the same length"
    return [v_i+w_i for v_i,w_i in zip(v,w)]
#zip allows to iterate on two lists/vectors at the same time
#done with list comprehension, which allows to initialize vectors/lists in one line

assert vector_add([1, 2, 3], [4, 5, 6]) == [5, 7, 9]



def vector_subtract(v,w):
    '''Subtract corresponding elements'''
    assert len(v) == len(w), "vectors must be the same length"
    return [v_i-w_i for v_i,w_i in zip(v,w)]

assert vector_subtract([5, 7, 9], [4, 5, 6]) == [1, 2, 3]



def vector_sum(vectors):
    '''Adds all corresponding elements'''
    result=vectors[0]
    for vector in vectors[1:]:
        result = vector_add(result,vector)
    return result

assert vector_sum([[1, 2], [3, 4], [5, 6], [7, 8]]) == [16, 20]



#Or alternatively
def vector_sum(vectors):
    #Sums all corresponding elements
    # Check that vectors is not empty
    assert vectors, "no vectors provided!"

    # Check the vectors are all the same size
    num_elements = len(vectors[0])
    assert all(len(v) == num_elements for v in vectors), "different sizes!"

    # the i-th element of the result is the sum of every vector[i]
    return [sum(vector[i] for vector in vectors)
            for i in range(num_elements)]
assert vector_sum([[1, 2], [3, 4], [5, 6], [7, 8]]) == [16, 20]



def scalar_multiply(c, v):
    """Multiplies every element by c"""
    return [c * v_i for v_i in v]

assert scalar_multiply(2, [1, 2, 3]) == [2, 4, 6]



#YOUR TURN

#Now do it yourselves for the following functions
def vector_mean(vectors):
    """Computes the element-wise average"""
    pass

assert vector_mean([[1, 2], [3, 4], [5, 6]]) == [3, 4]


def dot(v, w):
    """Computes v_1 * w_1 + ... + v_n * w_n"""
    pass

assert dot([1, 2, 3], [4, 5, 6]) == 32  # 1 * 4 + 2 * 5 + 3 * 6


def sum_of_squares(v):
    """Returns v_1 * v_1 + ... + v_n * v_n"""
    pass

assert sum_of_squares([1, 2, 3]) == 14  # 1 * 1 + 2 * 2 + 3 * 3


import math
def magnitude(v):
    """Returns the magnitude (or length) of v, using math.sqrt"""
    pass

assert magnitude([3, 4]) == 5


def squared_distance(v, w):
    """Computes (v_1 - w_1) ** 2 + ... + (v_n - w_n) ** 2"""
    pass


def distance(v, w):
    """Computes the distance between v and w"""
    pass



#Matrices
    
A = [[1, 2, 3],  # A has 2 rows and 3 columns
     [4, 5, 6]]

B = [[1, 2],     # B has 3 rows and 2 columns
     [3, 4],
     [5, 6]]

#Matrices are lists of lists
#Each inner list is a row, of the same size
#Generally represented with capital letters

#Matrices represent gray scale images
#What about images?
#RGB is a 3D tensor: 1 matrix for the R, G and B channels
#PNG has a 4th channel, the alpha channel for transparency

#So len(A) is the number of rows
#len[A[0]] is the number of columns
def shape(A):
    """Returns (# of rows of A, # of columns of A)"""
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0   # number of elements in first row
    return num_rows, num_cols

shape(A)


def get_row(A, i):
    """Returns the i-th row of A (as a Vector)"""
    return A[i]             # A[i] is already the i-th row

get_row(A, 1)


def get_column(A, j):
    """Returns the j-th column of A (as a Vector)"""
    return [A_i[j]          # j-th element of row A_i
            for A_i in A]   # for each row A_i

get_column(A, 1)






#Let's assume entry_fn a function to provide entry_fn(i,j)
def make_matrix(num_rows,num_cols,entry_fn):
    """
    Returns a num_rows x num_cols matrix
    whose (i,j)-th entry is entry_fn(i, j)
    """
    return [[entry_fn(i, j)             # given i, create a list
             for j in range(num_cols)]  #   [entry_fn(i, 0), ... ]
            for i in range(num_rows)]   # create one list for each i
#Note the [] brackets

def equal_fn(i,j):
    """Returns 1 if i==j """
    return 1 if i==j else 0

def identity_matrix(n):
    """Returns the n x n identity matrix"""
    return make_matrix(n, n, equal_fn)

identity_matrix(5)
assert identity_matrix(5) == [[1, 0, 0, 0, 0],
                              [0, 1, 0, 0, 0],
                              [0, 0, 1, 0, 0],
                              [0, 0, 0, 1, 0],
                              [0, 0, 0, 0, 1]]


#Alternatively
def identity_matrix(n):
    """Returns the n x n identity matrix, using lambda"""
    return make_matrix(n, n, lambda i, j: 1 if i == j else 0)

assert identity_matrix(5) == [[1, 0, 0, 0, 0],
                              [0, 1, 0, 0, 0],
                              [0, 0, 1, 0, 0],
                              [0, 0, 0, 1, 0],
                              [0, 0, 0, 0, 1]]


data = [[70, 170, 40],
        [65, 120, 26],
        [77, 250, 19],
        # ....
       ]


#            user 0  1  2  3  4  5  6  7  8  9
#
friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
               (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

friend_matrix = [[0, 1, 1, 0, 0, 0, 0, 0, 0, 0],  # user 0
                 [1, 0, 1, 1, 0, 0, 0, 0, 0, 0],  # user 1
                 [1, 1, 0, 1, 0, 0, 0, 0, 0, 0],  # user 2
                 [0, 1, 1, 0, 1, 0, 0, 0, 0, 0],  # user 3
                 [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],  # user 4
                 [0, 0, 0, 0, 1, 0, 1, 1, 0, 0],  # user 5
                 [0, 0, 0, 0, 0, 1, 0, 0, 1, 0],  # user 6
                 [0, 0, 0, 0, 0, 1, 0, 0, 1, 0],  # user 7
                 [0, 0, 0, 0, 0, 0, 1, 1, 0, 1],  # user 8
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]]  # user 9

assert friend_matrix[0][2] == 1, "0 and 2 are friends"
assert friend_matrix[0][8] == 0, "0 and 8 are not friends"

#Note it's symmetric
# only need to look at one row

friends_of_five = [i
                   for i, is_friend in enumerate(friend_matrix[5])
                   if is_friend]

friends_of_five















#YOUR TURN

#Now do it yourselves for the friends of five and three



friends_of_five_and_three = ...

friends_of_five_and_three


















