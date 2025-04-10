def getPropertyString(filename='db.properties'):
    props = {}
    try:
        with open(filename, 'r') as f:
            for line in f:
                if line.strip() and not line.startswith('#'):  # Skip comments and empty lines
                    key, value = line.strip().split('=', 1)
                    props[key] = value
    except FileNotFoundError:
        print("❌ Properties file not found.")
    except Exception as e:
        print(f"Error reading properties file: {e}")
    return props
