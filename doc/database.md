### UserInfo

> 用户个人信息

- userId
    - varchar
    - primary key
- userName
    - varchar
- password
    - varchar
- avatarUrl
    - varchar
- userAuthority
    - int



### Cookies

> 用户Cookie

- userId
    - varchar



### Articles

- aId
    - varchar

- articleTitle
- subTitle
- articleContent

- userId
- createTime
- commentNum
- likeNum
- classify

### Tags

- aId
- tId
    - primary key
- tagName

### ArticleImg

- aid
- iId
    - primary key
- imgUrl