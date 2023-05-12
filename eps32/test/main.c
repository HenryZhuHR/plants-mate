#include <stdio.h>
#include <time.h>
#include <cJSON.h>
#include <string.h>


#include <stdlib.h>
#include <unistd.h>
#include <sys/ioctl.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <net/if.h>

#define MAC_SIZE	18
int main(int argc, char const* argv[])
{
    printf("hello\n");

    return 0;


    {
        cJSON* cjson_test = cJSON_CreateObject();

        time_t    now;
        char      strftime_buf[64];
        struct tm timeinfo;
        time(&now);
        // 将时区设置为中国标准时间
        // setenv("TZ", "CST-8", 1);
        tzset();
        localtime_r(&now, &timeinfo);
        strftime(strftime_buf, sizeof(strftime_buf), "%c", &timeinfo);

        cJSON_AddStringToObject(cjson_test, "time", strftime_buf);
        cJSON_AddStringToObject(cjson_test, "device", "sads");
        cJSON_AddNumberToObject(cjson_test, "zip-code", 111111);
        cJSON_AddFalseToObject(cjson_test, "student");

        /* 添加一个嵌套的JSON数据（添加一个链表节点） */
        cJSON* cjson_address = cJSON_CreateObject();
        cJSON_AddStringToObject(cjson_address, "country", "China");
        cJSON_AddNumberToObject(cjson_address, "zip-code", 111111);
        cJSON_AddItemToObject(cjson_test, "address", cjson_address);

        /* 添加一个数组类型的JSON数据(添加一个链表节点) */
        cJSON* cjson_skill = cJSON_CreateArray();
        cJSON_AddItemToArray(cjson_skill, cJSON_CreateString("C"));
        cJSON_AddItemToArray(cjson_skill, cJSON_CreateString("Java"));
        cJSON_AddItemToArray(cjson_skill, cJSON_CreateString("Python"));
        cJSON_AddItemToObject(cjson_test, "skill", cjson_skill);

        char* str = cJSON_Print(cjson_test);
        printf("%s\n", str);

        for (long long i = 0; i < 2999999999; i++)
            ;
        time(&now);
        localtime_r(&now, &timeinfo);
        strftime(strftime_buf, sizeof(strftime_buf), "%c", &timeinfo);
        printf("year\t%d\n", timeinfo.tm_year);
        printf("month\t%d\n", timeinfo.tm_mon);
        printf("day\t%d\n", timeinfo.tm_mday);
        cJSON_ReplaceItemInObject(cjson_test, "time", cJSON_CreateString(strftime_buf));
        cJSON_ReplaceItemInObject(cjson_address, "country", cJSON_CreateString("England"));

        str = cJSON_Print(cjson_test);
        printf("%s\n", str);
    }
    return 0;
}
