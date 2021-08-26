<template>
  <div class="box login-box" id="login" v-show="showPage">
    <div class="light-heading"> <h3 align="left" padding-left="20"> Login </h3> </div> <br>
    <label type="text">Enter username: </label>
    <input type="text" v-model="data.username" name="uId"><br><br>

    <label type="text">Enter password: </label>
    <input type="password" v-model="data.password" name="uId"><br><br>

    <button @click="login"> Login </button><br><br>
    <button @click="signUp"> Sign Up </button><br><br>
  </div>
</template>

<script>

export default {
    name: "Login",
    components: {
    },
    props: {
        data: Object,
        login: Function,
        signUp: Function,
        showPage: Boolean
    },

    methods: {

    }
}
</script>

<style scoped>
h3 {
  padding-left: 20%;
}

.login-box {
  width: 50%;
}
</style>