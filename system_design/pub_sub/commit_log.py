import os
import struct


class CommitLog:
    def __init__(self, partition):
        self.partition = partition
        self.base_offset = 0
        self.file_name = f"partition_{partition}.log"
        self.file_size = 1024 * 1024 # 1MB
        self.segment_size = 1024 * 64 # 64KB
        self.current_offset = 0
        self.current_file = None
        self.current_segment = 0

    def append(self, value):
        if self.current_file is None or self.current_file.tell() >= self.segment_size:
            self._rotate_segment()

        offset = self.current_offset
        data = struct.pack('>QI', offset, len(value)) + value
        self.current_file.write(data)
        self.current_file.flush()
        self.current_offset += len(data)

        return offset

    def read(self, offset):
        if offset < self.base_offset:
            raise ValueError("Invalid offset")

        segment_offset = offset - self.base_offset
        print(segment_offset)
        segment_index = segment_offset // self.segment_size
        segment_file = open(self._get_segment_file(segment_index), 'rb')
        segment_file.seek(segment_offset % self.segment_size)

        value_offset, value_size = struct.unpack('>QI', segment_file.read(12))
        value = segment_file.read(value_size)

        return value, value_offset + value_size

    def _rotate_segment(self):
        if self.current_file is not None:
            self.current_file.close()

        if os.path.exists(self.file_name):
            file_size = os.path.getsize(self.file_name)
            if file_size >= self.file_size:
                self.base_offset += self.current_offset
                self.current_offset = 0
                self.current_segment += 1

        self.current_file = open(self._get_segment_file(self.current_segment), 'ab')
        self.current_segment += 1

    def _get_segment_file(self, segment_index):
        return f"{self.file_name}.{segment_index}"


if __name__ == '__main__':

    log = CommitLog(partition=0)

    # Produce some messages
    offsets = list()
    for idx in range(10000):
        offsets.append(log.append(f'Message {idx}'.encode('utf-8')))

    print(offsets)

    # Consume messages from the log
    offset = 0
    while offset < len(offsets):
        value, offset = log.read(offset)
        print(value, offset)
