import datetime as dt
import gzip
import io
import json
import logging
import os
import time
import uuid
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, wait

import boto3
# import pandas as pd
# import pyarrow.parquet as pq
# from pyarrow import orc
import smart_open as so
import xmltodict

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def s3_upload(body: str, bucket: str, key: str, type: str) -> None:
    """Uploads specified object to s3.

    Args:
        body (str): data to be uploaded
        bucket (str): destination bucket
        key (str): s3 object upload key path
        type (str): data type for upload (e.g., 'application/json')
    """
    s3_client = boto3.client("s3")
    s3_client.put_object(Body=body, Bucket=bucket, Key=key, ContentType=type)


def upload_path(s3_object_key: str, iteration: int) -> str:
    """Creates new s3 upload path.

    Args:
        s3_object_key (str): original s3 object key path
        iteration (int): iteration of process

    Returns:
        str: new s3 upload path
    """
    delim = '.'
    s3_seperated = s3_object_key.rsplit(delim, 1)
    file_type = s3_seperated[1]
    path = s3_seperated[0]
    new_path = f'{path}-{str(iteration).zfill(7)}.json'
    return new_path


def chunkit(l: list, n: int):
    """Yield successive n-sized chunks from l

    Args:
        l (list): list of data to be chunked
        n (int): number of data chunks

    Yields:
        generator: yeild successive n-sized chunks of data from list
    """
    for i in range(0, len(l), n):
        yield l[i:i + n]


def kinesis_put(jzon: str, stream_name: str) -> None:
    """Puts data into kinesis in 500 record chunks

    Args:
        jzon (str): json string
        stream_name (str): target kinesis stream name
    """
    try:
        data = json.loads(jzon)
        pfx = '[BatchShredder] :: '
        kinesis_client = boto3.client("kinesis")
        partition_key = str(uuid.uuid4())
        records = chunkit(
            [{"PartitionKey": partition_key, "Data": json.dumps(row)} for row in data], 500)
        for chunk in records:
            response = kinesis_client.put_records(
                StreamName=stream_name, Records=chunk)
            # status = response['ResponseMetadata']['HTTPStatusCode']
            # failed_records = response['FailedRecordCount']
            # logger.info(
            #     f'{pfx} Kinesis Response: {status}.  {failed_records} failed records.')
            time.sleep(1.5)
        logger.info(
            f'{pfx}Loaded {len(data)} records to kinesis - {dt.datetime.now()}')
    except:
        logger.info("Kinesis Put Records Failed")


def process_all(tasks: list):
    """Multi-thread execution for specified process

    Args:
        tasks (list): list of tasks for process/function should to be applied

    Returns:
        generator: executor response
    """
    with ThreadPoolExecutor(max_workers=10) as executor:
        resp = executor.map(process_files, tasks)
    return resp


def get_keys(d: dict, c=[]) -> list:
    """get all keys in a given dictionary

    Args:
        d (dict): any dictionary you want to obtain list of keys
        c (list): do not specify it is an empty list for recursive funciton

    Returns:
        list: list of dictionary keys
    """
    return [i for a, b in d.items() for i in ([c+[a]] if not isinstance(b, dict) else get_keys(b, c+[a]))]


def create_chunk(chunk, iteration: int, key: str, file_type: str, stream_name: str) -> list:
    """"helper function to help create tasks based on chunks of data for multi-thread executor

    Args:
        chunk = data, iteration = iteration of chunk, key = s3 object key, file_type(json, csv, etc.), stream_name = kinesis stream name


    Args:
        chunk (_type_): chunk of data for this iteration types varies depending on datatype (e.g., <class 'pyarrow.lib.RecordBatch'>, string, etc.)
        iteration (int): iteration of current file being processed
        key (str): s3 ivhectkey path for file to shre
        file_type (str):  type of file to process (e.g., json, csv, parquet, etc.)
        stream_name (str): target kinesis stream name for where data is being pushed

    Returns:
        list: list of arguments [file_type, path_like_object, s3_object_key, stream_name] to be passed for process_files task
    """
    t = []
    t.append(chunk)
    t.append(iteration)
    t.append(key)
    t.append(file_type)
    t.append(stream_name)
    return t


def process_files(task: list) -> int:
    """function to be passed for multi-thread execution, specific process for each data type

    Args:
        task (list): list of arguments [file_type, path_like_object, s3_object_key, stream_name] to be passed.  converts data to json and pushes to kinesis

    Returns:
        int: iteration completed for processed data
    """
    pfx = '[BatchShredder] :: '
    data = task[0]
    iteration = task[1]
    s3_object_key = task[2]
    file_type = task[3]
    stream_name = task[4]
    if file_type in ('parquet', 'orc'):
        var_df = data.to_pandas()
        jzon = var_df.to_json(orient='records')
    elif file_type == 'csv':
        jzon = data.to_json(orient='records')
    elif file_type in ('json', 'xml'):
        jzon = data
    else:
        logger.warning(f'{pfx} file type: {file_type} not supported')
    kinesis_put(jzon, stream_name)
    return iteration


def get_csv_tasks(file_type: str, path_like_object, s3_object_key: str, stream_name: str) -> list:
    """creates multi-thread executor tasks for for csv data type

    Args:
        file_type (str): type of file to process (e.g., json, csv, parquet, etc.)
        path_like_object (_type_): class of datatype being ingested via smart-open library (e.g., <class 'gzip.GzipFile'>, <class '_io.BufferedReader'>, etc.)
        s3_object_key (str): s3 ivhectkey path for file to shred
        stream_name (str): target kinesis stream name for where data is being pushed

    Returns:
        list: list of multi-thread executor tasks for for csv data type
    """
    bs = 1000
    tasks = []
    for iteration, chunk in enumerate(pd.read_csv(path_like_object, chunksize=bs)):
        t = create_chunk(chunk, iteration, s3_object_key,
                         file_type, stream_name)
        tasks.append(t)
    return tasks


def get_parquet_tasks(file_type: str, path_like_object, s3_object_key: str, stream_name: str) -> list:
    """creates multi-thread executor tasks for for parquet data type

    Args:
        file_type (str): type of file to process (e.g., json, csv, parquet, etc.)
        path_like_object (_type_): class of datatype being ingested via smart-open library (e.g., <class 'gzip.GzipFile'>, <class '_io.BufferedReader'>, etc.)
        s3_object_key (str): s3 ivhectkey path for file to shred
        stream_name (str): target kinesis stream name for where data is being pushed

    Returns:
        list: list of multi-thread executor tasks for for parquet data type
    """
    pfile = pq.ParquetFile(path_like_object)
    bs = 1000
    iteration = 0
    tasks = []
    for chunk in pfile.iter_batches(batch_size=bs):
        t = create_chunk(chunk, iteration, s3_object_key,
                         file_type, stream_name)
        tasks.append(t)
        iteration += 1
    return tasks


def get_json_tasks(file_type: str, path_like_object, s3_object_key: str, stream_name: str) -> list:
    """creates multi-thread executor tasks for for json data type

    Args:
        file_type (str): type of file to process (e.g., json, csv, parquet, etc.)
        path_like_object (_type_): class of datatype being ingested via smart-open library (e.g., <class 'gzip.GzipFile'>, <class '_io.BufferedReader'>, etc.)
        s3_object_key (str): s3 ivhectkey path for file to shred
        stream_name (str): target kinesis stream name for where data is being pushed

    Returns:
        list: list of multi-thread executor tasks for for json data type
    """
    ll = [json.loads(line.strip()) for line in path_like_object.readlines()]
    bs = 500
    iteration = 0
    total = len(ll) // bs
    tasks = []
    for iteration in range(total+1):
        chunk = json.dumps(ll[iteration * bs:(iteration + 1) * bs])
        t = create_chunk(chunk, iteration, s3_object_key,
                         file_type, stream_name)
        tasks.append(t)
        iteration += 1
    return tasks


def get_orc_tasks(file_type: str, path_like_object, s3_object_key: str, stream_name: str) -> list:
    """creates multi-thread executor tasks for for orc data type
    Args:
        file_type (str): type of file to process (e.g., json, csv, parquet, etc.)
        path_like_object (_type_): class of datatype being ingested via smart-open library (e.g., <class 'gzip.GzipFile'>, <class '_io.BufferedReader'>, etc.)
        s3_object_key (str): s3 ivhectkey path for file to shred
        stream_name (str): target kinesis stream name for where data is being pushed

    Returns:
        list: list of multi-thread executor tasks for for orc data type
    """
    orcfile = orc.ORCFile(path_like_object).read()
    bs = 500
    iteration = 0
    tasks = []
    for chunk in orcfile.to_batches(max_chunksize=bs):
        t = create_chunk(chunk, iteration, s3_object_key,
                         file_type, stream_name)
        tasks.append(t)
        iteration += 1
    return tasks


def get_xml_tasks(file_type: str, path_like_object, s3_object_key: str, stream_name: str) -> list:
    """creates multi-thread executor tasks for for xml data type
    Args:
        file_type (str): type of file to process (e.g., json, csv, parquet, etc.)
        path_like_object (_type_): class of datatype being ingested via smart-open library (e.g., <class 'gzip.GzipFile'>, <class '_io.BufferedReader'>, etc.)
        s3_object_key (str): s3 ivhectkey path for file to shred
        stream_name (str): target kinesis stream name for where data is being pushed

    Returns:
        list: list of multi-thread executor tasks for for xml data type
    """
    data_dict = xmltodict.parse(path_like_object.read())
    result = list(map('.'.join, get_keys(data_dict)))
    keys = result[0].split('.')
    # xml data is two levels down - TODO paramterize
    ll = data_dict[keys[0]][keys[1]]
    bs = 500
    iteration = 0
    total = len(ll) // bs
    tasks = []
    for iteration in range(total+1):
        chunk = json.dumps(ll[iteration * bs:(iteration + 1) * bs])
        t = create_chunk(chunk, iteration, s3_object_key,
                         file_type, stream_name)
        tasks.append(t)
        iteration += 1
    return tasks


def shredder(file_type: str, path_like_object, s3_object_key: str, stream_name: str) -> int:
    """main shredder function that shreds larger file into smaller chunks to be put into kinesis stream, process varies on datatype
    Args:
        file_type (str): type of file to process (e.g., json, csv, parquet, etc.)
        path_like_object (_type_): class of datatype being ingested via smart-open library (e.g., <class 'gzip.GzipFile'>, <class '_io.BufferedReader'>, etc.)
        s3_object_key (str): s3 ivhectkey path for file to shred
        stream_name (str): target kinesis stream name for where data is being pushed

    Returns:
        int: number of iterations required to process the file
    """
    pfx = '[BatchShredder] :: '
    logger.info(f'{pfx}Starting loop...')

    tasks = []
    if file_type == 'parquet':
        tasks = get_parquet_tasks(
            file_type, path_like_object, s3_object_key, stream_name)
    elif file_type == 'csv':
        tasks = get_csv_tasks(file_type, path_like_object,
                              s3_object_key, stream_name)
    elif file_type == 'json':
        tasks = get_json_tasks(file_type, path_like_object,
                               s3_object_key, stream_name)
    elif file_type == 'orc':
        tasks = get_orc_tasks(file_type, path_like_object,
                              s3_object_key, stream_name)
    elif file_type == 'xml':
        tasks = get_xml_tasks(file_type, path_like_object,
                              s3_object_key, stream_name)
    elif file_type == 'gz':
        if 'json' in s3_object_key:
            file_type = 'json'
            tasks = get_json_tasks(
                file_type, path_like_object, s3_object_key, stream_name)
        elif 'csv' in s3_object_key:
            file_type = 'csv'
            tasks = get_csv_tasks(
                file_type, path_like_object, s3_object_key, stream_name)
    else:
        logger.warning(f'{pfx}File type: {file_type} not supported...')

    iterations = len(tasks)
    process_all(tasks)
    return iterations


# TODO add support for avro file type
# def avro_shredder(path_like_object, s3_bucket_fanout, s3_object_key):
