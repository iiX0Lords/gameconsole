import math

class Vector3:
    """
    A class to represent a 3D vector, accessible via attributes or tuple-like indexing.
    """
    def __init__(self, x=0.0, y=0.0, z=0.0):
        """Initialize the vector with x, y, and z components."""
        self.x = x
        self.y = y
        self.z = z

    @staticmethod
    def lerp(v1, v2, t):
        """
        Linearly interpolate between two Vector3 instances.
        :param v1: Start vector
        :param v2: End vector
        :param t: Interpolation factor (0.0 = v1, 1.0 = v2)
        :return: Interpolated Vector3
        """
        if not (0 <= t <= 1):
            raise ValueError("Interpolation factor t must be between 0 and 1")
        return Vector3(
            v1.x + (v2.x - v1.x) * t,
            v1.y + (v2.y - v1.y) * t,
            v1.z + (v2.z - v1.z) * t
        )

    def __repr__(self):
        """Return a string representation of the vector for debugging."""
        return f"Vector3(x={self.x}, y={self.y}, z={self.z})"

    def __str__(self):
        """Return a human-readable string representation of the vector."""
        return f"<{self.x}, {self.y}, {self.z}>"

    def __getitem__(self, index):
        """Allow tuple-like access (e.g., vector[0] gives x)."""
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        elif index == 2:
            return self.z
        else:
            raise IndexError("Vector3 index out of range (0, 1, or 2)")

    def __iter__(self):
        """Allow iteration (e.g., tuple(vector))."""
        yield self.x
        yield self.y
        yield self.z

    def __add__(self, other):
        """Overload the + operator for vector addition."""
        if isinstance(other, Vector3):
            return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)
        raise TypeError("Operand must be a Vector3 instance")

    def __sub__(self, other):
        """Overload the - operator for vector subtraction."""
        if isinstance(other, Vector3):
            return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)
        raise TypeError("Operand must be a Vector3 instance")

    def __mul__(self, scalar):
        """Overload the * operator for scalar multiplication."""
        if isinstance(scalar, (int, float)):
            return Vector3(self.x * scalar, self.y * scalar, self.z * scalar)
        raise TypeError("Operand must be an int or float")

    def __rmul__(self, scalar):
        """Overload the * operator for reverse scalar multiplication (e.g., 2 * vector)."""
        return self.__mul__(scalar)

    def dot(self, other):
        """Calculate the dot product with another vector."""
        if isinstance(other, Vector3):
            return self.x * other.x + self.y * other.y + self.z * other.z
        raise TypeError("Operand must be a Vector3 instance")

    def magnitude(self):
        """Calculate the magnitude (length) of the vector."""
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def normalize(self):
        """Return a new unit vector (magnitude 1) in the same direction."""
        mag = self.magnitude()
        if mag == 0:
            return Vector3(0.0, 0.0, 0.0)
        return Vector3(self.x / mag, self.y / mag, self.z / mag)

class Vector2:
    """
    A class to represent a 2D vector, accessible via attributes or tuple-like indexing.
    """
    def __init__(self, x=0.0, y=0.0):
        """Initialize the vector with x and y components."""
        self.x = x
        self.y = y

    @staticmethod
    def lerp(v1, v2, t):
        """
        Linearly interpolate between two Vector2 instances.
        :param v1: Start vector
        :param v2: End vector
        :param t: Interpolation factor (0.0 = v1, 1.0 = v2)
        :return: Interpolated Vector2
        """
        if not (0 <= t <= 1):
            raise ValueError("Interpolation factor t must be between 0 and 1")
        return Vector2(
            v1.x + (v2.x - v1.x) * t,
            v1.y + (v2.y - v1.y) * t
        )

    def __repr__(self):
        """Return a string representation of the vector for debugging."""
        return f"Vector2(x={self.x}, y={self.y})"

    def __str__(self):
        """Return a human-readable string representation of the vector."""
        return f"<{self.x}, {self.y}>"

    def __getitem__(self, index):
        """Allow tuple-like access (e.g., vector[0] gives x)."""
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("Vector2 index out of range (0 or 1)")

    def __iter__(self):
        """Allow iteration (e.g., tuple(vector))."""
        yield self.x
        yield self.y

    def __add__(self, other):
        """Overload the + operator for vector addition."""
        if isinstance(other, Vector2):
            return Vector2(self.x + other.x, self.y + other.y)
        raise TypeError("Operand must be a Vector2 instance")

    def __sub__(self, other):
        """Overload the - operator for vector subtraction."""
        if isinstance(other, Vector2):
            return Vector2(self.x - other.x, self.y - other.y)
        raise TypeError("Operand must be a Vector2 instance")

    def __mul__(self, scalar):
        """Overload the * operator for scalar multiplication."""
        if isinstance(scalar, (int, float)):
            return Vector2(self.x * scalar, self.y * scalar)
        raise TypeError("Operand must be an int or float")

    def __rmul__(self, scalar):
        """Overload the * operator for reverse scalar multiplication (e.g., 2 * vector)."""
        return self.__mul__(scalar)

    def dot(self, other):
        """Calculate the dot product with another vector."""
        if isinstance(other, Vector2):
            return self.x * other.x + self.y * other.y
        raise TypeError("Operand must be a Vector2 instance")

    def magnitude(self):
        """Calculate the magnitude (length) of the vector."""
        return math.sqrt(self.x**2 + self.y**2)

    def normalize(self):
        """Return a new unit vector (magnitude 1) in the same direction."""
        mag = self.magnitude()
        if mag == 0:
            return Vector2(0.0, 0.0)
        return Vector2(self.x / mag, self.y / mag)