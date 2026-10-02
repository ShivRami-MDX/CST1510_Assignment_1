"""
Name  : Shiv Hiendrakumar Rami
MISIS : M01141944
Lane  : AI
Date  : 02/10/2026
"""

dataset_name = input("Dataset name: ")
rows_loaded = float(input("No. of Rows Loaded: "))
rows_expacted = float(input("No. of Rows Expacted: "))

difference = rows_expacted - rows_loaded
percent = (rows_loaded / rows_expacted)* 100

if percent >= 100:
    status = "OVER LIMIT"
elif percent >= 90:
    status = "WARNING"
else:
    status = "OK"

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {dataset_name}")
print("=" * 34)
print(f"Rows Loaded : {rows_loaded}")
print(f"Rows Expacted : {rows_expacted}")
print(f"Difference : {difference}")
print(f"percent : {percent:10.2f}%")
print(f"Status : {status}")
print("=" * 34)
