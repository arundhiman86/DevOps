#!/bin/bash

# set -x
for filename in 'test' 'data' 'log' 'config' 'sys' 'network' 'logify' 'testify' 'system' 'configuration' 'testify'
do
	for number in {1..6}
	do
		aws --endpoint-url=http://192.168.99.103:31566/ --profile localstack s3 mb s3://bucket${number} 2> /dev/null
		head -c "${number}0" < /var/log/system.log > ${filename}file${number}.txt
		aws --endpoint-url=http://192.168.99.103:31566/ --profile localstack s3 mv ./${filename}file${number}.txt s3://bucket${number}
	done
done
