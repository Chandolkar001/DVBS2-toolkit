import os

pipe_path = "mypipe"

# Open the named pipe for reading
with open(pipe_path, "r") as pipe:
    data_received = pipe.read()

print(f"Received data: {data_received}")
