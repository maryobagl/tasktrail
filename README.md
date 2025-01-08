# TaskTrail

TaskTrail is a Python program designed for Windows that monitors active processes and provides recommendations for optimizing task management. This utility aims to help users identify processes that consume significant CPU or memory resources, enabling them to make informed decisions about closing or optimizing these processes.

## Features

- Monitors CPU and memory usage of active processes.
- Provides recommendations for processes with high resource usage.
- Updates process information every 5 seconds.

## Installation

1. Ensure that you have Python installed on your system. You can download it from [python.org](https://www.python.org/).
2. Install the `psutil` library, which is required for accessing process information. You can install it using pip:

   ```
   pip install psutil
   ```

## Usage

Clone this repository or download the `task_trail.py` file. Run the script using Python:

```bash
python task_trail.py
```

The program will start monitoring the active processes and displaying their CPU and memory usage. It will also recommend actions for processes using more than 50% of CPU or memory.

Press `Ctrl+C` to exit the program.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to submit issues or pull requests if you would like to contribute to this project.

## Disclaimer

TaskTrail is provided "as is" without any warranty. The authors are not responsible for any damage or data loss caused by using this software.