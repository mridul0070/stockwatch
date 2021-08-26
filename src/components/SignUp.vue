<template>
  <div class="box" id='signup' v-show='showPage'>
    <br>
    <label type="text">Enter username: </label>
    <input type="text" v-model="data.username" name="uId"><br><br>

    <label type="text">Enter name: </label>
    <input type="text" v-model="data.name" name="uId"><br><br>

    <label type="text">Enter password: </label>
    <input type="text" v-model="data.password" name="uId"><br><br>  

  <button @click="signUp"> Save new user </button> <br> <br> 
  <button @click="loginPage"> Login instead </button> <br><br>
  </div>
</template>

<script>

export default {
    name: "SignUp",
    components: {
    },
    props: {
        data: Object,
        signUp: Function,
        loginPage: Function,
        showPage: Boolean
    },

    methods: {

    }
}
</script>