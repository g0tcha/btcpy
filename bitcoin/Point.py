from __future__ import annotations
from dataclasses import dataclass
from .curve import Curve
from .curve import bitcoin_curve

@dataclass 
class Point:
    """ An integer point (x,y) on a Curve"""
    curve: Curve
    x: int
    y: int

G = Point(
    curve = bitcoin_curve,
    x = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798,
    y = 0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8,
)

