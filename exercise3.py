import glob
import os
import heapq
import tempfile
import pandas as pd
from utils import timer
from multiprocessing import Pool


class MultiProcessDFExternalSorting:
    def __init__(self, no_processes, filename, buffer_size_):
        self.tempdir = tempfile.mkdtemp()
        self.no_processes = no_processes
        self.buffer_size_ = buffer_size_
        self.filename = filename

    def chunk_generator(self):
        reader = pd.read_csv(self.filename, chunksize=self.buffer_size_)
        for i, df in enumerate(reader):
            yield i, df

    def sort_chunks(self):
        pool = Pool(processes=self.no_processes)
        res = [_ for _ in pool.imap(self.sort_and_save, self.chunk_generator())]
        print(res)

    def sort_and_save(self, chunk_generator):
        i, df = chunk_generator
        # df = pd.read_csv(os.path.join(self.tempdir, f'sorted_{i}.csv'))
        df.sort_values('data', inplace=True)
        df.to_csv(os.path.join(self.tempdir, f'sorted_{i}.csv'), header=False, index=False)

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
    def external_sort(self, output_file):
        self.sort_chunks()
        self.sort_by_min_heap(output_file)


if __name__ == '__main__':
    sol = MultiProcessDFExternalSorting(no_processes=10, filename='sample.csv', buffer_size_=2000)
    with open('sorting-step3_process_time.txt', 'w') as f:
        timer = sol.external_sort(output_file='sorting-step3.csv')
        f.write(str(timer))
