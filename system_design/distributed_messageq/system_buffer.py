import mmap

# Open the system buffer file in read-only mode
with open('/dev/shm/my_queue_buffer', 'r') as f:
    # Memory-map the file
    with mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ) as mm:
        # Read the first message from the buffer
        msg_size = int.from_bytes(mm[:4], byteorder='big')
        msg_data = mm[4:4 + msg_size]

        # Process the message
        process_message(msg_data)

        # Continue reading messages from the buffer
        while True:
            # Wait for new data to be available in the buffer
            mm.seek(0)
            mm.read(1)
            mm.seek(0)

            # Read the next message from the buffer
            msg_size = int.from_bytes(mm[:4], byteorder='big')
            msg_data = mm[4:4 + msg_size]

            # Process the message
            process_message(msg_data)