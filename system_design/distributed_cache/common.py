### Socket related settings
SERVER_HOST = 'localhost'
BUFFER_SIZE = 1024

### Time related settings
HEART_BEAT_TIME_GAP = 60
HEART_BEAT_TIMEOUT = 150
REPORT_STATUS_TIMEOUT = 60
WARM_UP_TIME=1

### Message related settings
MESSAGE_SPLITTER = b'\n'
# Used in host:port
NODE_ID_SPLITTER = ':'
GET_MESSAGE = 'GET'
SET_MESSAGE = 'SET'


a = [1,2,3]
for idx, x in enumerate(a):
    a[idx] += 1
