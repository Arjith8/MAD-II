<script setup>
import UserTopbar from '@/components/topBar/UserTopbar.vue';
import { useRoute } from 'vue-router';
import { onBeforeMount, ref } from 'vue';
const token = ref(sessionStorage.getItem('MusicalToken'))
const route = useRoute()
const path = route.params.path
const data = ref({})
const title = ref('')
console.log(path)

onBeforeMount(async() => {
    function splitIntoBatches(data) {
        const batches = [];
        for (let i = 0; i < data.length; i += 5) {
            const batch = data.slice(i, i + 5);
            batches.push(batch);
        }
        return batches;
    }
    if (path == 'creator' ){
        title.value = 'All Creators'
        const response = await fetch('http://localhost:5000/api/v1/creators?creator_count=100')
        data.value = await response.json()
        console.log(data.value)
    }
    else if (path == 'album' ){
        title.value = 'All Albums'
        const response = await fetch('http://localhost:5000/api/v1/albums?album_count=100')
        data.value = await response.json()
    }
    else if (path == 'song' ){
        title.value = 'All Songs'
        const response = await fetch('http://localhost:5000/api/v1/songs?song_count=100')
        data.value = await response.json()
    }
    
    data.value = splitIntoBatches(data.value)
    console.log(data.value)

})


</script>
<template>
    <UserTopbar :logged="token" />
    <h1 class="text-white">{{ title }}</h1>
    <div class="row text-white">
        <div v-for="(batch,index) in data" :key="index" class="row ms-4 me-4">
            <!-- {{ batch }} -->
            <div v-for="(value,i) in batch" :key="i" class="p-2 col-2 bg-custom mx-2 my-1">
                <!-- {{ value }} -->
                <router-link :to="`${path}/${value.id}`">
                    <img :src="`/${path}/${value.id}.jpg`" style="width: 13rem;" :alt="`${value.name}`">
                    <p class="text-white text-center m-1 mb-0">{{value.name}}</p>
                </router-link>
            </div>
        </div>
    </div>

</template>

<style scoped>

.bg-custom{
    width: 14rem;
    background-color: rgba(255, 255, 255, 0.158);
}
.bg-custom:hover{
    background-color: rgba(255, 255, 255, 0.058);
}
a{
    text-decoration: none;
}

</style>