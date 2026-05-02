import unittest
from crop_analysis.analyzer import CropAnalyzer, CropRecord


class CropAnalyzerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.records = [
            CropRecord("Wheat", "North", "Winter", 100, 300, 600),
            CropRecord("Rice", "East", "Monsoon", 50, 250, 900),
            CropRecord("Wheat", "South", "Winter", 80, 200, 700),
        ]

    def test_overall_average_yield(self) -> None:
        analyzer = CropAnalyzer(self.records)
        self.assertAlmostEqual(analyzer.overall_average_yield(), 3.5, places=5)

    def test_best_crop(self) -> None:
        analyzer = CropAnalyzer(self.records)
        crop, value = analyzer.best_crop()
        self.assertEqual(crop, "Rice")
        self.assertAlmostEqual(value, 5.0)


if __name__ == "__main__":
    unittest.main()
