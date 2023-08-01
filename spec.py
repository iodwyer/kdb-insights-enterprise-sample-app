from kxi import sp
import pykx
import numpy as np
import pandas as pd 
import datetime

kfk_broker  = '104.198.219.51:9091'

def dbg(data):
  print(data)
  return(data)

trade_pipeline = (sp.read.from_kafka(topic='trade', brokers=kfk_broker)
    | sp.decode.json()
    | sp.map('{[data] (enlist[`timestamp]!enlist `time) xcol enlist "PS*j"$data }')
    | sp.map(dbg)
    | sp.write.to_stream(table = 'trade'))

sp.run(trade_pipeline)
