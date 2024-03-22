# class Solution:
#     def shortestToChar(self, S: str, C: str) -> List[int]:
#         import numpy as np
#         # get all the indices for C in S
#         Indices=np.array([k for k, val in enumerate(S) if val==C])
#         return [min(abs(Indices-k)) for k in range(len(S))]
        

