<template>
  <div class="input-item">
    <v-text-field :label="title" :append-icon="'mdi-' + icon"></v-text-field>
  </div>
</template>

<script>
export default {
  name: "BaseInput",
  props: {
    title: {
      type: String,
      required: true
    },
    icon: {
      type: String,
      required: true
    }
  }
};
</script>

<style lang="less" scoped>
@import "~@/assets/css/common";
.input-item {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  width: 95%;
}
</style>
