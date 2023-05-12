#include "sensor/dth11.h"




byte dth11_read_byte()
{
    byte i              = 0;
    byte ucharFLAG      = 0;
    byte uchartemp      = 0;
    byte dth11_com_data = 0;
    for (i = 0; i < 8; i++)
    {
        ucharFLAG = 2;

        while ((gpio_get_level(DHT11_PIN) == 0) && ucharFLAG) //等待IO口变低，变低后，通过延时去判断是0还是1
        {
            ucharFLAG++;
            ets_delay_us(10);
        }
        ets_delay_us(35); //延时35us
        uchartemp = 0;

        if (gpio_get_level(DHT11_PIN) == 1) //如果这个位是1，35us后，还是1，否则为0
            uchartemp = 1;
        ucharFLAG = 2;

        while ((gpio_get_level(DHT11_PIN) == 1) && ucharFLAG) //等待IO口变高，变高后，表示可以读取下一位
        {
            ucharFLAG++;
            ets_delay_us(10);
        }
        if (ucharFLAG == 1)
            break;

        dth11_com_data <<= 1;
        dth11_com_data |= uchartemp;
    }
    return dth11_com_data;
}

DTH11_DATA dth11_get()
{
    byte ucharFLAG           = 0;
    byte ucharRH_data_H_temp = 0;
    byte ucharRH_data_L_temp = 0;
    byte ucharT_data_H_temp  = 0;
    byte ucharT_data_L_temp  = 0;
    byte ucharcheckdata_temp = 0;
    byte uchartemp           = 0;

    DTH11_DATA dth11_data = {
        .temperature = 0.,
        .humidity    = 0.,
    };

    // https://zhuanlan.zhihu.com/p/136157998
    // 1、MCU发送开始起始信号
    {
        gpio_pad_select_gpio(DHT11_PIN);
        gpio_set_direction(DHT11_PIN, GPIO_MODE_OUTPUT); // 总线空闲状态为高电平，主机把总线拉低等待DHT11响应； 与MCU相连的SDA数据引脚置为输出模式；
        gpio_set_level(DHT11_PIN, 0);
        ets_delay_us(19 * 1000);      // 主机把总线拉低至少18ms
        gpio_set_level(DHT11_PIN, 1); // 然后拉高20-40us等待DHT返回响应信号；
        ets_delay_us(30);             // 然后拉高20-40us等待DHT返回响应信号；
    }
    // 2、读取DHT11响应
    {
        gpio_set_direction(DHT11_PIN, GPIO_MODE_INPUT); // SDA数据引脚设为输入模式；
    }
    // DHT11检测到起始信号后，会将总线拉低80us，然后拉高80us作为响应；
    if (!gpio_get_level(DHT11_PIN))
    {
        ucharFLAG = 2;
        while ((!gpio_get_level(DHT11_PIN)) && ucharFLAG) //等待总线被传感器拉高
        {
            ucharFLAG++;
            ets_delay_us(10);
        }
        ucharFLAG = 2;

        while ((gpio_get_level(DHT11_PIN)) && ucharFLAG) //等待总线被传感器拉低
        {
            ucharFLAG++;
            ets_delay_us(10);
        }
        ucharRH_data_H_temp = dth11_read_byte();                                                                     // 读取第1字节 湿度整数
        ucharRH_data_L_temp = dth11_read_byte();                                                                     // 读取第2字节 湿度小数
        ucharT_data_H_temp  = dth11_read_byte();                                                                     // 读取第3字节 温度整数
        ucharT_data_L_temp  = dth11_read_byte();                                                                     // 读取第4字节 温度小数
        ucharcheckdata_temp = dth11_read_byte();                                                                     // 读取第5字节 校验
        uchartemp           = (ucharT_data_H_temp + ucharT_data_L_temp + ucharRH_data_H_temp + ucharRH_data_L_temp); // 计算校验和
        if (uchartemp == ucharcheckdata_temp)                                                                        //保存温度和湿度
        {
            dth11_data.humidity    = ucharRH_data_H_temp + ucharRH_data_L_temp / 100.;
            dth11_data.temperature = ucharT_data_H_temp + ucharT_data_L_temp / 100.;
        }
        else
        {
            dth11_data.humidity    = 999;
            dth11_data.temperature = 999;
        }
    }
    else
    {
        dth11_data.humidity    = 888;
        dth11_data.temperature = 888;
    }
    {
        gpio_pad_select_gpio(DHT11_PIN);
        gpio_set_direction(DHT11_PIN, GPIO_MODE_OUTPUT);
        gpio_set_level(DHT11_PIN, 1);
    }
    return dth11_data;
}
