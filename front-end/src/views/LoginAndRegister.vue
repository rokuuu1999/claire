<template>
  <div class="full-size login-page">
    <v-card class="login-page-card">
      <div class="banner-container">
        <v-card class="input-banner" color="primary">
          <div class="banner-title">Login</div>
          <div class="third-party">
            <template v-for="(thirdPartyName, index) in thirdParty">
              <v-btn :key="index" depressed text fab small color="white">
                <v-icon dark>
                  {{ "mdi-" + thirdPartyName }}
                </v-icon>
              </v-btn>
            </template>
          </div>
        </v-card>
      </div>
      <div class="input-container">
        <template v-for="(item, index) in items">
          <BaseInput
            :title="item.title"
            :icon="item.icon"
            :key="index"
          ></BaseInput>
        </template>
      </div>
      <div class="button-container">
        <v-btn depressed tile width="50%">
          Register
        </v-btn>
        <v-btn depressed tile color="primary" width="50%">
          Submit
        </v-btn>
      </div>
    </v-card>
  </div>
</template>

<script>
import BaseInput from "@/components/BaseInput";

export default {
  name: "LoginAndRegister",
  components: {
    BaseInput
  },
  data() {
    return {
      items: [
        { title: "Name", icon: "account-circle" },
        { title: "Email", icon: "at" },
        { title: "Password", icon: "lock" }
      ],
      thirdParty: ["wechat", "qqchat", "github"]
    };
  },
  methods: {
    login: function() {},
    register: function() {}
  }
};
</script>

<style lang="less" scoped>
@import "~@/assets/css/common";
@import "~@/assets/css/varibale";

.login-page {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;

  .login-page-card {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
    width: 25%;
    height: 45%;

    .banner-container {
      display: block;
      width: 100%;
      height: 15%;
      .input-banner {
        position: absolute;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        width: 90%;
        height: 40%;
        top: -30%;
        left: 5%;
        .banner-title {
          margin-bottom: 10%;
          color: white;
          font-size: @default-font*1.5;
        }
        .third-party {
          position: absolute;
          display: flex;
          flex-direction: row;
          justify-content: space-around;
          align-items: center;
          width: 100%;
          bottom: 5%;
        }
      }
    }

    .input-container {
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      align-items: center;
      width: 100%;
      height: 60%;
    }
    .button-container {
      display: flex;
      flex-direction: row;
      justify-content: space-around;
      align-items: center;
      width: 90%;
      height: 20%;
    }
  }
}
</style>
