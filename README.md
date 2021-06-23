# ***KMerge-DataFrame***

### **Sub-tasks**
| Script | Description | 
| :---: | :---: |
| Exercise1 | Simple sort of a single DataFrame with sort_values()
| Exercise2 | External Sorting of dataframe, buffer capacity is limited for 2000 rows
| Exercise3 | External Sorting of dataframe, buffer capacity is limited for 2000 rows + multiprocess.Pool usage

### **usage**
1. install anaconda (or build a Docker image)
2. install the environment requirements.txt - with conda you can do this with one command.
3. run execise{number of task} - the output will appear in sorting-step{number of task}.csv

### Description
*Exercise1*: I used pandas for read, sort(quicksort) and write the final result. (simple one)
*Exercise2*: First, I'm reading all the data chunk by chunk, where each one has a size of 2k rows.
the next level is to sort each chunk of data, and save it to a different file with a unique id. (chunk id)
the final stage is to use a heapq, as a max heap - I'm loading each row of the minimal value of data from all the files.
and then, I'm using pop() and saves this row in the final csv, if the file is empty -> it get closed, or else the next minimal value get pushed to the max heap - repeat.
*Exercise3*: Same Idea as exercise2, but the usage of Multiprocessing.Pool - each shard of 2k dataframe rows get sorted by a worker.  
