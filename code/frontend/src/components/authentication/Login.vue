
<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import AlertMessage from '../alertMessages/AlertMessage.vue';

const incorrect_creds=ref(false)
const username=ref("")
const password=ref("")
const msg=ref('')
const alert=ref(false)
const router = useRouter()

async function checkCredentials(){

    if (!username.value || !password.value){
        alert.value = true
        msg.value = "All the fields are mandatory please fill them"
        setTimeout(()=>{
            alert.value=false
        },3000)
        return
    }
    


    const response = await fetch("http://127.0.0.1:5000/api/v1/login",{
        method:"POST",
        headers:{
            "Content-Type":"application/json"
        },
        body: JSON.stringify({
            username:username.value,
            password:password.value
        })
    })
    
    const responseData = await response.json()
    if (!responseData.token){

        msg.value=responseData.msg
        alert.value=true
        setTimeout(()=>{
            alert.value=false
        },3000)

        return
    }
    incorrect_creds.value=false
    window.sessionStorage.setItem('MusicalToken',responseData.token)
    router.push('/')

    // Now i have to connect  to state management and push to index page

}

</script>

<template>
    <AlertMessage :message="msg" v-if="alert"/>
    <div v-if="incorrect_creds" class="text-white bg-danger p-2">{{msg}}</div>

    <div class="position-absolute top-50 start-50 translate-middle">

        <div  class="p-4 rounded rounded-5 bg-white text-center custom-width">

            <img class="p-4" src="../../assets/normal.png"  style="width: 220px;">
            <!-- <img v-else src="../assets/warning.png"  style="width: 240px;"> -->

            <!-- <h1 class="p-2 ">LOGIN</h1> --><br>

            <label for="user" class="form-label ">USERNAME :</label><br>
            <input type="text" v-model="username"  name="user" class="form-control border-dark-subtle" required /> <br />

            <label for="pass" class="form-label">PASSWORD :</label><br>
            <input type="password" v-model="password" name="pass" class="form-control border-dark-subtle" required /><br />

            <button class="text-center rounded-4 " id="login_button" @click="checkCredentials">LOGIN</button>
                        
        </div>

    </div>

</template>

<style scoped>
button{
    width: 7rem;
    height: 2.5rem;
    background-color: rgb(100, 247, 139);
    border: 2px solid #0AE043;
}
button:hover{
    background-color: #0AE043;
}
.custom-width{
    min-width: 23rem;
    min-height: 25rem;
}

</style>
