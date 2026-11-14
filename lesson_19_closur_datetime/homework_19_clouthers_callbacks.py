# ==========================================
# Task 1. Voltage Converter factory
# ==========================================

def make_voltage_converter(factor: float):
    """Creates and returns a function that multiplies the input voltage by a factor."""
    def converter(voltage: float) -> float:
        return voltage * factor
    return converter

# Example usage:
step_up = make_voltage_converter(10.0)   # step-up
step_down = make_voltage_converter(0.5)    # step-down

print("--- Task 1 ---")
print(step_up(22.0))     # 220.0
print(step_down(220.0))  # 110.0
print(step_up(11.0))     # 110.0


# ==========================================
# Task 2. Electricity Meter
# ==========================================

def make_electricity_meter(address: str, initial_kwh: float = 0.0):
    """Creates an electricity meter with a closed state of consumption."""
    current_kwh = initial_kwh

    def add(kwh: float) -> float:
        nonlocal current_kwh
        current_kwh += kwh
        return current_kwh

    def reset() -> float:
        nonlocal current_kwh
        current_kwh = initial_kwh
        return current_kwh

    def report() -> str:
        return f"Address: {address} | Consumed: {current_kwh} kWh"

    return add, reset, report

# Example usage:
add, reset, report = make_electricity_meter("12 Franko St.", 150.0)

print("\n--- Task 2 ---")
print(add(30.5))    # 180.5
print(add(14.0))    # 194.5
print(report())     # Address: 12 Franko St. | Consumed: 194.5 kWh
print(reset())      # 150.0
print(report())     # Address: 12 Franko St. | Consumed: 150.0 kWh


# ==========================================
# Task 3. Emergency Event Dispatcher
# ==========================================

def make_dispatcher(station_name: str):
    """Creates a dispatcher for the substation that forwards events to a callback."""
    def dispatch(event: str, callback):
        message = f"[{station_name}] {event}"
        callback(message)
    return dispatch

def log_to_console(message: str):
    """Prints the message to the console."""
    print(message)

def log_to_file(message: str):
    """Appends the message to the dispatch_log.txt file."""
    with open("dispatch_log.txt", "a", encoding="utf-8") as f:
        f.write(message + "\n")

# Example usage:
dispatch = make_dispatcher("Substation No.7 Ivano-Frankivsk")

print("\n--- Task 3 ---")
dispatch("Overvoltage", log_to_console)
dispatch("Short circuit", log_to_console)
dispatch("Power restoration", log_to_file)
print("(Message successfully written to dispatch_log.txt)")


# ==========================================
# Task 4. Sorting substations
# ==========================================

substations = [
    {"name": "Substation No.3", "region": "Kolomyia",         "load_kw": 4500},
    {"name": "Substation No.7", "region": "Ivano-Frankivsk",  "load_kw": 8200},
    {"name": "Substation No.1", "region": "Kalush",           "load_kw": 3100},
    {"name": "Substation No.9", "region": "Nadvirna",         "load_kw": 6700},
]

def make_sorter(field: str, reverse: bool = False):
    """Creates a function that sorts a collection of dictionaries by the specified field."""
    def sorter(data: list) -> list:
        return sorted(data, key=lambda x: x[field], reverse=reverse)
    return sorter

# Example usage:
sort_by_load = make_sorter("load_kw", reverse=True)

print("\n--- Task 4 (sorting by load) ---")
for s in sort_by_load(substations):
    print(s["name"], s["load_kw"])

sort_by_name = make_sorter("name")

print("\n--- Task 4 (sorting by name) ---")
for s in sort_by_name(substations):
    print(s["name"])


# ==========================================
# Bonus. Circuit breaker
# ==========================================

def make_circuit_breaker(max_failures: int):
    """Pattern Circuit Breaker: blocks execution after reaching the error limit."""
    def protect(func):
        failure_count = 0

        def wrapper(*args, **kwargs):
            nonlocal failure_count
            if failure_count >= max_failures:
                raise RuntimeError("Breaker tripped!")
            try:
                return func(*args, **kwargs)
            except Exception as e:
                failure_count += 1
                raise e
        return wrapper
    return protect

# Example usage:
breaker = make_circuit_breaker(max_failures=2)

def unstable_sensor():
    raise ConnectionError("Sensor not responding")

safe_sensor = breaker(unstable_sensor)

print("\n--- Bonus (Circuit Breaker) ---")
for i in range(1, 5):
    try:
        safe_sensor()
    except (ConnectionError, RuntimeError) as err:
        print(f"Call {i}: {type(err).__name__}: {err}")
