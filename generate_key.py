from secrets import token_bytes


class salt():
    
    def __init__(self) :
        key = token_bytes(16)

        with open('key.bin','wb') as f:
            f.write(key)