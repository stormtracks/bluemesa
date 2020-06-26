# Note that these are generic functions which do not have
# anything to do with bluemesa but could be used generically
# across any project that uses python and redis

import unittest
import redis

rc = redis.Redis(host='localhost', port=6379, db=0)

def redis_set_to_python_set(key):
    members = set()
    rset = rc.smembers(key)
    for value in rset:
        value = value.decode("utf-8")
        members.add(value)
    return(members)

def redis_set_write(key,member):
    rc.sadd(key,member)

def redis_set_read(key,member):
    value = rc.sismember(key,member)
    return(value)

def redis_delete(key):
    rc.delete(key)

if __name__ == "__main__":
    redis_set_write("mykey","or")
    val = redis_set_read("mykey","or")
    assert val == True
    val = redis_set_read("mykey","nm")
    assert val == False
    redis_delete("mykey")
    val = rc.exists("mykey")
    assert val == False
