import glob
import os
import heapq
import tempfile
import pandas as pd
from utils import timer


class DFExternalSorting:
    def __init__(self):
        self.tempdir = tempfile.mkdtemp()

    @timer
    def sort_chunks(self, file_name, buffer_size_):
        reader = pd.read_csv(file_name, chunksize=buffer_size_)
        for i, df in enumerate(reader):
            df.sort_values('data', inplace=True)
            df.to_csv(os.path.join(self.tempdir, f'sorted_{i}.csv'), header=False, index=False)

    @timer
    def sort_by_min_heap(self, output_file):
        min_heap = []
        heapq.heapify(min_heap)

        for filename in glob.glob(os.path.join(self.tempdir, '*.csv'), recursive=True):
            file_ = open(filename, encoding='utf-8')
            row = file_.readline()
            val = row.split(',')[2]
            heapq.heappush(min_heap, (val, row, file_))

        with open(output_file, 'w', encoding='utf-8') as sorted_file:
            sorted_file.write('row_num,id,data\n')
            while len(min_heap) > 0:
                min_element = heapq.heappop(min_heap)
                sorted_file.write(min_element[1])
                next_row = min_element[2].readline()
                if next_row:
                    val = next_row.split(',')[2]
                    heapq.heappush(min_heap, (val, next_row, min_element[2]))
                else:
                    min_element[2].close()

    @timer
    def external_sort(self, input_file, output_file, buffer_size_):
        self.sort_chunks(input_file, buffer_size_)
        self.sort_by_min_heap(output_file)


if __name__ == '__main__':
    sol = DFExternalSorting()
    with open('sorting-step2_process_time.txt', 'w') as f:
        timer = sol.external_sort(input_file='sample.csv', output_file='sorting-step2.csv', buffer_size_=2000)
        f.write(str(timer))
