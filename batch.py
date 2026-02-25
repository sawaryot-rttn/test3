import os
import time
from datetime import datetime

def main():
    print("=== ECS Batch Start ===")
    print("time:", datetime.utcnow().isoformat() + "Z")
    print("env SAMPLE_VAR:", os.getenv("SAMPLE_VAR", "not_set"))

    # 動作確認用に少し待つ
    for i in range(5):
        print(f"working... {i+1}/5")
        time.sleep(2)

    print("=== ECS Batch Done (exit 0) ===")

if __name__ == "__main__":
    main()