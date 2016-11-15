import csv
import gzip
import io
import numpy as np

header = ["foo", "bar", "hoge"]
body = np.random.rand(3, 3)
csv_array = np.vstack([header, body])

stringio = io.StringIO()
writer = csv.writer(stringio)

writer.writerows(csv_array)

data = gzip.compress(stringio.getvalue().encode("utf-8"))
f = open("foo.csv.gz", "wb")
f.write(data)
f.close()
