import os

pipe_path = "mypipe"

# Create a named pipe (FIFO)
if not os.path.exists(pipe_path):
    os.mkfifo(pipe_path)

# Open the pipe for writing
with open(pipe_path, "w") as pipe:
    data_to_send = "Hello, receiver!"
    pipe.write(data_to_send)

print("Data sent to receiver.")
