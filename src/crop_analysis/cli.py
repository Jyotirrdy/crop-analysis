import argparse
from crop_analysis.analyzer import CropAnalyzer


def main() -> None:
    parser = argparse.ArgumentParser(description="Analyze crop dataset from CSV")
    parser.add_argument("csv", help="Path to crop CSV data")
    args = parser.parse_args()

    analyzer = CropAnalyzer.from_csv(args.csv)

    print("Crop Analysis Report")
    print("=" * 24)
    print(f"Total records: {len(analyzer.records)}")
    print(f"Overall average yield (tons/hectare): {analyzer.overall_average_yield():.2f}")
    print("\nAverage yield by crop:")
    for crop, yield_value in sorted(analyzer.average_yield_by_crop().items()):
        print(f"- {crop}: {yield_value:.2f}")

    best = analyzer.best_crop()
    if best:
        print(f"\nBest performing crop: {best[0]} ({best[1]:.2f} tons/hectare)")

    print("\nRainfall trend hint:")
    print(analyzer.rainfall_to_yield_correlation_hint())


if __name__ == "__main__":
    main()
