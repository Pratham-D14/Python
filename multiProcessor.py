from multiprocessing import Pool
import time
from datetime import datetime

def square(n):
    time.sleep(1)
    return n * n

print(datetime.now())
if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    with Pool(processes=3) as pool:  # 3 processes
        results = pool.map(square, numbers)

    print("Squares:", results)
print(datetime.now())