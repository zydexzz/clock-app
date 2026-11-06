"""Консольные часы: выводит текущее время и обновляет его каждую секунду."""
import sys
import time
from datetime import datetime


def main() -> None:
    try:
        while True:
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            sys.stdout.write(f"\r{now}")
            sys.stdout.flush()
            time.sleep(1 - (time.time() % 1))  # выравнивание по границе секунды
    except KeyboardInterrupt:
        print("\nВыход.")


if __name__ == "__main__":
    main()
