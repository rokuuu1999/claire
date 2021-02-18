### UserInfo

> 用户个人信息

| 字段名        | 类型 | 描述 |
| ------------- | ---- | ---- |
| userId        |      |      |
| userName      |      |      |
| password      |      |      |
| avatarUrl     |      |      |
| userAuthority |      |      |

### Cookies

> 用户Cookie

| 字段名     | 类型 | 描述 |
| ---------- | ---- | ---- |
| userId     |      |      |
| expireTime |      |      |

### Articles

| 字段名         | 类型 | 描述 |
| -------------- | ---- | ---- |
| selfId         |      |      |
| subTitle       |      |      |
| articleContent |      |      |
| classify       |      |      |

### Ideas

| 字段名      | 类型 | 描述 |
| ----------- | ---- | ---- |
| selfId      |      |      |
| ideaContent |      |      |
| classify    |      |      |

### Videos

| 字段名   | 类型 | 描述 |
| -------- | ---- | ---- |
| selfId   |      |      |
| videoUrl |      |      |

### Tags

| 字段名   | 类型 | 描述 |
| -------- | ---- | ---- |
| selfId   |      |      |
| parentId |      |      |
| tagName  |      |      |
| type     |      |      |

### Imgs

| 字段名   | 类型 | 描述 |
| -------- | ---- | ---- |
| selfId   |      |      |
| parentId |      |      |
| imgUrl   |      |      |
| type     | int  |      |

### Comments

| 字段名   | 类型 | 描述 |
| -------- | ---- | ---- |
| selfId   |      |      |
| parentId |      |      |
| comment  |      |      |
| type     | int  |      |

### Publish

| 字段名     | 类型 | 描述                      |
| ---------- | ---- | ------------------------- |
| selfId     |      | 主键、自增                |
| parentId   |      | 文章、想法、视频的ID      |
| createTime |      |                           |
| userId     |      |                           |
| Title      |      |                           |
| commentNum |      | 评论数量                  |
| likeNum    |      | 点赞数量                  |
| type       |      | 文章、想法、视频 三者之一 |

