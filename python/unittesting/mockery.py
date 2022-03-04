import unittest
from unittest.mock import MagicMock


def complicated_external_method():
    # Imagine that this is doing something more complicated
    return 'foo'


def result_wrapper(name):
    res = complicated_external_method()
    return { name: res }


class TestResultWrapper(unittest.TestCase):
    def test_result_wrapper(self):
        self.assertEqual({'x': 'foo'}, result_wrapper('x'))

    def test_result_wrapper_with_mocked_external_call(self):
        # Patch is a way of mocking an existing method
        # We use __main__ because that's the name of the current module
        with unittest.mock.patch('__main__.complicated_external_method', return_value='boo'):
            self.assertEqual({'y': 'boo'}, result_wrapper('y'))

    def test_result_wrapper_and_assert_external_method_called(self):
        # Here we want to confirm that the external method is called
        # with the expected arguments (i.e. none in this case)
        with unittest.mock.patch(
                '__main__.complicated_external_method',
                return_value='boo'
        ) as mocked_external_method:
            result_wrapper('z')

        mocked_external_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()
