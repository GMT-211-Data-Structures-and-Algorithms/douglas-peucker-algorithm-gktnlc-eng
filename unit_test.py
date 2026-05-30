import unittest
from dp import *

class TestPerpendicularDistance(unittest.TestCase):

    def test_simple_distance(self):
        # a point clearly above a horizontal line should have a known distance
        d = perpendicular_distance((0, 1), (0, 0), (1, 0))
        self.assertAlmostEqual(d, 1.0)

    def test_point_on_line(self):
        # if the point is on the line the distance should be zero
        d = perpendicular_distance((1, 0), (0, 0), (2, 0))
        self.assertAlmostEqual(d, 0.0)

    def test_same_start_end(self):
        # if start and end are the same we fall back to direct distance
        d = perpendicular_distance((3, 4), (0, 0), (0, 0))
        self.assertAlmostEqual(d, 5.0)


class TestDouglasPeucker(unittest.TestCase):

    def test_returns_endpoints(self):
        # no matter what, first and last point should always be kept
        points = [(0, 0), (1, 0.1), (2, 0)]
        result = douglas_peucker(points, 1.0)
        self.assertEqual(result[0], (0, 0))
        self.assertEqual(result[-1], (2, 0))

    def test_small_epsilon_keeps_more_points(self):
        # with a very small epsilon almost all points should be kept
        points = [(0, 0), (1, 1), (2, 0), (3, 1), (4, 0)]
        result_small = douglas_peucker(points, 0.01)
        result_large = douglas_peucker(points, 10.0)
        self.assertGreaterEqual(len(result_small), len(result_large))

    def test_two_points_returned_as_is(self):
        # if we only have two points there is nothing to simplify
        points = [(0, 0), (1, 1)]
        result = douglas_peucker(points, 0.5)
        self.assertEqual(result, [(0, 0), (1, 1)])

    def test_collinear_points_removed(self):
        # points sitting exactly on the line should all be removed
        points = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)]
        result = douglas_peucker(points, 0.1)
        self.assertEqual(result, [(0, 0), (4, 0)])


class TestConvertCoordinatesToLine(unittest.TestCase):

    def test_reads_correctly(self):
        # checking that the file is read and parsed into correct tuples
        result = convert_coordinates_to_line("line.txt")
        self.assertIsInstance(result, list)
        self.assertTrue(all(isinstance(p, tuple) for p in result))

    def test_first_point(self):
        # first point in line.txt should be (1.0, 2.0)
        result = convert_coordinates_to_line("line.txt")
        self.assertEqual(result[0], (1.0, 2.0))


if __name__ == '__main__':
    unittest.main()