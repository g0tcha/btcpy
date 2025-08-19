from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Curve:
    """
    Elliptic Curve over the field of integers modulo a prime.
    Points on the curve satisfy y^2 = x^3 + a*x + b (mod p).
    """
    p: int
    a: int
    b: int

# secp256k1 uses a = 0, b = 7, so the function is y^2 = x^3 + 7 (mod p)
bitcoin_curve = Curve(
    p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F,
    a = 0x0000000000000000000000000000000000000000000000000000000000000000,
    b = 0x0000000000000000000000000000000000000000000000000000000000000007,
)