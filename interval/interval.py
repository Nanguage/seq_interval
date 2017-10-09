class Interval:
    """
    The abstraction of interval with direction.
    
    example interval:
        
        |------------>        direction: +
        start        end
    
        <------------|        direction: -
        end          start

    >>> Interval(1, 10)
    Interval: 1 |-----> 10

    >>> Interval(10, 1)
    Interval: 1 <-----| 10
    
    """
    def __init__(self, start, end):
        """
        :start: interval start position
        :end: interval end position
        """
        self.start = start
        self.end = end 
        dire = '+' if start <= end else '-' 
        self.direction = dire
        if dire == '+':
            assert start <= end 
            self._s = start
            self._e = end
        elif dire == '-':
            assert start >= end 
            self._s = end
            self._e = start

    def __len__(self):
        return abs(self.end - self.start) + 1

    def __repr__(self):
        if self.direction == "+":
            s = "Interval: {} |-----> {}".format(self.start, self.end)
        else:
            s = "Interval: {} <-----| {}".format(self.end, self.start)
        return s

    def __str__(self):
        if self.direction == "+":
            s = "{} |-----> {}".format(self.start, self.end)
        else:
            s = "{} <-----| {}".format(self.end, self.start)
        return s

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end

    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        """
        self is completely greater than other
        e.g.
            
                             s1         e1
        self                 |---------->
        other  |----------> 
               s2        e2

        """
        s1, e1 = self._s, self._e
        s2, e2 = other._s, other._e
        if s1 > e2:
            return True
        else:
            return False

    def __ge__(self, other):
        """
        self is greater(not completely) than other
        e.g.
            
                      s1         e1
        self          |---------->
        other  |----------> 
               s2        e2

        """
        s1, e1 = self._s, self._e
        s2, e2 = other._s, other._e
        if s1 >= s2:
            return True
        else:
            return False

    def __lt__(self, other):
        s1, e1 = self._s, self._e
        s2, e2 = other._s, other._e
        if e1 < s2:
            return True
        else:
            return False

    def __le__(self, other):
        s1, e1 = self._s, self._e
        s2, e2 = other._s, other._e
        if e1 <= e2:
            return True
        else:
            return False

    def __add__(self, other):
        """
        join two Interval, two Interval must in same direction
        e.g.

            |----------->
         +      |------------> 
         --------------------------
         =  |---------------->

        """
        assert isinstance(other, Interval)
        assert self.direction == other.direction
        assert (self.is_intersect_with(other) or
                self.is_adjacent_with(other))
        dire = self.direction
        if dire == '+':
            new_start = min(self.start, other.start)
            new_end = max(self.end, other.end)
        elif dire == '-':
            new_start = max(self.start, other.start)
            new_end = min(self.end, other.end)
        return Interval(new_start, new_end)

    def __sub__(self, other):
        """
        get the difference of self and other, two Interval must in same direction
        e.g.

            |----------->
         -      |------------> 
         --------------------------
         =  |-->

        """
        assert isinstance(other, Interval)
        if not self.direction == other.direction:
            raise ValueError("Two Interval must in same direction")
        if not self.is_intersect_with(other):
            raise ValueError("Two Interval must have intersection")
        assert not (
                ((self._s > other._s) and (self._e < other._e))
                or
                ((other._s > self._s) and (other._e < self._e))
            )

        dire = self.direction
        if self == other:
            return None
        else:
            if dire == '+':
                if self >= other:
                    """
                    self        |-------->
                    other   |------->
                    res              |--->
                    """
                    return Interval(other.end + 1, self.end)
                elif other >= self:
                    """
                    self    |-------->
                    other       |------->
                    res     |-->
                    """
                    return Interval(self.start, other.start - 1)
            if dire == '-':
                if self >= other:
                    """
                    self        <--------|
                    other   <-------|
                    res              <---|
                    """
                    return Interval(self.start, other.start - 1)
                elif other >= self:
                    """
                    self    <--------|
                    other       <-------|
                    res     <--|
                    """
                    return Interval(other.end + 1, self.end)

    def __and__(self, other):
        """
        get the intersction of self and other
        e.g.
        
            |----------->
         &      |------------> 
         --------------------------
         =      |------->

        """
        if not self.is_intersect_with(other):
            return None

        if self.is_in(other):
            return self
        elif other.is_in(self):
            return other
        else:
            return self - (self - other)

    def __contains__(self, other):
        """
        reload `in` operator.
        judge other(int/float or Interval) is within self or not.
        e.g.
        >>> i1 = Interval(1, 10)

        >>> i2 = Interval(5, 8)

        >>> i2 in i1
        True

        >>> 5 in i1
        True

        >>> 11 in i1
        False
        """
        if type(other) is int or type(other) is float:
            return (other >= self._s and other <= self._e)
        elif isinstance(other, Interval):
            return other.is_in(self)
        else:
            raise TypeError("must be numeric type(int/float) or Interval")

    def reverse(self):
        """
        reverse the direction.
        """
        if self.direction == '+':
            self.direction = '-'
        else:
            self.direction = '+'
        self.start, self.end = self.end, self.start

    def is_intersect_with(self, other):
        """
        means two Interval has intersection
        like:

             s1         e1
        a    |---------->
        b      <-----------|
               s2          e2

        >>> a.is_intersect_with(b) 
        True

        """
        if self > other or self < other:
            return False
        else:
            return True

    def is_adjacent_with(self, other):
        """
        means two is adjacent
        like:

             s1         e1
        a    |---------->
        b                <-----------|
                         s2          e2

        >>> a.is_adjacent_with(b)
        True
            
        """
        s1, e1 = self._s, self._e
        s2, e2 = other._s, other._e
        if (e1 + 1 == s2) or (e2 + 1 == s1):
            return True
        else:
            return False

    def is_in(self, other):
        """
        means self is within other
        like:

                  s1         e1
        a         |---------->
        b    <-------------------|
             s2                  e2

        >>> a.is_in(b)
        True

        """
        s1, e1 = self._s, self._e
        s2, e2 = other._s, other._e
        if s1 >= s2 and e1 <= e2:
            return True
        else:
            return False

