# Functions to use `in` between two dictionaries or two lists/tuples in Python
### Some functions I made to use the `in` operator in Python between two lists/tuples or two dictionaries.

This repository has four functions I created:
* `inD(x,y,mode='single')`
* `inL(x,y,mode='single')`
* `allT(D)`
* `allF(D)`

The function `inD(x,y,mode='single')` will take two dictionaries, `x` and `y`, and check to see if every key in `x` also appears as a key in `y`. If every key from `x` *does* appear as a key in `y`, then `inD(x,y,mode='single')` will output `True`. If not, then `inD(x,y,mode='single')` will output `False`. If the argument `mode` is set to `'multiple'`, then `inD(x,y,mode='multiple')` will output a dictionary with the same keys as `x` and either `True` or `False` as the value for each key in `x` depending on whether or not that key also appeared as a key in `y`.

The function `inL(x,y,mode='single')` is the same as the function `inD()` but for lists and tuples instead of dictionaries. Specifying `mode='single'` will output `True` if every item in `x` also appears in `y`. Specifying `mode='multiple'` will output a dictionary whose keys are the values in `x` and whose values are either `True` or `False` depending on whether or not that value of `x` also appeared in `y`.

I also made two other functions, `allT(D)` and `allF(D)`, which take a dictionary as their argument and check to see if every value in that dictionary is `True` or `False`. `allT(D)` checks to see if every value in `D` is `True` and outputs `True` if so and `False` otherwise. `allF(D)` checks to see if every value in `D` is `False` and outputs `True` if so and `False` otherwise. You can also use `if allF(D): d=False` to take a dictionary of all `False` logical values and make a single boolean object that is `False`; I'm not immediately sure why this would be useful, but I'm sure someone can find a use for this.
