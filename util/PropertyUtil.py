import os

def getPropertyString(filename='db.properties'):
    props = {}
    try:
        # Resolve absolute path relative to the project root
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path = os.path.join(base_dir, filename)

        with open(file_path, 'r') as f:
            for line in f:
                if line.strip() and not line.startswith('#'):  # Skip comments and empty lines
                    key, value = line.strip().split('=', 1)
                    props[key] = value
    except FileNotFoundError:
        print(f" Properties file not found at {file_path}.")
    except Exception as e:
        print(f"Error reading properties file: {e}")
    return props
