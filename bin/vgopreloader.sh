#!/bin/bash

base_dir=$(cd $(dirname $(dirname $0)); pwd)
echo "[INFO] Hive loader location: "${base_dir}

if [ "${base_dir}" == "/" ];then
    echo "[ERROR] Wrong hive loader location!"
    exit 1
fi

# 添加工程目录到搜索路径(关键)
export PYTHONPATH=${base_dir}
cd ${base_dir}

script_file="scripts/vgopReload/vgopReload.py"
echo "[INFO] Begin running vgop reload script: "${script_file}
python ${script_file} "$@"
exit_code=$?

if [ ${exit_code} == 0 ]
then
    echo "[INFO] Run vgop reload script success"
else
    echo "[ERROR] Run vgop reload script failed: exitCode = "${exit_code}
    exit -1
fi
