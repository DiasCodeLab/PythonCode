#=================================
# Verificação de array 2d (matriz)ss
#=================================

import numpy as np

def array_dois_d():
    objeto = np.array([
        [1,2,3],
        [3,2,1],
        [4,5,6]]
    )
    return objeto.ndim

dimencoes = array_dois_d()
print(dimencoes)