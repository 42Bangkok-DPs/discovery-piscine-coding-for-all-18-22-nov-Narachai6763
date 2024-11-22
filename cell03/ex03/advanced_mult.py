
import sys


if len(sys.argv) > 1:
    if sys.argv[1] != "yolo":
        sys.exit(1)  
    else:
        print("none$")
        sys.exit(0)


for i in range(11):
    table = [str(i * j) for j in range(11)]
    print(f"Table de {i}: {' '.join(table)}")
