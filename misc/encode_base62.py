import hashlib
import string

BASE62 = string.digits + string.ascii_letters

def to_base62(num):
    if num == 0:
        return BASE62[0]
    
    base62 = []
    while num:
        num, rem = divmod(num, 62)
        base62.append(BASE62[rem])
    
    return ''.join(reversed(base62))

def hash_and_encode_to_base62(number):
    # Convert the number to a string and then to bytes
    number_bytes = str(number).encode('utf-8')
    
    # Create an MD5 hash of the number
    md5_hash = hashlib.md5(number_bytes).hexdigest()

    # Convert the MD5 hash (hex string) to an integer
    md5_int = int(md5_hash[:12], 16)
    
    # Encode the integer to a Base62 string
    base62_encoded = to_base62(md5_int)
    
    return base62_encoded

# Example usage
number = 123456
encoded = hash_and_encode_to_base62(number)
print(f"The Base62 encoded string for the MD5 hash of {number} is {encoded}")
