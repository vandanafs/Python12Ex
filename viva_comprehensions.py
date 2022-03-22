from typing import List, Dict, Set, Callable
import enum


class Parity(enum.Enum):
    ODD = 0
    EVEN = 1



def gen_list(start: int, stop: int, parity: Parity) -> List[int]:
    """
    Oh no some evil developer decided not to write docstrings. Maybe you can use the test cases to decipher
    what this method was supposed to do. Hey if you do, maybe you could do some good in this world by
    updating this here docstring to something useful.

    :param start:
    :param stop:
    :param parity:
    :return:
    """
   # if parity is parity.EVEN:
   #     res=[x for x in range(start,stop) if x%2==0]
   # else:
    #    res=[x for x in range(start,stop) if x%2==1]
   #return res

    return [x for x in range(start, stop) if (parity == parity.EVEN  and x % 2 == 0) or (parity == parity.ODD and x % 2 !=0)]

def gen_dict(start: int, stop: int, strategy: Callable) -> Dict:
    """
    Oh no some evil developer decided not to write docstrings. Maybe you can use the test cases to decipher
    what this method was supposed to do. Hey if you do, maybe you could do some good in this world by
    updating this here docstring to something useful.


    :param start:
    :param stop:
    :param strategy:
    :return:
    """
    #list_comp=[value for value in range(start, stop) ]
    #print(list_comp)
    #dict= {x:strategy(x) for x in list_comp }
    #return dict

    return { x:strategy(x) for x in range(start,stop)}







def gen_set(val_in: str) -> Set:
    """
    Oh no some evil developer decided not to write docstrings. Maybe you can use the test cases to decipher
    what this method was supposed to do. Hey if you do, maybe you could do some good in this world by
    updating this here docstring to something useful.

    :param val_in:
    :return:
    """
    dict_comp={val_in[x].upper() for x in range(0,len(val_in)) if val_in[x].islower()}
    list(dict_comp).sort()
    return set(dict_comp)

    #return{x.upper() for x in val_in if x==x.lower()}

