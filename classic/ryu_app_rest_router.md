# 如何使用 ryu.app.rest_router

## 启动

```shell
ryu-manager ryu.app.rest_router
```

## API 接口

`GET http://localhost:8080/router/0000000000000001 ` 是得到`01`号router的信息

```
POST http://localhost:8080/router/0000000000000001
{
} //JSON对象
```

是修改`01`号router的信息，由json对象指定修改内容。

+ `"address" : ""`指定`ip`
+ `"gateway":""`指定路由路径，**后面的参数填的是要送到的下一跳地址**
+ `"destination"`指定目的地址

