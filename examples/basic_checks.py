from bitcoin import bitcoin_curve
from bitcoin import bitcoin_gen
from bitcoin import G

# we can verify that the generator point is indeed on the curve, i.e y^2 = x^3 + 7 (mod p)
print("Generator IS on the curve : ", (G.y**2 - G.x**3 - 7) % bitcoin_curve.p == 0)

# some other totally random point will of course not be on the curve
import random
random.seed(1337)
x = random.randrange(0, bitcoin_curve.p)
y = random.randrange(0, bitcoin_curve.p)
print("Totally random point is not: ", (y**2 - x**3 - 7) % bitcoin_curve.p == 0)

secret_key = int.from_bytes(b'Vinz Bitcoin Testnet', 'big')
assert 1 <= secret_key < bitcoin_gen.n
print(secret_key)