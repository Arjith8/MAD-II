<script setup>
import { ref, onBeforeMount } from 'vue';
import { useRouter } from 'vue-router';
import UserTopbar from '@/components/topBar/UserTopbar.vue';

const token = ref(sessionStorage.getItem('MusicalToken'))
const router = useRouter()
const data = ref({})
const best_song = ref({})
const playback_percentage = ref(0)
const total_playback_count = ref(0)
const rank = ref([])
const songs = ref({})
const albums =ref([])
const lyrics = ref([])

async function deleteSong(song_id){
    const response = await fetch("http://127.0.0.1:5000/api/v1/song_operations", {
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

async function deleteLyrics(lyrics_id){
    console.log(`http://127.0.0.1:5000/api/v1/lyrics?lyrics_id=${lyrics_id}`)
    const response = await fetch(`http://127.0.0.1:5000/api/v1/lyrics?lyrics_id=${lyrics_id}`, {
        method: 'DELETE',
        headers: {
            "Authorization": `${token.value}`,
            // "Content-Type": "application/json"
        },

    })
    const data = await response.json()
    console.log(data)

    if (data.success){
        alert('Lyrics deleted successfully')
        router.go()
    }
    else{
        alert('Lyrics could not be deleted')
    }
}

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


onBeforeMount(async ()=>{
    if (!token.value){
        router.push('/login')
    }
    const response = await fetch('http://127.0.0.1:5000/api/v1/creator_dashboard', {
        headers: {
            "Authorization": `${token.value}`
        }
    })
    if (response.status === 400){
        if (confirm('You are not a creator would you like to become one?')){
            console.log('redirecting')
            router.push('/consent')
            return
        }

        router.push('/')
    }
    data.value = await response.json()
    songs.value = data.value.songs
    console.log(songs.value)
    if (songs.value.length==0){
        router.push('/song_upload')
        return
    }
    rank.value = data.value.ranks
    total_playback_count.value = data.value.total_playback_count
    best_song.value = data.value.songs[0]
    if (total_playback_count.value == 0){
        playback_percentage.value = 0
    }
    else{
        playback_percentage.value = Math.round(best_song.value.playback_count * 100 / total_playback_count.value)
    }
    

    albums.value = data.value.albums
    lyrics.value = data.value.lyrics

})
</script>

<template>
    <UserTopbar :logged="token" />
    <div class="text-white">
        <h1 class="py-4">CREATOR DASHBOARD <router-link to="/song_upload"><button class="btn btn-outline-warning">UPLOAD MUSIC</button></router-link></h1>
        <div class="row mx-4">

            <div  class="col-3 " style="background-color: rgba(255, 255, 255, 0.158)">
                <p class="text-center fs-3 pt-4">TOTAL PLAYBACKS</p>
                <p v-if="total_playback_count < 1000" class="custom-fs text-center ">{{total_playback_count}}</p>
                <p v-else class="custom-fs text-center ">{{ Math.round(total_playback_count/1000).toFixed(0) }}K</p>
            </div>
            <div class="col-3 ms-3 text-center " style="background-color: rgba(255, 255, 255, 0.158)">

                <router-link :to="`/song/${best_song.song_name}`"><img class="pt-3" :src="`/song/${best_song.song_id}.jpg`" style="width: 13rem;" :alt="`${best_song.song_id}`" ></router-link>
                <p class="text-white text-center m-1 mb-0 fs-2 pb-2">{{best_song.song_name}}</p>

            </div>
            <div class="col" style="background-color: rgba(255, 255, 255, 0.158)">

                <h2 class="text-center pt-3">OVERVIEW</h2>

                <p class="pt-2"><span class="text-white-50 ">Your most popular song :</span> {{best_song.song_name}}</p>

                <p class="pt-2"><span class="text-white-50 ">Platform wide rank :</span> {{rank[0]}}</p>
                
                <p><span class="text-white-50 ">Total playbacks :</span> {{best_song.playback_count}} ( {{playback_percentage}}% of your total playbacks )</p>

                <p><span class="text-white-50 ">Total number of uploads :</span> {{songs.length}}</p>

                <p><span class="text-white-50 ">Average playbacks : </span>{{Math.round(total_playback_count/songs.length).toFixed(0)}} </p>

            </div>
        </div>
        <div class="row mt-3 mx-4" style="">
            <h2 class="py-2">SONG ANALYTICS</h2>
            <table class="table table-dark table-striped  table-bordered  m-auto ">
                <tr class="text-center ">
                    <th>#</th>
                    <th class="p-2">Song Name</th>
                    <th>Rank</th>
                    <th>Genre</th>
                    <th>Released On</th>
                    <th>Playback Count</th>
                    <th>Delete</th>
                    <th>Change</th>
                </tr>
                <tr v-for="(song,index) in songs" :key="index">
                    <td class="p-2">{{index+1}}</td>
                    <td><router-link :to="`/song/${song.song_id}`" class="text-white ">{{song.song_name}}</router-link></td>
                    <td>{{rank[index]}}</td>
                    <td>{{song.genre}}</td>
                    <td>{{song.release_date}}</td>
                    <td>{{song.playback_count}}</td>
                    <td  class="text-center "><button @click="deleteSong(song.song_id)" class="btn btn-danger  ">Delete</button></td>
                    <td  class="text-center "><router-link :to="`/edit_song/${song.song_id}`" class="text-warning  ">Change</router-link></td>

                </tr>
            </table>
        </div><br>
        <div class="row mt-3 mx-4" style="">
            <h2 class="py-2">ALBUM ANALYTICS <router-link to="/create_album"><button class="btn btn-outline-warning"> CREATE ALBUM </button></router-link></h2>
            <table class="table table-dark table-striped  table-bordered  m-auto ">
                <tr class="text-center ">
                    <th>#</th>
                    <th class="p-2">Album Name</th>
                    <th>Song Count</th>
                    <th>Genre</th>
                    <th>Delete</th>
                    <th>Change</th>
                </tr>

                <tr v-for="(album, index) in albums" :key="index">
                    <td class="p-2">{{index+1}}</td>
                    <td><router-link :to="`/album/${album.album_id}`" class="text-white">{{ album.album_name }}</router-link></td>
                    <td>{{album.songs_count}}</td>
                    <td>{{album.genre}}</td>
                    <td  class="text-center "><button @click="deleteAlbum(album.album_id)" class="btn btn-danger  ">Delete</button></td>
                    <td  class="text-center "><router-link :to="`/edit_album/${album.album_id}`" class="text-warning">Change</router-link></td>
                </tr>
            </table>
        </div>
        <br>
        <!-- <div class="row mt-3 mx-4" style="background-color: rgba(255, 255, 255, 0.158)"> -->
        <div class="row mt-3 mx-4" style="">
            <h2 class="py-2">LYRICS VAULT <a href="/add_lyrics"><button class="btn btn-outline-warning"> ADD LYRICS </button></a></h2>
            <table class="table table-dark table-striped  table-bordered  m-auto ">
                <tr class="text-center ">
                    <th class="p-2">#</th>
                    <th>Lyrics Name</th>
                    <th>Date Of Creation</th>
                    <th>Delete</th>
                    <th>Change</th>
                </tr>
               
                <tr v-for="(i, index) in lyrics" :key="index">
                    <td class="p-2">{{index+1}}</td>
                    <td><router-link :to="`/lyrics/${i.lyrics_id}`" class="text-white">{{i.lyrics_name}}</router-link></td>
                    <td>{{i.release_date}}</td>
                    <td  class="text-center "><button @click="deleteLyrics(i.lyrics_id)" class="btn btn-danger  ">Delete</button></td>
                    <td  class="text-center "><router-link :to="`/edit_lyrics/${i.lyrics_id}`" class="text-warning">Change</router-link></td>
                </tr>
            </table>
        </div>
    </div>


</template>

<style scoped>
.custom-fs{
    font-size: 8rem;
}

a{
  text-decoration: none;
  color: inherit;
}

</style>