from __future__ import annotations
from dataclasses import dataclass
from .point import Point
from .point import G

@dataclass (frozen=True)
class Generator:
    """
    A generator over a curve: an initial point and the (pre-computed) order
    """
    G: Point    # a generator point on the curve
    n: int      # the order of the generating point, so 0*G = n*G = INF

bitcoin_gen = Generator(
    G = G,
    # the order of G is known and can be mathematically derived
    n = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
)