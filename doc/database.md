### UserInfo

> 用户个人信息

- id
    - varchar
    - primary key
- username
    - varchar
- password
    - varchar
- avatarUrl
    - varchar
- authority
    - int



### Cookies

> 用户Cookie

- userId
    - varchar



### Articles

- aid
    - varchar

- articleTitle
- subTitle
- articleContent

- userId
- time
- commentNum
- likeNum
- classify

### Tags

- aid
- tid
    - primary key
- tagName

### ArticleImg

- aid
- iimg
    - primary key
- img