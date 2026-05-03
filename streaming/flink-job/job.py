from pyflink.datastream import StreamExecutionEnvironment

env = StreamExecutionEnvironment.get_execution_environment()

ds = env.from_collection([
    ("user1", "login"),
    ("user2", "transfer")
])

ds.print()

env.execute("threat-detection-job")
