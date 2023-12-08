import time
import json

class Logging:
    def __init__(self):
        self.logs = []

    def logger(self, func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()

            log = {
                'timestamp': start_time,
                'function_name': func.__name__,
                'args': args,
                'kwargs': kwargs,
                'result': result,
                'execution_time': end_time - start_time,
            }
            self.logs.append(log)
            return result

        return wrapper

    def get_logs(self):
        for log in self.logs:
            yield log

    def save_logs(self, filename):
        with open(filename, 'w') as file:
            for log in self.logs:
                file.write(json.dumps(log) + '\n')
            self.logs = []

logging = Logging()

@logging.logger
def multiply(a, b):
    return a * b

multiply(3, 4)
multiply(5, 6)

log = logging.get_logs()

print(next(log))  # Поверне інформацію про виклик `multiply(3, 4)`
print(next(log))  # Поверне інформацію про виклик `multiply(5, 6)`

