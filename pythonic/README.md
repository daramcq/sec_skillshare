# What is Pythonic?
'Pythonic' is a term used to describe code that _looks_ like Python as well as being written in Python. I think about it as _idiomatic_ Python. You can learn a foreign language, and still not sound like a native speaker. In a natural language there are many ways to convey meaning, but a smaller amount that are actually used by native speakers. The same applies for programming languages. We will look at this through _The Zen of Python_ ([link](https://www.python.org/dev/peps/pep-0020/)), which outlined some of the principles of Pythonic code.

## _Beautiful is better than ugly_
Beauty is as fraught a concept as one can imagine, but I will quickly look at iteration in Python and talk about some ways to make it Pythonic.

### The basics
The basics of Python iteration is the humble for loop:
```python
numbers = [1, 2, 3]
for x in numbers:
    print(x)
```
Obviously this differs from a language with C-style iteration, like Javascript:
```javascript
numbers = [1, 2, 3];
for (var i = 0; i < numbers.length; i++) {
  console.log(i);
}
```
### Comprehension
However, more Pythonic again is list comprehension. This is a particularly popular style, that is a little confusing when first encountered. We could rewrite the above in this way:
```python
[print(x) for x in [1, 2, 3]]
```
We can also use this style for creating a new dictionary.
```python
squares = [x * x for x in [1, 2, 3]]
```
We can also do something similar when iterating through the elements of a dictionary.
```python
d = { 'a': 1, 'b': 2, 'c': 3 }
squares = { key: value * value for key, value in d.items() }
# squares => {'a': 1, 'b': 4, 'c': 9}
```
### Why is this better?
The above are types of _syntactic sugar_, syntax that makes it easy to express an operation. They need to be learnt, but they can tidy up code significantly. For instance, if we wanted to do the dictionary comprehension in a standard `for` loop, it would look like this:
```python
d = { 'a': 1, 'b': 2, 'c': 3 }
squares = {}
for key, value in d.items()
    squares[key] = value * value
```

## _Explicit is better than implicit_
Anyone who has coded with Ruby will know all about implicit behaviour. This is evident where your objects have methods and behaviours that are defined in some mysterious place in your codebase (or a dependency). Python, in contrast, requires, or at least promotes, explicit behaviours. For instance, imports are clearly stated:
```python
from module import method
# Or
import module.method
# Discouraged
from module import *
```
You can be implicit with Python, but it's best practice to make things clear.

## _Errors should never pass silently_
One difference in Python style to Ruby style is the level of tolerance for `nil`, or `None`. Typically, Ruby will avoid throwing errors if possible, and will return `nil` instead. We can see this in some Rails behaviour.
```rb
> Zendesk::Project.find_by(name: 'foo')
=> nil
```
Generally the impact is that you add 'guard clauses' to your code. For e.g.
```rb
names = ['foo', 'boo', 'sue']
names.each do |nm|
   person = Person.find_by(name: nm)
   next if person.nil?
   
   person.update(money: 5000)
end
```
That `next if` statement is a guard clause. If we were writing this in Python (using Django as an example), the code would look more like this:
```python
names = ['foo', 'boo', 'sue']
for nm in names:
    try:
        person = Person.get(name=nm)
        person.update(money: 5000)
    except Person.DoesNotExist:
        pass
```
    
    
