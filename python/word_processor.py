import os
import multiprocessing


def count_words(file_path):
    # get file size in bytes
    file_size = os.path.getsize(file_path)
    # get number of CPU cores
    num_cores = multiprocessing.cpu_count()
    # calculate optimal number of partitions based on file size and CPU cores
    partition_size = int(file_size / (num_cores * 2))
    num_partitions = int(file_size / partition_size) + 1

    print(file_size)
    print(num_cores)
    print(partition_size)
    print(num_partitions)
    # create a list of partition boundaries
    boundaries = []
    with open(file_path, 'rb') as file:
        for i in range(num_partitions):
            file.seek(partition_size * i)
            # read a chunk of data from the file
            chunk = file.read(partition_size)
            # find the nearest newline character to use as a partition boundary
            if i < num_partitions - 1:
                newline_pos = chunk.rfind(b'\n')
                if newline_pos == -1:
                    newline_pos = len(chunk)
                boundaries.append(partition_size * i + newline_pos)
    # create a list of partition ranges
    ranges = [(boundaries[i-1]+1, boundaries[i]) for i in range(1, len(boundaries))]
    ranges.insert(0, (0, boundaries[0]))
    ranges.append((boundaries[-1]+1, file_size))
    # create a pool of worker processes
    pool = multiprocessing.Pool(num_cores)
    # map the partitions to worker processes
    results = pool.map(count_words_in_range, [(file_path, r) for r in ranges])
    # combine the results from each partition
    word_count = sum(results)
    print(word_count)
    # close the worker pool
    pool.close()
    return word_count


def count_words_in_range(args):
    file_path, range = args
    word_count = 0
    with open(file_path, 'rb') as file:
        file.seek(range[0])
        chunk = file.read(range[1] - range[0])
        word_count = len(chunk.split())
    return word_count


count_words('/Users/n2203020/Downloads/word-processor-main/src/main/resources/words.txt')