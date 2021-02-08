<template>
  <div class="banner-container">
    <v-btn plain color="white">
      Community Demo
    </v-btn>
    <BaseInput
      :title="searchInfo.title"
      :icon="searchInfo.icon"
      :hideDetails="searchInfo.hideDetails"
      :rounded="searchInfo.rounded"
      :solo="searchInfo.solo"
      :dense="searchInfo.dense"
    ></BaseInput>
    <div class="banner-container banner-right ">
      <v-btn fab plain>
        <v-icon medium color="white">
          mdi-forum
        </v-icon>
      </v-btn>
      <v-btn fab plain>
        <v-icon medium color="white">
          mdi-account-circle
        </v-icon>
      </v-btn>
    </div>
  </div>
</template>

<script>
import BaseInput from "@/components/BaseInput";

export default {
  name: "AppBar",
  components: {
    BaseInput
  },
  data() {
    return {
      searchInfo: {
        title: "Search",
        icon: "magnify",
        hideDetails: true,
        rounded: true,
        solo: true,
        dense: true
      }
    };
  }
};
</script>

<style lang="less" scoped>
.banner-container {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  height: 100%;
  .banner-right {
    width: 8%;
  }
}
</style>
