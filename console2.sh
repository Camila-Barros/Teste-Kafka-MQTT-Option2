#!/bin/bash
cd /opt/kafka;
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic temperature4 --from-beginning;
exit;
