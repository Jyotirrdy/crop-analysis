from __future__ import annotations

from dataclasses import dataclass
from statistics import mean
from typing import Iterable
import csv


@dataclass(frozen=True)
class CropRecord:
    crop: str
    region: str
    season: str
    area_hectares: float
    production_tons: float
    rainfall_mm: float

    @property
    def yield_tph(self) -> float:
        if self.area_hectares <= 0:
            return 0.0
        return self.production_tons / self.area_hectares


class CropAnalyzer:
    def __init__(self, records: Iterable[CropRecord]) -> None:
        self.records = list(records)

    @classmethod
    def from_csv(cls, file_path: str) -> "CropAnalyzer":
        rows: list[CropRecord] = []
        with open(file_path, newline="", encoding="utf-8") as fh:
            reader = csv.DictReader(fh)
            for row in reader:
                rows.append(
                    CropRecord(
                        crop=row["crop"].strip(),
                        region=row["region"].strip(),
                        season=row["season"].strip(),
                        area_hectares=float(row["area_hectares"]),
                        production_tons=float(row["production_tons"]),
                        rainfall_mm=float(row["rainfall_mm"]),
                    )
                )
        return cls(rows)

    def overall_average_yield(self) -> float:
        if not self.records:
            return 0.0
        return mean(r.yield_tph for r in self.records)

    def average_yield_by_crop(self) -> dict[str, float]:
        grouped: dict[str, list[float]] = {}
        for record in self.records:
            grouped.setdefault(record.crop, []).append(record.yield_tph)
        return {crop: mean(values) for crop, values in grouped.items()}

    def best_crop(self) -> tuple[str, float] | None:
        by_crop = self.average_yield_by_crop()
        if not by_crop:
            return None
        crop = max(by_crop, key=by_crop.get)
        return crop, by_crop[crop]

    def rainfall_to_yield_correlation_hint(self) -> str:
        """A lightweight trend hint without external dependencies."""
        if len(self.records) < 3:
            return "Not enough data to estimate rainfall trend."

        low_rain = [r.yield_tph for r in self.records if r.rainfall_mm < 700]
        high_rain = [r.yield_tph for r in self.records if r.rainfall_mm >= 700]

        if not low_rain or not high_rain:
            return "Rainfall range is too narrow for trend detection."

        low_avg = mean(low_rain)
        high_avg = mean(high_rain)

        if high_avg > low_avg:
            return "Higher rainfall is associated with higher yield in this dataset."
        if high_avg < low_avg:
            return "Higher rainfall is associated with lower yield in this dataset."
        return "Rainfall does not show a clear relationship with yield in this dataset."
