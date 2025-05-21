def process_data(data):
    # Ejemplo simple de procesamiento
    return [d.upper() for d in data if isinstance(d, str)]

if __name__ == "__main__":
    sample = ["hola", "mundo", "python"]
    print(process_data(sample))
