

export PROJECT_HOME=$(pwd)
export LOG_DIR=$PROJECT_HOME/log

if [ ! -d $LOG_DIR/mosquitto ]; then
    mkdir -p $LOG_DIR/mosquitto
fi

mosquitto \
    -c $PROJECT_HOME/configs/mosquitto/mosquitto.conf

# mosquitto_pub -t "testtopic" -m  "pub发送内容"