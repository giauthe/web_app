#!/usr/bin/env bash
import redis,json

def connect_redis(hostname,port,password):
    r = redis.Redis(
        host=hostname,
        port=port,
        password=password)
    return r

def get_redis(connect_redis,key):
    value = connect_redis.get(key)
    # null = None
    # d = json.loads(value)
    # print(value)
    return value

# if __name__ == "__main__":
#     r = connect_redis('10.14.24.144','6400','5eqp3FhprgPhRjB3')
#     i = get_redis(r,'payment::feeTierByserviceCommandId::4439')
#     print(i)

