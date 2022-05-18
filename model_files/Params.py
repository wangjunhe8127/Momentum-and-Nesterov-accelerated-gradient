import numpy as np
def PARAMS(num):
    res={
    # MG第一题
    1:{
        'dimension':    2,
        'init_x':       np.array([-5, -3], dtype=float),
        'alpha':        5*10**-5,
        'beta' :        0.9,
        'steps':        2*10**5,
        'MG':           True,
    },
    # MG第二题
    2:{
        'dimension':    7,
        'init_x':       np.array([-5, -3, 4, 6, 7, 1, 2], dtype=float),
        'alpha':        1*10**-5,
        'beta' :        0.9,
        'steps':        5*10**2,
        'MG':           True,
    },
    # NAG题
    3:{
        'dimension':    2,
        'init_x':       np.array([-5, -2], dtype=float),
        'alpha':        5*10**-3,
        'beta' :        0.9,
        'steps':        2*10**4,
        'MG':           False,
    },
    # NAG题
    4:{
        'dimension':    2,
        'init_x':       np.array([-5, -2], dtype=float),
        'alpha':        5*10**-3,
        'beta' :        0.9,
        'steps':        2*10**4,
        'MG':           False,
    },
    # NAG题
    5:{
        'dimension':    2,
        'init_x':       np.array([-5, -2], dtype=float),
        'alpha':        9*10**-2,
        'beta' :        0.9,
        'steps':        2*10**4,
        'MG':           False,
    },
    # NAG题
    6:{
        'dimension':    2,
        'init_x':       np.array([-5, -2], dtype=float),
        'alpha':        9*10**-2,
        'beta' :        0.5,
        'steps':        2*10**4,
        'MG':           False,
    },
    # NAG题
    7:{
        'dimension':    2,
        'init_x':       np.array([-5, -2], dtype=float),
        'alpha':        9*10**-2,
        'beta' :        0.1,
        'steps':        2*10**4,
        'MG':           False,
    },
    }
    return res.get(num,None)
