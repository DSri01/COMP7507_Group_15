import csv
import json
import os

datasets = [
    'combinedRainfall',
      'combinedParticles',
      'combinedTemperature',
      'combinedWindspeed'
      ]
for d in datasets:
    REL_JSONL_FILE_PATH = ["dataset", f"{d}.jsonl"]
    REL_CSV_FILE_PATH = ["dataset", f"{d}.csv"]

    absJSONLFilePath = os.path.join(os.getcwd(), *REL_JSONL_FILE_PATH)
    absCSVFilePath = os.path.join(os.getcwd(), *REL_CSV_FILE_PATH)

    with open(absJSONLFilePath, mode="r") as inputFile:
        with open(absCSVFilePath, mode="w", newline='') as outputFile:
            lines = inputFile.readlines()
            firstRow = json.loads(lines[0].strip())

            fieldNames = [field for field in firstRow]
            writer = csv.DictWriter(outputFile, fieldnames=fieldNames)
            writer.writeheader()
            for line in lines:
                try:
                    rowDict = json.loads(line.strip())
                    writer.writerow(rowDict)
                except Exception as e:
                    print(f"Warning: .jsonl to .csv Conversion Failure ({e})")
            outputFile.close()
        inputFile.close()

# REL_JSONL_FILE_PATH = ["dataset", "combinedRainfall.jsonl"]
# REL_CSV_FILE_PATH = ["dataset", "combinedRainfall.csv"]

# absJSONLFilePath = os.path.join(os.getcwd(), *REL_JSONL_FILE_PATH)
# absCSVFilePath = os.path.join(os.getcwd(), *REL_CSV_FILE_PATH)

# with open(absJSONLFilePath, mode="r") as inputFile:
#     with open(absCSVFilePath, mode="w", newline='') as outputFile:
#         lines = inputFile.readlines()
#         firstRow = json.loads(lines[0].strip())

#         fieldNames = [field for field in firstRow]
#         writer = csv.DictWriter(outputFile, fieldnames=fieldNames)
#         writer.writeheader()
#         for line in lines:
#             try:
#                 rowDict = json.loads(line.strip())
#                 writer.writerow(rowDict)
#             except Exception as e:
#                 print(f"Warning: .jsonl to .csv Conversion Failure ({e})")
#         outputFile.close()
#     inputFile.close()

print("done")
