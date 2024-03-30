<script setup>
import UserTopbar from '../topBar/UserTopbar.vue';
import { onBeforeMount, ref } from 'vue';
import { useRoute } from 'vue-router';

const logged = ref(false)
const token = ref(localStorage.getItem('token'))
const data = ref({})
const router = useRoute()
const lyrics_id = router.params.id


onBeforeMount(async() => {
    if (token.value) {
        logged.value = true
    }
    const response = await fetch(`http://127.0.0.1:5000/api/v1/lyrics?lyrics_id=${lyrics_id}`, {
        headers: {
            'Content-Type': 'application/json'
        }
    })
    data.value = await response.json()
    console.log(data.value)
})

</script>

<template>
    <UserTopbar :logged="logged"/>
    <div class="row justify-content-center " style="height: 91.8vh; opacity: 95%;">
        <div class="col-auto px-4 rounded-2 text-center "style=" background-color: #525452;">
            <h1 class="text-white ">{{data.lyrics_name}}</h1>
            <p class="text-white ">Creator Name : <router-link class="text-white" :to="`/creator/${data.creator_id}`">{{data.creator_name}} </router-link></p>
            <iframe class="bg-black" style="width:34rem;height:35.2rem ; opacity: 70%;" :src="`/raw_lyrics/${lyrics_id}.txt`" frameborder="" scrolling="auto"></iframe>
        </div>
    </div>
</template>