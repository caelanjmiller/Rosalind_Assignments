#Given two positive integers, return the integer corresponding to the square of the hypotenuse
# of the triangle whose legs have length a and b

def hypotenuse(a,b):
    a,b = int(a),int(b)
    c = a**2 + b**2
    print(f"{c}")
hypotenuse(912,952)