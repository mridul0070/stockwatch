<template>
    <div class="box">
      <!-- <div class="grid-container" v-bind:key="stock.id" v-for="stock in stocksData">
        <div class="grid-item">{{stock.name}}</div>
        <div class="grid-item">{{stock.code}}</div>
        <div class="grid-item"> {{stock.price}}</div>
        <div class="grid-item"><button @click="delStock(stock.id)">Delete</button></div>
         <div class="grid-container">empty line</div>
      </div> -->

       <div class="watchlist">
     <div>
    <div v-show="(!showAddStock)"><button @click="add">Add Stock</button></div>
    <div v-show="showAddStock">
      <h3>Add Stock</h3>
      <label type="text">Enter stock name</label>
      <input type="text" v-model="saveNewData.name"/><br><br>
      <label type="text">Enter stock code</label>
       <input type="text" v-model="saveNewData.code"/><br><br>
       <label type="text">Enter stock price</label>
       <input type="text" v-model="saveNewData.price"/><br><br>
       <button @click="saveStock">Save</button>
       <button @click="cancelSave">Cancel</button>
    </div>
     </div>
    <br><br>
    <div style="text-align: right"> Sort By<select v-model="sortBy" @change="loadPage(1)" >
                        <option disabled value="sortBy ">{{sortBy}}</option>
                        <option value="ID">ID</option>
                        <option value="CODE">Code</option>
                        <option value="PRICE">Price</option>
                    </select>
</div>
<br><br>
    <div class="box" >
     <div class="grid-container"   >
           <div class="grid-item">Name</div>
            <div class="grid-item">Code</div>
           <div class="grid-item"> Price</div>
         <div class="grid-item">Delete</div>
        
        </div>
     <div class="grid-container" v-bind:key="stock.id" v-for="stock in stocksData" >
           <div class="grid-item">{{stock.name}}</div>
            <div class="grid-item">{{stock.code}}</div>
           <div class="grid-item"> {{stock.price}}</div>
         <div class="grid-item"><button @click="delStock(stock.id)" >Delete</button></div>
         
        </div>
       
    </div>

    </div>
      <div class="pagination">
        <a href="#">&laquo;</a>
        <div v-bind:key="page" v-for="page in pages">
          <a @click="loadPage(page)"> {{page}} </a>
        </div>
        <a href="#">&raquo;</a>

        
      </div>
      <div class="logoutbutton" v-show="tableVis"><button @click="logout">Logout</button></div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Stocks',
  

  components: {
    
  },

  props: {
    apiRoute: String,
    userId: [Number, String],
    logout: Function

  },

  data() {
    return {
      stocksData : [],
      pages: 0,
      pageSize: 11,
      sortBy: 'id',

      showAddStock: false,
      
      
      
      
      saveNewData: {
        id:0,
        name:'',
        code:'',
        price:'',
      },

      
    
    }

  },

  mounted() {
  console.log("mpunted")
  this.onCreate()
  },

  methods: {
    onCreate() {
      console.log(this.userId)
      axios.get(this.apiRoute + 'getCount?userId=' + this.userId.toString())
      .then(res => {
        if (res.data.RESULT > 0) {
          this.pages = Math.ceil(res.data.RESULT/this.pageSize);
          this.loadPage(1)
        }
      })
      .catch(err => console.log(err));
    },

    loadPage(pageNo) {
      this.visibility=true
      this.tableVis=true
      this.sortVis=true
      var offset = (pageNo-1) * this.pageSize;

      axios.get(this.apiRoute + 'getStocksPage?sortBy=' + this.sortBy + '&quantity=' + this.pageSize + '&offset=' + offset + '&userId=' + this.userId)
      .then(res => {
        this.pages = Math.ceil(res.data.SIZE/this.pageSize);
        this.parseStockData(res.data.RESULT);
      })
      .catch(err => console.log(err));
    },

    parseStockData(pageData) {
      console.log(pageData)
        this.stocksData = []
        for (var i in pageData) {
          const item = {
            id: pageData[i]['id'],
            name: pageData[i]['name'],
            code: pageData[i]['code'],
            price: pageData[i]['price']
          }
          this.stocksData.push(item);
        }
        console.log(this.stocksData)
    },

    resetForm(){
        this.saveNewData.name = ''
        this.saveNewData.code = '' 
        this.saveNewData.price = ''
    },

    // logout(){

    //   this.visibility=false
    //   this.sortVis=false
    //   this.tableVis=false
    //   // this.stocksData.name=''
    //   // this.stocksData.code=''
    //   // this.stocksData.price=''





   // },

    add(){
      this.showAddStock = true 

    },

    saveStock(){
      const item = {
        userId: this.userId,
        name: this.saveNewData.name,
        code: this.saveNewData.code,
        price: this.saveNewData.price,
      }
      if(item.name==''||item.code==''||item.price==0){
        alert("enter all fields")
        return
      }
      axios.post(this.apiRoute + 'appendStock', item)
      .then(res => {
        console.log(res)
        this.loadPage(1)
        //this.stocksData.push(item)
        this.showAddStock = false
        this.resetForm()
      })
      .catch(err => console.log(err));
      

    },

    cancelSave(){
     this.showAddStock = false 
     this.resetForm();
    },

    delStock(id) {

       const item = {
        userId: this.userId,
        id: id,
        name: this.saveNewData.name,
        code: this.saveNewData.code,
        price: this.saveNewData.price,
      }

      axios.post(this.apiRoute + 'delStock' ,item)
      .then(res => {
        console.log(res)
        for(var i in this.stocksData){
      if(this.stocksData[i].id==id)
      { 
         this.stocksData.splice(i,1)
      break
      }

    }

             
      }
      
      
      
      )
      

    }
  }
}
</script>

<style>



</style>
