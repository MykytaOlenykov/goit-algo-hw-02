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


def main():
    print(
        f"\nCommands:\ngenerate{' '*20}| adds a new request to the queue\nprocess{' '*21}| processes the request\nexit{' '*24}| exit the program\n"
    )

    while True:
        command = input(">>>").strip()

        if command == "exit":
            break
        elif command == "generate":
            generate_request()
        elif command == "process":
            process_request()
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
