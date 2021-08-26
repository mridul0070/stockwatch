<template>
  <div id="app">
    <h1>Stock Watchlist</h1>

    <Login v-bind:data="formData" v-bind:login="authenticate" v-bind:signUp="signUpView" v-bind:showPage="showLoginPage"/>
    <SignUp v-bind:data="formData" v-bind:signUp="saveNewUser" v-bind:showPage="showSignUp" v-bind:loginPage="logInstead"/>
    <Stocks v-if="loadStocks" v-bind:userId="userData.id" v-bind:apiRoute="apiRoute" v-bind:logout="logOut" v-show="showWatchlist" ref="childRef"/>
    
  </div>
</template>

<script>
import axios from 'axios'
import Login from '@/components/Login.vue'
import SignUp from '@/components/SignUp.vue'
import Stocks from '@/components/Stocks.vue'

export default {
  name: 'App',
  components: {
    Login,
    SignUp,
    Stocks,
    
  },

  data(){
    return{
      
      loadStocks:false,

       formData: {
        id:0,
        username: '',
        name:'',
        password:'',
      },

      userData: {
        id:0,
        username: '',
        name: '',
      },

      showLoginPage: true,
      showSignUp: false,
      showWatchlist:false,
      apiRoute:'https://stockbackend2.herokuapp.com/'

    }
  },

  mounted() {
     
    

  },
  methods: {

    resetAllData() {
      this.userData = {
        id: 0,
        username: '',
        name: '',
      },

      this.formData = {
        id: 0,
        userData: '',
        name: ''
      }

      this.resetStockPage()

    },

    resetStockPage()
    {
      this.stocksData.id = ''
      this.stocksData.name=''
      this.stocksData.code=''
      this.stocksData.price=''
      this.visibility=false 
    },

    logInstead(){

      this.showLoginPage= true
      this.showSignUp= false
    },
    








    signUpView() {
      this.showLoginPage = false;
      this.showSignUp = true; 
    },

    saveNewUser() {
      const request = {'username': this.formData.username, 'name': this.formData.name, 'password': this.formData.password}
      axios.post(this.apiRoute + 'register', request)
      .then(res => {
        if (res.data.RESULT == 'Ok') {
          console.log('Success');
          this.showSignUp = false;
          this.showLoginPage = true;
        }
        else {
          this.userMessage = 'Failed';
        }
      })
    },

    getUser(username) {
      axios.get(this.apiRoute + 'getUser/' + '?username=' + username)
      .then(res => {
        console.log(res.data.ID)
        this.userData.id = res.data.ID
        console.log(this.userData.id)
        this.userData.username = res.data.USERNAME
        this.userData.name = res.data.NAME
        this.loadStocks= true
        //this.$refs.childRef.onCreate()
      })
    },

    


    

    

    

    

    // getNewId(){
    //   var result = 0;
    //   for(var i in this.allStock){
    //     if(this.allStock[i].id > result)
    //     result = this.allStock[i].id
    //   }
    //   return(result+1)
     
    // },

    // syncData(){
    //     console.log(this.allStock)
    //    localStorage.setItem("data", JSON.stringify(this.allStock)); 
    // },

   

    signUp(){
      this.showLoginPage = false
      this.showSignUp= true
    },

    authenticate(){
     console.log("frontend auth called")
      axios.get(this.apiRoute + 'auth?username=' + this.formData.username + '&pass=' + this.formData.password)
      .then(res => {
        console.log(res.data)
        if (res.data.RESULT == 'Success') {
          console.log("success login")
          this.getUser(this.formData.username)
          this.showLoginPage=false
          this.showWatchlist=true
        }
        else if (res.data.RESULT == 'No_User'){
          this.userMessage = 'User not found, sign up instead?';
        }
        else {
          this.userMessage = 'Wrong Password';
        }
      })
      .catch(err => console.log(err));
   
    },
    
    logOut(){
      this.showWatchlist = false;
      this.showLoginPage = true;
      
    },

  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}



.grid-container {
    display: grid;
    grid-template-columns: auto auto auto auto;
    margin-left: auto;
    margin-right: auto;
    min-width: 300px;
    max-width:800px;
    overflow: auto;
    border: 1px solid black;
    text-align: center;
}

.grid-item {
  
  font-size: 15px;
  text-align: center;
  width: 50px;
 padding: 2%;
}


</style>
