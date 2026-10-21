import pandas as pd
from pathlib import Path

input_file = Path("train.csv")
output_file = Path("train_sample.csv")

print("Reading train.csv in chunks... (this can take a few minutes)", flush=True)

cols = ["ip", "app", "device", "os", "channel", "click_time", "is_attributed"]

parts = []
total_rows = 0

for i, chunk in enumerate(pd.read_csv(input_file, usecols=cols, chunksize=1_000_000)):
    total_rows += len(chunk)
    parts.append(chunk.sample(frac=0.005, random_state=42))
    print(f"Chunk {i + 1} done", flush=True)

sample = pd.concat(parts, ignore_index=True)
sample = sample.sort_values("click_time").reset_index(drop=True)

sample.to_csv(output_file, index=False)

print("\nRESULTS")
print("-" * 40)
print("Total rows in train.csv:", total_rows)
print("Rows in sample:", len(sample))
print("Downloads (is_attributed = 1):", int(sample["is_attributed"].sum()))
print("First click:", sample["click_time"].iloc[0])
print("Last click:", sample["click_time"].iloc[-1])
print("Saved file:", output_file.resolve())
print("Size (MB):", round(output_file.stat().st_size / (1024 ** 2), 2))