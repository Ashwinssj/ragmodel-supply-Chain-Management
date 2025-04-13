import subprocess
import json



def query_ollama(prompt):
    command = ["ollama", "run", "tinyllama", prompt]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout.strip()
