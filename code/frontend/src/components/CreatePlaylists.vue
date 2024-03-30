<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import UserTopbar from '@/components/topBar/UserTopbar.vue';
const token = ref(sessionStorage.getItem('MusicalToken'))
const playlist_name = ref('')
const thumbnail = ref(null)
const router = useRouter()

const songs = ref([]);
const song1 = ref('')
const song2 = ref('')
const song3 = ref('')
const song4 = ref('')
const song5 = ref('')
const song6 = ref('')


const onFileChange = (e) => {
    thumbnail.value = e.target.files[0]
}

// onBeforeMount(async()=>{
//     const response = await fetch(`http://127.0.0.1:5000/api/v1/songs?song_count=100`)
//     song_data.value = await response.json()
// })
console.log(songs.value)
async function createPlaylist(){
    const formData = new FormData()
    songs.value = []
    if (!playlist_name.value || !thumbnail.value || !song1.value){
        alert("Please fill atleast the first song and the playlist name and thumbnail")
        return
    }
    formData.append('playlist_name', playlist_name.value)
    formData.append('thumbnail', thumbnail.value)
    songs.value.push(song1.value)
    songs.value.push(song2.value)
    songs.value.push(song3.value)
    songs.value.push(song4.value)
    songs.value.push(song5.value)
    songs.value.push(song6.value)

    formData.append('songs', songs.value)
    for (let [key, value] of formData.entries()) {
        console.log(key, value);
    }
    const response = await fetch(`http://127.0.0.1:5000/api/v1/playlist`,{
        method:"POST",

        headers:{
            "Authorization":`${token.value}`,
            // "Content-Type":"multipart/form-data"
        },
        body:formData
    })
    if (response.status == 401){
        alert("Please Login to create a playlist, redirecting in 5 seconds")
        setTimeout(() => {
            router.push('/login')
        }, 5000);
        return
    }
    const data = await response.json()

    if (!data.success){
        alert(data.message)
        return
    }

    alert("Playlist Created")
    router.push('/playlists')

}

</script>

<template>
    <UserTopbar :logged="token" />
    <div class="row justify-content-center " style="height: 92vh" >
        <div class="col-auto bg-white p-3 rounded-4 " style="width: 50vw;">
            <div>
                <div class="p-2">
                    <div class="form-floating mb-3 ">
                        <input type="text" class="form-control " name="name" required v-model="playlist_name"> 
                        <label for="name" class="">Playlist Name :</label>
                    </div>
                        <label for="picture" class="form-label ">Thumbnail</label>
                        <input type="file" name="thumbnail" class="form-control " accept=".jpg" @change="onFileChange" required>
                        <label for="exampleDataList" class="form-label pt-2">Music 1 :</label>
                        <input class="form-control" list="datalistOptions" name="songs" placeholder="Type to search..." required v-model="song1" >
                        <label for="exampleDataList" class="form-label pt-2">Music 2 :</label>
                        <input class="form-control" list="datalistOptions" name="songs" placeholder="Type to search..." v-model="song2">
                        <label for="exampleDataList" class="form-label pt-2">Music 3 :</label>
                        <input class="form-control" list="datalistOptions" name="songs" placeholder="Type to search..." v-model="song3">
                        <label for="exampleDataList" class="form-label pt-2">Music 4 :</label>
                        <input class="form-control" list="datalistOptions" name="songs" placeholder="Type to search..." v-model="song4">
                        <label for="exampleDataList" class="form-label pt-2">Music 5 :</label>
                        <input class="form-control" list="datalistOptions" name="songs" placeholder="Type to search..." v-model="song5">
                        <label for="exampleDataList" class="form-label pt-2">Music 6 :</label>
                        <input class="form-control" list="datalistOptions" name="songs" placeholder="Type to search..." v-model="song6">
                    <div class="pt-4">
                        <button type="submit" class="btn btn-primary " @click="createPlaylist">SUBMIT</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>