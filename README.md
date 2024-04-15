# EEGSpark

## python venv

```bash
# activate env
cd /home/team4spark/EEGSpark
source .venv/bin/activate
# test env
python eegspark/test/pysparkdemo.py
# >>> Lines with a: 4, lines with b: 2 
```

## test demo

test demo with follow command.

```bash
python -m eegspark.test.test
```

### code demo
```py
source = fetcher.Source("/home/team4spark/EEGSpark/data/subject_02_PC.mat")

# 使用Source2EEGRDD将数据源转化为EEGRDD对象
eegrdd = Source2EEGRDD(source)
# 将低通滤波器应用于EEGRDD数据
lowpass_filter = LowPassFilter(lowpass=30, fs=500)
filtered_eegrdd = eegrdd.map_channel(lowpass_filter())
# 将高通滤波器应用于RDD数据
highpass_filter = HighPassFilter(highpass=0.5, fs=500)
filtered_eegrdd = filtered_eegrdd.map_channel(highpass_filter())
# 遍历EEGRDD的channelDataRDD并打印每个通道的前5个数据点
eegrdd.foreach_channel(lambda x: print(x[0:5]))

# 将低通滤波器应用到EEGRDD的channelDataRDD上，然后遍历并打印每个滤波后的通道的前5个数据点
filtered_eegrdd.foreach_channel(lambda x: print(x[0:5]))
```

## format command
```bash
cd /home/team4spark/EEGSpark
find ./eegspark -name "*.py" | xargs black
```