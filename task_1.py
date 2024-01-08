import random
import time

from queue import Queue

queue = Queue()

request_id = 1


def generate_request():
    global request_id

    request = f"Request: {request_id}"
    queue.put(request)
    request_id += 1

    print(f"{request} - added.")


def process_request():
    if queue.empty():
        print("Queue is empty.")
        return

    request = queue.get()
    print(f"{request} - processed.")


def auto_request():
    try:
        while True:
            random.choice([generate_request, process_request])()
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("\nAutomatic generation and processing of requests is stopped.")


def main():
    print(
        f"\nCommands:\nauto{' '*24}| starts automatic request generation and processing\ngenerate{' '*20}| adds a new request to the queue\nprocess{' '*21}| processes the request\nexit{' '*24}| exit the program\n"
    )

    while True:
        command = input(">>>").strip()

        if command == "exit":
            break
        elif command == "auto":
            auto_request()
        elif command == "generate":
            generate_request()
        elif command == "process":
            process_request()
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
