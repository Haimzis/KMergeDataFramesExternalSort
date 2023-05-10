# ***KMerge-DataFrame***

### **Sub-tasks**
| Script | Description | 
| :---: | :---: |
| Exercise1 | Simple sort of a single DataFrame with sort_values()
| Exercise2 | External Sorting of dataframe, buffer capacity is limited for 2000 rows
| Exercise3 | External Sorting of dataframe, buffer capacity is limited for 2000 rows + multiprocess.Pool usage

## Installation
To get started, you have two options:

### Option 1: Anaconda Installation
1. Install Anaconda from the official website: [Anaconda](https://www.anaconda.com/products/individual)
2. Once Anaconda is installed, open a terminal or command prompt.
3. Navigate to the project directory.
4. Create a new conda environment using the provided `requirements.txt` file:
   ```shell
   conda create --name myenv --file requirements.txt
   ```
5. Activate the newly created environment:
   ```shell
   conda activate myenv
   ```

### Option 2: Docker Installation
1. Build a Docker image using the provided Dockerfile:
   ```shell
   docker build -t myimage .
   ```
2. Run a Docker container based on the image:
   ```shell
   docker run -it myimage
   ```
3. The container will start with the required environment.

## Usage
Follow the steps below to run each exercise:

### Exercise 1
1. Run the command below to execute Exercise 1:
   ```shell
   python execise1.py
   ```
2. The output will be saved in `sorting-step1.csv`.

### Exercise 2
1. Run the command below to execute Exercise 2:
   ```shell
   python execise2.py
   ```
2. The output will be saved in `sorting-step2.csv`.

### Exercise 3
1. Run the command below to execute Exercise 3:
   ```shell
   python execise3.py
   ```
2. The output will be saved in `sorting-step3.csv`.

## Description
### Exercise 1
In Exercise 1, we utilize the pandas library to read, sort (using quicksort), and write the final result. This exercise is a simple one.

### Exercise 2
Exercise 2 involves reading the data in chunks, with each chunk containing 2k rows. The data chunks are sorted and saved to different files with unique IDs (chunk IDs). The final stage utilizes a heapq as a max heap. Each row with the minimum value from all the files is loaded and saved to the final CSV file using the `pop()` function. If a file is empty, it is closed. Otherwise, the next minimal value is pushed to the max heap, and the process is repeated.

### Exercise 3
Exercise 3 follows a similar approach to Exercise 2. However, it introduces the usage of `Multiprocessing.Pool`, where each shard of the 2k dataframe rows is sorted by a worker.

Please refer to the source code files for more detailed information and implementation.

