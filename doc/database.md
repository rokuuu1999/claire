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

| 字段名 | 类型 | 描述 |
| ------ | ---- | ---- |
| userId |      |      |

### Articles

| 字段名         | 类型 | 描述 |
| -------------- | ---- | ---- |
| id             |      |      |
| subTitle       |      |      |
| articleContent |      |      |
| classify       |      |      |

### Idea

| 字段名      | 类型 | 描述 |
| ----------- | ---- | ---- |
| id          |      |      |
| ideaContent |      |      |
| classify    |      |      |

### Video

| 字段名   | 类型 | 描述 |
| -------- | ---- | ---- |
| id       |      |      |
| videoUrl |      |      |

### Tags

| 字段名   | 类型 | 描述 |
| -------- | ---- | ---- |
| id       |      |      |
| parentId |      |      |
| tagName  |      |      |

### Img

| 字段名   | 类型 | 描述 |
| -------- | ---- | ---- |
| id       |      |      |
| parentId |      |      |
| imgUrl   |      |      |

### Comment

| 字段名   | 类型 | 描述 |
| -------- | ---- | ---- |
| id       |      |      |
| parentId |      |      |
| comment  |      |      |

### Publish

| 字段名     | 类型 | 描述                      |
| ---------- | ---- | ------------------------- |
| id         |      | 主键、自增                |
| parentId   |      | 文章、想法、视频的ID      |
| createTime |      |                           |
| userId     |      |                           |
| Title      |      |                           |
| commentNum |      |                           |
| likeNum    |      |                           |
| type       |      | 文章、想法、视频 三者之一 |

