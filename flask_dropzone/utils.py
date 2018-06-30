import os
import uuid


#: generate a random filename, replacement for werkzeug.secure_filename
def random_filename(old_filename):
    ext = os.path.splitext(old_filename)[1]
    new_filename = uuid.uuid4().hex + ext
    return new_filename
