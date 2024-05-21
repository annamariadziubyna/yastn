# Copyright 2024 The YASTN Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
""" Define rules for U(1)xU(1)xZ2 symmetry. """
import numpy as np
from .sym_abelian import sym_abelian

class sym_U1xU1xZ2(sym_abelian):
    """ U(1)xU(1)xZ2 -- here Z2 will be used to account for global fermionic parity. """

    SYM_ID = "U(1)xU(1)xZ2"
    NSYM = 3  # three ints used to distinguish symmetry sectors

    @classmethod
    def fuse(cls, charges, signatures, new_signature):
        """
        Fusion rule for ... symmetry

        Parameters
        ----------
            charges: nparray(int)
                `k x m x nsym` matrix, where `k` is the number of
                independent blocks, and `m` is the number of fused legs.

            signatures: numpy.ndarray(int)
                integer vector with `m` elements in `{-1, +1}`

            new_signature: int

        Returns
        -------
            nparray(int)
                integer matrix with shape (k,NSYM) of fused charges;
                includes multiplication by ``new_signature``
        """
        teff = new_signature * (charges.swapaxes(1,2) @ signatures)
        teff[:, 2] = np.mod(teff[:, 2], 2)
        return teff
