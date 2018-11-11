#!/bin/bash
IP=10.254.254.254
PORT=2
SAMPLE1=$(snmpget -Oqv -v 2c -c public ${IP} 1.3.6.1.2.1.31.1.1.1.10.${PORT})
sleep 2
SAMPLE2=$(snmpget -Oqv -v 2c -c public ${IP} 1.3.6.1.2.1.31.1.1.1.10.${PORT})

DIFF=$((SAMPLE2-SAMPLE1))
echo "${SAMPLE1} ${SAMPLE2} ${DIFF}"
