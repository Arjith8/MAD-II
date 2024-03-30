<script setup>
import { onBeforeMount, ref } from 'vue';
import AlertMessage from '../alertMessages/AlertMessage.vue';
import UserTopbar from '../topBar/UserTopbar.vue';
import { useRouter } from 'vue-router';

const message = ref('')
const token = ref(sessionStorage.getItem('MusicalToken'))
const logged = ref(false)
const router = useRouter()
const user_data = ref({})
const dataShangeStatus = ref(true)

onBeforeMount(async()=>{
    const response = await fetch("http://127.0.0.1:5000/api/v1/user_data",{
        headers:{
            "Content-Type":"application/json",
            "Authorization":token.value
        }
    })
    const data = await response.json()
    if (!data.success){
        message.value = "Invalid Token, Redirecting to login page in 5 seconds"
        setTimeout(()=>{
            router.push('/login')
        },5000)
        return
    }
    logged.value = true
    user_data.value = data
})


async function sendUserDataChangeRequest(){
    const response = await fetch("http://127.0.0.1:5000/api/v1/user_data",{
        headers:{
            "Content-Type":"application/json",
            "Authorization":token.value
        },
        method:"POST",
        body:JSON.stringify({
            username:user_data.value.username,
            first_name:user_data.value.first_name,
            last_name:user_data.value.last_name,
            email:user_data.value.email
        })
    })
    
    const message = await response.json()
    console.log(message)
    if (!message.success){
        dataShangeStatus.value = false
        return
    }
    dataShangeStatus.value = true

}
</script>

<template>
    
    <UserTopbar :logged="logged" />
    <AlertMessage v-show="!logged" :message="message" />
    <div v-if="logged" class="row justify-content-center pt-5">
        <div class="col-auto bg-white rounded-5 p-3 " style="width: 40vw; min-height:60vh">
            <div>

                <h1 class="text-center ">User Profile</h1>

                <label for="firstname" class="form-label p-2" >Firstname :</label>
                <input type="text" name="firstname" class="form-control " v-model="user_data.first_name">

                <label for="lastname" class="form-label p-2">Lastname :</label>
                <input type="text" name="lastname" class="form-control"  v-model="user_data.last_name">
                <label for="username" class="form-label p-2">Username :</label>
                <input type="text" name="username" class="form-control"  v-model="user_data.username">
                <label for="email" class="form-label p-2">Email :</label>
                <input type="email" name="email" class="form-control"  v-model="user_data.email">
                
                <div class="row pt-5">
                    <div class="col">
                        <p v-if="dataShangeStatus==false" class="bg-danger p-2">Username already exists</p>
                        <button @click="sendUserDataChangeRequest" class="btn btn-primary float-end ">Save Changes</button>
                    </div>
                </div>
                
            </div>

        </div>
    </div>


</template>