
<script setup>
import { ref } from 'vue';

const incorrect_creds=ref(false)
const username=ref("")
const password=ref("")

function checkCredentials(){
    fetch("http://127.0.0.1:5000/api/login")
}

</script>

<template>
    <div class="position-absolute top-50 start-50 translate-middle">

        <div  class="p-4 rounded rounded-5 bg-white text-center custom-width">

            <img v-if="!incorrect_creds" src="../assets/Screenshot 2023-11-03 202133.png"  style="width: 250px;">
            <img v-else src="../assets/Screenshot 2023-11-03 231016.png"  style="width: 250px;">

            <h1 class="p-2 ">LOGIN</h1>

            <label for="user" class="form-label ">USERNAME :</label><br>
            <input type="text" v-model="username"  name="user" class="form-control border-dark-subtle" required /> <br />

            <label for="pass" class="form-label">PASSWORD :</label><br>
            <input type="password" v-model="password" name="pass" class="form-control border-dark-subtle" required /><br />

            <div v-if="incorrect_creds">
                <span class="d-flex custom-pb"></span>
                <p class="bg-danger bg-gradient py-2 ">Username or password was incorrect</p>
            </div>

            <button class="text-center rounded-4 " @click="checkCredentials">LOGIN</button>
                        
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
    min-width: 24rem;
    min-height: 29rem;
}
.custom-pb{
    padding-bottom: .5rem;

}
</style>
