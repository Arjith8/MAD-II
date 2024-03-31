<script setup>
import { ref, onBeforeMount } from 'vue';
import AdminTopbar from '@/components/topBar/AdminTopbar.vue';
import { useRouter } from 'vue-router';

const token = ref(sessionStorage.getItem('MusicalToken'))
const user_retention = ref('')
const songs = ref([])
const creators = ref([])
const albums = ref([])
const router = useRouter()

async function deleteAlbum(album_id){
    const response = await fetch(`http://127.0.0.1:5000/api/v1/album?album_id=${album_id}`, {
        method: 'DELETE',
        headers: {
            "Authorization": `${token.value}`,
            "Content-Type": "application/json"
        },

    })
    const data = await response.json()
    console.log(data)

    if (data.success){
        alert('Album deleted successfully')
        router.go()
    }
    else{
        alert('Album could not be deleted')
    }
}

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
    console.log(data)

    if (data.success){
        alert('Song deleted successfully')
        router.go()
    }
    else{
        alert('Song could not be deleted')
    }
}


onBeforeMount(async () => {
    const response = await fetch('http://127.0.0.1:5000/api/v1/admin_dashboard', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': token.value
        }
    })
    const data = await response.json()
    user_retention.value = data.user_retention
    songs.value = data.songs
    creators.value = data.creators
    albums.value = data.albums
    console.log(data)
})

console.log(songs)
</script>

<template>
    <AdminTopbar />
    <h1 class="py-4 text-white">ADMIN DASHBOARD </h1>
    <div class="row mx-4 text-white">

        <div class="col-3 text-center " style="background-color: rgba(255, 255, 255, 0.158)">
            <h2 class="fs-2 pt-4">User Retention</h2><br>
            <p v-if="user_retention>50" class="text-success " style="font-size: 7.5rem;">{{user_retention}}%</p>
            <p v-else class="text-danger " style="font-size: 7.5rem;">{{user_retention}}%</p>
        </div>

        <div class="col-3 ms-3 text-center pe-5" style="background-color: rgba(255, 255, 255, 0.158)">

            <router-link :to="`/song/${songs[0].song_id}`"><img class="pt-3" :src="`/song/${songs[0].song_id}.jpg`" style="width: 13rem;" alt="{{songs[0].song_name}}" ></router-link>
            <p class="text-white text-center m-1 mb-0 fs-2 pb-2">{{songs[0].song_name}}</p>

        </div>

        <div class="col" style="background-color: rgba(255, 255, 255, 0.158)">

            <h2 class="text-center pt-3">OVERVIEW</h2>
            <p><span class="text-white-50 ">Most Popular Song : </span>{{songs[0].song_name}}</p>
            <p><span class="text-white-50 ">Most Popular Creator : </span>{{creators[0].username}}</p>
            <p><span class="text-white-50 ">Total Number of Songs : </span>{{songs.length}} </p>
            <p><span class="text-white-50 ">Total Number of Creators : </span> {{creators.length}} </p>
            <p><span class="text-white-50 ">Total Number of Albums : </span>{{albums.length}}</p>
        </div>
        
    </div>
    <div class="row mt-3 mx-4 text-white" style="">
        <h2 class="py-2">CREATOR ANALYTICS</h2>
        <table class="table table-dark table-striped  table-bordered  m-auto ">
            <tr class="text-center ">
                <th class="p-2">#</th>
                <th>Name</th>
                <th>Total Songs</th>
                <th>Total Playbacks</th>
                <th>Top Song</th>
                <th>Avg. Rating</th>
            </tr>

            <tr v-for="(i, index) in creators" class="text-center ">
                <td class="text-center p-2">{{index+1}}</td>
                <td><router-link :to="`/creator/${i.singer_id}`">{{i.username}}</router-link></td>
                <td>{{i.song_count}}</td>
                <td>{{i.total_playback_count}}</td>
                <td><router-link :to="`/song/${i.best_song_id}`">{{i.best_song}}</router-link></td>
                <td>{{ i.average_rating }}</td>
            </tr>
        </table>
    </div>
    <div class="row mt-3 mx-4 text-white" style="">
        <h2 class="py-2">ALBUM ANALYTICS</h2>
        <table class="table table-dark table-striped  table-bordered  m-auto ">
            <tr class="text-center ">
                <th class="p-2">#</th>
                <th>Album Name</th>
                <th>Genre</th>
                <th>Singer Name</th>
                <th>Playbacks</th>
                <th>Avg. Rating</th>
                <th>Delete</th>
            </tr>
            
            <tr v-for="(j,index) in albums" class="text-center ">
                <td class="text-center p-2">{{index+1}}</td>
                <td><router-link :to="`/album/${j.album_id}`">{{j.album_name}}</router-link></td>
                <td>{{j.genre}}</td>
                <td><router-link :to="`/creator/${j.singer_id}`">{{j.singer_name}}</router-link></td>
                <td>{{j.total_playbacks}}</td>
                <td>{{j.average_rating}}</td>
                <td><button class="btn btn-danger" @click="deleteAlbum(j.album_id)">Delete</button></td>
            </tr>
        </table> 
    </div>
    <div class="row mt-3 mx-4 text-white" style="">
        <h2 class="py-2">SONG ANALYTICS</h2>
        <table class="table table-dark table-striped  table-bordered  m-auto ">
            <tr class="text-center ">
                <th class="p-2">#</th>
                <th>Song Name</th>
                <th>Release Date</th>
                <th>Singer Name</th>
                <th>Playbacks</th>
                <th>Avg. Rating</th>
                <th>Delete</th> 
            </tr>

            <tr v-for="(k,index) in songs" class="text-center " >
                <td class="text-center p-2">{{index+1}}</td>
                <td><router-link :to="`/song/${k.song_id}`">{{k.song_name}}</router-link></td>
                <td>{{k.release_date}}</td>
                <td><router-link :to="`/creator/${k.singer_id}`">{{k.singer_name}}</router-link></td>
                <td>{{k.playback_count}}</td>
                <td>{{k.rating}}</td>
                <td><button class="btn btn-danger" @click="deleteSong(k.song_id)">Delete</button></td>
            </tr>
        </table> 
    </div>
</template>
    
<style scoped>
a{
    text-decoration: none;
}
</style> 