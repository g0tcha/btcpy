from bitcoin import Curve
from bitcoin import Point

# we can verify that the generator point is indeed on the curve, i.e y^2 = x^3 + 7 (mod p)
print("Generator IS on the curve : ", (Point.G.y**2 - Point.G.x**3 - 7) % Curve.bitcoin_curve.p == 0)

# some other totally random point will of course not be on the curve
import random
random.seed(1337)
x = random.randrange(0, Curve.bitcoin_curve.p)
y = random.randrange(0, Curve.bitcoin_curve.p)
print("Totally random point is not: ", (y**2 - x**3 - 7) % Curve.bitcoin_curve.p == 0)