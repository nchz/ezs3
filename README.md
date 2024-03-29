# ezS3

This library provides abstractions over [boto3](https://pypi.org/project/boto3/) to easily deal with S3 buckets.


## Usage

```python
from ezs3 import S3

# be sure to have set AWS_ACCESS_KEY_ID and
# AWS_SECRET_ACCESS_KEY env variables.
s3 = S3(bucket_name="some_bucket")

# or load credentials from file.
s3 = S3.from_credentials(bucket_name="some_bucket")

# upload everything in `./data` to `bucket_name://data/input`, imitating the
# directory structure. the directory `data` itself is not copied.
# these are equivalent:
#   s3.upload("./data", "data/input")
#   s3.upload("./data/", "data/input/")
s3.upload("./data/", "data/input")
# upload `/tmp/my_file` to `bucket_name://data/my_file`.
s3.upload("/tmp/my_file", "data/")

# download everything under `bucket_name://data/input` into `./data2`,
# imitating the prefix structure.
s3.download("data/input", "./data2/")
# download `bucket_name://data/my_file` into `/tmp`.
s3.download("data/my_file", "/tmp/")
# same as above, but file is renamed to `my_file2`.
s3.download("data/my_file", "/tmp/my_file2")

# remove files.
s3.remove(*s3.list_keys("data/"))
```
