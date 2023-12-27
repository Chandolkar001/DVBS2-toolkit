import os

named_pipe_path = "frame_stream"

with open(named_pipe_path, "r") as named_pipe:
    while True:
        data = named_pipe.readline()
        if not data:
            break
        print(f"Received data: {data.strip()}")
