<script setup>
import { ref } from 'vue'
import UserTopbar from '@/components/topBar/UserTopbar.vue';
import AlertMessage from '@/components/alertMessages/AlertMessage.vue';
import { useRouter } from 'vue-router';

const token = ref(sessionStorage.getItem('MusicalToken'))
const alert = ref(false)
const message = ref('')
const song_name = ref('')
const lyrics = ref('')
const song = ref('')
const thumbnail = ref('')
const genre = ref('')
const consent = ref(false)
const router = useRouter()

function lyricsChange(e){
    lyrics.value = e.target.files[0]
}

function songChange(e){
    song.value = e.target.files[0]
}

function thumbnailChange(e){
    thumbnail.value = e.target.files[0]
}

async function uploadSong(){
    if (!song_name.value || !lyrics.value || !song.value || !thumbnail.value || !genre.value || !consent.value){
        alert.value = true
        message.value = 'Please fill all the fields'
        setTimeout(() => {
            alert.value = false
        }, 5000);
        return
    }
    const formData = new FormData()
    formData.append('song_name', song_name.value)
    formData.append('lyrics', lyrics.value)
    formData.append('song', song.value)
    formData.append('thumbnail', thumbnail.value)
    formData.append('genre', genre.value)
    const response = await fetch('http://127.0.0.1:5000/api/v1/upload_song', {
        headers: {
            "Authorization": `${token.value}`
        },
        method: 'POST',
        body: formData
    })

    const data = await response.json()
    if (data.message == 'You are not a creator'){
        confirm('You are not a creator would you like to become one?') ? router.push('/consent') : router.push('/')
    }
    if (data.message == "Song already exists"){
        alert.value = true
        message.value = 'Song already exists'
        setTimeout(() => {
            alert.value = false
        }, 5000);
        return
    }

    router.push('/creator_menu')
       

}

</script>

<template>
    <UserTopbar :logged="token" />
    <div class="pt-3 px-5 text-white" >
        <h1 class="">UPLOAD SONG</h1>
        <AlertMessage v-show="alert" :message="message"/>

        <label for="title" class="form-label ">Song Name : </label>
        <input type="text" name="title" class="form-control " v-model="song_name">

        <label for="lyrics" class="form-label pt-2">Lyrics :</label>
        <input type="file" class="form-control " required name="lyrics" @change="lyricsChange" accept=".txt">

        <label for="song" class="form-label pt-2 ">Song :</label>
        <input type="file" class="form-control " required  name="song" @change="songChange" accept=".mp3">

        <label for="thumbnail" class="form-label pt-2 ">Thumbnail :</label>
        <input type="file" class="form-control " required  name="thumbnail" @change="thumbnailChange" accept=".jpg">

        <div class="bg-dark pt-2">

            <label for="genre" class="form-label ">Genre :</label>

            <label for="genre" class="ps-4 pe-1">Pop </label>
            <input type="radio" class="form-switch" name="genre" value="Pop" required v-model="genre">

            <label for="genre" class="ps-4 pe-1  ">Jazz </label>
            <input type="radio" class="form-switch " name="genre" value="Jazz" v-model="genre">

            <label for="genre" class="ps-4 pe-1  ">Electronic </label>
            <input type="radio" class="form-switch " name="genre" value="Electronic" v-model="genre">

            <label for="genre" class="ps-4 pe-1  ">Instrumental </label>
            <input type="radio" class="form-switch " name="genre" value="Instrumental" v-model="genre">
        </div>
        
        <label for="consent"> <span><input type="checkbox" name="consent" required v-model="consent"></span>  I have read and agree to the terms of service. By checking this box, I confirm that I have the legal right to upload the provided music content, and I grant permission for its hosting and distribution on this platform. I understand that I retain ownership and can remove the content at any time. My data will be handled in accordance with the privacy policy.</label>
        <div class="text-center bg-dark pt-3">
            <button class="btn btn-primary justify-content-center " @click="uploadSong"> Upload My Music </button>
        </div>

    </div>


</template>