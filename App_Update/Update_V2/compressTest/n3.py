import os
import time
import lzma
import lz4.frame
import zlib
import zstandard as zstd

folder_path = "test/"

# 待測壓縮算法
algorithms = {
    "zstd": (zstd.ZstdCompressor(), zstd.ZstdDecompressor()),
    "zlib": (zlib.compressobj(), zlib.decompressobj())
}
#    "lzma": (lzma.LZMACompressor(), lzma.LZMADecompressor()),

def compress_file(algorithm, file_path):
    compressor, decompressor = algorithms[algorithm]
    with open(file_path, "rb") as f: 
          compressed_data = compressor.compress(f.read())
    with open(f"{file_path}.{algorithm}", "wb") as f:
        f.write(compressed_data)

def decompress_file(algorithm, file_path):
    compressor, decompressor = algorithms[algorithm]
    with open(f"{file_path}.{algorithm}", "rb") as f1:
        data=f1.read()
    decompressed_data = decompressor.decompress(data)
    with open(file_path+".l", "wb") as f2:
        f2.write(decompressed_data)

# 壓縮和解壓縮時間
def measure_compression_time(algorithm, file_paths):
    compression_times = []
    decompression_times = []
    for file_path in file_paths:
        start_time = time.time()
        compress_file(algorithm, file_path)
        end_time = time.time()
        compression_times.append(end_time - start_time)
        
        start_time = time.time()
        decompress_file(algorithm, file_path)
        end_time = time.time()
        decompression_times.append(end_time - start_time)
    
    return compression_times, decompression_times

file_paths = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

# 不同壓縮算法的壓縮&解壓時間
results = {}
for algorithm in algorithms.keys():
    compression_times, decompression_times = measure_compression_time(algorithm, file_paths)
    results[algorithm] = (compression_times, decompression_times)

# 找出時間最短算法
fastest_algorithms = {}
download_speed = 2  # MB/s
algorithm_list = list(algorithms.keys())
for file_path in file_paths:
    file_name = os.path.basename(file_path)
    download_times = []
    for algorithm in algorithms.keys():
        file_size = os.path.getsize(f"{file_path}.{algorithm}")
        download_time = file_size / (download_speed * 1024 * 1024)  # 下載時間
        download_times.append(download_time)
    best_algorithm = min(algorithm_list, key=lambda x: sum(results[x][1]) + download_times[algorithm_list.index(x)])
    fastest_algorithms[file_name] = {"best": best_algorithm, "times": results, "download_times": download_times}

# 結果
for file_name, data in fastest_algorithms.items():
    print(f"File: {file_name}")
    print(f"Best Algorithm: {data['best']}")
    print("Decompression Times:")
    for algorithm, times in data["times"].items():
        print(f"{algorithm}: {sum(times[1]):.2f} seconds")
    print("Download and Decompression Times:")
    for i, algorithm in enumerate(algorithm_list):
        total_time = sum(data["times"][algorithm][1]) + data["download_times"][i]
        print(f"{algorithm}: {total_time:.2f} seconds")
    print()
