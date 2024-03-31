<script setup>
import { onBeforeMount, ref } from 'vue';
import UserTopbar from '@/components/topBar/UserTopbar.vue';


const token = ref(sessionStorage.getItem('MusicalToken'))
const data = ref({})
onBeforeMount(async()=>{
    function splitIntoBatches(data) {
        const batches = [];
        for (let i = 0; i < data.length; i += 5) {
            const batch = data.slice(i, i + 5);
            batches.push(batch);
        }
        return batches;
    }
    const response = await fetch(`http://127.0.0.1:5000/api/v1/playlists?playlist_count=100`,{
        headers:{
            "Authorization":`${token.value}`
        }}
    )
    data.value = await response.json()
    console.log(data.value)
    data.value = splitIntoBatches(data.value)
})

</script>

<template>
    <UserTopbar :logged="token" />
    <div>

    <h1 class="p-2 text-white ">PLAYLISTS</h1>

        <div class="d-grid text-end px-1">
            <router-link :to="`/create_playlist`"><button class="btn btn-primary">Create Playlist</button></router-link>
        </div>

        <div class="row ">  
            <p v-show="!data.length" class="fs-2 p-2 text-white-50">You haven't created any playlists</p>
            <div v-for="(batch,index) in data" :key="index" class="row ms-4 me-4">
                <div v-for="(playlist,i) in batch" :key="i" class="p-2 col-2 bg-custom mx-2 my-1" style="width:auto">
                    <router-link :to="`/playlist/${playlist.id}`">
                        <img :src='`/playlist/${ playlist.id }.jpg`' style="width: 13rem;" :alt="`${ playlist.name }`">
                        <p class="text-white text-center m-1 mb-0">{{ playlist.name }}</p>
                    </router-link>
                </div>
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