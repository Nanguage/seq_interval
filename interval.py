"""
The abstraction of interval with direction.

example interval:
    
    |------------>        direction: +
    start        end

    <------------|        direction: -
    end          start

"""

class Interval:
    def __init__(self, start, end):
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
        return abs(self.end - self.start)

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
        assert type(other) is Interval
        assert self.direction == other.direction
        assert self.is_intersect_with(other)
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
        assert type(other) is Interval
        assert self.direction == other.direction
        assert self.is_intersect_with(other)
        dire = self.direction
        if self == other:
            return None
        else:
            return 

    def __and__(self, other):
        """
        get the intersction of self and other
        e.g.
        
            |----------->
         &      |------------> 
         --------------------------
         =      |------->

        """
        return self - (self - other)

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

        a.is_intersect_with(b) == True

        """
        if self > other or self < other:
            return False
        else:
            return True

    def is_in(self, other):
        """
        means self is within other
        like:

                  s1         e1
        a         |---------->
        b    <-------------------|
             s2                  e2

        a.is_in(b) == True

        """
        s1, e1 = self._s, self._e
        s2, e2 = other._s, other._e
        if s1 >= s1 and e1 <= e2:
            return True
        else:
            return False

