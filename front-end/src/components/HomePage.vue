<template>
  <div class="full-size cards-container">
    <template v-for="(article, index) in articleList">
      <ArticleCard
        :hover="article.hover"
        :class="['page-card', 'card-' + (index + 1)]"
        :title="article.title"
        :sub-tile="article.subTitle"
        :author="article.author"
        :time="article.time"
        :tags="article.tags"
        :key="index"
      ></ArticleCard>
    </template>
    <Pagination class="pagination"></Pagination>
  </div>
</template>

<script>
import ArticleCard from "@/components/ArticleCard";
import Pagination from "@/components/Pagination";
export default {
  name: "HomePage",
  components: {
    ArticleCard,
    Pagination
  },
  data() {
    return {
      articleList: [
        {
          hover: false,
          title: "测试",
          subTitle: "第一篇测试",
          author: "siegelion",
          time: "2021/02/07 20:47",
          tags: ["测试", "测试", "测试", "测试"]
        },
        {
          title: "测试",
          subTitle: "第一篇测试",
          author: "siegelion",
          time: "2021/02/07 20:47",
          tags: ["测试", "测试", "测试", "测试"]
        },
        {
          title: "测试",
          subTitle: "第一篇测试",
          author: "siegelion",
          time: "2021/02/07 20:47",
          tags: ["测试", "测试", "测试", "测试"]
        },
        {
          title: "测试",
          subTitle: "第一篇测试",
          author: "siegelion",
          time: "2021/02/07 20:47",
          tags: ["测试", "测试", "测试", "测试"]
        },
        {
          title: "测试",
          subTitle: "第一篇测试",
          author: "siegelion",
          time: "2021/02/07 20:47",
          tags: ["测试", "测试", "测试", "测试"]
        }
      ]
    };
  }
};
</script>

<style lang="less" scoped>
@import "~@/assets/css/common";
.cards-container {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  grid-template-rows: 1fr repeat(5, 3fr) 2fr;
  grid-row-gap: 2%;

  .page-card {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: flex-start;
    width: 60vw;
    height: 30vh;
  }

  .loop(@counter) when(@counter<=7) {
    .card-@{counter} {
      grid-row-start: @counter+1;
      grid-row-end: @counter+2;
      grid-column-start: 2;
      grid-column-end: 3;
    }
    .loop((@counter+1));
  }
  .loop(1);

  .pagination {
    grid-row-start: 7;
    grid-row-end: 8;
    grid-column-start: 2;
    grid-column-end: 3;
    align-items: center;
    align-items: center;
  }
}
</style>
