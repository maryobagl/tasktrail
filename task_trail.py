import psutil
import time
import os

class TaskTrail:
    def __init__(self):
        self.process_info = {}

    def update_processes(self):
        self.process_info = {}
        for proc in psutil.process_iter(attrs=['pid', 'name', 'cpu_percent', 'memory_percent']):
            try:
                self.process_info[proc.info['pid']] = proc.info
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

    def display_processes(self):
        print(f"{'PID':<10} {'Name':<25} {'CPU%':<10} {'Memory%':<10}")
        print("-" * 55)
        for proc in self.process_info.values():
            print(f"{proc['pid']:<10} {proc['name']:<25} {proc['cpu_percent']:<10} {proc['memory_percent']:<10}")

    def recommend_action(self):
        high_cpu_procs = [proc for proc in self.process_info.values() if proc['cpu_percent'] > 50]
        high_mem_procs = [proc for proc in self.process_info.values() if proc['memory_percent'] > 50]

        if high_cpu_procs:
            print("\nHigh CPU Usage Processes:")
            for proc in high_cpu_procs:
                print(f"- {proc['name']} (PID: {proc['pid']}) is using {proc['cpu_percent']}% CPU.")
            print("Consider closing or optimizing these processes.")

        if high_mem_procs:
            print("\nHigh Memory Usage Processes:")
            for proc in high_mem_procs:
                print(f"- {proc['name']} (PID: {proc['pid']}) is using {proc['memory_percent']}% memory.")
            print("Consider closing or optimizing these processes.")

    def run(self):
        try:
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                self.update_processes()
                self.display_processes()
                self.recommend_action()
                time.sleep(5)
        except KeyboardInterrupt:
            print("\nExiting TaskTrail.")

if __name__ == "__main__":
    task_trail = TaskTrail()
    task_trail.run()