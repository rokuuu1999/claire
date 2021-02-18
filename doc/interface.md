- login
    - path : /login
    - method : Post
    - parameter : 
        - userName : String
        - email : String
        - password : String
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

    - path : /homePage

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
                        userId : "" ,
                        createTime : "",
                        classify : "" ,
                        tags:[
                            
                        ]
                    },
                    {
                        id : "" ,
                        type : "idea",
                        title : "" ,
                        ideaContent : "" ,
                        userId : "" ,
                        createTime : "",
                        classify : "" ,
                        tags:[
                            
                        ]
                    },
                    {
                        id : "" ,
                        type : "video",
                        title : "" ,
                        videoUrl : "",
                        userId : "" ,
                        createTime : "",
            
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



