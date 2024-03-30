<script setup>
import { ref, onBeforeMount } from 'vue';
import { useRoute } from 'vue-router';
import UserTopbar from '@/components/topBar/UserTopbar.vue';

const token = ref(sessionStorage.getItem('MusicalToken'))
const route = useRoute()
const logged = ref(false)
const album_data = ref('')
let songs = ref([])

onBeforeMount(async()=>{
    if (token.value){
        logged.value = true
    }
    const album_id = route.params.id
    const response = await fetch(`http://127.0.0.1:5000/api/v1/album?album_id=${album_id}`,{
        headers:{
            "Content-Type":"application/json",
        }
    })
    album_data.value = await response.json()
    songs.value = album_data.value.songs
})



</script>


<template>
    <UserTopbar :logged="logged" />
    <h1 class="text-white">{{ album_data.name }}</h1>
    <div class="row justify-content-center ">
        <div class="col-auto " style="width: 70vw; ">
            <table class="table table-dark table-striped  table-bordered table-ce">
                <tr class="text-center ">
                    <th>#</th>
                    <th class="p-2">Name</th>
                    <th>Playbacks</th>
                </tr>
                <tr v-for="(song, index) in songs" :key="index" class="p-4 ">
                    <td>{{ index + 1 }}</td>
                    <td class="p-2"><router-link :to="`/song/${song.song_id}`" class="p-1">{{ song.song_name }}</router-link></td>
                    <td>{{ song.playback_count }}</td>
                </tr>

            </table> 
        </div>
    </div>

</template>

<style scoped>
a{
    text-decoration: none;
}
</style>