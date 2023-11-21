#!/bin/bash
cd /opt/kafka;
bin/kafka-topics.sh --create --topic temperature4 --bootstrap-server localhost:9092;
exit;
