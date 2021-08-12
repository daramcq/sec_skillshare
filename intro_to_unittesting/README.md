# Introduction to Unit Testing
Unit Testing is a standard practice in software engineering. It helps in both writing new code (by specifying behaviour in advance) and in protecting code from breaking changes.

## Test Driven Development
Test Driven Development is a concept from 'eXtreme Programming' (XP), which is not as much fun as it sounds. The focus here is on writing tests 'up-front', i.e. before writing the code, and then incrementally writing code to make the tests pass.

## Using UnitTest
There are several different libraries (`nose`, `pytest`, etc.) for testing Python, but the inbuilt library, `unittest` has enough functionality for smaller projects. The basic concepts are:
- Write your test suite in a class or classes inheriting from `unitest.TestCase`.
- Write individual tests as methods prefixed with `test_` in that class or classes.
- Define _assertions_ in your individual tests using `self.assertEqual` (or other assert statements).
- Run your tests using a method call to `unittest.main()`.
You can see an example of these in `basic.py`.

## Testing simple behaviour
The most simple test is that where we:
- Define a method that takes certain arguments, performs an operation and performs a result.
- The method should be stateless - it only deals with the parameters passed to it and does not have any other state.
- Write a test that confirms that for certain known inputs, the outputs will be as expected.
In the most basic example, we can say that the behaviour of the 'method under test' is isolated - i.e. it does not use or modify any state, and it does not make method calls to other modules.

## Using mocks to test more complex behaviour
Most of the code we write will be more complicated than this. We may keep state in a database, we may require data from HTTP API calls, we may request data from other classes/functions in our application. In order to handle this complexity, we try to reduce the scope of our tests by creating convenience objects to replace the reliance on other parts of our program. This is known as 'mocking'. Common patterns include writing mocks to supply our 'methods-under-test' with test data (i.e. mocks to provide inputs), and writing mocks to confirm that our 'methods-under-test' perform as expected (i.e. mocks to test outputs).

There are some examples of both of these cases in `mockery.py`.

## Mock external HTTP Calls
