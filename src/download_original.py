"""Tải bộ dữ liệu gốc 20.000 dòng và lưu thành data/original.csv (notebook cần file này)."""
import os
import shutil
from pathlib import Path

import kagglehub

ROOT = Path(__file__).resolve().parent
env = ROOT / ".env"
if env.exists():  # nạp thông tin đăng nhập Kaggle từ .env (không in ra màn hình)
    for line in env.read_text(encoding="utf-8").splitlines():
        if "=" in line and not line.lstrip().startswith("#"):
            k, v = line.split("=", 1)
            os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))

src = Path(kagglehub.dataset_download("uditjain13/credit-card-fraud-detection-2026"))
csvs = sorted(src.rglob("*.csv"))
print("Các file CSV tìm thấy:", [str(p) for p in csvs])
if len(csvs) != 1:
    raise SystemExit("Có nhiều hoặc không có file CSV, hãy chọn file đúng rồi copy thành data/original.csv")
(ROOT / "data").mkdir(exist_ok=True)
shutil.copy(csvs[0], ROOT / "data" / "original.csv")
print("Đã lưu:", ROOT / "data" / "original.csv")
