<template>
  <div class="full-size page-container">
    <div class="article-card">
      <div class="content">
        <div class="content-header">
          <v-avatar>
            <img :src="author.avatarUrl" alt="avatar" />
          </v-avatar>
          <div class="content-header-info">
            <div>{{ author.nickName }}</div>
            <div v-text="changeTimeStamp(this.publishTime)"></div>
          </div>
        </div>
        <div class="content-body">
          <router-view :content-data="contentData"></router-view>
        </div>
        <div class="content-footer">
          <v-btn
            small
            outlined
            rounded
            color="primary"
            v-for="(tag, index) in tags"
            :key="index"
            >{{ tag }}</v-btn
          >
          <div class="content-footer-btn">
            <v-btn depressed text>
              <v-icon left color="primary">mdi-thumb-up-outline</v-icon>
              2662
            </v-btn>
          </div>
        </div>
      </div>
      <v-divider></v-divider>
      <v-card flat>
        <div class="title">说说我的看法</div>
        <v-textarea outlined></v-textarea>
        <v-btn block color="primary">发表</v-btn>
      </v-card>
      <v-card flat>
        <div class="title">全部评论</div>
        <div
          class="comment"
          v-for="(comment, index) in commentList"
          :key="index"
        >
          <v-divider></v-divider>
          <div class="comment-header">
            <v-avatar size="40">
              <img :src="comment.author.icon" alt="" />
            </v-avatar>
            <strong class="comment-header-name">{{
              comment.author.name
            }}</strong>
          </div>
          <div class="comment-body">
            {{ comment.text }}
            <div class="comment-footer">
              <div v-text="changeTimeStamp(comment.time)"></div>
              <div>
                <v-btn depressed text v-on:click="comment.show = !comment.show">
                  <v-icon left color="primary">mdi-comment-edit-outline</v-icon>
                  回复
                </v-btn>
                <v-btn depressed text>
                  <v-icon left color="primary">mdi-thumb-up-outline</v-icon>
                  2662
                </v-btn>
              </div>
            </div>
          </div>
          <div class="comment-reply-input" v-if="comment.show">
            <v-textarea outlined label="回复"></v-textarea>
          </div>
          <div class="comment-reply">
            <div v-for="(reply, index) in comment.reply" :key="index">
              <div class="comment-reply-header">
                <v-avatar size="30"
                  ><img :src="reply.author.icon" alt="avatar" />
                </v-avatar>

                <strong class="comment-reply-header-name">{{
                  reply.author.name
                }}</strong>
              </div>
              <div class="comment-reply-body">
                <div>
                  {{ reply.text }}
                </div>
                <div class="comment-reply-footer">
                  <div v-text="changeTimeStamp(reply.time)"></div>
                  <div style="margin-left:10px">
                    <v-btn depressed text v-on:click="reply.show = !reply.show">
                      <v-icon left color="primary">
                        mdi-comment-edit-outline
                      </v-icon>
                      回复
                    </v-btn>
                    <v-btn depressed text>
                      <v-icon left color="primary">
                        mdi-thumb-up-outline
                      </v-icon>
                      2662
                    </v-btn>
                  </div>
                </div>
              </div>
              <div class="comment-reply-input" v-if="reply.show">
                <v-textarea outlined label="回复"></v-textarea>
              </div>
            </div>
          </div>
        </div>
      </v-card>
    </div>
  </div>
</template>

<script>
export default {
  name: "PostLayout",
  data() {
    return {
      commentList: [
        {
          show: false,
          commentId: "69:24641022:9223370424156591948:9803",
          text: "加入官方米粉群，报名米粉顾问团。\n下一次你也有机会参加哦",
          extra:
            '{"product":"cas","model":"Mi 10 Ultra","anonyComment":false,"adopted":false,"atUsers":"","featureComment":1}',
          imagesInfo: [
            {
              imageUrl:
                "https://cdn.cnbj1.fds.api.mi-img.com/middle.community.vip.bkt/6f84e8098787bd9b56f7404ac0a045e4",
              height: 2105,
              width: 1080
            }
          ],
          author: {
            userId: 684689925,
            name: "黄建",
            icon:
              "https://cdn.cnbj1.fds.api.mi-img.com/middle.community.vip.bkt/vip1564747679039",
            time: 0,
            identified: true,
            pinnedBadgeIcon:
              "https://ts.market.mi-img.com/download/MiVip/05f59141c9aaf45ac1dcbe11cc640008203d316e9",
            personalTag: "小米社区督察组",
            pendants: [
              {
                id: 10279,
                image:
                  "MIUI_VIP_WEB_ROOT_URLMiVip/0f26253fafa927760a5c93ccf3d55ed9f85435d29",
                description: "",
                text: "Kino&Hoho",
                isExpired: false,
                styleId: 0
              }
            ],
            hasVipRight: true,
            postSource: "_",
            vipType: 5
          },
          userId: 684689925,
          subjectId: "24641022",
          supportNum: 372,
          time: 1612698183859,
          support: false,
          ownComment: false,
          isAdmin: 0,
          top: false,
          feature: true,
          reply: [
            {
              show: false,
              commentId: "69:24641022:9223370423739768583:17051",
              text: "新年快乐哦",
              extra:
                '{"product":"cezanne","model":"Redmi K30 Ultra","anonyComment":false,"adopted":false,"atUsers":"","featureComment":0}',
              author: {
                userId: 2496541295,
                name: "shallowlove",
                icon:
                  "https://cdn.cnbj1.fds.api.mi-img.com/middle.community.vip.bkt/49f5b19a3fd3e71625dcf0f1790cf56d",
                time: 0,
                identified: false,
                pinnedBadgeIcon: "",
                pendants: [],
                hasVipRight: false,
                postSource: "",
                vipType: -1
              },
              userId: 2496541295,
              subjectId: "24641022",
              supportNum: 10,
              time: 1613115007224,
              support: false,
              ownComment: false,
              isAdmin: 0,
              top: false,
              feature: false,
              count: 0,
              sourceUserId: 0,
              sorted: false,
              deviceType: "Redmi K30 至尊纪念版",
              anonyComment: false,
              adopted: false
            },
            {
              show: false,
              commentId: "69:24641022:9223370423752056906:14414",
              text: "新年快乐",
              extra:
                '{"product":"dipper","model":"MI 8","anonyComment":false,"adopted":false,"atUsers":"","featureComment":0}',
              author: {
                userId: 943796397,
                name: "Mi_红潮雪浪醉千寻",
                icon:
                  "https://cdn.cnbj1.fds.api.mi-img.com/middle.community.vip.bkt/49f5b19a3fd3e71625dcf0f1790cf56d",
                time: 0,
                identified: false,
                pinnedBadgeIcon:
                  "https://ts.market.mi-img.com/download/MiVip/0c5bf4999e6a1671e4f6a60c51cdac035da42f4e3",
                pendants: [],
                hasVipRight: false,
                postSource: "",
                vipType: -1
              },
              userId: 943796397,
              subjectId: "24641022",
              supportNum: 7,
              time: 1613102718901,
              support: false,
              ownComment: false,
              isAdmin: 0,
              top: false,
              feature: false,
              count: 0,
              sourceUserId: 0,
              sorted: false,
              deviceType: "小米8",
              anonyComment: false,
              adopted: false
            }
          ],
          count: 31,
          sourceUserId: 0,
          sorted: false,
          deviceType: "_小米10 至尊纪念版",
          anonyComment: false,
          adopted: false
        },
        {
          show: false,
          commentId: "69:24641022:9223370424155521452:9490",
          text:
            "MIUI稳定性那个问题雷总避而不谈，说明小米团队肯本就没有打算实现MIUI的稳定性这一实际问题",
          extra:
            '{"product":"venus","model":"Mi 11","anonyComment":false,"adopted":false,"atUsers":"","featureComment":0}',
          author: {
            userId: 1477696082,
            name: "Mi_Indulge",
            icon:
              "https://cdn.cnbj1.fds.api.mi-img.com/middle.community.vip.bkt/4cf423bb5923596a6eff2cf98d98c78e",
            time: 0,
            identified: false,
            pinnedBadgeIcon:
              "https://ts.market.mi-img.com/download/MiVip/0181a464e26eb37a0e065df4635e81e538c42f13e",
            pendants: [],
            hasVipRight: false,
            postSource: "",
            vipType: -1
          },
          userId: 1477696082,
          subjectId: "24641022",
          supportNum: 376,
          time: 1612699254355,
          support: false,
          ownComment: false,
          isAdmin: 0,
          top: false,
          feature: false,
          reply: [
            {
              show: false,
              commentId: "69:24641022:9223370423754851872:13778",
              text:
                "却是如此MIUI的稳定性确实差，系统bug问题太多了必须要解决这些问题啊",
              extra:
                '{"product":"dipper","model":"MI 8","anonyComment":false,"adopted":false,"atUsers":"","featureComment":0}',
              author: {
                userId: 1420786283,
                name: "米粉宝可梦",
                icon:
                  "https://cdn.cnbj1.fds.api.mi-img.com/middle.community.vip.bkt/e4ee8dbd1b80ce6053c2a67251ac1421",
                time: 0,
                identified: false,
                pinnedBadgeIcon:
                  "https://ts.market.mi-img.com/download/MiVip/06d8a4b1a14dbe4db472e2d1b903541384840390d",
                pendants: [],
                hasVipRight: false,
                postSource: "",
                vipType: -1
              },
              userId: 1420786283,
              subjectId: "24641022",
              supportNum: 8,
              time: 1613099923935,
              support: false,
              ownComment: false,
              isAdmin: 0,
              top: false,
              feature: false,
              count: 0,
              sourceUserId: 0,
              sorted: false,
              deviceType: "小米8",
              anonyComment: false,
              adopted: false
            },
            {
              show: false,
              commentId: "69:24641022:9223370423831168793:18440",
              text: "洪峰怎么出走的",
              extra:
                '{"product":"umi","model":"Mi 10","anonyComment":false,"adopted":false,"atUsers":"","featureComment":0}',
              author: {
                userId: 53953100,
                name: "听不见的风",
                icon:
                  "https://cdn.cnbj1.fds.api.mi-img.com/middle.community.vip.bkt/84c7764aed9fbd3a56a7b6a77584cd77",
                time: 0,
                identified: false,
                pinnedBadgeIcon:
                  "https://ts.market.mi-img.com/download/MiVip/07d025d7d421089702a2dea72f04b67c74d42ba23",
                pendants: [],
                hasVipRight: false,
                postSource: "",
                vipType: -1
              },
              replier: {
                userId: 74158981,
                name: "Mi_74158981",
                icon: "",
                time: 0,
                identified: false,
                pinnedBadgeIcon: "",
                pendants: [],
                hasVipRight: false,
                postSource: "",
                vipType: -1
              },
              userId: 53953100,
              subjectId: "24641022",
              supportNum: 7,
              time: 1613023607014,
              support: false,
              ownComment: false,
              isAdmin: 0,
              top: false,
              feature: false,
              count: 0,
              sourceId: "69:24641022:9223370423921839391:12257",
              sourceUserId: 74158981,
              sorted: false,
              deviceType: "小米10",
              anonyComment: false,
              adopted: false
            }
          ],
          count: 56,
          sourceUserId: 0,
          sorted: false,
          deviceType: "小米11",
          anonyComment: false,
          adopted: false
        }
      ],
      author: {},
      tags: [],
      publishTime: 1615201410185,
      contentData: {}
    };
  },
  computed: {},
  methods: {
    changeTimeStamp: function(timeStamp) {
      return new Date(timeStamp).toLocaleDateString();
    }
  },
  created() {
    let type;
    if (this.$route.name === "ArticleDetail") {
      type = 0;
    } else if (this.$route.name === "IdeaDetail") {
      type = 1;
    } else {
      type = 2;
    }
    this.axios
      .get("/post", {
        params: {
          type: type,
          id: this.$route.params.id
        }
      })
      .then(
        function(res) {
          this.author = {
            avatarUrl: res.data.contain.avatarUrl,
            nickName: res.data.contain.nickName
          };
          this.tags = res.data.contain.tags;
          this.publishTime = Number(res.data.contain.createTime);
          if (type === 0) {
            this.contentData = {
              articleContent: res.data.contain.articleContent
            };
          } else if (type === 1) {
            this.contentData = {
              pics: res.data.contain.pics,
              ideaContent: res.data.contain.ideaContent
            };
          } else {
            this.contentData = {
              videoUrl: res.data.contain.videoUrl
            };
            console.log("contentData", this.contentData);
          }
        }.bind(this)
      )
      .catch();
  }
};
</script>

<style lang="less" scoped>
@import "~@/assets/css/common.less";
@import "~@/assets/css/varibale.less";

.page-container {
  display: grid;
  grid-template-columns: 10% 45% 25% 5%;
  grid-template-rows: 10fr 1fr;
  grid-row-gap: 1%;
  grid-column-gap: 5%;
  .article-card {
    margin-top: 20px;
    grid-row-start: 1;
    grid-row-end: 2;
    grid-column-start: 2;
    grid-column-end: 3;
    .content {
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      margin-bottom: 20px;
      &-header {
        display: flex;
        flex-direction: row;
        justify-content: flex-start;
        align-items: center;
        padding: 20px 0 20px 0;
        &-avatar {
        }
        &-info {
          display: flex;
          flex-direction: column;
          justify-content: space-between;
          align-items: center;
          margin-left: 10px;
        }
      }
      &-body {
        margin-bottom: 20px;
      }
      &-footer {
        display: flex;
        justify-content: space-between;
        align-items: center;
        &-btn {
          display: flex;
          justify-content: space-between;
          align-items: center;
        }
      }
      .image-list {
        display: flex;
        justify-content: flex-start;
        align-items: center;
        padding: 10px 0 10px 0;
        .image-box {
          margin: 0 5px 0 5px;
        }
        .image-picked {
          margin: 0 3px 0 3px;
          border: 2px solid RoyalBlue;
        }
      }
    }
    .title {
      font-size: @default-font*3;
      margin: 20px 0 5px 0;
    }

    .comment,
    .comment-reply {
      &-footer {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        align-items: center;
      }
      &-header {
        padding-top: 10px;
        &-name {
          padding-left: 10px;
          color: black;
        }
      }
      .comment-reply-input {
        padding: 0 40px 0 40px;
      }
    }

    .comment {
      .comment-header {
        padding-top: 20px;
      }
      .comment-body {
        padding: 20px 20px 20px 50px;
        font-size: @default-font;
      }
    }

    .comment-reply {
      margin: 0 30px 26px 30px;
      padding: 0 20px 0 20px;
      font-size: @default-font*0.9;
      color: gray;
      background: rgba(0, 0, 0, 0.1);
      border-radius: 10px;

      .comment-reply-body {
        padding: 0 0 20px 40px;
      }
      .comment-reply-footer {
        justify-content: flex-start;
      }
    }
  }
}
</style>
