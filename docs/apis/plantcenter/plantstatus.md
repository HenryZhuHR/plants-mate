## 接口

根据不同的请求

### 请求
<table>

<thead>
<tr>
<th colspan="2">基本</th>
</tr>
</thead>
<tbody>

<tr>
<td>URL</td> <td>/plantcenter/plantstatus</td>
</tr>

<tr>
<td>Method</td> <td>POST</td>
</tr>

</tbody>
</table>


### 请求头


| 名称         | 类型   | 必填 | 描述                                      |
| ------------ | ------ | ---- | ----------------------------------------- |
| Content-Type | string | 是   | 固定值："application/json; charset=utf-8" |



### 请求体

| 名称   | 类型 | 必填 | 示例值 | 描述     |
| ------ | ---- | ---- | ------ | -------- |
| device | int  | 是   | 749  | 设备编号  |
| date | int  | 是   | 749  | 设备编号 <br/> |


<table>
<thead>
<tr> <th>名称</th> <th>类型</th> <th>必填</th> <th>描述</th> </tr>
</thead>
<tbody>
<tr>
<td>device</td> <td>int</td> <td>是</td>
<td>
设备编号，编号的规则详见 <a link="../data/database.md">基本数据存储格式</a>
</td>
</tr>
<tr>
<td>date</td> <td>array</td> <td>否</td>
<td>
</td>
</tr>
</tbody>
</table>
