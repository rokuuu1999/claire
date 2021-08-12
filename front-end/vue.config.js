module.exports = {
  transpileDependencies: ["vuetify"],
  devServer: {
    port: 8090, //修改服务端口号
    proxy: "http://localhost:8080"
  }
};
