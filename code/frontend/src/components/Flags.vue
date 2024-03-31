<script setup>
import { ref, onBeforeMount } from 'vue';
import AdminTopbar from '@/components/topBar/AdminTopbar.vue';

const token = ref(sessionStorage.getItem('MusicalToken'))
const songs = ref([])
onBeforeMount(async () => {
    const response = await fetch('http://127.0.0.1:5000/api/v1/flag', {
        headers: {
            "Authorization": `${token.value}`
        }
    })
    const data = await response.json()
    console.log(data)
    songs.value = data
    console.log(songs.value)
})


async function deleteSong(song_id){
    const response = await fetch("http://127.0.0.1:5000/api/v1/song_operation", {
        method: 'DELETE',
        headers: {
            "Authorization": `${token.value}`,
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            "song_id": song_id
        })
    })
    const data = await response.json()

    if (data.success){
        alert('Song deleted successfully')
        router.go()
    }
    else{
        alert('Song could not be deleted')
    }
}

</script>

<template>
    <AdminTopbar/>
    <div class="row mt-3 mx-4" style="">
        <h2 class="py-2">FLAGGED SONGS</h2>
        <table class="table table-dark table-striped  table-bordered  m-auto ">
            <tr class="text-center ">
                <th>#</th>
                <th class="p-2">Song Name</th>
                <th>Released On</th>
                <th>Playback Count</th>
                <th>Flags</th>
                <th>Delete</th>
            </tr>
            <tr v-for="(song,index) in songs" :key="index" class="text-center">
                <td class="p-2">{{index+1}}</td>
                <td><router-link :to="`/song/${song.song_id}`" class="text-white ">{{song.song_name}}</router-link></td>
                <td>{{song.release_date}}</td>
                <td>{{song.playback_count}}</td>
                <td>{{song.flags}}</td>
                <td  class="text-center "><button @click="deleteSong(song.song_id)" class="btn btn-danger  ">Delete</button></td>
            </tr>
        </table>
    </div>
</template>