# Unit tests in Ruby
This section will introduce Ruby unit testing using the very popular [Minitest](https://github.com/seattlerb/minitest) library. This is part of the standard library so it does not need to be installed separately.

## What is a unit test?
Strictly speaking, a unit test is a test written to cover a unit of code. This is not a very helpful definition, but suffice to say that unit tests aim to test individual components of code rather than large blocks. They generally prefer to _isolate_ dependencies (e.g. calls to sub-methods) through the use of mock objects and stubs. These are complex topics in their own right, so we will simply focus on basic testing here.


## How to run
You can execute the tests in `test_spec.rb` by running `ruby test_spec.rb` from the terminal. You should see output like the below:
```
> ruby testing/test_spec.rb
Run options: --seed 31107

# Running:

....

Finished in 0.000979s, 4085.8018 runs/s, 4085.8018 assertions/s.

4 runs, 4 assertions, 0 failures, 0 errors, 0 skips
```
This shows that all the test pass. You can change the expected results and re-run to see what it looks like when there is a failure.

## Structure of tests
Here we have written tests in a 'spec' syntax. This is not the only way that unit tests can be written in Minitest, but it is common. The basics are that a `describe` block will contain a number of `it` blocks, and can also contain additional `describe` blocks. A `describe` block can be used to test a method (in the example, we specify this using `#method_name`) and can also specify a context for the test (e.g. `'when the inputs do not match'`). The `it` block will refer to the expected result of the test. For instance, `it 'returns true'`.

## Expectations
Minitest tests are written in the format `expect(tested_value).must_equal(expected_value)`. The `expect` is a method that transforms the `tested_value` into an Expectation. The expectation object then has convenience methods such as `must_equal` available. The Minitest library has many similar methods available.
