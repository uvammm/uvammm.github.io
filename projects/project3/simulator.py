import random
import hashlib
from datetime import datetime
import csv

# This function generates a random blood type
def rand_blood():
    b = random.random()
    if b < 0.45:
        return 'O'
    elif b < 0.85:
        return 'A'
    elif b < 0.95:
        return 'B'
    else:
        return 'AB'

# This function generates a random PRA type
def rand_pra():
    b = random.random()
    if b < 0.70:  # low PRA
        return 'Low'
    elif b < 0.90: # medium PRA
        return 'Medium'
    else: # high PRA
        return 'High'

def is_blood_compatible(blood_don, blood_recv):
    """
    This function returns True if the donor with blood type blood_don is
    compatible with receiver with bood type blood_recv.
    """
    if blood_don == 'O':
        return True
    elif blood_don == 'A':
        return blood_recv in ('A', 'AB')
    elif blood_don == 'B':
        return blood_recv in ('B', 'AB')
    elif blood_don == 'AB':
        return blood_recv == 'AB'
    else:
        raise InvalidParameterException("Invalid blood type: " + blood_don)

def is_tissue_compatible(recv_pra, recv_tissueid, don_tissueid):
    """
    Modeling actual tissue compatibility is complex, and depends on
    properties of different HLA markers and various other complications.
    Instead of dealing with the medical complexities, we use a simple 
    model that produces a uniformly-distributed value that is dependent
    on the two inputs, and outputs a discretized probability.
    
    It's not important to understand the following code. But you should 
    call this function with the receiver's PRA-type, receiver's tissue ID, 
    and the donor's tissue ID to check if their tissues are compatible or not.
    
    Example usage: is_tissue_compatible('Low', 4474, 3587)
    """
    
    # This code is a convoluted way to approximate a random oracle on the tissue ids (so the
    # output is uniformly random in [0, 1), but for a given tissue pair, the same output is always
    # produced). 
    
    hexval = hashlib.md5((str(recv_tissueid) + str(don_tissueid)).encode()).hexdigest()
    intval = int(hexval, 16)
    b = intval / (1 << 129 - 1)  # md5 generates 128-bit number; we normalize it to [0, 1]

    if recv_pra == 'Low':
        return b <= 0.95
    elif recv_pra == 'Medium':
        return b <= 0.45
    else:  # high pra
        assert recv_pra == 'High'
        return b <= 0.10

# This function returns True if the donor from pair1 is compatible with 
# receiver from pair2, otherwise it returns False
def is_pair_compatible(pair1, pair2):
    return is_blood_compatible(pair1['don_blood'], pair2['recv_blood']) and is_tissue_compatible(pair2['recv_pra'], pair2['recv_tissueid'], pair1['don_tissueid'])

# This function generates a random reciever-donor pair
def rand_pair():
    recv_tissueid = random.randint(0, 10000)
    recv_blood = rand_blood()
    recv_pra = rand_pra()
    recv_survprb = round(max(min(random.gauss(0.8, 0.5), 0.99), 0.01), 2)

    while True:
        don_tissueid = random.randint(0, 10000)
        don_blood = rand_blood()
        if not is_blood_compatible(don_blood, recv_blood) or not is_tissue_compatible(recv_pra, recv_tissueid, don_tissueid):
            break

    pair_dict = {'recv_tissueid': recv_tissueid,
                 'recv_blood': recv_blood,
                 'recv_pra': recv_pra,
                 'recv_survprb': recv_survprb,
                 'don_tissueid': don_tissueid,
                 'don_blood': don_blood,
                 }
    return pair_dict

def main():
    random.seed(4501)
    lst_pairs = []
    print("TimePeriod,ReceiverTissueID,ReceiverBloodType,ReceiverPRA,ReceiverSurvivalPrb,DonorTissueID,DonorBloodType")
    for t in range(6):
        for i in range(100):
            pair_dict = rand_pair()
            print(','.join([str(t)] + [str(pair_dict[k]) for k in pair_dict]))
            lst_pairs.append(pair_dict)

if __name__ == "__main__":
    main()
