- login
    - path : /login

    > method : POST

    - parameter : 
        - userName : String
        - password : String
    - 返回值
           - 成功：`{code:200 , msg:""}`
        - 失败：`{code:500 , msg:""}`
    
> method : GET

- 返回值
           - 成功：`{code:200 , msg:""}`
       
     - 失败：`{code:500 , msg:""}`
    
- register
    - path : /register
    - method : Post
    - parameter : 
        - name :
        - email : 
        - password :
        - repassword : 
    - 返回值
        - 成功：`{code:200 , msg:""}`
        - 失败：`{code:500 , msg:""}`
    
- homePage

    > 跳转主界面后，请求相关数据

    - path : /homePage?page=1

    - method : Get

    - 返回值

        - 成功：

            ```json
            {
                code : 200 ,
                msg : "" ,
                publishList : [
                    {
                        id : "" ,
                        type : "article",
                        title : "" ,
                        subTitle : "" ,
                        articleContent : "" ,
                        userid : "",
                        authorName : "" ,
                        avatarURL : "" ,
                        createTime : "",
                        classify : "" ,
                        cover : "",
                        tags : [
                            
                        ],
                        pics : [
                            
                        ]
                    },
                    {
                        id : "" ,
                        type : "idea",
                        ideaContent : "" ,
                        userId : "" ,
                        authorName : "" ,
                        avatarURL : "" ,
                        createTime : "",
                        classify : "" ,
                        tags : [
                            
                        ],
                        pics : [
                            
                        ]
                    },
                    {
                        id : "" ,
                        type : "video",
                        title : "" ,
                        videoUrl : "",
                        userId : "" ,
                        authorName : "" ,
                        avatarURL : "" ,
                        createTime : "",
                        classify : "" ,
                        tags : [
                            
                        ],
                        cover : "" 
            
                    }
                ] ,
                tagList : [
                    {
                        aId : "",
                        tId : "",
                        tagName :""
                    }
                ] ,
                
            }
            ```
            
        - 失败：`{code:500 , msg:""}`
    
- 发表想法:thinking:

    - path : /publishIdea
    - method : POST
    - paramter : 
        - createTime 
        - ideaContent
        - classify
        - tags : Array
        - pics : Array
    - 返回值
        - 成功：`{code:200 , msg:""}`
        - 失败：`{code:500 , msg:""}`
    
- 发表文章:blue_book:

    - path : /publishArticle
    - method : POST
    - paramter :
        - createTime     
        - title
          subtitle
        - articleContent      
        - classify
        - tags : Array
        - cover : 
        - pics :
    - 返回值
        - 成功：`{code:200 , msg:""}`
        - 失败：`{code:500 , msg:""}`
    
- 发表视频:movie_camera:

    - path : /publishVideo
    - method : POST
    - paramter :
        - createTime     
        - title 
        - classify
        - tags : Array
        -  videoUrl  :

- 上传视频​/图片​
    - path :  /uploadFile
    - method : POST
    - paramter : 
        - file : 
        - type :
    
- 最热门的5篇文章

    - path : /popularArticle

    - method : GET

    - paramter :

    - 返回值 :

        - 成功 :

            ```json
            [
                {
                    "id":"",
                    "title":""
                }
            ]
            ```

            

- 根据标签查询发布

    - path : /articlesOfTag

    - method : GET

    - paramter :

        - tagName : String

    - 返回值 :

        - 成功 :

            ```json
            [
                {
                    "id":"",
                    "type":0,
                    "title":""
                }
            ]
            ```

            