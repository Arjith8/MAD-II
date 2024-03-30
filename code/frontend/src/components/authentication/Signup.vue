<script setup>
import AlertMessage from '../alertMessages/AlertMessage.vue';
import { useRouter } from 'vue-router';

import { ref } from 'vue';
const first_name = ref('')
const last_name = ref('')
const username = ref('')
const password = ref('')
const email = ref('')

const alert = ref(false)
const msg = ref("")
const router = useRouter()

async function sendData(){
    if (!first_name.value || !last_name.value || !username.value || !password.value){
        alert.value = true
        msg.value = "All the fields are mandatory please fill them"
        setTimeout(()=>{
            alert.value = false
        },3000)
        return
    }

    const response = await fetch("http://127.0.0.1:5000/api/v1/signup",{
        method:"POST",
        headers:{
            "Content-Type":"application/json"
        },
        body: JSON.stringify({
            first_name:first_name.value,
            last_name:last_name.value,
            username:username.value,
            email:email.value,
            password:password.value
        })
    })

    const body = await response.json()
    if (!body.token){
        alert.value = true
        msg.value = body.msg
        setTimeout(()=>{
            alert.value = false
        },3000)
        return
    }

    window.sessionStorage.setItem('MusicalToken',body.token)
    router.push('/')
}

</script>

<template>
<AlertMessage v-if="alert" :message="msg"/>

<div class="position-absolute top-50 start-50 translate-middle ">

    <div class="p-4 rounded rounded-5 bg-white text-center custom-width">
        <img src="../../assets/normal.png" style="width: 150px;">
        <h1 class="p-2">SIGN UP</h1>

        
        <label for="f_name" class="form-label p-2">FIRST NAME : </label>
        <input type="text" name="f_name" class="form-control border-dark-subtle " required v-model="first_name">


        <label for="l_name" class=" form-label p-2 ">LAST NAME : </label>
        <input name="l_name" type="text" class="form-control border-dark-subtle" required v-model="last_name">  
        

        <label for="user" aria-disabled="true" class="form-label p-2">USERNAME : </label>
        <input type="text" name="user" class="form-control border-dark-subtle" required v-model="username" /> 

        <label for="user" aria-disabled="true" class="form-label p-2">EMAIL : </label>
        <input type="text" name="user" class="form-control border-dark-subtle" required v-model="email" /> 

        <label for="pass" class="fs-6 form-label p-2">PASSWORD : </label>
        <input type="password" name="pass" class="form-control border-dark-subtle"  required v-model="password" /> <br>

        <button class="border border-primary btn btn-primary" @click="sendData">SIGN UP</button>
            
    </div>

</div>

</template>


<style scoped>
.custom-width{
    width: 26rem;
    min-height: 37rem;
}
.custom-pb{
    padding-bottom: .5rem;
}


</style>
