<template>
  <div id="app"><img width="15%" src="./assets/logo.png" /> <Attachment /></div>
</template>

<script>
import Attachment from "./components/Attachment";

export default {
  name: "App",
  components: {
    Attachment
  }
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
