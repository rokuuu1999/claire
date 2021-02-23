<template>
  <div class="full-size">
    <div v-for="(item, index) in focusTag" :key="index" style="height: 6%">
      <div class="row">
        <div class="user-info">
          <v-chip :color="randomColor()" text-color="white">
            <v-icon left> mdi-label </v-icon>{{ item.name }}
          </v-chip>
        </div>
        <div class="btn">
          <v-btn v-if="item.focus" block color="grey">已关注</v-btn>
          <v-btn v-if="!item.focus" block color="primary">关注</v-btn>
        </div>
      </div>
      <v-divider></v-divider>
    </div>
  </div>
</template>

<script>
import { randomColor } from "@/assets/js/GlobalFunction";

export default {
  name: "FocusTag",
  data() {
    return {
      focusTag: [
        {
          name: "第一个标签",
          focus: false
        },
        {
          name: "第一个标签",
          focus: true
        }
      ]
    };
  },
  methods: {
    randomColor: function() {
      return randomColor();
    }
  }
};
</script>

<style lang="less" scoped>
@import "~@/assets/css/common";
.row:extend(.flex-layout) {
  height: 100%;
  margin: 10px 20px 10px 20px;

  .user-info:extend(.flex-layout) {
    width: 20%;
    height: 100%;
  }

  .btn {
    width: 10%;
  }
}
</style>
