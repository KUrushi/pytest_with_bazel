import sys
import unittest


def test_passing():
    assert (1, 2, 3) == (1, 2, 3)


if __name__ == "__main__":
    unittest.main()
    # sys.exit(pytest.main([__file__]))
