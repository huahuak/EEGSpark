# EEGSpark 环境搭建指南

本指南将帮助您在本地机器和 Docker 环境中搭建 PySpark 开发和运行环境。请确保您已经安装了 Docker（如果选择 Docker 环境），并且具备基本的 Docker、PySpark 和 Python 知识。

## 本地机器环境搭建

### 步骤 1: 安装 Java

确保您的机器上安装了 Java。可以从 [Oracle 官网](https://www.oracle.com/java/technologies/javase-jdk11-downloads.html) 下载并安装适合您操作系统的 Java 版本。

### 步骤 2: 安装 Apache Spark

下载 Apache Spark 并解压到您的本地目录。可以从 [Apache Spark 官网](https://spark.apache.org/downloads.html) 下载适合您操作系统的版本。

```sh
wget https://downloads.apache.org/spark/spark-3.1.2/spark-3.1.2-bin-hadoop3.2.tgz
tar -xzf spark-3.1.2-bin-hadoop3.2.tgz
```

### 步骤 3: 配置环境变量

将 Spark 的 bin 目录添加到您的 PATH 环境变量中。

```sh
export SPARK_HOME=/path/to/your/spark
export PATH=$PATH:$SPARK_HOME/bin
```

### 步骤 4: 安装 Python 和 pip

确保您的机器上安装了 Python 和 pip。可以从 [Python 官网](https://www.python.org/downloads/) 下载并安装适合您操作系统的 Python 版本。

### 步骤 5: 安装 PySpark

使用 pip 安装 PySpark。

```sh
pip install pyspark
```

### 步骤 6: 编写并运行测试脚本

在本地环境中，编写并运行您的 PySpark 测试脚本。

```sh
python test_pyspark.py
```
### 步骤 7: 下载EEGspark源码并创建数据目录

```sh
git clone https://github.com/huahuak/EEGSpark.git
```
建议本地数据目录放在EEGspark目录下
```sh
mkdir （数据目录名称）
```
修改test目录下test数据路径为本地数据路径
### 步骤 8: 安装EEGspark依赖
```sh
pip install -r requirments.txt
```
### 步骤 9: 打包环境

将 eegspark 库及其依赖打包成一个 ZIP 文件：

```sh
zip -r eegspark.zip eegspark
```
### 步骤 10: 使用 spark-submit 提交作业

使用 spark-submit 命令提交您的 PySpark 脚本，并指定包含 eegspark 库的 ZIP 文件路径：

```sh
spark-submit --py-files /path-to-your-eegspark-directory/eegspark.zip test.py
```

### 步骤 11: 查看结果

在 Spark UI 中查看您的作业运行情况：

```plaintext
http://localhost:8080
```

---
## Docker 环境搭建

### 步骤 1: 安装 Docker

确保您已经在您的机器上安装了 Docker。可以从 [Docker 官网](https://www.docker.com/get-started) 下载并安装适合您操作系统的版本。

### 步骤 2: 拉取 Apache Spark 镜像

使用以下命令拉取最新的 Apache Spark 镜像：

```sh
docker pull apache/spark:latest
```

### 步骤 3: 创建 Spark Master 容器

创建一个新的 Spark Master 容器，并将本地目录挂载到容器中：

```sh
docker run -it --name spark-master -v (本地目录):/home --user root apache/spark:latest bash
```

进入容器后，启动 Spark Master：

```sh
cd /opt/spark/
./bin/spark-class org.apache.spark.deploy.master.Master
```

### 步骤 4: 创建 Spark Worker 容器

创建一个新的 Spark Worker 容器，并链接至 Spark Master：

```sh
docker run -it --name spark-worker --link spark-master:spark-master --user root apache/spark:latest bash
```

进入容器后，启动 Spark Worker：

```sh
cd /opt/spark/
./bin/spark-class org.apache.spark.deploy.worker.Worker spark://spark-master:7077
```

### 步骤 5: 进入 Spark Master 容器并且导入仓库

使用以下命令进入 Spark Master 容器的 bash 环境：

```sh
docker exec -it spark-master bash
```
```sh
git clone https://github.com/huahuak/EEGSpark.git
```
建议本地数据目录放在EEGspark目录下
```sh
mkdir （数据目录名称）
```
修改test目录下test数据路径为本地数据路径

### 步骤 6: 创建虚拟环境

在 Spark Master 容器中创建一个新的虚拟环境：

```sh
sudo apt-get update
sudo apt-get install python3
python3 -m venv venv
cd eegspark
pip install -r requirments.txt
```

### 步骤 7: 激活虚拟环境

使用以下命令激活虚拟环境：

```sh
source venv/bin/activate
```

### 步骤 8: 安装 PySpark

在虚拟环境中安装 PySpark：

```sh
pip install pyspark
```

### 步骤 9: 编写并运行测试脚本

在虚拟环境中，编写并运行您的 PySpark 测试脚本：

```sh
python test_pyspark.py
```

### 步骤 10: 打包环境

将 eegspark 库及其依赖打包成一个 ZIP 文件：

```sh
zip -r eegspark.zip eegspark
```

### 步骤 11: 使用 spark-submit 提交作业

使用 spark-submit 命令提交您的 PySpark 脚本，并指定包含 eegspark 库的 ZIP 文件路径：

```sh
spark-submit --py-files /path-to-your-eegspark-directory/eegspark.zip test.py
```

### 步骤 12: 查看结果

在 Spark UI 中查看您的作业运行情况：

```plaintext
http://localhost:8080
```

---

以上步骤将帮助您搭建一个完整的 eegSpark 开发和运行环境。请根据实际情况调整命令和配置。
