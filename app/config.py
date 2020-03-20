from os import environ
import multiprocessing

PORT = int(environ.get("PORT", 8080))
DEBUG_MODE = int(environ.get("DEBUG_MODE", 1))

bind = ":" + str(PORT)
workers = multiprocessing.cpu_count() * 2 + 1
threads = multiprocessing.cpu_count() * 2
