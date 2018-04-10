Seq Interval 
=====================================================

Interval operations for sequencing data.

Project status: under development

# usage

## Interval
### Create an interval

```Python
>>> from seq_interval import Interval
>>> iv1 = Interval(1, 10)
>>> iv1
Interval: 1 |-----> 10
```

### Reverse direction

```Python
>>> iv1.reverse()
>>> iv1
Interval: 1 <-----| 10
```

### Merge two interval

```Python
>>> iv1 = Interval(1, 10)
>>> iv2 = Interval(5, 15)
>>> iv1 + iv2
Interval: 1 |-----> 15
```

### Intersection

```Python
>>> iv1.is_intersect_with(iv2)
True
>>> iv1 & iv2
Interval: 5 |-----> 10
```

### 'in' operator

```Python
>>> 5 in iv1
True
>>> 42 in iv1
False
>>> Interval(5, 7) in iv1
True
```
