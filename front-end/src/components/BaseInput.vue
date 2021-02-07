<template>
  <v-text-field
    class="input-item"
    :type="title.indexOf('Password') !== -1 ? 'password' : 'text'"
    :label="title"
    :append-icon="'mdi-' + icon"
    v-model="value"
  ></v-text-field>
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
  },
  data() {
    return {
      value: ""
    };
  },
  watch: {
    value: function(newVal) {
      this.$emit("change", newVal);
    }
  }
};
</script>

<style lang="less" scoped>
@import "~@/assets/css/common";
.input-item {
  width: 95%;
}
</style>
